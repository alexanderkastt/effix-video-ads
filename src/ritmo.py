"""Ritmo de montaje — parte cada línea en planos cortos sin generar video nuevo.

El problema que resuelve: hasta ahora un plano era una línea de guión. Una
línea de seis segundos era un plano de seis segundos, y el corte visual caía
cada seis segundos. En un feed eso se lee como lento aunque el guión sea bueno.

La salida barata sería generar dos clips por línea larga, pero eso duplica el
gasto de video y rompe el tope de 6 USD por ad. Así que el segundo plano sale
del MISMO clip, reencuadrado: `trim` del tramo que toca y un `crop` distinto.
Es el punch-in de toda la vida — la misma toma vista más cerca se lee como
otra cámara. Los planos extra no cuestan un centavo.

El tope de zoom es 1.25x a propósito: recortar al 80% de 1080x1920 y volver a
escalar deja 864x1536 reales estirados, que todavía aguanta. Más que eso y se
empieza a ver el pixel.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from .paths import env_float, env_int

# Los límites de un plano. Debajo de 1.25s el ojo no alcanza a leer el encuadre
# y el corte se siente como un error; por encima de 2.5s vuelve el problema que
# esto viene a arreglar.
PLANO_MIN_S = env_float("PLANO_MIN_S", 1.5)
PLANO_MAX_S = env_float("PLANO_MAX_S", 2.5)

# Piso duro: un plano nunca baja de aquí, ni partiendo una línea larga.
PLANO_PISO_S = 1.25

# Cuánto se puede acercar el reencuadre antes de que se note la pérdida.
ZOOM_MAX = 1.25

# Cada encuadre es (zoom, offset_x, offset_y) en fracción del cuadro. El
# vertical negativo sube el recorte: en 9:16 la cara vive en el tercio de
# arriba, y un crop centrado le corta la frente.
ENCUADRES: dict[str, tuple[float, float, float]] = {
    "full":     (1.00,  0.00,  0.00),
    "punch":    (1.25,  0.00, -0.08),
    "lateral":  (1.14,  0.06, -0.04),
    "contra":   (1.14, -0.06, -0.04),
}

# El orden en que se alternan dentro de una misma línea. Nunca dos planos
# seguidos con el mismo encuadre: eso se ve como un salto de montaje, no como
# un corte.
CICLO = ["full", "punch", "lateral", "full", "contra", "punch"]


@dataclass
class Plano:
    """Un corte: qué tramo del clip se usa y con qué encuadre."""

    inicio_s: float      # dónde empieza dentro del clip fuente
    fin_s: float         # dónde termina dentro del clip fuente
    encuadre: str

    @property
    def duracion_s(self) -> float:
        return round(self.fin_s - self.inicio_s, 3)


def cuantos(dur: float) -> int:
    """Cuántos planos sacar de una línea de `dur` segundos.

    Se reparte para que ninguno quede por debajo del piso: es preferible un
    plano de 2.8s que dos de 1.4s mal cortados a mitad de palabra.
    """
    if dur <= 0:
        return 1
    # Redondeo hacia arriba, no al más cercano: con `round` una línea de 3.6s
    # daba un solo plano de 3.6s, que es justo el plano largo que esto viene a
    # eliminar. Partir de más nunca deja un plano por encima del techo.
    n = max(1, math.ceil(dur / PLANO_MAX_S))
    # Y ajusta hacia abajo hasta que todos superen el piso: es preferible un
    # plano de 2.8s a dos de 1.4s cortados a mitad de palabra.
    while n > 1 and dur / n < PLANO_PISO_S:
        n -= 1
    return n


def planos(dur: float, *, desde: int = 0) -> list[Plano]:
    """Parte una línea en sus planos, alternando encuadre.

    `desde` es la posición en el ciclo de encuadres: se le pasa un contador
    global para que dos líneas seguidas no arranquen las dos en `full` y el
    corte entre ellas se pierda.
    """
    n = cuantos(dur)
    tramo = dur / n
    return [
        Plano(
            inicio_s=round(i * tramo, 3),
            fin_s=round((i + 1) * tramo, 3) if i < n - 1 else round(dur, 3),
            encuadre=CICLO[(desde + i) % len(CICLO)],
        )
        for i in range(n)
    ]


def planos_en_fuente(
    dur_destino: float, dur_fuente: float, *, desde: int = 0
) -> list[Plano]:
    """Planos que llenan `dur_destino` en el montaje sacándolos de un clip que
    sólo dura `dur_fuente`.

    Es el caso del ad musical: la canción manda, y el tramo que le toca a una
    línea de la letra puede ser más largo que los cinco segundos que se le
    pagaron a Kling. Las salidas obvias son malas — congelar el último frame se
    ve como un cuelgue, y estirar con `setpts` es cámara lenta, que está
    prohibida.

    Lo que sí funciona: cada plano dura como mucho `PLANO_MAX_S`, así que
    siempre cabe entero dentro del clip; lo único que cambia es DESDE DÓNDE se
    toma. Los offsets recorren el clip de principio a fin, de modo que los
    planos se solapan en el material pero nunca en el encuadre. Un tramo de 6.5s
    sale de un clip de 5s como tres tomas distintas de la misma acción, sin
    repetir cuadro ni pagar un clip más.
    """
    if dur_fuente <= 0:
        raise ValueError("El clip fuente no puede durar cero.")
    n = cuantos(dur_destino)
    tramo = dur_destino / n
    # Con una ventana útil corta —un clip que se estropea a mitad y del que sólo
    # sirve el principio— el plano de reparto normal no cabe. Se parte en más
    # planos, que es gratis, mientras ninguno baje del piso legible.
    while tramo > dur_fuente + 0.001 and dur_destino / (n + 1) >= PLANO_PISO_S:
        n += 1
        tramo = dur_destino / n
    if tramo > dur_fuente + 0.001:
        raise ValueError(
            f"Un plano de {tramo:.2f}s no cabe en un clip de {dur_fuente:.2f}s "
            f"sin bajar del piso de {PLANO_PISO_S}s. Genera un clip más largo "
            f"o amplía la ventana útil."
        )
    margen = max(0.0, dur_fuente - tramo)
    return [
        Plano(
            inicio_s=round(0.0 if n == 1 else margen * i / (n - 1), 3),
            fin_s=round((0.0 if n == 1 else margen * i / (n - 1)) + tramo, 3),
            encuadre=CICLO[(desde + i) % len(CICLO)],
        )
        for i in range(n)
    ]


def imantar(
    cortes: list[float],
    golpes: list[float],
    *,
    tolerancia_s: float = 0.6,
    piso_s: float = PLANO_PISO_S,
) -> list[float]:
    """Lleva cada corte al golpe de la canción más cercano, si conviene.

    Dos guardas, porque imantar a lo bruto empeora el montaje:

    1. Un golpe a más de `tolerancia_s` del corte teórico no es el golpe de esa
       frase — arrastrarlo hasta allá descuadra la letra con la imagen.
    2. Si mover el corte deja un plano por debajo del piso legible, se deja
       donde estaba. Un corte a tiempo no vale un plano de medio segundo.

    El primero y el último corte no se tocan: son el principio y el fin del ad.
    """
    if not golpes or len(cortes) < 3:
        return list(cortes)
    salida = list(cortes)
    for i in range(1, len(salida) - 1):
        cercano = min(golpes, key=lambda g: abs(g - cortes[i]))
        if abs(cercano - cortes[i]) > tolerancia_s:
            continue
        if cercano - salida[i - 1] < piso_s or cortes[i + 1] - cercano < piso_s:
            continue
        salida[i] = round(cercano, 3)
    return salida


def repartir(duraciones: list[float]) -> list[list[Plano]]:
    """Los planos de un ad entero, con el ciclo de encuadres corrido.

    Devuelve una lista por línea. El contador se arrastra entre líneas para
    que el encuadre cambie también en el corte de una línea a la siguiente.
    """
    salida: list[list[Plano]] = []
    cursor = 0
    for dur in duraciones:
        grupo = planos(dur, desde=cursor)
        salida.append(grupo)
        cursor += len(grupo)
    return salida


def _crop(zoom: float, dx: float, dy: float, w: int, h: int) -> str:
    """El par scale+crop que produce el reencuadre.

    Se agranda el cuadro y se recorta al tamaño final, en vez de recortar y
    volver a escalar: así el resultado siempre sale exactamente en WxH y
    ffmpeg no tiene que adivinar redondeos que le dejarían un pixel impar
    (libx264 con yuv420p exige dimensiones pares).
    """
    zoom = min(zoom, ZOOM_MAX)
    if zoom <= 1.001:
        return (f"scale={w}:{h}:force_original_aspect_ratio=increase,"
                f"crop={w}:{h}")
    # `iw`/`ih` ya son el cuadro escalado; el offset se mide sobre el sobrante.
    return (
        f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},"
        f"scale=iw*{zoom:.4f}:ih*{zoom:.4f},"
        f"crop={w}:{h}:x='(iw-{w})/2+({dx:.4f}*iw)':y='(ih-{h})/2+({dy:.4f}*ih)'"
    )


def filtro_video(
    plano: Plano,
    entrada: str,
    salida: str,
    *,
    w: int = 1080,
    h: int = 1920,
    fps: int = 24,
    clonar_cola_s: float = 2.0,
) -> str:
    """La cadena de filtros de un plano, lista para el filter_complex.

    `clonar_cola_s` existe porque el lip-sync devuelve el clip cortado a la voz
    (`sync_mode=cut_off`): si el plano pide un poco más de lo que dura el clip,
    `tpad` sostiene el último frame en vez de dejar el video en negro. En una
    conversación real el aire entre réplicas es justamente la cara sosteniendo
    el gesto.
    """
    zoom, dx, dy = ENCUADRES.get(plano.encuadre, ENCUADRES["full"])
    partes = [
        f"tpad=stop_mode=clone:stop_duration={clonar_cola_s}",
        f"trim={plano.inicio_s:.3f}:{plano.fin_s:.3f}",
        "setpts=PTS-STARTPTS",
        _crop(zoom, dx, dy, w, h),
        f"fps={fps}",
    ]
    if env_int("RITMO_PUSH_IN", 0):
        # Push-in continuo sobre el plano ya reencuadrado. Va detrás de una
        # bandera porque zoompan es lento y en zooms lentos hace jitter: el
        # corte de encuadre ya da la sensación de cámara distinta sin eso.
        frames = max(1, int(plano.duracion_s * fps))
        partes.append(
            f"zoompan=z='min(zoom+0.0009,1.08)':d={frames}"
            f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={w}x{h}:fps={fps}"
        )
    return f"[{entrada}]" + ",".join(partes) + f"[{salida}]"


def filtro_audio(plano: Plano, entrada: str, salida: str) -> str:
    """El tramo de voz que le toca a este plano.

    El audio no se reencuadra: se corta en el mismo punto que el video para que
    los planos de una línea sigan sonando como una frase corrida. `apad` cubre
    el caso de que la voz sea un pelo más corta que el tramo pedido.
    """
    dur = plano.duracion_s
    return (
        f"[{entrada}]atrim={plano.inicio_s:.3f}:{plano.fin_s:.3f},"
        f"asetpts=PTS-STARTPTS,apad=whole_dur={dur:.3f},"
        f"atrim=0:{dur:.3f},asetpts=PTS-STARTPTS[{salida}]"
    )


def resumen(grupos: list[list[Plano]]) -> str:
    """Una línea legible para la consola: cuántos planos y de qué largo."""
    todos = [p for g in grupos for p in g]
    if not todos:
        return "sin planos"
    largos = [p.duracion_s for p in todos]
    fuera = [d for d in largos if d > PLANO_MAX_S + 0.01]
    texto = (
        f"{len(grupos)} lineas -> {len(todos)} planos "
        f"({min(largos):.2f}-{max(largos):.2f}s, "
        f"promedio {sum(largos) / len(largos):.2f}s)"
    )
    if fuera:
        texto += f" | {len(fuera)} por encima de {PLANO_MAX_S}s"
    return texto
