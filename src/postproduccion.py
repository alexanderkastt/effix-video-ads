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

DURACION_ENTRADA = 0.22
DURACION_SALIDA = 0.18
DESPLAZAMIENTO = 34  # píxeles que sube al entrar

# Separación entre renglones, en fracción del cuerpo. El interlineado propio de
# `drawtext` deja las mayúsculas de Montserrat Black flotando muy separadas: en
# caja alta no hay descendentes que llenar, así que 1.0 del cuerpo ya deja el
# aire justo y el overlay se lee como un bloque y no como dos textos sueltos.
INTERLINEA = 1.0

# El texto no se queda quieto una vez que entra: flota un par de píxeles. En un
# feed, un overlay perfectamente inmóvil sobre imagen en movimiento se lee como
# un pegote de render; el movimiento mínimo es lo que lo hace ver intencional.
FLOTA_PX = 3.0
FLOTA_PERIODO_S = 2.4

# Caracteres que separan y no cierran: no pueden quedar al final de un renglón.
_SEPARADORES = {"·", "|", "—", "–", "-", "/"}


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


def ajustar(
    texto: str, ancho_video: int = 720, *, max_lineas: int = 2
) -> tuple[str, int, bool]:
    """Envuelve el overlay en varias líneas y devuelve el cuerpo que le sirve.

    `cuerpo_para` sólo sabe medir una línea, y con eso la mayoría de los
    overlays de siete palabras no cabía ni al piso legible: se dibujaban a 40px
    porque no había otra, que es lo mismo que no ponerlos — un ad tiene que
    funcionar sin sonido.

    Partirlos en dos deja el mismo texto al doble de tamaño. Se prueba primero
    en una línea (siempre se lee mejor de un vistazo) y sólo se parte si hace
    falta, buscando el corte que deje las dos mitades más parejas: un renglón
    largo sobre uno de dos palabras se ve como un error de maquetación.
    """
    cuerpo, cabe = cuerpo_para(texto, ancho_video)
    if cabe or max_lineas < 2:
        return texto, cuerpo, cabe

    palabras = texto.split()
    if len(palabras) < 2:
        return texto, cuerpo, cabe

    mejor: tuple[int, int, bool, str] | None = None
    for corte in range(1, len(palabras)):
        arriba, abajo = palabras[:corte], palabras[corte:]
        # Un separador que cae justo en la frontera se descarta: el "·" de
        # "FERIA EFFIX · 15–19 OCT" separa dentro de un renglón, y al partir en
        # dos el salto de línea ya hace ese trabajo. Dejarlo colgando al final
        # del primero se lee como un error de maquetación.
        while arriba and arriba[-1] in _SEPARADORES:
            arriba = arriba[:-1]
        while abajo and abajo[0] in _SEPARADORES:
            abajo = abajo[1:]
        if not arriba or not abajo:
            continue
        filas = [" ".join(arriba), " ".join(abajo)]
        cuerpos = [cuerpo_para(f, ancho_video) for f in filas]
        # El cuerpo lo manda la fila más ancha: las dos se dibujan igual.
        c = min(x for x, _ in cuerpos)
        entra = all(ok for _, ok in cuerpos)
        desequilibrio = abs(len(filas[0]) - len(filas[1]))
        candidato = (c, -desequilibrio, entra, "\n".join(filas))
        if mejor is None or candidato[:2] > mejor[:2]:
            mejor = candidato
    if mejor is None:
        return texto, cuerpo, cabe

    c, _, entra, envuelto = mejor
    return envuelto, c, entra


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


# ─────────────────────────── logo de marca ──────────────────────────

# El logo original es plateado con degradado (luminancia media 189/255). Sobre
# el gris del diorama de crochet o sobre la feria iluminada se pierde. El
# branding pide "outline blanco grueso, estilo sticker", que además es lo que
# lo hace legible sobre cualquier fondo — el mismo tratamiento que los
# subtítulos.
LOGO_ORIGINAL = ROOT / "referencias" / "marca" / "logo_effix.png"
LOGO_SOMBRA_PX = 14
LOGO_DESENFOQUE = 10


