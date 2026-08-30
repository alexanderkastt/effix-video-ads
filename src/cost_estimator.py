"""Estimación de costo antes de producir.

Los precios viven en `config/costos.json` y hoy están en cero con
`verificado: false`. Este módulo NO inventa tarifas: si el archivo no tiene
precios reales cargados, lo dice en vez de devolver un número inventado.

MASTER_CONTEXT.md ya documenta el error de hacer un preflight con parámetros
distintos a los finales: subestimó el costo real en más del doble.
"""

from __future__ import annotations

import json
from typing import Any

from .paths import CONFIG_DIR

COSTOS_JSON = CONFIG_DIR / "costos.json"


def _cargar() -> dict[str, Any]:
    if not COSTOS_JSON.exists():
        return {"verificado": False}
    with COSTOS_JSON.open(encoding="utf-8") as fh:
        return json.load(fh)


def estimar(
    n_clips: int,
    duracion_clip_s: int,
    modelo_fal: str,
    caracteres_voz: int,
    modelo_voz: str = "eleven_multilingual_v2",
    con_musica: bool = False,
) -> dict[str, Any]:
    """Devuelve el desglose de costo estimado y si es confiable."""
    tarifas = _cargar()
    verificado = bool(tarifas.get("verificado", False))

    precio_video_s = tarifas.get("fal_ai", {}).get(modelo_fal, 0.0)
    precio_voz_1k = tarifas.get("elevenlabs", {}).get(modelo_voz, 0.0)
    precio_cancion = tarifas.get("suno", {}).get("cancion", 0.0)

    segundos = n_clips * duracion_clip_s
    costo_video = segundos * precio_video_s
    costo_voz = (caracteres_voz / 1000) * precio_voz_1k
    costo_musica = precio_cancion if con_musica else 0.0
    total = costo_video + costo_voz + costo_musica

    return {
        "verificado": verificado,
        "moneda": tarifas.get("moneda", "USD"),
        "segundos_video": segundos,
        "caracteres_voz": caracteres_voz,
        "costo_video": round(costo_video, 4),
        "costo_voz": round(costo_voz, 4),
        "costo_musica": round(costo_musica, 4),
        "total": round(total, 4),
        "aviso": (
            ""
            if verificado
            else "Tarifas sin verificar en config/costos.json — este total no sirve "
                 "para decidir presupuesto. Medir una generación real y actualizarlo."
        ),
    }


def formatear(est: dict[str, Any]) -> str:
    """Línea legible para mostrar en el CLI."""
    if not est["verificado"]:
        return (
            f"💰 Costo estimado: SIN CALCULAR "
            f"({est['segundos_video']}s de video · {est['caracteres_voz']} caracteres de voz)\n"
            f"   ⚠️  {est['aviso']}"
        )
    return (
        f"💰 Costo estimado: {est['total']} {est['moneda']} "
        f"(video {est['costo_video']} · voz {est['costo_voz']} · música {est['costo_musica']})"
    )
