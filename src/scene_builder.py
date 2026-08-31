"""Escenografía por estilo — convierte un beat narrativo en un prompt de video.

La capa que traduce "Beat 03 — DOLOR" en una escena concreta y filmable.

Dos reglas duras heredadas de MASTER_CONTEXT.md:

1. El bloque de audio de todo prompt cierra con `no discernible speech`. La voz
   siempre entra por ElevenLabs en post; si el modelo genera murmullo con voces
   reconocibles, choca con la locución y el mix suena sucio.
2. En `ugc_realista` están prohibidas las palabras `cinematic`, `professional`,
   `stunning`, `8k`, `studio` y `perfect`. Delatan el prompt y el clip deja de
   parecer grabado con un teléfono.

Regla creativa: si el beat es emocional, el visual MUESTRA ese estado. Nunca se
filma a alguien describiendo su dolor; se filma el dolor.
"""

from __future__ import annotations

import re
from typing import Any

# ---------------------------------------------------------------------------
# Catálogo de estilos
# ---------------------------------------------------------------------------

ESTILOS: dict[str, dict[str, Any]] = {
    "ugc_realista": {
        "ambiente": "interior doméstico (sala, cocina, oficina casera) o exterior natural — nunca estudio",
        "iluminacion": "luz natural de ventana o exterior dorado, leve sobreexposición permitida",
        "personaje": "ropa casual-profesional, postura natural ligeramente hacia cámara",
        "movimiento": "handheld sutil, sujeto habla o reacciona naturalmente",
        "prefijo_prompt": "iPhone handheld selfie-style, authentic UGC, natural window light, casual setting,",
        "sufijo_prompt": "real person, authentic micro-expressions, no studio lighting, visible pores, slight motion blur, candid",
        "negative": "studio, professional lighting, teleprompter look, too polished, green screen, fake smile",
        "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
        "fps": 24,
        "escena_en": "a modest Latin American home interior with everyday clutter, a laptop and a phone on the table",
        "luz_en": "soft directional daylight from a side window, mild overexposure on the highlights",
        "sujeto_en": "a Latin American entrepreneur in their early thirties, casual shirt, unstyled hair",
    },
    "cinematic": {
        "ambiente": "exteriores urbanos latinoamericanos — plazas, mercados, skyline, o interiores con carácter",
        "iluminacion": "golden hour, blue hour, o luz de noche con neones cálidos — siempre direccional",
        "personaje": "outfits que marquen identidad — no traje, sí estilo definido",
        "movimiento": "dolly-in lento o rack focus — el sujeto domina el frame",
        "prefijo_prompt": "cinematic 4K, anamorphic lens, shallow depth of field, film grain, golden hour light,",
        "sufijo_prompt": "professional cinematography, bokeh background, color graded, atmospheric, wide cinematic bars",
        "negative": "flat lighting, amateur footage, overexposed, distracting background clutter",
        "modelo_fal": "fal-ai/kling-video/v2.1/pro/image-to-video",
        "fps": 24,
        "escena_en": "a Medellin urban exterior, textured concrete and greenery, distant city skyline",
        "luz_en": "low golden hour sun raking across the frame, long shadows, warm haze",
        "sujeto_en": "a Latin American entrepreneur with a defined personal style, confident posture",
    },
    "pixar_animado": {
        "ambiente": "mundo 3D estilizado — puede ser representación animada de Medellín, de un evento, de una tienda",
        "iluminacion": "iluminación volumétrica cálida, subsurface scattering en personajes, sombras suaves",
        "personaje": "mascota o personaje 3D con rasgos exagerados expresivos — ojos grandes, gestos amplios",
        "movimiento": "animación fluida con anticipación — personaje reacciona antes de moverse",
        "prefijo_prompt": "Pixar 3D CGI style, subsurface scattering skin, volumetric warm lighting, expressive eyes,",
        "sufijo_prompt": "high detail textures, cinematic color grade, Disney Pixar quality render, smooth animation",
        "negative": "realistic human, photo-realistic, flat colors, 2D, cheap animation, uncanny valley",
        "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
        "fps": 24,
        "escena_en": "a stylized 3D version of a Medellin street and a small storefront, rounded shapes",
        "luz_en": "warm volumetric light shafts, soft rounded shadows, gentle rim light",
        "sujeto_en": "an expressive 3D character with oversized eyes and broad readable gestures",
    },
    "cyberpunk": {
        "ambiente": "ciudad nocturna latinoamericana futurista — Medellín 2080, neon, lluvia en pavimento",
        "iluminacion": "neon magenta + cian + ámbar, reflejos en charcos, niebla volumétrica",
        "personaje": "ropa tech con detalles LED, augmentaciones visuales, expresión intensa",
        "movimiento": "cámara baja que sube (low angle tilt), efectos de hologramas en el aire",
        "prefijo_prompt": "cyberpunk neon-noir, rain-slicked streets, holographic UI elements, magenta and cyan lighting,",
        "sufijo_prompt": "blade runner aesthetic, volumetric fog, neon reflections, ultra detailed, cinematic color grading",
        "negative": "daylight, bright cheerful, warm tones, clean streets, no neon",
        "modelo_fal": "fal-ai/kling-video/v2.1/pro/image-to-video",
        "fps": 24,
        "escena_en": "a futuristic Medellin street at night, wet asphalt, floating holographic signage in Spanish",
        "luz_en": "magenta and cyan neon spill, amber practicals, volumetric fog cutting the beams",
        "sujeto_en": "a figure in tech-wear with subtle LED trim, intense focused expression",
    },
    "anime": {
        "ambiente": "dos sub-estilos disponibles: Ghibli (naturaleza, luz suave, nostálgico) o Shonen (acción, energía, dramático)",
        "iluminacion": "Ghibli: luz difusa dorada de tarde. Shonen: contraluz dramático, rayos de energía",
        "personaje": "diseño anime con rasgos grandes, colores vivos, expresiones exageradas",
        "movimiento": "Ghibli: movimiento lento y fluido del ambiente. Shonen: velocidad, impacto, sakuga",
        "prefijo_prompt": "anime style, cel shading, hand-drawn look, Studio Ghibli soft colors,",
        "sufijo_prompt": "high quality anime production, detailed background art, expressive character animation",
        "negative": "photorealistic, 3D CGI, western animation, flat colors without cel shading",
        "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
        "fps": 24,
        "escena_en": "a hand-painted Latin American street with lush plants and hand-drawn background art",
        "luz_en": "diffuse golden late-afternoon light, soft gradients across the sky",
        "sujeto_en": "an anime character with large expressive eyes and vivid clothing colors",
    },
    "claymation": {
        "ambiente": "mundo en miniatura de plastilina — sets construidos a mano, texturas imperfectas visibles",
        "iluminacion": "luz práctica cálida de estudio pequeño — lámparas de escritorio visibles o sugeridas",
        "personaje": "figuras de arcilla con dedadas visibles, ojos de botón o marcados con herramienta",
        "movimiento": "stop-motion judder a 12fps, movimiento rígido-fluido, imperfecciones entre frames",
        "prefijo_prompt": "claymation stop-motion, Aardman Studios style, plasticine textures, handcrafted miniature set,",
        "sufijo_prompt": "clay fingerprint textures, practical lighting, Wallace and Gromit aesthetic, 12fps stop-motion feel",
        "negative": "smooth CGI, digital animation, realistic textures, high frame rate, clean",
        "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
        "fps": 12,
        "escena_en": "a handmade miniature set of a small shop and a market street, visible craft materials",
        "luz_en": "warm practical desk lamps just off frame, small hard shadows on the clay",
        "sujeto_en": "a plasticine figure with visible thumbprints and tool-marked eyes",
    },
    "minecraft": {
        "ambiente": "mundo vóxel — bloques, pixelado, isométrico o primera persona",
        "iluminacion": "luz de día Minecraft (flat + block shadows) o antorcha interior (cálida parpadeante)",
        "personaje": "skin de personaje vóxel con proporciones Minecraft — cabeza grande, cuerpo cuadrado",
        "movimiento": "cámara de juego — primera persona o tercera persona walking",
        "prefijo_prompt": "Minecraft voxel art style, cubic blocks, pixelated textures, game render,",
        "sufijo_prompt": "blocky aesthetic, Minecraft shaders, procedural world, isometric or first-person view",
        "negative": "realistic, smooth curves, organic shapes, photorealistic, 4K detail",
        "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
        "fps": 24,
        "escena_en": "a voxel world street of cubic buildings and a blocky market stall",
        "luz_en": "flat daylight with hard block shadows, occasional flickering torch",
        "sujeto_en": "a voxel character with a large cubic head and square body proportions",
    },
    "avengers": {
        "ambiente": "escena de acción épica — cielo dramático, ciudad bajo amenaza, epicentro de batalla",
        "iluminacion": "dramático contraluz, explosiones como fuente de luz, nubes que generan rayos",
        "personaje": "traje de superhéroe o armadura — postura heroica, capa al viento",
        "movimiento": "cámara rotatoria (hero shot), slow-motion en momento de poder",
        # El look es el del cine de superheroes, no el de una franquicia: nombrar
        # "Marvel" o "MCU" en un ad que va a pauta es IP ajena, y ademas Kling
        # filtra marcas registradas — el clip rechazado se paga igual.
        "prefijo_prompt": "epic superhero cinematic scene, dramatic backlight, high-end VFX,",
        "sufijo_prompt": "blockbuster visual quality, lens flares, epic scale, IMAX cinematic, dynamic hero pose",
        "negative": "mundane setting, casual clothes, no powers visible, static camera, boring, trademarked costume, comic-book logo",
        "modelo_fal": "fal-ai/kling-video/v2.5-turbo/pro/image-to-video",
        "fps": 24,
        "escena_en": "an epic city skyline under a churning storm sky, debris suspended in the air",
        "luz_en": "hard dramatic backlight, explosions acting as practical light sources, lightning",
        "sujeto_en": "a heroic figure in armored suit, cape catching the wind, grounded stance",
    },
    "musical_sync": {
        "ambiente": "visual que cambia con el beat — puede usar cualquier estilo base como layer visual",
        "iluminacion": "strobes sincronizados al beat, colores que pulsan, waveform visual",
        "personaje": "movimiento sincronizado con la música — baile, reacción, lip-sync",
        "movimiento": "cortes exactos en cada beat de la canción — el video VIVE para la música",
        "prefijo_prompt": "music video style, beat-synchronized editing, dynamic movement,",
        "sufijo_prompt": "music video production quality, rhythm-matched cuts, energetic pacing",
        "negative": "static shot, no movement, ignoring the beat, monotonous",
        "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
        "fps": 24,
        "escena_en": "a performance space with pulsing light rigs and a reactive crowd silhouette",
        "luz_en": "strobing colored light synced to the beat, pulsing saturation shifts",
        "sujeto_en": "a performer moving in time with the music, full-body expressive motion",
        "nota": "Este estilo requiere music_engine.py — Suno genera la canción primero",
    },
}

