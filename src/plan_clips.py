"""Planificador de clips — corte cada 4s, video final entre 30 y 60 segundos.

Dos unidades distintas, y confundirlas es lo que rompía el formato:

- **Beat narrativo**: uno de los once pasos de la micro-situación. Dura lo que
  dura su línea hablada.
- **Clip**: 4 segundos exactos de video generado. Es la unidad de corte.

Un beat que habla 7 segundos NO se convierte en un plano largo de 7 segundos:
se convierte en DOS clips de 4s, dos escenas distintas contando el mismo beat.
El corte visual sigue cayendo cada 4 segundos.

    total_clips = Σ ceil(locución_del_beat / 4)
    duración     = total_clips × 4  →  debe caer entre 30 y 60 s

Si se pasa de 60s hay que recortar texto; si no llega a 30s, hay que darle aire.
`planificar()` lo dice con números en vez de dejarlo para el montaje.

ORDEN DE PRODUCCIÓN — el audio manda
    1. `planificar()` estima a 2.2 palabras/segundo. Sirve para presupuestar
       ANTES de gastar: cuántos clips van a hacer falta, cuánto va a costar.
    2. Se genera la voz en ElevenLabs.
    3. `planificar_desde_audio()` mide el mp3 real con ffprobe y recalcula los
       clips sobre ese dato.
    4. Recién ahí se generan los videos.

    Al revés se generan clips que no cuadran con la locución y hay que
    regenerarlos pagando de nuevo. La estimación es para decidir; el audio es
    para producir.
"""

from __future__ import annotations

import math
import os
import subprocess
from pathlib import Path
from typing import Any

from .paths import env_int

# Kling no vende segundos sueltos: cobra tramos de 5 o de 10. Con la ventana
# en 4s cada clip paga cinco segundos y usa cuatro — un 20% del gasto de video
# que nadie ve. En 5s se paga lo mismo por clip y hacen falta menos clips para
# cubrir el mismo audio. Se deja en el .env porque el ritmo de corte es
# decisión de estilo: 4s va mejor en UGC, 5s en lo cinematográfico.
DURACION_CLIP_S = env_int("DURACION_CLIP_S", 4)
MIN_VIDEO_S = 30
MAX_VIDEO_S = 60
# Medido el 2026-08-30 sobre la locucion real del ad de dropshipping: 107
# palabras en 36,13s con la voz "Medellin - Conversational and Intense" y
# ELEVENLABS_SPEED=0.83. El 2.2 anterior era una estimacion de escritorio y
# sobredimensionaba la locucion en un 34%, que se traducia en clips de mas.
PALABRAS_POR_SEGUNDO = 2.96

# Cola después de que termina la voz: el video no corta en seco sobre la
# última sílaba, pero tampoco sigue corriendo en silencio.
COLA_FINAL_S = 0.4

MIN_CLIPS = MIN_VIDEO_S // DURACION_CLIP_S          # 7 clips = 28s → se redondea a 8
MAX_CLIPS = MAX_VIDEO_S // DURACION_CLIP_S          # 15 clips = 60s


def clips_para(texto: str) -> int:
    """Cuántos clips de 4s necesita una línea hablada. Mínimo uno."""
    segundos = len(texto.split()) / PALABRAS_POR_SEGUNDO
    return max(1, math.ceil(segundos / DURACION_CLIP_S))


