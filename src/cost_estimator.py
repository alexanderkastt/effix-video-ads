"""Estimación de costo antes de producir.

Los precios viven en `config/costos.json` y hoy están en cero con
`verificado: false`. Este módulo NO inventa tarifas: si el archivo no tiene
precios reales cargados, lo dice en vez de devolver un número inventado.

MASTER_CONTEXT.md ya documenta el error de hacer un preflight con parámetros
distintos a los finales: subestimó el costo real en más del doble.

**Presupuesto:** cada ad se planifica para caber en 5 USD en promedio, con 6 USD
de tope por video. El objetivo vive en `config/costos.json` → `presupuesto`, y
`estimar()` devuelve el veredicto contra él: un total que se pasa no bloquea
nada, pero obliga a avisar y proponer el recorte ANTES de gastar.
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


def presupuesto() -> dict[str, Any]:
    """El objetivo de gasto por video, tal como está fijado en el config."""
    p = _cargar().get("presupuesto", {})
    return {
        "objetivo_promedio": float(p.get("objetivo_promedio", 5.0)),
        "tope_por_video": float(p.get("tope_por_video", 6.0)),
        "regla": p.get("regla", ""),
        "palancas": p.get("palancas", []),
    }


def contra_presupuesto(total: float) -> dict[str, Any]:
    """Compara un total contra el objetivo y dice qué hacer si se pasa.

    No bloquea: el que decide si un ad vale seis dólares es Alexander. Lo que
    no puede pasar es que se entere cuando ya está pagado.
    """
    p = presupuesto()
    objetivo, tope = p["objetivo_promedio"], p["tope_por_video"]
    if total <= objetivo:
        estado, aviso = "dentro", ""
    elif total <= tope:
        estado = "sobre_el_promedio"
        aviso = (f"{total:.2f} USD pasa el promedio de {objetivo:.2f} pero cabe bajo el "
                 f"tope de {tope:.2f}. Vale si otro ad de la tanda queda por debajo.")
    else:
        estado = "sobre_el_tope"
        aviso = (f"{total:.2f} USD supera el tope de {tope:.2f} por video. Avisar y "
                 f"proponer recorte antes de gastar: " + " · ".join(p["palancas"]))
    return {"estado": estado, "objetivo_promedio": objetivo, "tope_por_video": tope,
            "exceso": round(max(0.0, total - objetivo), 2), "aviso": aviso}


def estimar(
    n_clips: int,
    duracion_clip_s: int,
    modelo_fal: str,
    caracteres_voz: int,
    modelo_voz: str = "eleven_multilingual_v2",
    con_musica: bool = False,
    n_imagenes: int = 0,
    modelo_imagen: str = "fal-ai/nano-banana-2",
) -> dict[str, Any]:
    """Devuelve el desglose de costo estimado, si es confiable y si cabe en el
    presupuesto.

    Las imágenes cuentan: un ad de nueve planos con keyframes lleva diecisiete,
    y dejarlas fuera del cálculo esconde más de un dólar — la quinta parte del
    presupuesto de un video.
    """
    tarifas = _cargar()
    verificado = bool(tarifas.get("verificado", False))

    precio_video_s = tarifas.get("fal_ai", {}).get(modelo_fal, 0.0)
    precio_voz_1k = tarifas.get("elevenlabs", {}).get(modelo_voz, 0.0)
    precio_cancion = tarifas.get("suno", {}).get("cancion", 0.0)
    precio_imagen = tarifas.get("fal_ai_por_unidad", {}).get(
        f"{modelo_imagen}__por_imagen", 0.0)

    segundos = n_clips * duracion_clip_s
    costo_video = segundos * precio_video_s
    costo_voz = (caracteres_voz / 1000) * precio_voz_1k
    costo_musica = precio_cancion if con_musica else 0.0
    costo_imagenes = n_imagenes * precio_imagen
    total = costo_video + costo_voz + costo_musica + costo_imagenes

    return {
        "verificado": verificado,
        "moneda": tarifas.get("moneda", "USD"),
        "segundos_video": segundos,
        "caracteres_voz": caracteres_voz,
        "n_imagenes": n_imagenes,
        "costo_video": round(costo_video, 4),
        "costo_voz": round(costo_voz, 4),
        "costo_musica": round(costo_musica, 4),
        "costo_imagenes": round(costo_imagenes, 4),
        "total": round(total, 4),
        "presupuesto": contra_presupuesto(total),
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
    linea = (
        f"💰 Costo estimado: {est['total']} {est['moneda']} "
        f"(video {est['costo_video']} · imágenes {est.get('costo_imagenes', 0)} · "
        f"voz {est['costo_voz']} · música {est['costo_musica']})"
    )
    p = est.get("presupuesto", {})
    if p.get("estado") == "dentro":
        return f"{linea}\n   ✅ dentro del promedio de {p['objetivo_promedio']:.2f} por video"
    if p.get("aviso"):
        marca = "⚠️ " if p["estado"] == "sobre_el_promedio" else "🛑 "
        return f"{linea}\n   {marca}{p['aviso']}"
    return linea
