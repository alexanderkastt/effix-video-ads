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

import re
import subprocess
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


# Cómo se ESCRIBE para que se CANTE bien. La grafía del guion es la correcta
# para leer y para alinear con whisper; ésta es la que se le manda al modelo.
#
# "Feria Effix" se cantaba mal en los dos primeros ads: whisper transcribió
# "Feria Fix" y "Vería fix". No es que el modelo no sepa decirlo — es la
# sinalefa del español, que funde la "a" final de Feria con la "E" inicial de
# Effix y produce "feriéffix". La tilde rompe la fusión y obliga a atacar la E
# como sílaba propia. La marca es requisito duro: nunca se abrevia ni se
# deforma, así que esto no es opcional.
# Los dos fallos medidos son el mismo fenómeno: el enlace entre palabras del
# español hablado, que al cantarse se come una sílaba entera.
PRONUNCIACION_CANTADA: list[tuple[str, str]] = [
    # "Feria Effix" → sinalefa a+E. La tilde obliga a atacar la E.
    (r"Feria\s+Effix", "Feria Éffix"),
    # NO hay entrada para "resultados", y es a propósito. MiniMax se come la L
    # de "re-SUL-ta-dos" y canta "resurodios": falló tres veces en dos canciones
    # distintas, y separarla con coma no arregló nada. Cuando el modelo no sabe
    # decir una palabra, la salida barata no es pelear con la grafía sino
    # escribir otra palabra — el verso se cambió a "de los que ya están
    # vendiendo" en los guiones, que además es lo que ya decía el overlay.
    # Regla general: esta tabla arregla pronunciación, no palabras rotas.
]

# Se pide además por el canal de estilo, que es donde el modelo lee las
# instrucciones de interpretación y no de letra.
TAG_PRONUNCIACION = (
    "pronounce the brand 'Feria Éffix' as two separate stressed words, "
    "never blend them into one"
)


def _letra_para_minimax(letra: str) -> str:
    for es, en in SECCIONES.items():
        letra = letra.replace(es, en)
    for patron, cantado in PRONUNCIACION_CANTADA:
        letra = re.sub(patron, cantado, letra, flags=re.IGNORECASE)
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

    etiquetas = list(brief.get("suno_style_tags", []))
    if not any("pronounce" in t.lower() for t in etiquetas):
        etiquetas.append(TAG_PRONUNCIACION)
    tags = ", ".join(etiquetas)
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

MODELO_CANCION_11 = "fal-ai/elevenlabs/music"

# MiniMax Music 3: la versión nueva de la 2.6 con la que empezó el proyecto.
# Trae las dos cosas que faltaban —campo `duration` para encargar los segundos
# que caben en el formato, y `guidance_scale` para apretar la dicción— y cobra
# por segundo: 58s salen por 0.116 USD, la quinta parte de ElevenLabs Music.
MODELO_CANCION_MM3 = "minimax/music-3"

# Decisión de Alexander (2026-09-06), al oír la primera canción de Music 3: le
# gustó, pero las quiere "un poco más animadas, la música más movida". Un ad de
# feed compite con el scroll y una pista correcta pero tibia no lo gana. Se pide
# por dos vías a la vez, porque el modelo atiende mejor a la suma: descripción
# de energía y un empujón sobre el BPM que trae el guion.
ENERGIA = (
    "high energy, driving rhythm, strong danceable groove, punchy drums, "
    "uptempo and lively throughout, never mellow or laid back"
)
BPM_EXTRA = 12

# Palabras que los modelos de canto DEFORMAN. Todas medidas, ninguna supuesta:
# cada una costó al menos una canción. Se comprueban en la validación del guion
# —gratis— para no descubrirlas otra vez pagando.
#
# El patrón es siempre el mismo: grupos consonánticos que el modelo no articula
# (la L de re-SUL-ta-dos) o palabras inglesas dentro de una letra en español,
# que intenta leer con fonética castellana y destroza. La salida no es pelear
# con la grafía sino escribir otra palabra: son letras publicitarias, siempre
# hay sinónimo.
PALABRAS_QUE_NO_CANTA: dict[str, str] = {
    "resultados": 'sale "resurodios", "bra rosados", "jesuitos" — 5 fallos en 4 canciones',
    "trafficker": 'sale "tráfico, me encas" — palabra inglesa en letra española',
    "ecommerce": 'sale "Kecoxie", "Conte Day"',
    "dropshipping": "palabra inglesa larga, mismo riesgo que trafficker",
}

# Music 3 lee las etiquetas de estructura en minúscula y EXIGE que cada una vaya
# sola en su línea: el texto que comparta línea con una etiqueta se descarta.
SECCIONES_MM3 = {
    "[Verso 1]": "[verse]", "[Verso 2]": "[verse]", "[Verso 3]": "[verse]",
    "[Verso]": "[verse]", "[Pre-coro]": "[pre-chorus]", "[Coro]": "[chorus]",
    "[Puente]": "[bridge]", "[Intro]": "[intro]", "[Outro]": "[outro]",
}


