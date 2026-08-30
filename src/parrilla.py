"""Parrilla de producción — 3 guiones por nicho, con formato distinto en cada uno.

Tres guiones del mismo nicho no son tres versiones del mismo video: son tres
apuestas distintas sobre la misma micro-situación. Lo que cambia entre ellas:

1. **El hook** (A, B o C) — tres entradas al mismo momento. Es lo que la guía
   manda probar: mismo ángulo, misma persona, distinta forma de entrar.
2. **El estilo visual** — ninguno se repite dentro del nicho.
3. **El nivel de conciencia y el objetivo** — el guión A ataca arriba del embudo,
   el B y el C cierran. Así la parrilla cubre alcance y conversión, no solo una.

Meta lo pide explícitamente: con Andromeda el sistema elige entre decenas de
millones de candidatos, así que **el volumen y la diversidad de creativos importan
más que el gancho perfecto**. Tres variantes distintas le dan al algoritmo tres
apuestas reales, no tres sinónimos.
"""

from __future__ import annotations

from typing import Any

from .estilos_especiales import estilos_especiales_disponibles
from .ganchos import categorias_para
from .guiones_effix import construir_guion, validar
from .narracion_effix import CTA_POR_PASE
from .nichos_effix import nichos_disponibles, obtener

# Los 14 estilos, ordenados para que la rotación reparta parejo entre los que
# son baratos de producir y los que no.
TODOS_LOS_ESTILOS = [
    "micro_doc_ugc",   # el más barato y el que mejor convierte en frío
    "crochet",
    "cinematic",
    "skeleton",
    "pixar_animado",
    "zack_films",
    "ugc_realista",
    "claymation",
    "cyberpunk",
    "object_talk",
    "anime",
    "minecraft",
    "musical_sync",
    "avengers",
]

# Qué papel cumple cada uno de los tres guiones de un nicho
ROLES = [
    {
        "id": "A",
        "papel": "Alcance — abre el nicho",
        "hook": "A",
        "nivel": "unaware",
        "objetivo": "alcance",
        "pase": "generico",
        "gatillo": "dejar_de_ganar",
        "nota": "Entra por el momento exacto. Todavía no vende un pase concreto.",
    },
    {
        "id": "B",
        "papel": "Conversión — el que cierra",
        "hook": "B",
        "nivel": "problem",
        "objetivo": "conversion",
        "pase": "pase_3_dias",
        "gatillo": "inclusion",
        "nota": "El caballo de batalla. Cierra en el Pasaporte: viernes a domingo, sin pedir permiso.",
    },
    {
        "id": "C",
        "papel": "Urgencia — pasa una vez al año",
        "hook": "C",
        "nivel": "solution",
        "objetivo": "conversion",
        "pase": "pase_3_dias_escasez",
        "gatillo": "escasez",
        "nota": "El evento pasa una vez al año y se llena. Escasez real, sin fecha que caduque.",
    },
]


def _estilos_para(indice_nicho: int) -> list[str]:
    """Tres estilos distintos por nicho, rotando para que se repartan parejo.

    Con 10 nichos × 3 guiones = 30 asignaciones sobre 14 estilos, cada uno sale
    dos veces salvo un par que salen tres. El desfase de 3 en 3 evita que dos
    nichos consecutivos compartan la misma terna.
    """
    n = len(TODOS_LOS_ESTILOS)
    return [TODOS_LOS_ESTILOS[(indice_nicho * 3 + i) % n] for i in range(3)]


def construir_parrilla(marca: str = "effix") -> dict[str, Any]:
    """Devuelve la parrilla completa: 10 nichos × 3 guiones."""
    nichos: list[dict[str, Any]] = []

    for i, nicho in enumerate(nichos_disponibles()):
        datos = obtener(nicho)
        estilos = _estilos_para(i)

        guiones: list[dict[str, Any]] = []
        for rol, estilo in zip(ROLES, estilos):
            g = construir_guion(nicho, pase=rol["pase"], hook_variante=rol["hook"])
            g.update({
                "id": f"{nicho}-{rol['id']}",
                "variante": rol["id"],
                "papel": rol["papel"],
                "nota_rol": rol["nota"],
                "gatillo_rol": rol["gatillo"],
                "estilo": estilo,
                "es_estilo_especial": estilo in estilos_especiales_disponibles(),
                "nivel": rol["nivel"],
                "objetivo": rol["objetivo"],
                "categorias_validas": categorias_para(rol["nivel"], rol["objetivo"]),
                "validacion": validar(g),
            })
            guiones.append(g)

        nichos.append({
            "nicho": nicho,
            "etiqueta": datos["etiqueta"],
            "audiencia": datos["audiencia"],
            "ancla": datos["ancla"],
            "gatillo_principal": datos["gatillo_principal"],
            "micro_situacion": {
                k: datos[k] for k in (
                    "momento", "sintoma", "reaccion_interna", "explicacion_fallida",
                    "patron", "causa_raiz", "mecanismo",
                )
            },
            "guiones": guiones,
        })

    total = sum(len(n["guiones"]) for n in nichos)
    segundos = sum(g["duracion_s"] for n in nichos for g in n["guiones"])
    clips = sum(g["total_clips"] for n in nichos for g in n["guiones"])

    return {
        "marca": marca,
        "nichos": nichos,
        "total_nichos": len(nichos),
        "total_guiones": total,
        "total_clips": clips,
        "total_segundos": segundos,
        "estilos_usados": sorted({g["estilo"] for n in nichos for g in n["guiones"]}),
    }


def verificar(parrilla: dict[str, Any]) -> list[str]:
    """Comprueba que la parrilla cumple lo que promete."""
    errores: list[str] = []

    if parrilla["total_nichos"] != 10:
        errores.append(f"{parrilla['total_nichos']} nichos, se esperan 10.")
    if parrilla["total_guiones"] != 30:
        errores.append(f"{parrilla['total_guiones']} guiones, se esperan 30.")

    for nicho in parrilla["nichos"]:
        estilos = [g["estilo"] for g in nicho["guiones"]]
        if len(set(estilos)) != len(estilos):
            errores.append(f"{nicho['nicho']}: repite estilo entre sus guiones ({estilos}).")

        hooks = [g["beats"][0]["narracion"] for g in nicho["guiones"]]
        if len(set(hooks)) != len(hooks):
            errores.append(f"{nicho['nicho']}: repite hook entre sus guiones.")

        for g in nicho["guiones"]:
            if g["validacion"] != ["OK"]:
                errores.append(f"{g['id']}: {g['validacion']}")
            # Un creativo que tiene que cerrar nunca lleva curiosidad
            if g["objetivo"] == "conversion" and "curiosidad" in g["categorias_validas"]:
                errores.append(f"{g['id']}: curiosidad en un creativo de conversión.")

    disponibles = set(TODOS_LOS_ESTILOS)
    faltan = disponibles - set(parrilla["estilos_usados"])
    if faltan:
        errores.append(f"Estilos sin usar en toda la parrilla: {', '.join(sorted(faltan))}.")

    return errores or ["OK"]
