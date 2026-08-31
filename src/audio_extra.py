"""Música y efectos por fal, y elección de voz según el guión.

El brief de música que arma music_engine.py se pegaba a mano en suno.com y
volvía como archivo. Ahora se compone por API desde el mismo brief, así que
el video sale completo de una corrida.

Música y efectos van por fal y no por ElevenLabs directo: el precio es
verificable con `get_pricing` antes de gastar (Stable Audio 2.5 cobra $0.20
por pista, ElevenLabs Music $0.60 por minuto) y deja una sola factura.

La VOZ es la excepción y se queda en ElevenLabs directo: las voces de la
marca — "Voz Femenina Grupo Effi", el acento paisa — son voces privadas de la
cuenta de Alexander, y fal ejecuta ElevenLabs con la suya. Por fal habría que
locutar con una voz de catálogo, que para un ad de Medellín es un downgrade.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import fal_client
import requests
from elevenlabs.client import ElevenLabs

from .paths import AUDIO_DIR, env

FORMATO = "mp3_44100_128"

# Música: Stable Audio 2.5 cobra por pista y no por minuto, así que un fondo
# de 50s cuesta lo mismo que uno de 190s. Para una cama instrumental que va al
# 25% de volumen debajo de la locución, la diferencia con ElevenLabs Music no
# se oye — y son cuarenta centavos por video.
MODELO_MUSICA = "fal-ai/stable-audio-25/text-to-audio"
MODELO_SFX = "fal-ai/elevenlabs/sound-effects/v2"


# Voces de la cuenta que sirven para creativos de Effix. La clave es el
# perfil que pide el guión, no el nombre: así el motor elige por tono y no
# por acordarse de un id.
VOCES: dict[str, dict[str, str]] = {
    "marca_femenina": {
        "nombre": "Voz Femenina Grupo Effi",
        "cuando": "voz oficial de la marca, colombiana y joven — la primera opción",
        "genero": "f",
    },
    "cercana_medellin": {
        "nombre": "Medellin -  Conversational and Intense",
        "cuando": "conversacional y con acento local, para guiones que hablan de la ciudad",
        "genero": "f",
    },
    "anfitriona": {
        "nombre": "Daniela - Friendly Host",
        "cuando": "presentadora animada, para hooks y CTA con energía",
        "genero": "f",
    },
    "amiga": {
        "nombre": "Valentina - Joyful, Lively Friend",
        "cuando": "cercana y liviana, para historias en primera persona",
        "genero": "f",
    },
    "narrador_serio": {
        "nombre": "Carlos Aguilar",
        "cuando": "narración con autoridad, para ángulos de negocio o cifras",
        "genero": "m",
    },
}


def perfiles_de(genero: str) -> list[str]:
    """Los perfiles de voz que sirven para un personaje de ese género."""
    return [k for k, v in VOCES.items() if v.get("genero") == genero]


def verificar_genero(perfil: str, personaje: str | None) -> None:
    """Impide locutar a un personaje con una voz del otro género.

    Pasó una vez: un video entero con Andrés en pantalla y voz femenina
    encima, con lip-sync sincronizando la boca de un hombre a una voz de
    mujer. No es un detalle de estilo, es un video inservible — y sólo se
    nota al mirarlo, cuando ya está pagado.
    """
    if not personaje:
        return
    from .personaje import genero_de

    del_personaje = genero_de(personaje)
    de_la_voz = VOCES.get(perfil, {}).get("genero")
    if del_personaje and de_la_voz and del_personaje != de_la_voz:
        sirven = ", ".join(perfiles_de(del_personaje)) or "ninguno en el catálogo"
        raise ValueError(
            f"El personaje '{personaje}' es '{del_personaje}' y el perfil de voz "
            f"'{perfil}' es '{de_la_voz}'. Perfiles que sirven: {sirven}."
        )


def _cliente() -> ElevenLabs:
    api_key = env("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("Falta ELEVENLABS_API_KEY en el .env.")
    return ElevenLabs(api_key=api_key)


def voz_para(perfil: str = "marca_femenina", personaje: str | None = None) -> tuple[str, str]:
    """Devuelve (voice_id, nombre) buscando la voz por su nombre en la cuenta.

    Se resuelve por nombre y no por id fijo: los ids cambian entre cuentas y
    un id muerto en el .env rompe la locución sin decir por qué.
    """
    if perfil not in VOCES:
        raise KeyError(f"Perfil '{perfil}' no existe. Hay: {', '.join(VOCES)}")
    verificar_genero(perfil, personaje)
    buscado = VOCES[perfil]["nombre"]

    for v in _cliente().voices.get_all().voices:
        if v.name == buscado:
            return v.voice_id, v.name
    raise LookupError(
        f"La cuenta no tiene la voz '{buscado}'. Perfiles disponibles: {', '.join(VOCES)}"
    )


def componer_musica(
    brief: dict[str, Any],
    duracion_s: float,
    *,
    job_id: str,
    destino: Path | None = None,
) -> Path:
    """Compone la pista de fondo a partir del brief de music_engine.

    Se pide instrumental de forma explícita: una letra cantada pelea con la
    locución, que es lo único que tiene que entenderse.
    """
    prompt = brief.get("suno_prompt") or brief.get("suno_title") or "upbeat lo-fi"
    tags = ", ".join(brief.get("suno_style_tags", []))
    bpm = brief.get("bpm_recomendado")

    completo = f"{prompt}"
    if tags:
        completo += f". Style: {tags}"
    if bpm:
        completo += f". Around {bpm} BPM"
    completo += ". Instrumental only, no vocals, steady bed for a voiceover."

    salida = fal_client.subscribe(
        env("FAL_MODEL_MUSICA", MODELO_MUSICA),
        {"prompt": completo, "seconds_total": int(duracion_s)},
    )
    ruta = destino or (AUDIO_DIR / job_id / "musica.mp3")
    return _bajar(salida, ruta)



# Canción cantada: la letra ES el guión. Stable Audio no canta, así que el
# modo musical_sync va por MiniMax Music 2.6 ($0.15 la pista, con voz y
# arreglos a partir de la letra y una descripción de estilo).
MODELO_CANCION = "fal-ai/minimax-music/v2.6"

# MiniMax lee etiquetas de estructura en inglés. La letra sigue en español;
# lo único que se traduce es el marcador de sección.
SECCIONES = {
    "[Verso 1]": "[Verse]", "[Verso 2]": "[Verse]", "[Verso 3]": "[Verse]",
    "[Verso]": "[Verse]", "[Pre-coro]": "[Pre Chorus]", "[Coro]": "[Chorus]",
    "[Puente]": "[Bridge]", "[Intro]": "[Intro]", "[Outro]": "[Outro]",
}


def _letra_para_minimax(letra: str) -> str:
    for es, en in SECCIONES.items():
        letra = letra.replace(es, en)
    return letra


def componer_cancion(
    brief: dict[str, Any],
    *,
    job_id: str,
    destino: Path | None = None,
) -> Path:
    """Compone la canción cantada del modo sincronizado.

    Al revés que `componer_musica`, aquí la voz SÍ va en la pista: no hay
    locución debajo con la que pelear, la letra es lo que se entiende.
    """
    letra = _letra_para_minimax(brief["suno_custom_lyrics"])
    if len(letra) > 3500:
        raise ValueError(f"La letra tiene {len(letra)} caracteres; el tope es 3500.")

    tags = ", ".join(brief.get("suno_style_tags", []))
    bpm = brief.get("bpm_recomendado")
    prompt = f"{tags}. Colombian Spanish vocals, clear diction, radio-ready ad jingle"
    if bpm:
        prompt += f", around {bpm} BPM"

    salida = fal_client.subscribe(
        env("FAL_MODEL_CANCION", MODELO_CANCION),
        {"prompt": prompt, "lyrics": letra, "is_instrumental": False},
    )
    ruta = destino or (AUDIO_DIR / job_id / "cancion.mp3")
    return _bajar(salida, ruta)

def efecto(
    descripcion: str,
    duracion_s: float,
    *,
    job_id: str,
    nombre: str,
    destino: Path | None = None,
) -> Path:
    """Genera un efecto puntual: un golpe de transición, un ambiente, un whoosh."""
    salida = fal_client.subscribe(
        env("FAL_MODEL_SFX", MODELO_SFX),
        {
            "text": descripcion,
            "duration_seconds": duracion_s,  # el endpoint acepta de 0.5 a 22s
            "output_format": FORMATO,
        },
    )
    ruta = destino or (AUDIO_DIR / job_id / "sfx" / f"{nombre}.mp3")
    return _bajar(salida, ruta)


def _bajar(salida: dict[str, Any], destino: Path) -> Path:
    """Baja a disco el audio que fal deja en una URL temporal."""
    audio = salida.get("audio")
    url = audio["url"] if isinstance(audio, dict) else audio
    if not url:
        raise KeyError(f"La respuesta de fal no trae audio: {list(salida)}")
    destino.parent.mkdir(parents=True, exist_ok=True)
    respuesta = requests.get(url, timeout=300)
    respuesta.raise_for_status()
    destino.write_bytes(respuesta.content)
    return destino
