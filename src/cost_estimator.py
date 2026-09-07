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


# Alto x ancho reales de cada resolucion en 9:16, para el cobro por tokens.
_RESOLUCIONES_TOKENS = {"480p": (480, 854), "720p": (720, 1280),
                        "1080p": (1080, 1920)}


def estimar(
    n_clips: int,
    duracion_clip_s: int,
    modelo_fal: str,
    caracteres_voz: int,
    modelo_voz: str = "eleven_multilingual_v2",
    # Ojo: `con_musica=True` es el caso RARO, no el normal. Todo ad lleva
    # música, pero sale de la librería del repo y no cuesta nada. Esto solo se
    # enciende cuando el ad pide componer una pista propia porque el catálogo
    # no tiene su mood.
    con_musica: bool = False,
    n_imagenes: int = 0,
    modelo_imagen: str = "fal-ai/nano-banana-2",
    # Modo `musical_sync`: la pista no es una cama de librería sino una canción
    # cantada que se paga por pieza. Cuando viene, manda sobre `con_musica`.
    modelo_cancion: str | None = None,
    # Sólo para modelos que cobran por minuto.
    duracion_cancion_ms: int | None = None,
    # Gastos sueltos que no encajan en ninguna de las cuatro columnas: hoy la
    # transcripción con whisper, que cuesta centavos pero no es cero.
    costo_extras: float = 0.0,
    # Modelos que cobran por tokens de video (Seedance) y no por segundo: el
    # precio depende de la resolucion y los fps, no solo de la duracion.
    resolucion: str = "1080p",
    fps: int = 24,
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
    # Seedance y compania cobran por tokens: (alto x ancho x fps x seg) / 1024,
    # pagados por millon. Si se buscara solo la tarifa por segundo el video
    # saldria en cero y el presupuesto entero quedaria mal medido.
    por_millon = tarifas.get("fal_ai_por_unidad", {}).get(
        f"{modelo_fal}__por_millon_tokens")
    if por_millon is not None:
        alto, ancho = _RESOLUCIONES_TOKENS.get(
            resolucion, _RESOLUCIONES_TOKENS["1080p"])
        tokens = (alto * ancho * fps * segundos) / 1024
        costo_video = tokens / 1_000_000 * por_millon
    else:
        costo_video = segundos * precio_video_s
    costo_voz = (caracteres_voz / 1000) * precio_voz_1k
    if modelo_cancion:
        unidad = tarifas.get("fal_ai_por_unidad", {})
        # Dos formas de cobrar una canción: por pieza (MiniMax) o por minuto
        # (ElevenLabs Music, que a cambio acepta duración objetivo).
        ms = duracion_cancion_ms or 58000
        por_minuto = unidad.get(f"{modelo_cancion}__por_minuto")
        por_segundo = unidad.get(f"{modelo_cancion}__por_segundo")
        if por_minuto is not None:
            costo_musica = por_minuto * ms / 60000
        elif por_segundo is not None:
            costo_musica = por_segundo * ms / 1000
        else:
            costo_musica = unidad.get(f"{modelo_cancion}__por_cancion", 0.0)
    else:
        costo_musica = precio_cancion if con_musica else 0.0
    costo_imagenes = n_imagenes * precio_imagen
    total = costo_video + costo_voz + costo_musica + costo_imagenes + costo_extras

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
        "costo_extras": round(costo_extras, 4),
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
    partes = [
        f"video {est['costo_video']}",
        f"imágenes {est.get('costo_imagenes', 0)}",
        f"voz {est['costo_voz']}",
        f"música {est['costo_musica']}",
    ]
    if est.get("costo_extras"):
        partes.append(f"extras {est['costo_extras']}")
    linea = (
        f"💰 Costo estimado: {est['total']} {est['moneda']} "
        f"({' · '.join(partes)})"
    )
    p = est.get("presupuesto", {})
    if p.get("estado") == "dentro":
        return f"{linea}\n   ✅ dentro del promedio de {p['objetivo_promedio']:.2f} por video"
    if p.get("aviso"):
        marca = "⚠️ " if p["estado"] == "sobre_el_promedio" else "🛑 "
        return f"{linea}\n   {marca}{p['aviso']}"
    return linea
