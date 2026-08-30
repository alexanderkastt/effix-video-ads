"""Locución con ElevenLabs — la voz de Alexander sobre el guión aprobado.

Genera un MP3 por beat y la pista completa. Los beats sueltos son los que
manda `planificar_desde_audio()` para cortar los clips donde de verdad
termina cada frase, en vez de asumir cuatro segundos parejos.

El módulo es el primero del pipeline que gasta dinero: cada carácter que
entra aquí se factura, así que `generar_locucion()` avisa cuántos van antes
de llamar y `dry_run=True` devuelve el conteo sin tocar la API.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from elevenlabs.client import ElevenLabs
from elevenlabs.types.voice_settings import VoiceSettings

from .paths import AUDIO_DIR, env, env_float

# El formato manda en el costo y en lo que ffmpeg sabe concatenar sin recodificar.
FORMATO = "mp3_44100_128"


@dataclass
class Locucion:
    """Lo que queda después de hablar: los archivos y lo que costó."""

    beats: list[Path]
    caracteres: int
    duraciones_s: list[float]

    @property
    def duracion_total_s(self) -> float:
        return round(sum(self.duraciones_s), 2)


def _cliente() -> ElevenLabs:
    api_key = env("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Falta ELEVENLABS_API_KEY en el .env. Sin eso no hay voz."
        )
    return ElevenLabs(api_key=api_key)


def _settings() -> VoiceSettings:
    """Los valores validados del .env, no los que trae el SDK por defecto."""
    return VoiceSettings(
        stability=env_float("ELEVENLABS_STABILITY", 0.28),
        similarity_boost=env_float("ELEVENLABS_SIMILARITY", 0.83),
        style=env_float("ELEVENLABS_STYLE", 0.12),
        speed=env_float("ELEVENLABS_SPEED", 0.83),
        use_speaker_boost=str(env("ELEVENLABS_SPEAKER_BOOST", "true")).lower() == "true",
    )


def duracion_de(mp3: Path) -> float:
    """Segundos reales del archivo, medidos con ffprobe.

    El pipeline entero se recalcula sobre este número: si la voz tardó 4.6s,
    el clip dura 4.6s. Devuelve 0.0 si ffprobe no está — el llamador decide
    si eso es fatal.
    """
    try:
        salida = subprocess.run(
            [env("FFPROBE_BIN", "ffprobe"), "-v", "error",
             "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", str(mp3)],
            capture_output=True, text=True, check=True,
        )
        return round(float(salida.stdout.strip()), 3)
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        return 0.0


def generar_locucion(
    guion: dict[str, Any],
    *,
    voice_id: str | None = None,
    dry_run: bool = False,
    destino: Path | None = None,
) -> Locucion:
    """Convierte la narración de cada beat en un MP3.

    Con `dry_run=True` no llama a la API: sólo cuenta los caracteres que se
    facturarían, para saber el gasto antes de comprometerlo.
    """
    beats = guion.get("beats", [])
    if not beats:
        raise ValueError("El guión no tiene beats que locutar.")

    textos = [b.get("narracion", "").strip() for b in beats]
    caracteres = sum(len(t) for t in textos)

    if dry_run:
        return Locucion(beats=[], caracteres=caracteres, duraciones_s=[])

    voice_id = voice_id or env("ELEVENLABS_VOICE_ID")
    if not voice_id:
        raise RuntimeError("Falta ELEVENLABS_VOICE_ID en el .env.")

    carpeta = destino or (AUDIO_DIR / str(guion.get("job_id", "sin-job")))
    carpeta.mkdir(parents=True, exist_ok=True)

    cliente = _cliente()
    modelo = env("ELEVENLABS_MODEL", "eleven_multilingual_v2")
    settings = _settings()

    rutas: list[Path] = []
    duraciones: list[float] = []

    for beat, texto in zip(beats, textos):
        ruta = carpeta / f"beat_{beat['beat']:02d}.mp3"
        # previous_text/next_text le dan a la voz el contexto de la frase
        # anterior y la siguiente: sin eso cada beat suena como una locución
        # independiente y el video se oye a pedazos.
        audio = cliente.text_to_speech.convert(
            voice_id,
            text=texto,
            model_id=modelo,
            output_format=FORMATO,
            voice_settings=settings,
            previous_text=textos[beat["beat"] - 2] if beat["beat"] > 1 else None,
            next_text=textos[beat["beat"]] if beat["beat"] < len(textos) else None,
        )
        ruta.write_bytes(b"".join(audio))
        rutas.append(ruta)
        duraciones.append(duracion_de(ruta))

    return Locucion(beats=rutas, caracteres=caracteres, duraciones_s=duraciones)
