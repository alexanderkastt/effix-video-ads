"""Personaje del video — uno solo, el mismo en todas las escenas.

Cada escena se generaba por su cuenta y salían diez personas distintas: una
con camisa de cuadros, la siguiente de beige, la otra de verde, todas con la
misma voz encima. Para un anuncio eso no es un detalle, es lo que rompe la
ilusión de que hay alguien contando algo.

La solución es una hoja de personaje: una imagen de referencia que se genera
una vez, se sube una vez, y viaja como referencia a todas las escenas. El
modelo de edición reconoce la cara y la conserva mientras cambia el
escenario, la acción y el encuadre.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import fal_client

from .paths import CLIPS_DIR, env

# Modelo con consistencia de personaje por imagen de referencia.
MODELO_PERSONAJE = "fal-ai/nano-banana-2"
MODELO_ESCENA = "fal-ai/nano-banana-2/edit"


@dataclass
class Personaje:
    """Quién protagoniza el video, y dónde vive su referencia."""

    nombre: str
    descripcion_en: str
    imagen: str
    url_referencia: str
    estilo: str

    @property
    def ruta(self) -> Path:
        return Path(self.imagen)


# Hojas de personaje que ya existen en el repo. Cuando hay una, se usa como
# referencia en vez de generar una nueva: Effi es la mascota de la marca y
# tiene turnaround y expresiones dibujadas, así que inventarle una cara
# nueva cada vez sería empezar de cero teniendo el trabajo hecho.
HOJAS_EN_REPO: dict[str, str] = {
    "effi": "referencias/personajes/character-sheet-effi.png",
    "lana": "referencias/personajes/lana-sheet-v2.jpg",
}


# Personajes de la casa. La descripción es en inglés porque es lo que leen
# los modelos, y es deliberadamente específica: los rasgos que se repiten
# (color de blusa, aretes, peinado) son lo que hace reconocible a alguien
# de un plano a otro.
CATALOGO: dict[str, str] = {
    # Texto oficial de prompts-listos/pixar/effix-2026-ia-45s.md. La primera
    # version la escribi mirando la imagen y se me escapo que el dron se
    # llama BIT y que la paleta esta bloqueada — dos cosas que la familia
    # entera tiene que respetar.
    "effi": (
        "EFFI: an anthropomorphic corrugated cardboard shipping box character, "
        "rounded corners, two expressive eyes on the front panel, short stubby "
        "cardboard arms, wearing a canvas work apron with a single chest pocket, "
        "packing tape strip across one corner like a scar"
    ),
    "lana": (
        "Lana, a crocheted amigurumi character made of visible yarn fibre, "
        "hand-stitched features, soft wool texture"
    ),
    "camila": (
        "a Latin American woman in her early thirties, warm brown eyes, dark wavy "
        "shoulder-length hair loosely tied back, small silver hoop earrings, a "
        "mustard-yellow blouse over a white tee, friendly and determined expression, "
        "light freckles across the nose"
    ),
    "andres": (
        "a Latin American man in his early thirties, short dark hair, trimmed beard, "
        "olive-green button shirt with sleeves rolled up, a simple leather-strap watch, "
        "calm and focused expression"
    ),
}


# Compañero fijo de la familia y paleta cerrada: los dos vienen del prompt
# oficial de Effi y son lo que hace que diez objetos distintos se lean como
# un mismo universo y no como diez mascotas sueltas.
BIT = (
    "Beside the character at correct relative scale: BIT, a small floating "
    "spherical assistant, matte white shell, single soft cyan light-ring for a "
    "face, sized to hover at shoulder height."
)

PALETA = (
    "Palette locked to amber #F4A300, deep blue #1B2A4A, cardboard brown "
    "#C9772F, cream #E8E2D5, and cyan #3DD6C4 on BIT's ring only."
)


def prompt_hoja_familia(descripcion: str) -> str:
    """Model sheet de un personaje de la familia Effi.

    Las dos cabezas —boca abierta y boca cerrada— no son decorativas: son lo
    que permite el lip-sync después. El prompt oficial de Effi lo dice y por
    eso se repiten aquí para cada miembro de la familia.
    """
    return (
        "Character model sheet on a plain flat neutral grey background. "
        "Pixar-grade 3D animation render.\n\n"
        f"{descripcion}\n\n"
        "Layout: full-body front view, full-body three-quarter view, full-body "
        "side view, plus two head close-ups side by side — one with the mouth "
        "open mid-speech, one with the mouth closed neutral.\n\n"
        f"{BIT}\n\n"
        f"{PALETA} Even flat studio lighting, sharp focus throughout, deep "
        "depth of field, no cast shadows on the background."
    )


def _prompt_hoja(descripcion: str, estilo_en: str) -> str:
    """La hoja de personaje: cara clara, luz neutra, nada de escenografía.

    Cuanto más limpia la referencia, mejor la conserva el modelo de edición:
    un fondo cargado se le pega al personaje y reaparece en cada escena.
    """
    return (
        f"{estilo_en}. Character reference sheet, single character, front-facing "
        f"three-quarter portrait, head and shoulders, neutral studio background, "
        f"even soft lighting, no props, no text. Character: {descripcion}. "
        f"Consistent, recognizable facial features."
    )


def crear_personaje(
    clave: str,
    *,
    estilo_en: str,
    job_id: str,
    carpeta: Path | None = None,
    descripcion: str | None = None,
) -> Personaje:
    """Genera la hoja de personaje y la deja lista para las escenas.

    Si ya existe en disco la reutiliza: la referencia se paga una vez por
    video, no una vez por escena.
    """
    carpeta = carpeta or (CLIPS_DIR / job_id)
    carpeta.mkdir(parents=True, exist_ok=True)
    ficha = carpeta / "personaje.json"

    if ficha.exists():
        return Personaje(**json.loads(ficha.read_text(encoding="utf-8")))

    descripcion = descripcion or CATALOGO.get(clave)
    if not descripcion:
        disponibles = ", ".join(CATALOGO)
        raise KeyError(f"No conozco al personaje '{clave}'. Hay: {disponibles}")

    # Si el repo ya trae su hoja, esa manda: es la version aprobada del
    # personaje, no una interpretacion nueva del modelo.
    from .paths import ROOT
    hoja = ROOT / HOJAS_EN_REPO.get(clave, "")
    if clave in HOJAS_EN_REPO and hoja.exists():
        import shutil
        imagen = carpeta / "personaje.png"
        shutil.copy2(hoja, imagen)
        with open(imagen, "rb") as fh:
            url_referencia = fal_client.upload(fh.read(), "image/png")
        personaje = Personaje(
            nombre=clave, descripcion_en=descripcion, imagen=str(imagen),
            url_referencia=url_referencia, estilo=estilo_en,
        )
        ficha.write_text(
            json.dumps(asdict(personaje), ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return personaje

    salida = fal_client.subscribe(
        MODELO_PERSONAJE,
        {
            "prompt": _prompt_hoja(descripcion, estilo_en),
            "aspect_ratio": "3:4",     # retrato: da cara grande para la referencia
            "resolution": "1K",
            "num_images": 1,
        },
    )
    url = salida["images"][0]["url"]

    import requests
    imagen = carpeta / "personaje.png"
    imagen.write_bytes(requests.get(url, timeout=300).content)

    # Se sube una sola vez y la URL se reutiliza en las diez escenas.
    with open(imagen, "rb") as fh:
        url_referencia = fal_client.upload(fh.read(), "image/png")

    personaje = Personaje(
        nombre=clave,
        descripcion_en=descripcion,
        imagen=str(imagen),
        url_referencia=url_referencia,
        estilo=estilo_en,
    )
    ficha.write_text(
        json.dumps(asdict(personaje), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return personaje


def prompt_de_escena(beat: dict[str, Any], personaje: Personaje) -> str:
    """Reescribe el prompt del beat para que hable de ESTE personaje.

    El prompt original describe un sujeto genérico del estilo ("an expressive
    3D character..."). Dejarlo tal cual pelea con la imagen de referencia: el
    texto pide una persona y la referencia muestra otra.
    """
    base = beat.get("prompt_imagen_base", "")
    return (
        f"Keep the exact same character from the reference image — same face, "
        f"same hair, same outfit. {personaje.descripcion_en}. "
        f"Place her in this scene: {base}"
    )
