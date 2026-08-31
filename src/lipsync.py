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

# El modelo sale del .env, como los de imagen y video. El default es el
# barato: sync-lipsync cuesta 0.70 USD/min, sync-3 son 8 y react-1 son 10.
MODELO_POR_DEFECTO = "fal-ai/sync-lipsync"


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


def _payload(modelo: str, url_video: str, url_audio: str) -> dict[str, Any]:
    """Arma el input del modelo, que no es el mismo en toda la familia sync.

    sync-lipsync y sync-3 comparten `sync_mode`. react-1 lo llama
    `lipsync_mode`, exige una emocion y decide con `model_mode` cuanto de la
    cara mueve. Sin esta traduccion, cambiar el modelo en el .env manda un
    payload que el endpoint rechaza.

    En los tres casos se corta al terminar el audio: el video dura lo que
    dura, y si el audio se queda corto es mejor cortar ahi que estirar la
    boca hasta el final del plano.
    """
    base = {"video_url": url_video, "audio_url": url_audio}
    if "react-1" in modelo:
        return base | {
            "lipsync_mode": "cut_off",
            "emotion": env("FAL_LIPSYNC_EMOTION", "neutral"),
            "model_mode": env("FAL_LIPSYNC_MODE", "face"),
        }
    return base | {"sync_mode": "cut_off"}


def sincronizar_clip(
    clip: Path,
    audio: Path,
    *,
    destino: Path | None = None,
    modelo: str | None = None,
) -> Sincronizado:
    """Manda un clip y su audio al modelo de lip-sync y baja el resultado."""
    import time

    modelo = modelo or env("FAL_MODEL_LIPSYNC", MODELO_POR_DEFECTO)
    numero = int(clip.stem.split("_")[-1])
    inicio = time.monotonic()

    with open(clip, "rb") as fh:
        url_video = fal_client.upload(fh.read(), "video/mp4")
    with open(audio, "rb") as fh:
        url_audio = fal_client.upload(fh.read(), "audio/mpeg")

    salida = fal_client.subscribe(modelo, _payload(modelo, url_video, url_audio))
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
    fallos: list[dict[str, Any]] | None = None,
) -> list[Sincronizado]:
    """Sincroniza los clips indicados y deja el resto intacto.

    `clips_a_camara` son los números de clip donde el personaje mira al lente.
    Los demás se quedan como están: ahí la voz es narración, no diálogo.

    Los fallos se acumulan en `fallos` en vez de cortar la corrida: un 404 de
    la cola de fal no es motivo para dejar sin sincronizar los clips que
    venían detrás.
    """
    fallos = [] if fallos is None else fallos
    job_id = str(guion.get("job_id") or "sin-job")
    carpeta = CLIPS_DIR / job_id
    voz = AUDIO_DIR / job_id / "locucion_completa.mp3"
    if not voz.exists():
        # La pista unida la creaba el montaje, asi que sincronizar antes de
        # montar fallaba por un orden implicito que nadie habia escrito.
        from .video_assembler import unir_locucion
        voz = unir_locucion(job_id)

    dur = plan["duracion_clip_s"]
    hechos: list[Sincronizado] = []

    for n in clips_a_camara:
        clip = carpeta / f"clip_{n:02d}.mp4"
        if not clip.exists():
            raise FileNotFoundError(f"No existe {clip}")
        if clip.with_name(f"{clip.stem}_sync.mp4").exists():
            continue  # ya sincronizado: no se vuelve a pagar
        inicio, fin = (n - 1) * dur, min(n * dur, plan["audio_total_s"])
        if fin <= inicio:
            continue  # ventana sin voz: no hay nada que sincronizar
        audio = _recorte_de_audio(
            voz, inicio, fin, carpeta / "audio_por_clip" / f"clip_{n:02d}.mp3"
        )
        # La cola de fal a veces pierde una peticion y devuelve 404 al
        # recogerla. Sin aislar el fallo, ese 404 se llevaba por delante los
        # clips que venian despues, que no tenian nada de malo.
        for intento in (1, 2):
            try:
                hechos.append(sincronizar_clip(clip, audio))
                break
            except Exception as error:
                if intento == 2:
                    fallos.append({"clip": n, "error": f"{type(error).__name__}: {error}"})
                    break
    return hechos