def componer_cancion_minimax3(
    brief: dict[str, Any],
    *,
    job_id: str,
    destino: Path | None = None,
    duracion_s: int = 58,
) -> Path:
    """Compone la canción con MiniMax Music 3.

    Devuelve WAV, así que se convierte a mp3 para que el resto del pipeline no
    tenga que saber de formatos.
    """
    letra = brief["suno_custom_lyrics"]
    for es, en in SECCIONES_MM3.items():
        letra = letra.replace(es, en)
    for patron, cantado in PRONUNCIACION_CANTADA:
        letra = re.sub(patron, cantado, letra, flags=re.IGNORECASE)

    etiquetas = list(brief.get("suno_style_tags", []))
    if not any("pronounce" in t.lower() for t in etiquetas):
        etiquetas.append(TAG_PRONUNCIACION)
    prompt = ", ".join(etiquetas) + f". {ENERGIA}. Colombian Spanish vocals, "
    prompt += "clear diction, full musical arrangement with instruments, "
    prompt += "radio-ready ad jingle"
    bpm = brief.get("bpm_recomendado")
    if bpm:
        # El BPM del guion es el punto de partida, no el destino: la primera
        # tanda salió correcta pero apagada para un feed.
        prompt += f", around {int(bpm) + BPM_EXTRA} BPM"

    salida = fal_client.subscribe(
        env("FAL_MODEL_CANCION_MM3", MODELO_CANCION_MM3),
        {
            "prompt": prompt,
            "lyrics": letra,
            "duration": duracion_s,
            # Más pasos sí (el cómputo extra de un ad de 58s no cuesta nada),
            # pero el guidance apenas por encima del default de 1.7. A 2.2 la
            # pista degeneró en "de-de-de-de" durante 58 segundos: guidance alto
            # aprieta la dicción hasta que el modelo se atasca en una sílaba,
            # que es el modo de fallo clásico de la difusión sobreguiada.
            "num_inference_steps": 40,
            "guidance_scale": 1.8,
        },
    )
    ruta = destino or (AUDIO_DIR / job_id / "cancion.mp3")
    crudo = _bajar(salida, ruta.with_suffix(".wav"))
    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         "-i", str(crudo), "-c:a", "libmp3lame", "-b:a", "256k", str(ruta)],
        check=True)
    crudo.unlink(missing_ok=True)
    return ruta


def _plan_de_composicion(brief: dict[str, Any], duracion_ms: int | None = None,
                         sections: int | None = None) -> dict[str, Any]:
    """Traduce la letra del guion al `composition_plan` de ElevenLabs Music.

    A diferencia de MiniMax, este endpoint no tiene campo `lyrics`: la letra
    viaja dentro del plan, una sección por bloque ([Verso], [Coro]…) y una
    entrada de `lines` por verso. Es lo que permite que cante el guion palabra
    por palabra en vez de improvisar sobre una descripción.

    `sections` recorta el plan a las primeras N secciones, que es como se pide
    una prueba corta sin pagar la canción entera.
    """
    bloques: list[tuple[str, list[str]]] = []
    for linea in _letra_para_minimax(brief["suno_custom_lyrics"]).splitlines():
        limpia = linea.strip()
        if not limpia:
            continue
        if limpia.startswith("[") and limpia.endswith("]"):
            bloques.append((limpia.strip("[]"), []))
        elif bloques:
            bloques[-1][1].append(limpia)
        else:
            bloques.append(("Verse", [limpia]))

    bloques = [b for b in bloques if b[1]]
    if sections:
        bloques = bloques[:sections]

    versos = sum(len(l) for _, l in bloques) or 1
    total = duracion_ms or int(versos * 3800)   # ~3.8s por verso cantado
    estilos = list(brief.get("suno_style_tags", []))
    if not any("pronounce" in t.lower() for t in estilos):
        estilos.append(TAG_PRONUNCIACION)

    # fal expone el plan en snake_case, no en el camelCase de la API de
    # ElevenLabs. Mandarlo en camelCase devuelve un 422 con todos los campos
    # marcados como faltantes (gratis, pero no genera nada).
    return {
        "positive_global_styles": estilos + ["Colombian Spanish vocals", "clear diction"],
        "negative_global_styles": ["mumbled vocals", "slurred words", "instrumental only"],
        "sections": [
            {
                "section_name": nombre,
                "positive_local_styles": ["clear sung vocals"],
                "negative_local_styles": ["spoken word"],
                "duration_ms": max(3000, int(total * len(lineas) / versos)),
                "lines": lineas,
            }
            for nombre, lineas in bloques
        ],
    }


def componer_cancion_elevenlabs(
    brief: dict[str, Any],
    *,
    job_id: str,
    destino: Path | None = None,
    duracion_ms: int | None = None,
    sections: int | None = None,
) -> Path:
    """Compone la canción con ElevenLabs Music en vez de MiniMax.

    Cuesta 0.60 USD el minuto —seis veces MiniMax— así que sólo se usa cuando
    MiniMax no logra cantar bien algo que no se puede ceder, como el nombre de
    la marca. Se paga por duración, de modo que una prueba de 15s cuesta 0.15 y
    sirve para comprobar que de verdad canta la letra antes de pagar la entera.
    """
    plan = _plan_de_composicion(brief, duracion_ms, sections)
    salida = fal_client.subscribe(
        env("FAL_MODEL_CANCION_11", MODELO_CANCION_11),
        {"composition_plan": plan, "output_format": "mp3_44100_128"},
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
