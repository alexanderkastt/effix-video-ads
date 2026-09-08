"""Transcripción de la canción y alineación de la letra con el reloj real.

En modo `musical_sync` la canción manda: el montaje tiene que cortar cuando el
cantante cambia de frase, no cada N segundos. El problema es que MiniMax
devuelve un mp3 y nada más — no dice dónde arranca a cantar ni cuánto dura cada
verso, y esos tiempos escritos a mano fue lo que hizo falta en el ad musical
anterior (`_montaje_skeleton.py` los tenía clavados en una constante).

Aquí se resuelven solos:

1. Whisper transcribe la canción con marca de tiempo por palabra (0.0008 USD el
   segundo de cómputo: centavos frente a los 0.15 de la canción).
2. El tramo cantado sale de la primera y la última palabra — el intro y la cola
   instrumental se recortan, y con ellos los segundos muertos que hacían que el
   ad empezara sin letra.
3. La letra del guion se alinea contra esa transcripción con `difflib`, no por
   coincidencia exacta: el modelo canta "Effix" como "efix" o se come un
   artículo, y un emparejamiento literal fallaría en la mitad de las líneas.
"""

from __future__ import annotations

import json
import re
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import fal_client

from .paths import AUDIO_DIR, env

MODELO_WHISPER = "fal-ai/whisper"


def _normalizar(palabra: str) -> str:
    """Baja una palabra a su esqueleto comparable: sin tildes, sin puntuación.

    Whisper escribe lo que oye; el guion está escrito con ortografía. Comparar
    "Medellín," con "medellin" tiene que dar igual, o la alineación se rompe en
    cada nombre propio.
    """
    sin_tildes = "".join(
        c for c in unicodedata.normalize("NFD", palabra.lower())
        if unicodedata.category(c) != "Mn"
    )
    return re.sub(r"[^a-z0-9]", "", sin_tildes)


def _palabras(texto: str) -> list[str]:
    return [p for p in (_normalizar(t) for t in texto.split()) if p]


def transcribir(audio: Path, *, job_id: str, forzar: bool = False) -> dict[str, Any]:
    """Transcribe la canción con marcas por palabra y cachea el resultado.

    Se cachea porque la transcripción no cambia entre corridas del montaje y
    volver a pedirla es pagar dos veces por el mismo dato.
    """
    ficha = AUDIO_DIR / job_id / "transcripcion.json"
    if ficha.exists() and not forzar:
        return json.loads(ficha.read_text(encoding="utf-8"))

    with open(audio, "rb") as fh:
        url = fal_client.upload(fh.read(), "audio/mpeg")
    salida = fal_client.subscribe(
        env("FAL_MODEL_WHISPER", MODELO_WHISPER),
        {"audio_url": url, "task": "transcribe", "language": "es",
         "chunk_level": "word"},
    )
    ficha.parent.mkdir(parents=True, exist_ok=True)
    ficha.write_text(json.dumps(salida, ensure_ascii=False, indent=2), encoding="utf-8")
    return salida


def _marcas(transcripcion: dict[str, Any]) -> list[tuple[str, float, float]]:
    """(palabra normalizada, inicio, fin) de cada palabra que whisper reconoció."""
    salida: list[tuple[str, float, float]] = []
    for trozo in transcripcion.get("chunks") or []:
        marca = trozo.get("timestamp") or trozo.get("timestamps") or []
        if not marca or marca[0] is None:
            continue
        inicio = float(marca[0])
        fin = float(marca[1]) if len(marca) > 1 and marca[1] is not None else inicio
        for palabra in _palabras(str(trozo.get("text") or "")):
            salida.append((palabra, inicio, fin))
    return salida


def tramo_cantado(transcripcion: dict[str, Any]) -> tuple[float, float]:
    """Dónde empieza y termina la voz, para recortar intro y cola instrumental."""
    marcas = _marcas(transcripcion)
    if not marcas:
        raise ValueError(
            "Whisper no reconoció ninguna palabra: la canción salió instrumental "
            "o el audio está mudo. Escúchala antes de montar."
        )
    return round(marcas[0][1], 3), round(marcas[-1][2], 3)


