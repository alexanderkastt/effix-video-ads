"""Genera la librería de música de fondo. Se corre una vez, no por ad.

Seis pistas instrumentales de 75s, una por mood, a 0.20 USD cada una con
stable-audio-25. Son 1.20 USD de una sola vez y a partir de ahí cada ad toma
la suya gratis: componer música nueva por video sería 0.20 recurrentes por un
fondo que nadie va a distinguir del anterior.

Es idempotente — la pista que ya existe no se vuelve a pagar. Para rehacer una,
borrar su mp3 y volver a correr.

    python scripts/generar_soundtracks.py            # las que falten
    python scripts/generar_soundtracks.py --lista    # qué hay y qué falta
    python scripts/generar_soundtracks.py alegre     # solo esa
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.audio_extra import componer_musica          # noqa: E402
from src.music_engine import SOUNDTRACKS_DIR, catalogo  # noqa: E402

PRECIO_POR_PISTA = 0.20


def _brief(mood: str, datos: dict) -> dict:
    """El brief con la forma que espera `componer_musica`."""
    return {
        "suno_prompt": datos["prompt"],
        "suno_style_tags": ["latin", "latam", mood],
        "bpm_recomendado": datos["bpm"],
    }


def _comprimir(ruta: Path) -> Path:
    """Recodifica la pista a MP3 192k.

    fal devuelve WAV crudo con extensión .mp3: 1411 kbps, unos 13 MB por pista.
    Para una cama que suena al 18% debajo de la voz eso es absurdo, y son 76 MB
    de librería que no caben en el repo. A 192k son ~1.8 MB y suenan igual.
    """
    import subprocess
    from src.paths import env

    temporal = ruta.with_suffix(".tmp.mp3")
    proceso = subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         "-i", str(ruta), "-c:a", "libmp3lame", "-b:a", "192k", "-ar", "44100",
         str(temporal)],
        capture_output=True, text=True,
    )
    if proceso.returncode != 0:
        print(f"     aviso: no se pudo comprimir ({proceso.stderr.strip()[:120]}); "
              f"se deja como vino")
        temporal.unlink(missing_ok=True)
        return ruta
    temporal.replace(ruta)
    return ruta


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("moods", nargs="*", help="Moods a generar. Vacío = los que falten.")
    ap.add_argument("--lista", action="store_true", help="Solo mostrar el estado.")
    ap.add_argument("--duracion", type=int, default=75, help="Segundos por pista.")
    args = ap.parse_args()

    moods = catalogo()
    if not moods:
        print("No encuentro config/soundtracks.json o no tiene moods.")
        return 1

    SOUNDTRACKS_DIR.mkdir(parents=True, exist_ok=True)
    pedidos = args.moods or list(moods)

    desconocidos = [m for m in pedidos if m not in moods]
    if desconocidos:
        print(f"Moods que no están en el catálogo: {', '.join(desconocidos)}")
        print(f"Hay: {', '.join(moods)}")
        return 1

    faltan = []
    for mood in pedidos:
        ruta = SOUNDTRACKS_DIR / moods[mood]["archivo"]
        estado = "ok" if ruta.exists() else "FALTA"
        print(f"  {mood:<14} {moods[mood]['bpm']:>4} BPM  {estado:<6} {ruta.name}")
        if not ruta.exists():
            faltan.append(mood)

    if args.lista:
        return 0

    if not faltan:
        print("\nLa librería está completa. No hay nada que pagar.")
        return 0

    costo = len(faltan) * PRECIO_POR_PISTA
    print(f"\nFaltan {len(faltan)}: {', '.join(faltan)}")
    print(f"Costo: {costo:.2f} USD ({PRECIO_POR_PISTA} por pista)")

    for mood in faltan:
        datos = moods[mood]
        destino = SOUNDTRACKS_DIR / datos["archivo"]
        print(f"\n  componiendo {mood} ({datos['bpm']} BPM)...")
        ruta = componer_musica(
            _brief(mood, datos),
            args.duracion,
            job_id="soundtracks",
            destino=destino,
        )
        ruta = _comprimir(ruta)
        print(f"  -> {ruta}  ({ruta.stat().st_size / 1024:.0f} KB)")

    print(f"\nListo. {len(faltan)} pista(s), {costo:.2f} USD.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
