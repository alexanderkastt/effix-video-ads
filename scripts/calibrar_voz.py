"""Mide cuántas palabras por segundo locuta de verdad la voz configurada.

El pipeline estima cuántos clips hacen falta ANTES de gastar en video, y esa
estimación sale de `PALABRAS_POR_SEGUNDO`. El número depende de la voz y del
`ELEVENLABS_SPEED`: el 2.96 que había estaba medido a speed 0.83, así que al
subir a 1.15 la estimación sobra clips que después hay que tirar.

Locuta tres frases patrón con los settings vigentes, las mide con ffprobe y
dice qué valor poner en el .env. Son ~180 caracteres: centavos.

    python scripts/calibrar_voz.py
    python scripts/calibrar_voz.py --perfil anfitriona
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.paths import AUDIO_DIR, env  # noqa: E402
from src.voice_generator import (  # noqa: E402
    FORMATO, _cliente, _settings, duracion_de, respiro_s,
)

# Tres frases con la forma real de un guión de Effix: una de gancho, una de
# cuerpo y el cierre con la marca. La marca va entera a propósito — "Feria
# Effix" nunca se abrevia, y es justo donde un speed alto se nota si atropella.
FRASES = [
    "Llevas un año viendo la misma blusa colgada en la vitrina.",
    "No es que no venda: es que nadie sabe que existe fuera de tu cuadra.",
    "Te esperamos en la Feria Effix, del quince al diecinueve de octubre.",
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--perfil", default=None, help="Perfil de voz (ver audio_extra.VOCES).")
    ap.add_argument("--voice-id", default=None, help="Voice id explícito.")
    args = ap.parse_args()

    voice_id = args.voice_id
    nombre = voice_id or "(del .env)"
    if not voice_id and args.perfil:
        from src.audio_extra import voz_para
        voice_id, nombre = voz_para(args.perfil)
    voice_id = voice_id or env("ELEVENLABS_VOICE_ID")
    if not voice_id:
        print("No hay voz: pasa --perfil o define ELEVENLABS_VOICE_ID en el .env.")
        return 1

    settings = _settings()
    modelo = env("ELEVENLABS_MODEL", "eleven_multilingual_v2")
    print(f"voz {nombre} · {modelo}")
    print(f"speed {settings.speed} · stability {settings.stability} · "
          f"style {settings.style} · respiro {respiro_s()}s\n")

    carpeta = AUDIO_DIR / "calibracion"
    carpeta.mkdir(parents=True, exist_ok=True)
    cliente = _cliente()

    palabras_total = 0
    segundos_total = 0.0
    for i, frase in enumerate(FRASES, 1):
        ruta = carpeta / f"calibra_{i:02d}.mp3"
        audio = cliente.text_to_speech.convert(
            voice_id, text=frase, model_id=modelo,
            output_format=FORMATO, voice_settings=settings,
            previous_text=FRASES[i - 2] if i > 1 else None,
            next_text=FRASES[i] if i < len(FRASES) else None,
        )
        ruta.write_bytes(b"".join(audio))
        dur = duracion_de(ruta)
        palabras = len(frase.split())
        palabras_total += palabras
        segundos_total += dur
        print(f"  {i}. {palabras:>2} palabras en {dur:5.2f}s "
              f"({palabras / dur:.2f} p/s)  {ruta.name}")
        print(f"     {frase}")

    pps = palabras_total / segundos_total
    print(f"\n{palabras_total} palabras en {segundos_total:.2f}s")
    print(f"PALABRAS_POR_SEGUNDO={pps:.2f}")
    print(f"\nUn ad de 45s de locución son ~{pps * 45:.0f} palabras.")
    print(f"Los mp3 quedan en {carpeta} — escúchalos antes de dar el speed por bueno.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
