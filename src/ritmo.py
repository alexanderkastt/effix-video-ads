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