def planificar(beats: list[dict[str, Any]]) -> dict[str, Any]:
    """Reparte los beats en clips de 4s y valida el rango 30-60s.

    Devuelve el plan completo: cuántos clips lleva cada beat, la duración final,
    y si cae dentro del rango. No modifica los beats.
    """
    reparto: list[dict[str, Any]] = []
    total_clips = 0

    for beat in beats:
        texto = beat.get("narracion", "")
        n_clips = clips_para(texto)
        locucion = round(len(texto.split()) / PALABRAS_POR_SEGUNDO, 1)

        reparto.append(
            {
                "beat": beat.get("beat"),
                "nombre": beat.get("nombre", ""),
                "palabras": len(texto.split()),
                "locucion_s": locucion,
                "clips": n_clips,
                "duracion_s": n_clips * DURACION_CLIP_S,
                "holgura_s": round(n_clips * DURACION_CLIP_S - locucion, 1),
                "clip_inicial": total_clips + 1,
            }
        )
        total_clips += n_clips

    duracion = total_clips * DURACION_CLIP_S
    palabras = sum(r["palabras"] for r in reparto)
    locucion_total = round(palabras / PALABRAS_POR_SEGUNDO, 1)

    if duracion > MAX_VIDEO_S:
        estado = "largo"
        sobran = duracion - MAX_VIDEO_S
        recorte = math.ceil((locucion_total - MAX_VIDEO_S) * PALABRAS_POR_SEGUNDO)
        diagnostico = (
            f"Se pasa {sobran}s del techo de {MAX_VIDEO_S}s. "
            f"Recortar ~{max(recorte, 0)} palabras de locución."
        )
    elif duracion < MIN_VIDEO_S:
        estado = "corto"
        faltan = MIN_VIDEO_S - duracion
        diagnostico = (
            f"Faltan {faltan}s para el piso de {MIN_VIDEO_S}s. "
            f"Agregar {math.ceil(faltan / DURACION_CLIP_S)} clip(s): "
            f"dar dos escenas a los beats con más carga."
        )
    else:
        estado = "ok"
        diagnostico = f"{duracion}s — dentro del rango {MIN_VIDEO_S}-{MAX_VIDEO_S}s."

    return {
        "total_clips": total_clips,
        "duracion_s": duracion,
        "duracion_clip_s": DURACION_CLIP_S,
        "palabras": palabras,
        "locucion_s": locucion_total,
        "holgura_total_s": round(duracion - locucion_total, 1),
        "estado": estado,
        "en_rango": estado == "ok",
        "diagnostico": diagnostico,
        "reparto": reparto,
    }


