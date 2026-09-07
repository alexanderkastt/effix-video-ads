"""Mezcla final de audio — la música debajo de la voz, con ducking de verdad.

Antes había tres mezclas distintas en tres archivos: el módulo canónico bajaba
la música al 25%, los dos scripts vivos al 13%, y uno de ellos tenía el
fade-out escrito a mano en el segundo 48 —correcto solo para ese video—. El
mismo ad sonaba distinto según por dónde se montara.

Lo que aquí se hace y antes no existía en ningún lado:

1. **Ducking real** con `sidechaincompress`: la música se hunde sola cuando
   alguien habla y vuelve a subir en los silencios. Bajarla a un volumen fijo
   obliga a elegir entre que se oiga o que no tape la voz; el sidechain no
   obliga a elegir.
2. **Fade-out derivado de la duración real**, no de un número escrito a mano.
3. **`loudnorm` en el master a −14 LUFS**, que es lo que piden Instagram,
   TikTok y YouTube. Sin esto cada ad sale a un volumen distinto y el de la
   competencia suena más fuerte en el mismo feed.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from .paths import env, env_float

# Loudness de destino. -14 LUFS es el estándar de las plataformas: subir más
# no hace que suene más fuerte, solo hace que la plataforma lo baje ella misma
# y de paso aplaste la dinámica.
LUFS_OBJETIVO = -14.0
TRUE_PEAK_MAX = -1.5

# Cuánto sube el pico al codificar a AAC. Medido con la misma pista: limitada a
# −1.5 el WAV sale a −1.4997 y el AAC a 192k a −0.38, es decir 1.1 dB de
# overshoot intersample. Con la canción del p02 —que MiniMax entregó ya
# clippeada, con picos de +1.79 dBFS— hizo falta llegar a 4.5: medido, con
# 3.0 el render salía a −0.69 y con 6.0 el loudness ya bajaba a −14.5. El
# loudness aguanta porque loudnorm fija los LUFS antes; esto sólo baja picos.
MARGEN_CODEC = 4.5

# Curvas de entrada y salida de la música. La entrada es corta porque el ad
# arranca con el gancho: un fade largo se come el primer segundo, que es el
# único que decide si alguien se queda.
FADE_IN_S = 0.8
FADE_OUT_S = 3.0


def _limitador() -> str:
    """Techo duro de true peak, detrás del loudnorm.

    `loudnorm` en una sola pasada estima el pico y a veces se queda corto: una
    canción de MiniMax Music 3, que viene masterizada caliente, salió a +0.1
    dBTP con el objetivo puesto en −1.5. Eso es clipping, y en el feed se oye
    como distorsión en los golpes.

    `alimiter` no estima: recorta. Cuesta cero y garantiza el techo que piden
    las plataformas, que es lo que el QA comprueba.

    Ojo con la unidad: `limit` es amplitud LINEAL entre 0.0625 y 1, no dB.
    Escribirle "-1.5dB" no da error — ffmpeg lo descarta en silencio y el
    limitador se queda en 1.0, o sea sin limitar, que es como pasó inadvertido
    la primera vez.

    Y se limita por debajo del objetivo a propósito. Medido sobre la misma
    pista: limitando a −1.5 el WAV sale a −1.4997, pero el mismo audio pasado a
    AAC 192k sube a −0.38. El codec reconstruye con picos intersample que no
    existían en la señal limitada, así que el techo hay que ponerlo
    `MARGEN_CODEC` más abajo para que el archivo ENTREGADO cumpla.
    """
    lineal = 10 ** ((TRUE_PEAK_MAX - MARGEN_CODEC) / 20)
    # `attack` por defecto son 5 ms y con eso los transitorios de una batería
    # se cuelan enteros: el p02 salía a +0.58 dBTP con el limitador puesto.
    # Medio milisegundo los caza sin que se oiga bombeo.
    return f"alimiter=limit={lineal:.4f}:attack=0.5:release=20:level=disabled"


def _ffmpeg(args: list[str]) -> None:
    proceso = subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error", *args],
        capture_output=True, text=True,
    )
    if proceso.returncode != 0:
        raise RuntimeError(f"ffmpeg falló:\n{proceso.stderr.strip()[:2000]}")


def cadena_audio(
    voz: str,
    musica: str,
    salida: str,
    *,
    duracion_s: float,
    volumen: float | None = None,
) -> str:
    """El filtro de mezcla, para meter dentro de un filter_complex más grande.

    `voz` y `musica` son etiquetas de entrada ya existentes (`0:a`, `[aud]`…).
    La voz se divide con `asplit` porque se usa dos veces: como señal y como
    disparador del sidechain.
    """
    vol = env_float("MUSICA_VOLUMEN", 0.18) if volumen is None else volumen
    salida_fade = max(duracion_s - FADE_OUT_S, 0.0)
    return (
        f"[{voz}]asplit=2[vz][llave];"
        f"[{musica}]volume={vol:.3f},"
        f"afade=t=in:st=0:d={FADE_IN_S},"
        f"afade=t=out:st={salida_fade:.2f}:d={FADE_OUT_S}[bg];"
        # threshold bajo y ratio alto: basta que la voz asome para que la
        # música ceda. El release de 400ms evita el bombeo audible entre
        # palabra y palabra de una misma frase.
        f"[bg][llave]sidechaincompress="
        f"threshold=0.05:ratio=8:attack=20:release=400[duck];"
        # normalize=0 para que amix no baje los dos canales a la mitad: la voz
        # tiene que salir al mismo nivel al que entró.
        f"[vz][duck]amix=inputs=2:duration=first:normalize=0[crudo];"
        f"[crudo]loudnorm=I={LUFS_OBJETIVO}:TP={TRUE_PEAK_MAX}:LRA=11,"
        f"{_limitador()}[{salida}]"
    )


def cadena_master(
    entrada: str,
    salida: str,
    *,
    duracion_s: float,
    fade_out_s: float = FADE_OUT_S,
    fin_voz_s: float | None = None,
) -> str:
    """Master de una pista que ya viene mezclada: sólo fades y loudnorm.

    El modo `musical_sync` no tiene nada que duckear — la canción ES la pista,
    no hay locución debajo. Pero sí tiene que salir a los mismos −14 LUFS que
    el resto de los ads.

    `fin_voz_s` es la regla de Alexander: **el fade no puede empezar mientras
    todavía se canta**. Estaba clavado a tres segundos del final sin mirar la
    letra, y en dos ads se comió el último verso entero — el CTA, justamente.
    Con la última palabra medida, el desvanecido arranca ahí y usa la cola
    instrumental que quede; si no queda cola, se reduce a un cierre mínimo, que
    es preferible a apagar una idea a medias.
    """
    if fin_voz_s is not None:
        arranque = min(max(fin_voz_s, 0.0), duracion_s)
        fade_out_s = max(min(fade_out_s, duracion_s - arranque), 0.15)
    salida_fade = max(duracion_s - fade_out_s, 0.0)
    return (
        f"[{entrada}]afade=t=in:st=0:d={FADE_IN_S},"
        f"afade=t=out:st={salida_fade:.2f}:d={fade_out_s},"
        f"loudnorm=I={LUFS_OBJETIVO}:TP={TRUE_PEAK_MAX}:LRA=11,"
        f"{_limitador()}[{salida}]"
    )


def mezclar(
    video: Path,
    musica: Path,
    salida: Path,
    *,
    duracion_s: float,
    volumen: float | None = None,
) -> Path:
    """Le pone música a un video que ya tiene la voz montada.

    El video no se recodifica (`-c:v copy`): esto es una pasada de audio, y
    volver a comprimir la imagen solo para cambiarle la pista es perder
    calidad a cambio de nada.

    La música se repite con `-stream_loop` si es más corta que el video: las
    pistas de la librería duran ~75s y hay ads más largos.
    """
    if not Path(musica).exists():
        raise FileNotFoundError(f"No encuentro la música en {musica}")

    salida.parent.mkdir(parents=True, exist_ok=True)
    _ffmpeg([
        "-i", str(video),
        "-stream_loop", "-1", "-i", str(musica),
        "-filter_complex", cadena_audio(
            "0:a", "1:a", "aud", duracion_s=duracion_s, volumen=volumen
        ),
        "-map", "0:v", "-map", "[aud]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-shortest", "-movflags", "+faststart",
        str(salida),
    ])
    return salida


def medir_loudness(archivo: Path) -> dict[str, float]:
    """Mide el loudness integrado de un render, para verificar la mezcla.

    Devuelve dict vacío si ffmpeg no reporta el bloque JSON — el llamador
    decide si eso es fatal. Se usa en la verificación, no en el pipeline.
    """
    import json
    import re

    proceso = subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-hide_banner", "-i", str(archivo),
         "-af", "loudnorm=print_format=json", "-f", "null", "-"],
        capture_output=True, text=True,
    )
    bloques = re.findall(r"\{[^{}]*\"input_i\"[^{}]*\}", proceso.stderr, re.S)
    if not bloques:
        return {}
    datos = json.loads(bloques[-1])
    return {
        "lufs": float(datos.get("input_i", 0)),
        "true_peak": float(datos.get("input_tp", 0)),
        "lra": float(datos.get("input_lra", 0)),
    }