# Palabras que delatan un prompt de UGC y lo sacan del registro "grabado con teléfono"
PROHIBIDAS_UGC = ["cinematic", "professional", "stunning", "8k", "studio", "perfect"]

# Cómo se MUESTRA cada beat. Nada de "una persona explicando su problema":
# el estado emocional se ve en la acción, el cuerpo y el entorno.
BEAT_VISUALS: dict[int, dict[str, str]] = {
    1: {
        "accion_en": "the subject stops mid-task and looks straight into the lens, caught off guard",
        "lectura_en": "an unfinished gesture holds in the air, attention snapping to camera",
        "es": "el sujeto interrumpe lo que hacía y mira de frente al lente, tomado por sorpresa",
    },
    2: {
        "accion_en": "the subject leans slightly toward the lens, one hand gesturing to themselves",
        "lectura_en": "recognition landing, a small nod of self-identification",
        "es": "el sujeto se inclina hacia el lente y se señala a sí mismo: esto va por él",
    },
    3: {
        "luz_en": "only the cold glow of the screen lighting the face in a dark room",
        "accion_en": "the subject sits alone late at night in front of a screen, shoulders dropped, no one else in frame",
        "lectura_en": "quiet ordinary frustration, not theatrical despair — a slow exhale",
        "es": "solo, de noche, frente a la pantalla, hombros caídos. Frustración leve, no dramática",
    },
    4: {
        "accion_en": "the empty room widens around the subject as the camera pulls back, chair after chair unoccupied",
        "lectura_en": "isolation growing physically larger, the cost becoming visible",
        "es": "la cámara se abre y el vacío alrededor crece — el costo se vuelve visible",
    },
    5: {
        "accion_en": "a door opens and warm light spills in, the subject lifts their head toward it",
        "lectura_en": "the first change in posture, spine straightening",
        "es": "una puerta se abre, entra luz, y el sujeto levanta la cabeza",
    },
    6: {
        "accion_en": "a long table crowded with people talking to each other, hands moving, several conversations at once",
        "lectura_en": "density of real people, no one performing for camera",
        "es": "mesa larga llena de gente hablando entre sí, varias conversaciones a la vez",
    },
    7: {
        "accion_en": "hands exchange a physical product across a stand, both people examining it closely",
        "lectura_en": "the mechanism shown as a concrete transaction, not a diagram",
        "es": "manos intercambiando producto físico en un stand, ambos revisándolo de cerca",
    },
    8: {
        "accion_en": "the subject walks through a busy venue greeting people, phone full of new contacts",
        "lectura_en": "belonging in motion, being recognized by others",
        "es": "el sujeto camina por el recinto saludando gente, ya lo reconocen",
    },
    9: {
        "luz_en": "even ambient venue light, the signage clearly legible",
        "accion_en": "a wall calendar or venue signage fills the frame, the date physically present in the scene",
        "lectura_en": "time made tangible and close",
        "es": "un calendario o señalética del recinto llena el cuadro — la fecha se vuelve tangible",
    },
    10: {
        "accion_en": "the subject holds up a ticket or badge toward the lens, relaxed and direct",
        "lectura_en": "a low-pressure invitation, not a hard sell",
        "es": "el sujeto muestra la entrada o escarapela al lente, tranquilo y directo",
    },
    11: {
        "accion_en": "the subject shrugs once and half-smiles, conceding something small without apology",
        "lectura_en": "an honest concession, low stakes, delivered plainly",
        "es": "el sujeto concede algo pequeño con media sonrisa, sin disculparse",
    },
    12: {
        "accion_en": "the subject walks out of frame into the crowd, no longer alone, the empty chair behind them",
        "lectura_en": "the opening image answered, the loop closing",
        "es": "el sujeto sale de cuadro hacia la multitud; la silla vacía del inicio queda atrás",
    },
}

