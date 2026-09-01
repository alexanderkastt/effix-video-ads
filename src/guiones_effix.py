"""Arma los guiones de Feria Effix: nicho + pase + gancho → clips de 4 segundos.

Reemplaza la cadena anterior (`microsituaciones` + `narracion_hablada`), que
estaba construida sobre ángulos de dolor genéricos. Aquí el nicho es un vertical
de audiencia real — un contador, un importador, un laboratorio — y cada uno trae
su propia micro-situación de siete pasos.
"""

from __future__ import annotations

from typing import Any

from .narracion_effix import (
    BEATS_CON_AIRE, CTA_POR_PASE, PALABRAS_POR_SEGUNDO, PASE_POR_DEFECTO,
    clips_del_beat, cta_de, hablado_de,
)
from .nichos_effix import NICHOS, nichos_disponibles, obtener

from .plan_clips import DURACION_CLIP_S  # la ventana la fija el .env
MIN_VIDEO_S = 30
MAX_VIDEO_S = 60

# Los doce beats: los siete del framework de micro-situaciones más los cinco
# que cierran la venta.
BEATS = [
    {"n": 1,  "nombre": "MOMENTO",       "campo": "momento",             "emoji": "🪝", "emocion": "reconocimiento"},
    {"n": 2,  "nombre": "SÍNTOMA",       "campo": "sintoma",             "emoji": "🫵", "emocion": "auto_relevancia"},
    {"n": 3,  "nombre": "REACCIÓN",      "campo": "reaccion_interna",    "emoji": "😔", "emocion": "identificacion"},
    {"n": 4,  "nombre": "EXPL. FALLIDA", "campo": "explicacion_fallida", "emoji": "🤷", "emocion": "baja_resistencia"},
    {"n": 5,  "nombre": "PATRÓN",        "campo": "patron",              "emoji": "🔁", "emocion": "tension"},
    {"n": 6,  "nombre": "CAUSA RAÍZ",    "campo": "causa_raiz",          "emoji": "💡", "emocion": "cambio_creencia"},
    {"n": 7,  "nombre": "MECANISMO",     "campo": "mecanismo",           "emoji": "⚙️", "emocion": "claridad"},
    {"n": 8,  "nombre": "PRUEBA",        "campo": "prueba_social",       "emoji": "🤝", "emocion": "confianza"},
    {"n": 9,  "nombre": "VISUALIZACIÓN", "campo": "visualizacion",       "emoji": "🎬", "emocion": "aspiracion"},
    {"n": 10, "nombre": "CTA",           "campo": "urgencia_cta",        "emoji": "🎟️", "emocion": "oportunidad"},
    {"n": 11, "nombre": "DEFECTO",       "campo": "defecto_admitido",    "emoji": "🫱", "emocion": "honestidad"},
    {"n": 12, "nombre": "LOOP",          "campo": "loop_rewatch",        "emoji": "♻️", "emocion": "pertenencia"},
]

# El encuadre cambia con la carga emocional del beat
MOVIMIENTO = {
    1: "closeup", 2: "handheld", 3: "static", 4: "handheld", 5: "dolly-in",
    6: "closeup", 7: "dolly-in", 8: "pan", 9: "pan", 10: "closeup",
    11: "static", 12: "handheld",
}

# Tipo de clip: B cuando el beat cambia de estado, C cuando se sostiene
TIPO_CLIP = {
    1: "A", 2: "C", 3: "C", 4: "A", 5: "A", 6: "B",
    7: "B", 8: "A", 9: "A", 10: "C", 11: "C", 12: "B",
}


def construir_beats(
    nicho: str,
    pase: str = PASE_POR_DEFECTO,
    hook_variante: str = "A",
) -> list[dict[str, Any]]:
    """Los doce beats de un guión, con su narración, overlay y encuadre."""
    datos = obtener(nicho)
    lineas = hablado_de(nicho)
    overlays = datos["overlays"]
    hooks = datos["hooks"]

    indice = {"A": 0, "B": 1, "C": 2}.get(hook_variante, 0)
    hook = hooks[min(indice, len(hooks) - 1)]
    cta = cta_de(pase)

    beats: list[dict[str, Any]] = []
    for meta in BEATS:
        n = meta["n"]

        if n == 1:
            narracion, overlay = hook["hablado"], hook["overlay"]
        elif n == 10:
            narracion, overlay = cta["hablado"], cta["overlay"]
        else:
            narracion, overlay = lineas[n - 1], overlays[n - 1]

        palabras = len(narracion.split())
        beats.append(
            {
                "beat": n,
                "nombre": meta["nombre"],
                "emoji": meta["emoji"],
                "emocion": meta["emocion"],
                "componente_microsituacion": meta["campo"],
                "narracion": narracion,
                "palabras_narracion": palabras,
                "locucion_s": round(palabras / PALABRAS_POR_SEGUNDO, 1),
                "texto_pantalla": overlay,
                "investigacion": datos.get(meta["campo"], ""),
                "clips": clips_del_beat(n),
                "movimiento_camara": MOVIMIENTO[n],
                "tipo_clip": TIPO_CLIP[n],
            }
        )

    # Codas: los beats con aire ocupan dos clips y el segundo venía sosteniendo
    # la imagen en silencio. Una coda le pone voz a ese segundo clip sin
    # alargar el video ni robarle fuerza al beat. Se usan para lo que la
    # estructura de doce beats no tiene sitio propio: el callout de identidad
    # (beat 1, entre el MOMENTO y el SÍNTOMA) y las fechas del evento (beat 7,
    # que el CTA del pase no dice). Los nichos que no las definen quedan igual.
    for numero, coda in (datos.get("codas") or {}).items():
        beat = beats[numero - 1]
        if beat["clips"] >= 2:
            beat["coda"] = coda

    return beats


