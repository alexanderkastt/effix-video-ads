"""Montaje final con ffmpeg — clips, voz y música en un solo MP4.

Cada clip se recorta a su ventana antes de encadenarlo: Kling entrega 5
segundos mínimo y montarlos enteros correría el video muy por encima de la
locución. El corte es el que fijó plan_clips, no uno nuevo.

Dentro de esa ventana el clip ya no es un solo plano: `ritmo.py` lo parte en
tomas de 1.5–2.5s reencuadradas, para que el corte visual caiga seguido sin
pagar video nuevo. Y la mezcla de audio la hace `mezcla.py`, con la música
hundiéndose sola bajo la voz.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from . import mezcla, ritmo
from .paths import AUDIO_DIR, CLIPS_DIR, RENDERS_DIR, ROOT, env


@dataclass
class Render:
    video: Path
    duracion_s: float
    clips: int


# La marca pide Montserrat 900 para los titulares — BRANDING-EFFIX.md dice
# textualmente que los textos van en post con esa fuente. El repo trae la
# variable; Montserrat-Black.ttf es su instancia de peso 900. Las de sistema
# quedan como respaldo para no dejar el montaje sin overlays.
FUENTES = [
    Path("referencias/esteticas/fuentes/Montserrat-Black.ttf"),
    Path("referencias/esteticas/fuentes/Montserrat.ttf"),
    Path("C:/Windows/Fonts/seguibl.ttf"),
    Path("C:/Windows/Fonts/arialbd.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
]


def _fuente() -> str:
    """Ruta de fuente escapada como la quiere el filtro de ffmpeg."""
    for f in FUENTES:
        f = f if f.is_absolute() else (ROOT / f)
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


def _clips_de(carpeta: Path) -> list[Path]:
    """Los clips en orden, prefiriendo la versión con lip-sync.

    El glob de clip_*.mp4 tambien atrapa los clip_NN_sync.mp4, y montarlos
    todos duplicaria cada plano sincronizado. Se listan los originales y por
    cada uno se elige su version sincronizada si existe.
    """
    originales = sorted(
        c for c in carpeta.glob("clip_*.mp4") if not c.stem.endswith("_sync")
    )
    return [
        c.with_name(f"{c.stem}_sync.mp4")
        if c.with_name(f"{c.stem}_sync.mp4").exists() else c
        for c in originales
    ]


def ensamblar(
    guion: dict[str, Any],
    plan: dict[str, Any],
    *,
    musica: Path | bool | None = None,
    destino: Path | None = None,
    overlays: bool = True,
) -> Render:
    """Monta el video final: clips partidos en planos + voz + música.

    `musica` acepta tres cosas, y el default cambió: antes era None = sin
    música, y como nadie pasaba nada, ningún ad salía con fondo.

    - `None` (default): toma la pista que le toca al estilo del guión, de la
      librería en `assets/audio/soundtracks/`. Es lo que hay que querer.
    - una `Path`: esa pista concreta.
    - `False`: sin música. Solo para el modo `musical_sync`, donde la canción
      ya es la pista principal y meterle un fondo debajo sería absurdo.
    """
    job_id = str(guion.get("job_id") or "sin-job")
    carpeta = CLIPS_DIR / job_id
    clips = _clips_de(carpeta)
    if not clips:
        raise FileNotFoundError(f"No hay clips en {carpeta}")

    dur_clip = plan["duracion_clip_s"]
    corte = plan["corte_final_s"]
    voz = unir_locucion(job_id)

    if musica is None:
        from .music_engine import pista_de_libreria
        musica = pista_de_libreria(
            str(guion.get("estilo", "")), str(guion.get("tono", ""))
        )
        if musica is None:
            print("   aviso: no hay pista en la librería para este estilo. "
                  "Corre `python scripts/generar_soundtracks.py`.")

    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = destino or (RENDERS_DIR / f"{job_id}.mp4")

    # Un filter_complex en vez de archivos intermedios: cada clip se parte en
    # sus planos, se normaliza el timestamp y se concatena de una sola pasada.
    grupos = ritmo.repartir([float(dur_clip)] * len(clips))
    print(f"   ritmo: {ritmo.resumen(grupos)}")

    entradas: list[str] = []
    filtros: list[str] = []
    etiquetas: list[str] = []
    for i, (clip, planos) in enumerate(zip(clips, grupos)):
        entradas += ["-i", str(clip)]
        for j, plano in enumerate(planos):
            # Cada plano sale del mismo clip: distinto tramo, distinto
            # encuadre. Dos entradas al concat donde antes había una.
            etiqueta = f"v{i}_{j}"
            filtros.append(
                ritmo.filtro_video(plano, f"{i}:v", etiqueta, w=720, h=1280)
            )
            etiquetas.append(f"[{etiqueta}]")
    cadena = "".join(etiquetas)
    n_planos = len(etiquetas)
    if overlays:
        # La capa de texto vive en postproduccion.py: decide cuerpo y
        # animacion, y sabe cuando un overlay no cabe en una linea.
        from .postproduccion import filtros as filtros_texto, resolver
        resueltos = resolver(guion, plan)
        largos = [o.texto for o in resueltos if not o.cabe]
        if largos:
            print(f"   aviso: {len(largos)} overlay(s) no caben en una linea "
                  f"y salen al minimo legible: {', '.join(largos[:3])}")
        dibujos = filtros_texto(resueltos, carpeta)
    else:
        dibujos = []
    if dibujos:
        # El texto va encima del video ya concatenado, no clip por clip: un
        # beat puede cruzar dos clips y su overlay no debe cortarse ahi.
        filtros.append(f"{cadena}concat=n={n_planos}:v=1:a=0[crudo]")
        filtros.append("[crudo]" + ",".join(dibujos) + "[vid]")
    else:
        filtros.append(f"{cadena}concat=n={n_planos}:v=1:a=0[vid]")

    n_voz = len(clips)
    entradas += ["-i", str(voz)]

    if isinstance(musica, (str, Path)) and Path(musica).exists():
        # `-stream_loop -1`: las pistas de la librería duran 75s y hay ads más
        # largos. Sin el loop la música se acaba a mitad del video.
        entradas += ["-stream_loop", "-1", "-i", str(musica)]
        filtros.append(mezcla.cadena_audio(
            f"{n_voz}:a", f"{n_voz + 1}:a", "aud", duracion_s=float(corte)
        ))
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
