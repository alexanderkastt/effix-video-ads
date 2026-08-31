"""Postproducción de textos — los subtítulos que van encima del video.

El branding manda: caja alta, Montserrat 900, tratamiento sticker con
outline blanco grueso. Nada de cuadros de fondo — el contorno es lo que da
legibilidad sobre cualquier imagen, y además es la identidad de la marca.

Cada overlay entra con un fade corto y un empujón desde abajo, y sale
igual. En un feed, un texto que aparece de golpe y se queda quieto se lee
como un error de render; el movimiento mínimo es lo que lo hace ver
intencional.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import ImageFont

from .paths import ROOT

# Margen lateral: por debajo de esto el texto toca el borde de la pantalla.
MARGEN_X = 40
# Cuerpo máximo y mínimo. El piso no es estético: por debajo de 40px un
# overlay no se lee en un móvil a distancia de scroll.
CUERPO_MAX = 72
CUERPO_MIN = 40
# Altura del texto, en fracción de la altura del video. 0.72 lo deja por
# encima de la botonera de Reels y TikTok.
ALTURA = 0.72

DURACION_ENTRADA = 0.18
DESPLAZAMIENTO = 28  # píxeles que sube al entrar


@dataclass
class Overlay:
    """Un texto ya resuelto: qué dice, cuándo y de qué tamaño."""

    texto: str
    inicio: float
    fin: float
    cuerpo: int
    cabe: bool


def _fuente(nombre: str = "Montserrat-Black.ttf") -> Path:
    ruta = ROOT / "referencias" / "esteticas" / "fuentes" / nombre
    if not ruta.exists():
        raise FileNotFoundError(f"Falta la fuente de marca en {ruta}")
    return ruta


def cuerpo_para(texto: str, ancho_video: int = 720) -> tuple[int, bool]:
    """El cuerpo más grande con el que el texto entra en UNA línea.

    Devuelve también si de verdad cupo: cuando un overlay necesita bajar del
    piso legible, el problema no es el tamaño sino que el texto es largo, y
    eso se arregla escribiéndolo más corto, no encogiéndolo.
    """
    disponible = ancho_video - 2 * MARGEN_X
    fuente = str(_fuente())
    for cuerpo in range(CUERPO_MAX, CUERPO_MIN - 1, -2):
        ancho = ImageFont.truetype(fuente, cuerpo).getbbox(texto.upper())[2]
        if ancho <= disponible:
            return cuerpo, True
    return CUERPO_MIN, False


def resolver(guion: dict[str, Any], plan: dict[str, Any], ancho: int = 720) -> list[Overlay]:
    """Convierte los texto_pantalla del guión en overlays con tiempo y cuerpo."""
    por_beat = {b["beat"]: b.get("texto_pantalla", "").strip() for b in guion["beats"]}
    salida: list[Overlay] = []
    for tramo in plan["reparto"]:
        texto = por_beat.get(tramo["beat"], "")
        if not texto:
            continue
        cuerpo, cabe = cuerpo_para(texto, ancho)
        salida.append(
            Overlay(texto=texto.upper(), inicio=tramo["t_inicio_s"],
                    fin=tramo["t_fin_s"], cuerpo=cuerpo, cabe=cabe)
        )
    return salida


def _escapar(ruta: Path) -> str:
    return str(ruta).replace("\\", "/").replace(":", r"\:")


def filtros(overlays: list[Overlay], carpeta: Path, alto: int = 1280) -> list[str]:
    """Un drawtext por overlay, con contorno sticker y entrada animada."""
    fuente = _escapar(_fuente())
    textos = carpeta / "overlays"
    textos.mkdir(parents=True, exist_ok=True)

    filtros: list[str] = []
    for i, o in enumerate(overlays):
        archivo = textos / f"overlay_{i:02d}.txt"
        archivo.write_text(o.texto, encoding="utf-8")
        t0, t1 = o.inicio, o.fin
        entrada = DURACION_ENTRADA

        # Opacidad: sube al entrar, baja al salir. Fuera del tramo el filtro
        # ni se dibuja, asi que basta con cubrir el interior.
        alpha = (
            f"if(lt(t,{t0 + entrada:.2f}),(t-{t0:.2f})/{entrada},"
            f"if(gt(t,{t1 - entrada:.2f}),({t1:.2f}-t)/{entrada},1))"
        )
        # Sube {DESPLAZAMIENTO}px mientras aparece y ahi se queda.
        y = (
            f"{alto * ALTURA:.0f}-th/2"
            f"+{DESPLAZAMIENTO}*max(0\\,1-(t-{t0:.2f})/{entrada})"
        )
        filtros.append(
            f"drawtext=textfile='{_escapar(archivo)}':fontfile='{fuente}'"
            f":fontsize={o.cuerpo}:fontcolor=white"
            # El contorno es lo que sustituye a la caja negra: se lee sobre
            # cualquier fondo y es el tratamiento sticker de la marca.
            f":borderw={max(4, o.cuerpo // 12)}:bordercolor=black"
            f":shadowx=0:shadowy={max(2, o.cuerpo // 20)}:shadowcolor=black@0.45"
            f":x=(w-text_w)/2:y={y}"
            f":alpha='{alpha}'"
            f":enable='between(t,{t0},{t1})'"
        )
    return filtros
