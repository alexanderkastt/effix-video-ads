"""Reparto de clips sobre la canción, para el modo `musical_sync`.

Antes había una correspondencia rígida: una línea de la letra, un clip. Eso ató
la unidad de PAGO (el clip) a la unidad de GUION (la línea), y con Kling —que
sólo vende tramos de 5 o 10s— obligaba a estirar clips cortos y a reencuadrar
los largos hasta que el mismo material se veía tres veces.

Seedance acepta de 4 a 12 segundos, así que la unidad de pago pasa a ser una
rejilla regular de clips cortos sobre la canción entera. Una línea larga recibe
varios clips distintos —material nuevo, no reencuadres del mismo— y una línea
corta comparte el suyo con la vecina.

Y como Seedance acepta frame final, el reparto decide además dónde encadenar:

- El clip que **cierra una línea** lleva `end_image` = la escena de la línea
  siguiente. La transición entre dos ideas del guion deja de ser un corte seco
  y pasa a ser un movimiento continuo, que es de donde sale la sensación de que
  el ad está estructurado.
- Los clips **intermedios dentro de una misma línea** van sin frame final: ahí
  se quiere movimiento libre, y con cuatro segundos no da tiempo a que el
  personaje derive.
- El **último clip del ad** cierra sin destino.
"""

from __future__ import annotations

import math
from typing import Any

# Por debajo de esto un hueco no da para un plano: se funde con el anterior.
PISO_TRAMO_S = 1.25


def repartir_clips(
    lineas: list[dict[str, Any]],
    tramos: list[tuple[float, float]],
    duracion_s: float,
    *,
    dur_clip: int = 4,
) -> list[dict[str, Any]]:
    """La rejilla de clips que cubre la canción, cada uno atado a su línea.

    Devuelve, por clip: su hueco en el montaje (`t0`/`t1`), de qué línea toma
    la imagen (`linea`) y, si toca encadenar, hacia qué línea va (`end_linea`).
    """
    if duracion_s <= 0 or not lineas:
        return []

    cuantos = max(1, math.ceil(duracion_s / dur_clip))
    plan: list[dict[str, Any]] = []
    for i in range(cuantos):
        t0 = round(i * dur_clip, 3)
        t1 = round(min(t0 + dur_clip, duracion_s), 3)
        # La línea del clip es la que está sonando en su punto medio: así un
        # clip a caballo entre dos versos se queda con el que más ocupa.
        centro = (t0 + t1) / 2
        idx = next(
            (j for j, (a, b) in enumerate(tramos) if a <= centro < b),
            len(tramos) - 1,
        )
        plan.append({
            "i": i, "t0": t0, "t1": t1,
            "idx": idx, "linea": lineas[idx]["n"],
        })

    # El último hueco de la rejilla casi nunca cae redondo: con 68.05s y clips
    # de 4s sobran 0.05, y eso montado es un plano de un frame que se ve como
    # un parpadeo. Se le regala al clip anterior, que pasa a durar un pelo más.
    if len(plan) > 1 and (plan[-1]["t1"] - plan[-1]["t0"]) < PISO_TRAMO_S:
        plan[-2]["t1"] = plan[-1]["t1"]
        plan.pop()

    for i, clip in enumerate(plan):
        siguiente = plan[i + 1] if i + 1 < len(plan) else None
        # Sólo se encadena en el salto de una línea a otra. Dentro de la misma
        # línea, el frame final ataría al modelo sin necesidad.
        clip["end_linea"] = (
            lineas[siguiente["idx"]]["n"]
            if siguiente and siguiente["idx"] != clip["idx"]
            else None
        )
    return plan


def resumen(plan: list[dict[str, Any]]) -> str:
    """Una línea para la consola: cuántos clips y cuántos van encadenados."""
    if not plan:
        return "sin clips"
    encadenados = sum(1 for c in plan if c["end_linea"])
    lineas = len({c["idx"] for c in plan})
    return (f"{len(plan)} clips de {plan[0]['t1'] - plan[0]['t0']:.0f}s sobre "
            f"{lineas} líneas · {encadenados} encadenados con frame final")
