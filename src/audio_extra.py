"""Música y efectos con ElevenLabs, y elección de voz según el guión.

El brief de música que arma music_engine.py se pegaba a mano en suno.com y
volvía como archivo. ElevenLabs compone desde el mismo brief y con la misma
key que ya usa la locución, así que el video sale completo de una corrida.

La voz también deja de estar clavada en el .env: el guión sabe de qué habla
y con qué tono, y de ahí sale a quién conviene que lo cuente.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from elevenlabs.client import ElevenLabs

from .paths import AUDIO_DIR, env

FORMATO = "mp3_44100_128"
MODELO_SFX = "eleven_text_to_sound_v2"


# Voces de la cuenta que sirven para creativos de Effix. La clave es el
# perfil que pide el guión, no el nombre: así el motor elige por tono y no
# por acordarse de un id.
VOCES: dict[str, dict[str, str]] = {
    "marca_femenina": {
        "nombre": "Voz Femenina Grupo Effi",
        "cuando": "voz oficial de la marca, colombiana y joven — la primera opción",
    },
    "cercana_medellin": {
        "nombre": "Medellin -  Conversational and Intense",
        "cuando": "conversacional y con acento local, para guiones que hablan de la ciudad",
    },
    "anfitriona": {
        "nombre": "Daniela - Friendly Host",
        "cuando": "presentadora animada, para hooks y CTA con energía",
    },
    "amiga": {
        "nombre": "Valentina - Joyful, Lively Friend",
        "cuando": "cercana y liviana, para historias en primera persona",
    },
    "narrador_serio": {
        "nombre": "Carlos Aguilar",
        "cuando": "narración con autoridad, para ángulos de negocio o cifras",
    },
}


def _cliente() -> ElevenLabs:
    api_key = env("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError("Falta ELEVENLABS_API_KEY en el .env.")
    return ElevenLabs(api_key=api_key)


def voz_para(perfil: str = "marca_femenina") -> tuple[str, str]:
    """Devuelve (voice_id, nombre) buscando la voz por su nombre en la cuenta.

    Se resuelve por nombre y no por id fijo: los ids cambian entre cuentas y
    un id muerto en el .env rompe la locución sin decir por qué.
    """
    if perfil not in VOCES:
        raise KeyError(f"Perfil '{perfil}' no existe. Hay: {', '.join(VOCES)}")
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

    audio = _cliente().music.compose(
        prompt=completo,
        music_length_ms=int(duracion_s * 1000),
        force_instrumental=True,
        output_format=FORMATO,
    )
    ruta = destino or (AUDIO_DIR / job_id / "musica.mp3")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(b"".join(audio))
    return ruta


def efecto(
    descripcion: str,
    duracion_s: float,
    *,
    job_id: str,
    nombre: str,
    destino: Path | None = None,
) -> Path:
    """Genera un efecto puntual: un golpe de transición, un ambiente, un whoosh."""
    audio = _cliente().text_to_sound_effects.convert(
        text=descripcion,
        duration_seconds=duracion_s,
        model_id=MODELO_SFX,
        output_format=FORMATO,
    )
    ruta = destino or (AUDIO_DIR / job_id / "sfx" / f"{nombre}.mp3")
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_bytes(b"".join(audio))
    return ruta
