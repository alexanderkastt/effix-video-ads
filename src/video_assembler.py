"""Montaje final con ffmpeg — clips, voz y música en un solo MP4.

Cada clip se recorta a su ventana de 4s antes de encadenarlo: Kling entrega
5 segundos mínimo y montarlos enteros correría el video 10 segundos por
encima de la locución. El corte es el que fijó plan_clips, no uno nuevo.

La voz manda sobre la música, que entra al volumen del brief (25% por
defecto) y se corta con el video.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .paths import AUDIO_DIR, CLIPS_DIR, RENDERS_DIR, env, env_float


@dataclass
class Render:
    video: Path
    duracion_s: float
    clips: int


# Segoe UI Black existe en cualquier Windows; Arial Bold es el respaldo.
FUENTES = [
    Path("C:/Windows/Fonts/seguibl.ttf"),
    Path("C:/Windows/Fonts/arialbd.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]


def _fuente() -> str:
    """Ruta de fuente escapada como la quiere el filtro de ffmpeg."""
    for f in FUENTES:
        if f.exists():
            # En un filtro, los dos puntos de "C:/" separan argumentos.
            return str(f).replace("\\", "/").replace(":", r"\:")
    raise RuntimeError(f"No encontré ninguna fuente para los overlays: {FUENTES}")


def _en_lineas(texto: str, ancho: int = 34) -> str:
    """Parte el overlay en líneas cortas.

    Siete palabras no caben en 720px de ancho a cuerpo grande, y ffmpeg no
    hace saltos de línea solo: el texto se sale del cuadro por los dos lados.
    """
    lineas: list[str] = []
    actual = ""
    for palabra in texto.split():
        if actual and len(actual) + 1 + len(palabra) > ancho:
            lineas.append(actual)
            actual = palabra
        else:
            actual = f"{actual} {palabra}".strip()
    if actual:
        lineas.append(actual)
    return "\n".join(lineas)


def _filtros_overlay(
    guion: dict[str, Any], plan: dict[str, Any], carpeta: Path
) -> list[str]:
    """Un drawtext por beat, encendido sólo durante su tramo de locución.

    El texto va en archivo y no en el filtro: los overlays llevan tildes,
    signos de apertura y separadores, y escaparlos dentro de la cadena de
    filtros es una fuente de errores que no vale la pena.
    """
    fuente = _fuente()
    textos = carpeta / "overlays"
    textos.mkdir(parents=True, exist_ok=True)
    por_beat = {b["beat"]: b.get("texto_pantalla", "") for b in guion["beats"]}

    filtros: list[str] = []
    for tramo in plan["reparto"]:
        texto = por_beat.get(tramo["beat"], "").strip()
        if not texto:
            continue
        archivo = textos / f"beat_{tramo['beat']:02d}.txt"
        archivo.write_text(_en_lineas(texto), encoding="utf-8")
        ruta = str(archivo).replace("\\", "/").replace(":", r"\:")
        filtros.append(
            f"drawtext=textfile='{ruta}':fontfile='{fuente}'"
            f":fontsize=38:fontcolor=white:line_spacing=-6"
            f":box=1:boxcolor=black@0.62:boxborderw=13"
            f":x=(w-text_w)/2:y=h*0.70"
            f":enable='between(t,{tramo['t_inicio_s']},{tramo['t_fin_s']})'"
        )
    return filtros


def _ffmpeg(args: list[str]) -> None:
    """Corre ffmpeg y, si falla, muestra su queja en vez de un exit code pelado."""
    proceso = subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error", *args],
        capture_output=True, text=True,
    )
    if proceso.returncode != 0:
        raise RuntimeError(f"ffmpeg falló:\n{proceso.stderr.strip()[:2000]}")


def unir_locucion(job_id: str, destino: Path | None = None) -> Path:
    """Pega los MP3 de los beats en una sola pista, en orden.

    Es la pista que lleva el video y también la que conviene escuchar de
    corrido para saber si la locución fluye antes de montar nada.
    """
    carpeta = AUDIO_DIR / job_id
    partes = sorted(carpeta.glob("beat_*.mp3"))
    if not partes:
        raise FileNotFoundError(f"No hay MP3 de beats en {carpeta}")

    lista = carpeta / "concat_voz.txt"
    lista.write_text(
        "".join(f"file '{p.name}'\n" for p in partes), encoding="utf-8"
    )
    salida = destino or (carpeta / "locucion_completa.mp3")
    _ffmpeg(["-f", "concat", "-safe", "0", "-i", str(lista), "-c", "copy", str(salida)])
    return salida


def ensamblar(
    guion: dict[str, Any],
    plan: dict[str, Any],
    *,
    musica: Path | None = None,
    destino: Path | None = None,
    overlays: bool = True,
) -> Render:
    """Monta el video final: clips recortados + voz + música opcional."""
    job_id = str(guion.get("job_id") or "sin-job")
    carpeta = CLIPS_DIR / job_id
    clips = sorted(carpeta.glob("clip_*.mp4"))
    if not clips:
        raise FileNotFoundError(f"No hay clips en {carpeta}")

    dur_clip = plan["duracion_clip_s"]
    corte = plan["corte_final_s"]
    voz = unir_locucion(job_id)

    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = destino or (RENDERS_DIR / f"{job_id}.mp4")

    # Un filter_complex en vez de archivos intermedios: cada clip se recorta a
    # su ventana, se normaliza el timestamp y se concatena de una sola pasada.
    entradas: list[str] = []
    filtros: list[str] = []
    for i, clip in enumerate(clips):
        entradas += ["-i", str(clip)]
        filtros.append(
            f"[{i}:v]trim=0:{dur_clip},setpts=PTS-STARTPTS,"
            f"scale=720:1280:force_original_aspect_ratio=increase,"
            f"crop=720:1280,fps=24[v{i}]"
        )
    cadena = "".join(f"[v{i}]" for i in range(len(clips)))
    dibujos = _filtros_overlay(guion, plan, carpeta) if overlays else []
    if dibujos:
        # El texto va encima del video ya concatenado, no clip por clip: un
        # beat puede cruzar dos clips y su overlay no debe cortarse ahi.
        filtros.append(f"{cadena}concat=n={len(clips)}:v=1:a=0[crudo]")
        filtros.append("[crudo]" + ",".join(dibujos) + "[vid]")
    else:
        filtros.append(f"{cadena}concat=n={len(clips)}:v=1:a=0[vid]")

    n_voz = len(clips)
    entradas += ["-i", str(voz)]

    if musica and Path(musica).exists():
        entradas += ["-i", str(musica)]
        vol = env_float("MUSICA_VOLUMEN", 0.25)
        filtros.append(
            f"[{n_voz + 1}:a]volume={vol}[bg];"
            f"[{n_voz}:a][bg]amix=inputs=2:duration=first:dropout_transition=0[aud]"
        )
        mapa_audio = "[aud]"
    else:
        mapa_audio = f"{n_voz}:a"

    _ffmpeg([
        *entradas,
        "-filter_complex", ";".join(filtros),
        "-map", "[vid]", "-map", mapa_audio,
        "-t", str(corte),
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart",
        str(salida),
    ])
    return Render(video=salida, duracion_s=corte, clips=len(clips))
