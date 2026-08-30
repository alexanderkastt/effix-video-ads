"""Lip-sync selectivo — sólo los clips donde el personaje habla al lente.

El guión es una voz en off: durante buena parte del video Camila hace cosas
(revisa producto, camina, trabaja de noche) mientras alguien narra. Aplicar
lip-sync a todo la convertiría en una presentadora que habla de espaldas,
que es peor que no sincronizar nada.

Así que se sincronizan sólo los clips marcados, con el tramo de locución que
les corresponde: cada clip cubre una ventana de la línea de tiempo, y su
audio es ese recorte de la pista completa, no la pista entera.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import fal_client
import requests

from .paths import AUDIO_DIR, CLIPS_DIR, env

MODELO = "fal-ai/sync-lipsync"


@dataclass
class Sincronizado:
    clip: int
    video: Path
    segundos_de_espera: float


def _recorte_de_audio(
    voz: Path, inicio: float, fin: float, destino: Path
) -> Path:
    """Saca de la pista completa el tramo que suena durante este clip."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    proceso = subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         "-i", str(voz), "-ss", f"{inicio:.3f}", "-to", f"{fin:.3f}",
         "-c:a", "libmp3lame", "-b:a", "192k", str(destino)],
        capture_output=True, text=True,
    )
    if proceso.returncode != 0:
        raise RuntimeError(f"ffmpeg falló recortando audio:\n{proceso.stderr[:800]}")
    return destino


def sincronizar_clip(
    clip: Path,
    audio: Path,
    *,
    destino: Path | None = None,
) -> Sincronizado:
    """Manda un clip y su audio al modelo de lip-sync y baja el resultado."""
    import time

    numero = int(clip.stem.split("_")[-1])
    inicio = time.monotonic()

    with open(clip, "rb") as fh:
        url_video = fal_client.upload(fh.read(), "video/mp4")
    with open(audio, "rb") as fh:
        url_audio = fal_client.upload(fh.read(), "audio/mpeg")

    salida = fal_client.subscribe(
        MODELO,
        {
            "video_url": url_video,
            "audio_url": url_audio,
            # El video dura lo que dura; si el audio se queda corto, se corta
            # ahí en vez de estirar la boca hasta el final del plano.
            "sync_mode": "cut_off",
        },
    )
    url = salida["video"]["url"] if isinstance(salida.get("video"), dict) else salida["video"]

    ruta = destino or clip.with_name(f"{clip.stem}_sync.mp4")
    ruta.write_bytes(requests.get(url, timeout=600).content)
    return Sincronizado(
        clip=numero, video=ruta, segundos_de_espera=round(time.monotonic() - inicio, 1)
    )


def sincronizar(
    guion: dict[str, Any],
    plan: dict[str, Any],
    clips_a_camara: list[int],
) -> list[Sincronizado]:
    """Sincroniza los clips indicados y deja el resto intacto.

    `clips_a_camara` son los números de clip donde el personaje mira al lente.
    Los demás se quedan como están: ahí la voz es narración, no diálogo.
    """
    job_id = str(guion.get("job_id") or "sin-job")
    carpeta = CLIPS_DIR / job_id
    voz = AUDIO_DIR / job_id / "locucion_completa.mp3"
    if not voz.exists():
        raise FileNotFoundError(f"Falta la pista de voz completa en {voz}")

    dur = plan["duracion_clip_s"]
    hechos: list[Sincronizado] = []

    for n in clips_a_camara:
        clip = carpeta / f"clip_{n:02d}.mp4"
        if not clip.exists():
            raise FileNotFoundError(f"No existe {clip}")
        inicio, fin = (n - 1) * dur, min(n * dur, plan["audio_total_s"])
        if fin <= inicio:
            continue  # ventana sin voz: no hay nada que sincronizar
        audio = _recorte_de_audio(
            voz, inicio, fin, carpeta / "audio_por_clip" / f"clip_{n:02d}.mp3"
        )
        hechos.append(sincronizar_clip(clip, audio))
    return hechos