def expandir_a_clips(beats: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convierte los beats en la lista real de clips de 4s.

    Cada clip hereda la narración de su beat, pero es una escena distinta: el
    campo `escena_del_beat` numera cuál de las escenas del beat le toca, para
    que el director le dé un encuadre y una acción propios.
    """
    clips: list[dict[str, Any]] = []
    numero = 1

    for beat in beats:
        n_clips = clips_para(beat.get("narracion", ""))
        for i in range(n_clips):
            clip = dict(beat)
            clip.update(
                {
                    "clip": numero,
                    "duracion_s": DURACION_CLIP_S,
                    "beat_origen": beat.get("beat"),
                    "escena_del_beat": i + 1,
                    "escenas_del_beat": n_clips,
                    # La locución completa del beat va en su primer clip; los
                    # siguientes son continuación visual del mismo texto.
                    "lleva_narracion": i == 0,
                    "t_inicio_s": (numero - 1) * DURACION_CLIP_S,
                    "t_fin_s": numero * DURACION_CLIP_S,
                }
            )
            clips.append(clip)
            numero += 1

    return clips


# ---------------------------------------------------------------------------
# El audio manda: primero se locuta, después se decide cuántos clips
# ---------------------------------------------------------------------------

def medir_audio(path: str | Path) -> float:
    """Duración real de un archivo de audio, en segundos, con ffprobe.

    Las 2.2 palabras/segundo son una estimación para presupuestar antes de
    gastar. Esto es el dato: ElevenLabs no locuta a velocidad constante, y con
    `ELEVENLABS_SPEED=0.83` la diferencia contra la estimación es grande.
    """
    ruta = Path(path)
    if not ruta.exists():
        raise FileNotFoundError(f"No encuentro el audio en {ruta}")

    salida = subprocess.run(
        [
            os.getenv("FFPROBE_BIN", "ffprobe"),
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(ruta),
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    return round(float(salida.stdout.strip()), 3)


def planificar_desde_audio(
    beats: list[dict[str, Any]],
    audios: dict[int, str | Path] | None = None,
    duraciones: dict[int, float] | None = None,
) -> dict[str, Any]:
    """Reparte los clips a partir del audio REAL, no de la estimación.

    Este es el orden correcto de producción: primero se genera la voz, se mide
    lo que dura de verdad, y recién entonces se decide cuántos clips de 4s hacen
    falta. Al revés se generan clips que no cuadran con la locución y hay que
    tirar plata regenerando.

    `audios` es {numero_de_beat: ruta_al_mp3}; `duraciones` permite pasar los
    segundos ya medidos sin volver a llamar a ffprobe.
    """
    if not audios and not duraciones:
        raise ValueError(
            "planificar_desde_audio necesita el audio ya generado. "
            "Para presupuestar antes de gastar, usá planificar()."
        )

    medidas: dict[int, float] = dict(duraciones or {})
    for n, ruta in (audios or {}).items():
        if n not in medidas:
            medidas[n] = medir_audio(ruta)

    # Línea de tiempo continua: los beats se encadenan uno tras otro y el corte
    # cada 4s cae encima, global. Redondear cada beat por separado paga video
    # que nadie ve: un beat de 4.3s se llevaba dos clips enteros (8s) para
    # cubrir 4.3s de voz. Sobre la línea continua, ese sobrante lo aprovecha el
    # beat siguiente.
    linea: list[dict[str, Any]] = []
    t = 0.0

    for beat in beats:
        n = beat.get("beat")
        real = medidas.get(n)
        if real is None:
            raise KeyError(
                f"Falta el audio del beat {n}. Todos los beats necesitan su "
                f"locución medida antes de repartir clips."
            )
        estimado = round(len(beat.get("narracion", "").split()) / PALABRAS_POR_SEGUNDO, 1)
        linea.append(
            {
                "beat": n,
                "nombre": beat.get("nombre", ""),
                "t_inicio_s": round(t, 2),
                "t_fin_s": round(t + real, 2),
                "locucion_real_s": real,
                "locucion_estimada_s": estimado,
                "desvio_s": round(real - estimado, 2),
            }
        )
        t += real

    audio_total = round(t, 2)
    total_clips = max(1, math.ceil(audio_total / DURACION_CLIP_S))
    video = total_clips * DURACION_CLIP_S

    # Cada clip cubre su ventana de 4s; le toca la escena del beat que más
    # tiempo ocupa dentro de ella.
    for entrada in linea:
        primero = int(entrada["t_inicio_s"] // DURACION_CLIP_S) + 1
        ultimo = max(primero, math.ceil(entrada["t_fin_s"] / DURACION_CLIP_S))
        entrada["clip_inicial"] = primero
        entrada["clip_final"] = min(ultimo, total_clips)
        entrada["clips"] = entrada["clip_final"] - primero + 1

    reparto = linea

    # El video se corta a la duración del audio más una cola corta: el último
    # clip queda parcial, que es lo normal en montaje. Lo que no puede pasar es
    # que el video siga corriendo con la voz ya terminada.
    corte_final_s = round(min(video, audio_total + COLA_FINAL_S), 2)

    desvio_total = round(
        audio_total - sum(r["locucion_estimada_s"] for r in reparto), 2
    )

    if corte_final_s > MAX_VIDEO_S:
        estado, diagnostico = "largo", (
            f"El audio real dura {audio_total}s y el corte queda en {corte_final_s}s, "
            f"por encima del techo de {MAX_VIDEO_S}s. Recortar locución y regenerar la voz."
        )
    elif corte_final_s < MIN_VIDEO_S:
        estado, diagnostico = "corto", (
            f"El audio real dura {audio_total}s: {MIN_VIDEO_S - corte_final_s:.1f}s "
            f"por debajo del piso de {MIN_VIDEO_S}s."
        )
    else:
        estado, diagnostico = "ok", (
            f"{corte_final_s}s de video contra {audio_total}s de locución — "
            f"dentro del rango {MIN_VIDEO_S}-{MAX_VIDEO_S}s."
        )

    return {
        "fuente": "audio_real",
        "total_clips": total_clips,
        "duracion_clip_s": DURACION_CLIP_S,
        "video_bruto_s": video,
        "audio_total_s": audio_total,
        "corte_final_s": corte_final_s,
        "cola_s": round(corte_final_s - audio_total, 2),
        "desvio_vs_estimacion_s": desvio_total,
        "estado": estado,
        "en_rango": estado == "ok",
        "diagnostico": diagnostico,
        "reparto": reparto,
    }


def resumen(plan: dict[str, Any]) -> str:
    """Línea legible para el CLI."""
    icono = {"ok": "✅", "largo": "⚠️", "corto": "⚠️"}[plan["estado"]]
    return (
        f"{icono} {plan['total_clips']} clips × {DURACION_CLIP_S}s = "
        f"{plan['duracion_s']}s · locución {plan['locucion_s']}s · "
        f"holgura {plan['holgura_total_s']}s\n   {plan['diagnostico']}"
    )