def expandir_a_clips(beats: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convierte los beats en la secuencia real de clips de 4 segundos.

    Un beat de dos clips son dos escenas distintas del mismo beat: la locución
    entra en el primero y el segundo la sostiene con otro encuadre, para que el
    corte se lea como corte y no como error de montaje.
    """
    alterno = {"closeup": "pan", "handheld": "closeup", "static": "dolly-in",
               "dolly-in": "static", "pan": "handheld"}
    clips: list[dict[str, Any]] = []
    numero = 1

    for beat in beats:
        for i in range(beat["clips"]):
            clip = dict(beat)
            clip.update({
                "clip": numero,
                "duracion_s": DURACION_CLIP_S,
                "beat_origen": beat["beat"],
                "escena_del_beat": i + 1,
                "escenas_del_beat": beat["clips"],
                "lleva_narracion": i == 0,
                "t_inicio_s": (numero - 1) * DURACION_CLIP_S,
                "t_fin_s": numero * DURACION_CLIP_S,
            })
            if i > 0:
                clip["movimiento_camara"] = alterno.get(beat["movimiento_camara"], "handheld")
            if i == 1 and beat.get("coda"):
                coda = beat["coda"]
                clip.update({
                    "nombre": coda.get("nombre", beat["nombre"]),
                    "emoji": coda.get("emoji", beat["emoji"]),
                    "emocion": coda.get("emocion", beat["emocion"]),
                    "componente_microsituacion": "coda",
                    "narracion": coda["hablado"],
                    "palabras_narracion": len(coda["hablado"].split()),
                    "texto_pantalla": coda["overlay"],
                    "lleva_narracion": True,
                })
            clips.append(clip)
            numero += 1

    return clips


def resumen_de(beats: list[dict[str, Any]]) -> dict[str, Any]:
    """Duración, clips y holgura de un guión."""
    clips = sum(b["clips"] for b in beats)
    palabras = sum(b["palabras_narracion"] for b in beats)
    palabras += sum(
        len(b["coda"]["hablado"].split()) for b in beats if b.get("coda")
    )
    locucion = round(palabras / PALABRAS_POR_SEGUNDO, 1)
    video = clips * DURACION_CLIP_S

    return {
        "total_clips": clips,
        "duracion_s": video,
        "palabras": palabras,
        "locucion_s": locucion,
        "holgura_s": round(video - locucion, 1),
        "en_rango": MIN_VIDEO_S <= video <= MAX_VIDEO_S,
    }


def construir_guion(
    nicho: str,
    pase: str = PASE_POR_DEFECTO,
    hook_variante: str = "A",
) -> dict[str, Any]:
    """Un guión completo, listo para storyboard."""
    datos = obtener(nicho)
    beats = construir_beats(nicho, pase, hook_variante)

    return {
        "nicho": nicho,
        "etiqueta": datos["etiqueta"],
        "audiencia": datos["audiencia"],
        "ancla": datos["ancla"],
        "gatillo_principal": datos["gatillo_principal"],
        "pase": pase,
        "cta": cta_de(pase),
        "hook_variante": hook_variante,
        "visual_clave": datos["visual_clave"],
        "visual_clave_en": datos["visual_clave_en"],
        "beats": beats,
        "linea_tiempo": expandir_a_clips(beats),
        **resumen_de(beats),
    }


def validar(guion: dict[str, Any]) -> list[str]:
    """Comprueba lo que no puede fallar en un guión listo para producir."""
    errores: list[str] = []

    if not guion["en_rango"]:
        errores.append(
            f"{guion['duracion_s']}s fuera del rango {MIN_VIDEO_S}-{MAX_VIDEO_S}s."
        )

    if len(guion["beats"]) != 12:
        errores.append(f"{len(guion['beats'])} beats, se esperan 12.")

    clips = guion["linea_tiempo"]
    for i in range(len(clips) - 1):
        if clips[i]["t_fin_s"] != clips[i + 1]["t_inicio_s"]:
            errores.append(f"Hueco entre el clip {clips[i]['clip']} y el siguiente.")
    if any(c["duracion_s"] != DURACION_CLIP_S for c in clips):
        errores.append("Hay clips que no duran 4 segundos.")

    for b in guion["beats"]:
        if len(b["texto_pantalla"].split()) > 7:
            errores.append(f"Beat {b['beat']:02d}: overlay de más de 7 palabras.")

    return errores or ["OK"]