def alinear(
    textos: list[str],
    transcripcion: dict[str, Any],
    *,
    inicio_s: float,
    fin_s: float,
) -> list[tuple[float, float]]:
    """Devuelve el tramo (inicio, fin) de cada línea del guion dentro de la canción.

    Los tiempos vienen relativos al tramo ya recortado: la línea 1 arranca en
    0.0 y la última termina en `fin_s - inicio_s`. El resultado es contiguo a
    propósito — en un montaje musical no hay huecos entre planos, la imagen
    siguiente entra donde salió la anterior.

    Cuando una línea no se pudo anclar (whisper se comió esa frase), se reparte
    proporcionalmente el hueco entre las dos líneas ancladas que la rodean, que
    es mejor que dejarla en cero y amontonar tres cortes en el mismo segundo.
    """
    marcas = _marcas(transcripcion)
    if not marcas:
        raise ValueError("No hay palabras transcritas con las que alinear.")

    # Secuencia del guion, recordando de qué línea salió cada palabra.
    del_guion: list[str] = []
    linea_de: list[int] = []
    for i, texto in enumerate(textos):
        for palabra in _palabras(texto):
            del_guion.append(palabra)
            linea_de.append(i)

    de_whisper = [m[0] for m in marcas]
    emparejadas: dict[int, list[int]] = {}
    for bloque in SequenceMatcher(None, del_guion, de_whisper, autojunk=False)\
            .get_matching_blocks():
        for k in range(bloque.size):
            emparejadas.setdefault(linea_de[bloque.a + k], []).append(bloque.b + k)

    largo = fin_s - inicio_s
    anclas: dict[int, float] = {}
    for i in range(len(textos)):
        indices = emparejadas.get(i)
        if indices:
            # El arranque de la línea es la primera palabra suya que se oyó.
            anclas[i] = max(0.0, marcas[min(indices)][1] - inicio_s)

    # Monotonía: una línea nunca puede empezar antes que la anterior. Whisper
    # repite palabras del coro y sin esto el orden se desordena solo.
    previo = 0.0
    for i in sorted(anclas):
        anclas[i] = previo = max(anclas[i], previo)

    inicios: list[float] = []
    for i in range(len(textos)):
        if i in anclas:
            inicios.append(anclas[i])
            continue
        # Interpolación entre las dos anclas que la rodean.
        antes = [j for j in anclas if j < i]
        despues = [j for j in anclas if j > i]
        izq = anclas[max(antes)] if antes else 0.0
        der = anclas[min(despues)] if despues else largo
        base = max(antes) if antes else -1
        techo = min(despues) if despues else len(textos)
        paso = (der - izq) / max(1, techo - base)
        inicios.append(round(izq + paso * (i - base), 3))

    inicios[0] = 0.0
    tramos: list[tuple[float, float]] = []
    for i, comienzo in enumerate(inicios):
        final = inicios[i + 1] if i + 1 < len(inicios) else largo
        tramos.append((round(comienzo, 3), round(max(final, comienzo), 3)))
    return tramos


def cobertura_de_lineas(
    textos: list[str],
    transcripcion: dict[str, Any],
) -> list[float]:
    """Qué fracción de cada línea del guion aparece de verdad en la canción.

    `alinear()` da por hecho que todo se cantó y reparte el hueco de lo que no
    encuentra; sirve para el montaje, pero esconde justo el fallo que más caro
    sale: que el modelo se quedara sin tope y no llegara al CTA. Esto compara
    palabra a palabra y devuelve la cobertura de cada línea, de 0.0 a 1.0.

    Se descubrió con el P02 (2026-09-07): dos canciones pagadas murieron en "de
    las tiendas", sin la cuña final ni el CTA, y la única forma de verlo era
    leer la transcripción entera a mano.
    """
    oidas = [m[0] for m in _marcas(transcripcion)]
    if not oidas:
        return [0.0 for _ in textos]

    del_guion: list[str] = []
    linea_de: list[int] = []
    for i, texto in enumerate(textos):
        for palabra in _palabras(texto):
            del_guion.append(palabra)
            linea_de.append(i)

    aciertos = [0] * len(textos)
    for bloque in SequenceMatcher(None, del_guion, oidas, autojunk=False)            .get_matching_blocks():
        for k in range(bloque.size):
            aciertos[linea_de[bloque.a + k]] += 1

    totales = [max(len(_palabras(t)), 1) for t in textos]
    return [round(min(a / tot, 1.0), 2) for a, tot in zip(aciertos, totales)]


def golpes(cancion: Path) -> list[float]:
    """Los tiempos de beat de la canción, para que los cortes caigan en ellos."""
    import librosa  # import diferido: librosa tarda ~2s en cargar

    y, sr = librosa.load(str(cancion), sr=None, mono=True)
    _, frames = librosa.beat.beat_track(y=y, sr=sr)
    return librosa.frames_to_time(frames, sr=sr).tolist()
