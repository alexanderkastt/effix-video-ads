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
    # La familia por nicho, ya generada en Pixar. Las de otros formatos se
    # crean bajo demanda y quedan al lado con el nombre de hoja_de().
    "dropshipping": "referencias/personajes/familia/effi_pixar.png",
    "ia": "referencias/personajes/familia/bit_pixar.png",
    "contadores": "referencias/personajes/familia/cifra_pixar.png",
    "abogados": "referencias/personajes/familia/lex_pixar.png",
    "agencias_contenido": "referencias/personajes/familia/clap_pixar.png",
    "agencias_pauta": "referencias/personajes/familia/panel_pixar.png",
    "ecommerce": "referencias/personajes/familia/carri_pixar.png",
    "importadores": "referencias/personajes/familia/conte_pixar.png",
    "laboratorios": "referencias/personajes/familia/matra_pixar.png",
    "logistica": "referencias/personajes/familia/vani_pixar.png",
}



# La familia por nicho. Cada oficio tiene su objeto, con el mismo lenguaje
# que Effi: cuerpo de objeto real, dos ojos expresivos en la cara frontal,
# brazos cortos, delantal de lona, y una marca de uso que le da carácter
# (la cinta de embalar de Effi es "como una cicatriz"). BIT los acompaña a
# todos, y la paleta es la misma: son diez miembros de un universo, no diez
# mascotas sueltas.
POR_NICHO: dict[str, str] = {
    "abogados": (
        "LEX: an anthropomorphic legal case folder character, thick manila file "
        "with a bulldog clip on top, two expressive eyes on the front cover, "
        "short stubby paper arms "
        "wearing a small dark barrister's robe with a white collar tab, a red ribbon bookmark hanging from one side like a tie"
    ),
    "agencias_contenido": (
        "CLAP: an anthropomorphic film clapperboard character, hinged top slate "
        "that opens like a mouth, two expressive eyes on the black slate face, "
        "short stubby arms "
        "wearing a backwards director's cap and headphones slung around its neck, chalk marks half-erased across its front"
    ),
    "agencias_pauta": (
        "PANEL: an anthropomorphic billboard character, small rectangular sign "
        "body on two stubby legs, two expressive eyes on the display face, short "
        "stubby arms "
        "wearing a bomber jacket and a lanyard with a blank pass, a bent corner on the frame from use"
    ),
    "contadores": (
        "CIFRA: an anthropomorphic pocket calculator character, rounded plastic "
        "body, two expressive eyes above a small numeric display that works as a "
        "mouth, rows of chunky buttons across the belly, short stubby arms, "
        "wearing a knitted sweater vest, a green accountant's visor and cloth sleeve garters, one button worn blank from being pressed too much"
    ),
    "dropshipping": (
        "EFFI: an anthropomorphic corrugated cardboard shipping box character, "
        "rounded corners, two expressive eyes on the front panel, short stubby "
        "cardboard arms "
        "wearing a canvas work apron with a single chest pocket, packing tape strip across one corner like a scar"
    ),
    "ecommerce": (
        "CARRI: an anthropomorphic shopping cart character, chrome wire basket "
        "body, two expressive eyes on the front grille, short stubby arms, "
        "wearing a shop assistant's half-apron and a price tag dangling from one side, one wheel slightly crooked so it always leans a little"
    ),
    "ia": (
        "BIT: a small floating spherical assistant, matte white shell, single "
        "soft cyan light-ring for a face, no arms, hovering"
    ),
    "importadores": (
        "CONTE: an anthropomorphic shipping container character, corrugated steel "
        "body with rounded corners, two expressive eyes above the door latches, "
        "short stubby arms "
        "wearing a hard hat and a hi-vis safety vest, faded stencilled marks and rust spots along one side"
    ),
    "laboratorios": (
        "MATRA: an anthropomorphic laboratory flask character, rounded glass body "
        "with a narrow neck, two expressive eyes on the glass, gentle liquid "
        "sloshing inside, short stubby arms "
        "wearing a white lab coat and safety goggles pushed up on its head, a cork stopper tilted on top"
    ),
    "logistica": (
        "VANI: an anthropomorphic delivery van character, small rounded van body, "
        "two expressive eyes in place of the windshield, short stubby arms, "
        "wearing a delivery driver's cap and a hi-vis vest, one headlight slightly dimmer than the other"
    ),
}


# El género de cada quien, para que la voz no contradiga lo que se ve en
# pantalla. Lo consume audio_extra.verificar_genero().
GENEROS: dict[str, str] = {"camila": "f", "andres": "m"}


def genero_de(clave: str) -> str | None:
    """'f', 'm' o None si el personaje no está declarado."""
    return GENEROS.get(clave)


# Personajes de la casa. La descripción es en inglés porque es lo que leen
# los modelos, y es deliberadamente específica: los rasgos que se repiten
# (color de blusa, aretes, peinado) son lo que hace reconocible a alguien
# de un plano a otro.
CATALOGO: dict[str, str] = {
    **POR_NICHO,
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


def estilo_de_formato(formato: str) -> str:
    """El prefijo visual que usa ese formato, tal como lo define el proyecto.

    El personaje tiene que existir en el estilo del video: la calculadora de
    los contadores no se ve igual en Pixar que en crochet o en Minecraft.
    En vez de escribir el estilo a mano en cada llamada, se toma del mismo
    sitio del que salen los prompts de escena, para que no se separen.
    """
    from .scene_builder import ESTILOS
    if formato in ESTILOS:
        return ESTILOS[formato]["prefijo_prompt"].rstrip(", ")
    # Los estilos especiales no tienen prefijo: su look vive en
    # `universal_positivo`, que es el bloque que va en todos sus prompts.
    from .estilos_especiales import ESTILOS_ESPECIALES
    especial = ESTILOS_ESPECIALES.get(formato)
    if especial:
        # crochet lleva su look en `universal_positivo`; los demas solo
        # tienen `descripcion`, que describe el formato entero y no el
        # aspecto. Se usa lo que haya y se recorta, porque una hoja de
        # personaje no necesita las reglas de montaje del estilo.
        texto = especial.get("universal_positivo") or especial.get("descripcion") or formato
        return str(texto).split(".")[0].rstrip(", ")
    return formato


def hoja_de(clave: str, formato: str, carpeta: Path) -> Path:
    """Dónde vive la hoja de un personaje en un formato dado.

    Una hoja por par personaje+formato: diez personajes en catorce formatos
    son ciento cuarenta, y pre-generarlas todas seria pagar por combinaciones
    que quiza no se usen nunca. Se genera la primera vez que hace falta y se
    reutiliza siempre.
    """
    return carpeta / f"hoja_{clave}_{formato}.png"


def crear_personaje(
    clave: str,
    *,
    estilo_en: str | None = None,
    formato: str | None = None,
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

    if estilo_en is None:
        if not formato:
            raise ValueError("Hace falta `formato` o `estilo_en` para saber cómo dibujarlo.")
        estilo_en = estilo_de_formato(formato)

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
    # El pronombre estaba quemado en "her". Con un personaje masculino el
    # prompt le pedía al modelo una mujer mientras la referencia mostraba un
    # hombre: dos instrucciones que se contradicen y degradan la imagen.
    pronombre = {"f": "her", "m": "him"}.get(genero_de(personaje.nombre), "them")
    return (
        f"Keep the exact same character from the reference image — same face, "
        f"same hair, same outfit. {personaje.descripcion_en}. "
        f"Place {pronombre} in this scene: {base}"
    )