def logo_marca() -> Path:
    """El logo en blanco puro con sombra, listo para superponer. Se cachea."""
    from PIL import Image, ImageFilter

    destino = ROOT / "assets" / "marca" / "logo_effix_blanco.png"
    if destino.exists():
        return destino
    if not LOGO_ORIGINAL.exists():
        raise FileNotFoundError(f"Falta el logo de marca en {LOGO_ORIGINAL}")

    original = Image.open(LOGO_ORIGINAL).convert("RGBA").crop(
        Image.open(LOGO_ORIGINAL).convert("RGBA").getbbox())
    alfa = original.getchannel("A")

    # Lienzo con margen para que la sombra no se recorte.
    m = LOGO_SOMBRA_PX * 3
    lienzo = Image.new("RGBA", (original.width + m * 2, original.height + m * 2),
                       (0, 0, 0, 0))

    sombra = Image.new("RGBA", lienzo.size, (0, 0, 0, 0))
    sombra.paste(Image.new("RGBA", original.size, (0, 0, 0, 190)),
                 (m, m + LOGO_SOMBRA_PX // 2), alfa)
    lienzo.alpha_composite(sombra.filter(
        ImageFilter.GaussianBlur(LOGO_DESENFOQUE)))

    # El trazo, en blanco puro.
    lienzo.paste(Image.new("RGBA", original.size, (255, 255, 255, 255)),
                 (m, m), alfa)

    destino.parent.mkdir(parents=True, exist_ok=True)
    lienzo.save(destino)
    return destino


def filtros_logo(
    momentos: list[tuple[float, float, str]],
    entrada: str,
    salida: str,
    *,
    w: int = 1080,
    h: int = 1920,
    entradas_logo: list[str] | None = None,
) -> list[str]:
    """Superpone el logo en los tramos pedidos, con entrada y salida animadas.

    `momentos` son tramos `(desde, hasta, sitio)`. Dos sitios, que responden a
    dos necesidades distintas:

    - `esquina`: pequeño, arriba a la derecha. Es la mosca de televisión —
      firma el ad sin taparlo. Sirve para cumplir la regla de que la marca
      aparezca en los primeros cinco segundos.
    - `centro`: grande y centrado. Se reserva para el momento en que la canción
      NOMBRA la marca y para el cierre; puesto ahí, el logo entra justo cuando
      se canta "Feria Effix", que es lo que lo hace memorable en vez de
      decorativo.

    El logo se dibuja DESPUÉS de los subtítulos para que nunca quede debajo.
    """
    ANCHOS = {"esquina": 0.22, "centro": 0.62}
    filtros: list[str] = []
    actual = entrada
    for i, (t0, t1, sitio) in enumerate(momentos):
        ancho = int(w * ANCHOS.get(sitio, ANCHOS["esquina"]))
        etiqueta = f"lg{i}"
        # Cada uso necesita su propia copia escalada: el mismo input no se
        # puede consumir dos veces en un filter_complex.
        entra = min(0.35, max((t1 - t0) * 0.25, 0.12))
        fuente = (entradas_logo or [])[i] if entradas_logo else f"L{i}"
        filtros.append(
            f"[{fuente}]scale={ancho}:-1,format=rgba,"
            f"fade=t=in:st={t0:.2f}:d={entra:.2f}:alpha=1,"
            f"fade=t=out:st={max(t1 - entra, t0):.2f}:d={entra:.2f}:alpha=1"
            f"[{etiqueta}]"
        )
        if sitio == "centro":
            x, y = "(W-w)/2", f"(H-h)/2-{int(h * 0.06)}"
        else:
            x, y = f"W-w-{int(w * 0.045)}", f"{int(h * 0.045)}"
        siguiente = f"cl{i}" if i < len(momentos) - 1 else salida
        filtros.append(
            f"[{actual}][{etiqueta}]overlay={x}:{y}:"
            f"enable='between(t,{t0:.2f},{t1:.2f})'[{siguiente}]"
        )
        actual = siguiente
    return filtros


def filtros(overlays: list[Overlay], carpeta: Path, alto: int = 1280) -> list[str]:
    """Un drawtext por RENGLÓN, con contorno sticker y entrada animada.

    Por renglón y no por overlay porque `drawtext` con texto de varias líneas
    centra el bloque entero y deja cada línea alineada a la izquierda dentro de
    él: un overlay de dos renglones salía descuadrado, con el segundo empezando
    donde empezaba el primero. Dibujando cada línea por separado, cada una
    recibe su propio `x=(w-text_w)/2` y las dos quedan centradas de verdad — y
    de paso el interlineado lo decidimos nosotros y no el filtro.

    Las dos líneas comparten animación (entran y salen juntas), así que el
    overlay se sigue leyendo como una sola pieza.
    """
    fuente = _escapar(_fuente())
    textos = carpeta / "overlays"
    textos.mkdir(parents=True, exist_ok=True)

    filtros: list[str] = []
    for i, o in enumerate(overlays):
        renglones = [r for r in o.texto.split("\n") if r.strip()]
        if not renglones:
            continue
        t0, t1 = o.inicio, o.fin
        # Entrada y salida se acortan si el overlay dura poco: una animación de
        # 0.4s sobre un texto que vive 0.6s no llega a leerse nunca quieto.
        entrada = min(DURACION_ENTRADA, max((t1 - t0) * 0.25, 0.08))
        salida = min(DURACION_SALIDA, max((t1 - t0) * 0.2, 0.06))

        # Opacidad con easing: arranca rápido y frena. Un fade lineal se ve
        # como un cross-dissolve de editor, no como un sticker que aparece.
        alpha = (
            f"if(lt(t,{t0 + entrada:.3f}),"
            f"pow((t-{t0:.3f})/{entrada:.3f},0.6),"
            f"if(gt(t,{t1 - salida:.3f}),"
            f"pow(({t1:.3f}-t)/{salida:.3f},0.6),1))"
        )
        # Movimiento: sube desde abajo frenando (ease-out cúbico), flota
        # mientras está en pantalla, y baja al salir.
        desplazamiento = (
            f"if(lt(t,{t0 + entrada:.3f}),"
            f"{DESPLAZAMIENTO}*pow(1-(t-{t0:.3f})/{entrada:.3f},3),0)"
            f"+if(gt(t,{t1 - salida:.3f}),"
            f"{DESPLAZAMIENTO * 0.4:.1f}*pow((t-{t1 - salida:.3f})/{salida:.3f},3),0)"
            f"+{FLOTA_PX}*sin(2*PI*(t-{t0:.3f})/{FLOTA_PERIODO_S})"
        )

        paso = o.cuerpo * INTERLINEA
        # El bloque se centra sobre la altura de siempre, así que un overlay de
        # dos renglones no empuja el texto hacia la botonera de Reels.
        tope = alto * ALTURA - (paso * len(renglones)) / 2
        for j, renglon in enumerate(renglones):
            archivo = textos / f"overlay_{i:02d}_{j}.txt"
            archivo.write_text(renglon, encoding="utf-8")
            centro = tope + paso * j + paso / 2
            filtros.append(
                f"drawtext=textfile='{_escapar(archivo)}':fontfile='{fuente}'"
                f":fontsize={o.cuerpo}:fontcolor=white"
                # El contorno es lo que sustituye a la caja negra: se lee sobre
                # cualquier fondo y es el tratamiento sticker de la marca.
                f":borderw={max(4, o.cuerpo // 12)}:bordercolor=black"
                f":shadowx=0:shadowy={max(2, o.cuerpo // 20)}:shadowcolor=black@0.45"
                f":x='(w-text_w)/2':y='{centro:.1f}-th/2+({desplazamiento})'"
                f":alpha='{alpha}'"
                f":enable='between(t,{t0},{t1})'"
            )
    return filtros