MOVIMIENTO_EN = {
    "handheld": "loose handheld camera with natural micro-shake",
    "dolly-in": "slow dolly-in pushing toward the subject",
    "static": "locked-off static frame",
    "pan": "steady horizontal pan following the action",
    "closeup": "tight close-up framing on the face and hands",
}


class SceneBuilder:
    """Construye la escenografía y el prompt de video de cada beat."""

    def __init__(self, estilo: str) -> None:
        if estilo not in ESTILOS:
            disponibles = ", ".join(sorted(ESTILOS))
            raise KeyError(f"Estilo '{estilo}' no existe. Disponibles: {disponibles}")
        self.estilo = estilo
        self.tpl = ESTILOS[estilo]

    # -- API ----------------------------------------------------------------

    def build_scene_prompt(
        self,
        beat_dict: dict[str, Any],
        estilo: str | None = None,
        angulo_narrativo: str = "",
    ) -> dict[str, Any]:
        """Combina beat + template de estilo + ángulo y devuelve la escena completa.

        Devuelve un dict con `prompt_video` (inglés, 120-200 palabras),
        `prompt_imagen_base`, `escenografia`, `descripcion_visual` y
        `notas_produccion`.
        """
        tpl = ESTILOS[estilo] if estilo and estilo in ESTILOS else self.tpl
        n = beat_dict["beat"]
        visual = BEAT_VISUALS[n]
        movimiento = beat_dict.get("movimiento_camara", "handheld")
        movimiento_en = MOVIMIENTO_EN.get(movimiento, MOVIMIENTO_EN["handheld"])

        # angulo_narrativo llega en inglés: mezclar idiomas dentro del prompt
        # confunde al modelo y degrada el clip.
        contexto = f" Wider context of the scene: {angulo_narrativo}." if angulo_narrativo else ""

        # El prompt se arma por bloques nombrados: los modelos responden mejor a
        # secciones explícitas que a un párrafo corrido.
        bloques = [
            tpl["prefijo_prompt"],
            f"Shot: {movimiento_en}, vertical 9:16 framing.",
            f"Subject: {tpl['sujeto_en']}.",
            f"Action: {visual['accion_en']}.",
            f"Setting: {tpl['escena_en']}.{contexto}",
            f"Lighting: {visual.get('luz_en') or tpl['luz_en']}.",
            f"Emotional read: {visual['lectura_en']}, shown through body language only.",
            "Audio: ambient room tone and natural background texture, "
            "no music, no discernible speech.",
            tpl["sufijo_prompt"] + ".",
        ]
        prompt = " ".join(b.strip() for b in bloques if b.strip())
        prompt = self._ajustar_longitud(prompt, tpl)

        escenografia = {
            "ambiente": tpl["ambiente"],
            "iluminacion": tpl["iluminacion"],
            "personaje": tpl["personaje"],
            "movimiento": tpl["movimiento"],
            "modelo_fal": tpl["modelo_fal"],
            "fps": tpl["fps"],
            "negative": tpl["negative"],
        }

        return {
            "prompt_video": prompt,
            "prompt_imagen_base": self._prompt_imagen(tpl, visual, movimiento_en),
            "negative_prompt": tpl["negative"],
            "escenografia": escenografia,
            "descripcion_visual": visual["es"],
            "notas_produccion": self._notas(n, tpl),
            "palabras_prompt": len(prompt.split()),
        }

    def apply_to_script(self, script_json: dict[str, Any]) -> dict[str, Any]:
        """Rellena todos los beats de un guión con su escenografía. Muta y devuelve."""
        angulo = script_json.get("visual_clave_en") or script_json.get("visual_clave", "")
        for beat in script_json["beats"]:
            escena = self.build_scene_prompt(beat, self.estilo, angulo)
            beat.update(escena)
        script_json["estilo"] = self.estilo
        script_json["modelo_fal"] = self.tpl["modelo_fal"]
        script_json["fps"] = self.tpl["fps"]
        return script_json

    def validate_prompts(self, script_json: dict[str, Any]) -> list[str]:
        """Verifica longitud (120-200 palabras) y vocabulario prohibido por estilo."""
        errores: list[str] = []
        for beat in script_json.get("beats", []):
            prompt = beat.get("prompt_video", "")
            n = beat["beat"]
            palabras = len(prompt.split())

            if not 120 <= palabras <= 200:
                errores.append(
                    f"Beat {n:02d}: prompt de {palabras} palabras, fuera del rango 120-200."
                )

            if "no discernible speech" not in prompt:
                errores.append(
                    f"Beat {n:02d}: el bloque de audio no cierra con 'no discernible speech'."
                )

            if self.estilo == "ugc_realista":
                for palabra in PROHIBIDAS_UGC:
                    if self._usa_prohibida_ugc(prompt, palabra):
                        errores.append(
                            f"Beat {n:02d}: '{palabra}' está prohibida en ugc_realista."
                        )
        return errores or ["OK"]

    @staticmethod
    def _usa_prohibida_ugc(prompt: str, palabra: str) -> bool:
        """¿El prompt PIDE esa palabra, o la está negando?

        `no studio lighting` es exactamente lo que queremos en UGC: niega el look
        de estudio. Marcarlo como error convertiría la regla en su contrario, así
        que sólo cuenta la aparición que no viene precedida de una negación.
        """
        negadores = {"no", "not", "without", "never", "zero", "avoid"}
        patron = re.compile(r"\b" + re.escape(palabra) + r"\b", re.IGNORECASE)

        for coincidencia in patron.finditer(prompt):
            previos = re.findall(r"[a-zA-Z]+", prompt[: coincidencia.start()])[-2:]
            if not any(p.lower() in negadores for p in previos):
                return True
        return False

    # -- internos -----------------------------------------------------------

    # Relleno de detalle que sube el conteo sin ensuciar el registro del estilo.
    RELLENO = [
        "Framing keeps headroom tight and the horizon slightly low.",
        "Background elements stay soft and unobtrusive behind the subject.",
        "Colour palette stays restrained, letting the subject carry the frame.",
        "Movement resolves inside the four seconds, ending on a settled pose.",
        "Texture detail is visible on fabric and surfaces near the lens.",
        "Depth is built with a clear foreground, midground and background layer.",
    ]

    def _ajustar_longitud(self, prompt: str, tpl: dict[str, Any]) -> str:
        """Lleva el prompt al rango 120-200 palabras exigido por el pipeline."""
        palabras = prompt.split()

        # Corto: agrega detalle de encuadre hasta pasar el mínimo
        i = 0
        while len(palabras) < 125 and i < len(self.RELLENO):
            prompt = f"{prompt} {self.RELLENO[i]}"
            palabras = prompt.split()
            i += 1

        # Largo: recorta por frase completa, nunca a mitad de oración
        if len(palabras) > 200:
            frases = re.split(r"(?<=\.)\s+", prompt)
            recortado: list[str] = []
            total = 0
            for frase in frases:
                n = len(frase.split())
                if total + n > 200:
                    break
                recortado.append(frase)
                total += n
            prompt = " ".join(recortado)

        return prompt.strip()

    @staticmethod
    def _prompt_imagen(tpl: dict[str, Any], visual: dict[str, str], movimiento_en: str) -> str:
        """Prompt del frame inicial. Es una foto fija: describe estado, no acción."""
        return (
            f"{tpl['prefijo_prompt']} still frame, vertical 9:16. "
            f"{tpl['sujeto_en']}, mid-action: {visual['accion_en']}. "
            f"Setting: {tpl['escena_en']}. Lighting: {tpl['luz_en']}. "
            f"Composition matches a {movimiento_en}. {tpl['sufijo_prompt']}."
        )

    @staticmethod
    def _notas(n: int, tpl: dict[str, Any]) -> str:
        notas = [f"Modelo: {tpl['modelo_fal']} · {tpl['fps']}fps."]
        if n == 1:
            notas.append("Frame inicial del video: es el que decide si paran el scroll.")
        if n == 11:
            notas.append("Debe cerrar el círculo con el beat 01 para que el loop funcione.")
        if tpl["fps"] == 12:
            notas.append("12fps: el judder es parte del estilo, no corregir en post.")
        if "nota" in tpl:
            notas.append(tpl["nota"])
        return " ".join(notas)


def estilos_disponibles() -> list[str]:
    """Lista de estilos registrados. Agregar uno es agregar una entrada a ESTILOS."""
    return sorted(ESTILOS)
