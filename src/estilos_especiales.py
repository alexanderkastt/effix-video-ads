"""Estilos de producción avanzados, cada uno con su pipeline propio.

Los textos universales (positivo, negativo, cierre I2V, Character Bibles) están
copiados VERBATIM de los skills de origen. No se reescriben ni se "mejoran": los
modelos responden a esas cadenas exactas, y cambiarles una palabra es lo que
convierte un clip bueno en uno inservible.

Fuentes:
  · crochet.md          — Crochet Ad Visuals
  · skeleton.md         — Skeleton Ad Director
  · Zack-d-fimls-skill  — zack-d-films
  · object-talk/SKILL   — Object Talk
  · guía-microsituaciones.pdf — micro-doc UGC

Cada estilo declara `reglas_criticas`: limitaciones reales de los modelos
medidas en producción. Respetarlas evita generaciones fallidas.
"""

from __future__ import annotations

from typing import Any

# ===========================================================================
# ESTILO 1 — CROCHET / TEJIDO
# ===========================================================================

CROCHET: dict[str, Any] = {
    "nombre": "crochet",
    "descripcion": (
        "Mundo miniatura completamente tejido en crochet/lana. Cada superficie, "
        "personaje, objeto y piel está hecho de puntos de hilo visibles y lazos "
        "de tela."
    ),
    "modelos": {
        "imagen": "Seedream 4.5 (mejor, soporta negativos) · Nano Banana Pro · ChatGPT/DALL-E",
        "video": "Seedance 1.5 Pro (el más barato confiable) · Kling · Veo",
    },
    # --- textos universales: VERBATIM, no tocar ---
    "universal_positivo": (
        "The entire scene is fully crocheted and knitted — every surface, character, "
        "object, and skin is made of visible yarn stitches and fabric loops. No "
        "realistic skin, no smooth surfaces, no photorealistic textures anywhere in "
        "the frame. Every element, including hands, arms, faces, and backgrounds, "
        "must have visible knit and crochet stitch texture throughout. Stop-motion "
        "animation diorama scene, handmade knitted and crocheted miniature world."
    ),
    "universal_negativo": (
        "realistic skin, smooth skin, photorealistic hands, photorealistic faces, "
        "realistic textures, smooth surfaces, CGI render, claymation, clay texture, "
        "Pixar style, Disney style, 3D animation, plastic texture, flat cartoon, "
        "airbrushed, anime, illustrated, 2D, studio lighting, ring light, HDR, "
        "symmetrical lighting, harsh shadows, perfectly exposed."
    ),
    "cierre_i2v": (
        "Ensure the entire scene remains fully crocheted and knitted throughout every "
        "frame — all characters, objects, and surfaces must retain visible yarn stitch "
        "texture with no realistic or smooth surfaces at any point. Non-CGI. "
        "Non-cinematic. Animations must start at the first frame. Non-disney."
    ),
    # Un solo foco motivado por escena. NUNCA studio/ring light/HDR.
    "iluminacion": {
        "interior_dia": "soft natural light from a small diorama window to the left",
        "bar_noche": "warm motivated light from tiny knitted overhead pendant lamps",
        "calle_noche": "warm soft glow from tiny crocheted streetlamps",
        "baño": "soft cool flat natural light from a window to the left",
        "exterior": "soft diffused daylight from above-left",
        "sala_acogedora": "warm lamplight from a tiny knitted floor lamp in the corner",
    },
    "reglas_criticas": [
        "Enmarcar el MUNDO como diorama stop-motion, nunca al personaje como 'crocheted man'. "
        "El modelo renderiza la textura de lana en la piel mucho mejor si todo el mundo es diorama.",
        "NUNCA describir 'piel tejida' directamente — produce resultados inconsistentes. "
        "El framing de diorama lo lleva automáticamente.",
        "Evitar poses complejas de brazos/manos. El modelo no renderiza dedos en lana. "
        "Simplificar a: de pie, sentado, gesto de un solo brazo, inclinado, caminando.",
        "Los efectos de partículas fallan como nubes densas o explosiones (salen a humo/CGI). "
        "Reemplazar por yarn ball orbs individuales 'floating' o 'hovering'.",
        "Fragancia/vapor por partículas no funciona. Usar storytelling de personaje: "
        "el personaje huele su muñeca y reacciona. Comunica lo mismo y sí genera.",
        "Nunca describir como: glass particles, CGI sparkles, realistic mist, smoke, vapor cloud.",
    ],
    "particulas": {
        "forma": "yarn ball orbs — pequeños, redondos, con textura de lana, tamaño variado",
        "color": {
            "fragancia": "amber", "hidratacion": "blue", "frescura": "green",
            "lujo": "gold", "pureza": "white",
        },
        "cantidad": "un puñado pequeño — visibles, nunca llenando el cuadro",
        "movimiento": "drift lazily, bob gently, hover — nunca estallidos ni nubes densas",
        "antes": "los orbs se evaporan / se desvanecen",
        "despues": "los orbs persisten, flotan suavemente, nunca desaparecen",
    },
    "tipos_de_clip": {
        "A": "Solo frame inicial — la acción ocurre y se resuelve dentro del clip. "
             "Empieza y termina en el MISMO estado visual.",
        "B": "Frame inicial + frame final — cambio de estado. El frame final es el "
             "estado FINAL ATERRIZADO, nunca a mitad de movimiento.",
        "C": "Solo frame inicial — plano sostenido o movimiento mínimo (fibra que "
             "se mece, push lento de cámara, respiración).",
    },
    "estructura_prompt_imagen": [
        "1. Descripción específica de la escena — qué pasa, quién, dónde, qué props",
        "2. Universal Positivo — verbatim",
        "3. Iluminación — un solo template",
        "4. Universal Negativo — verbatim (modelos que lo soporten)",
        "5. @image1 si el producto aparece en escena",
    ],
    "estructura_prompt_video": [
        "1. Movimiento primario — qué se mueve, cómo, a qué ritmo",
        "2. Elementos secundarios — qué queda quieto, qué reacciona sutilmente",
        "3. Dirección de cámara — locked / slow push / slow pull. Mínima.",
        "4. Cierre I2V — verbatim",
    ],
    "fps": 24,
}


# ===========================================================================
# ESTILO 2 — SKELETON AD (escalada progresiva)
# ===========================================================================

SKELETON: dict[str, Any] = {
    "nombre": "skeleton",
    "descripcion": (
        "Video vertical 9:16 de 30-60s con un esqueleto de dibujos animado que vive "
        "una progresión escalada, narrado en segunda persona presente."
    ),
    "modelos": {
        "imagen": "Nano Banana 2 (default) · GPT Image · Seedance · Midjourney",
        "video": "Kling · Seedance · Veo",
    },
    "mecanicas_obligatorias": {
        "A_hook_curiosidad": "Una pregunta que el cerebro necesita cerrar.",
        "B_espina_escalada": "Escalera de marcadores que intensifican (Tiempo / Cantidad / Etapa).",
        "C_especificos_viscerales": "Cada beat es UNA imagen física y sensorial, no una afirmación abstracta.",
        "D_payoff": "Aterriza en triunfo o en catástrofe.",
    },
    "tipos_de_arco": {
        "transformacion": {
            "cuando": "El beneficio se acumula con el tiempo",
            "spine": "Día 1 → Día 30 → Día 365",
            "payoff": "Triunfo",
        },
        "costo_inaccion": {
            "cuando": "Hay un status quo doloroso que empeora si no actúa",
            "spine": "Día 1 → Mes 3 → Año 2",
            "payoff": "Catástrofe",
        },
        "sobrecarga": {
            "cuando": "La forma antigua de hacer las cosas se rompe",
            "spine": "1 vez → 10 veces → 100 veces",
            "payoff": "Colapso del método viejo",
        },
        "escenario_origen": {
            "cuando": "El producto es visualmente vívido en un mundo inesperado",
            "spine": "Etapa 1 → Etapa 3 → Etapa Final",
            "payoff": "Triunfo épico",
        },
    },
    "reglas_de_beat": [
        "Segunda persona, tiempo presente: 'Te despiertas. Día uno. Tu bandeja es una zona de guerra.'",
        "Una imagen concreta por beat. Frases cortas. Los fragmentos construyen ritmo.",
        "Cada beat debe sentirse más grande/peor/mejor que el anterior.",
        "PROHIBIDO: revolucionario, sin fricciones, aprovechar, solución, game-changer.",
        "Abrir el loop en el hook y NO responderlo antes del payoff.",
        "Ganarse el producto con un 'turn' limpio — nunca pegarlo al final como corte publicitario.",
        "Una idea por beat. Meter dos mata el ritmo y el loop.",
        "El CTA va con la inercia: suave y confiado, nunca 'compra ya'.",
    ],
    "tabla_beneficio_a_visceral": {
        "ahorra tiempo": "Parpadeas y el trabajo ya está hecho. Te quedas mirando la lista vacía, confundido.",
        "reduce churn": "Los clientes se desvanecían como humo. Ahora están encadenados a ti, sonriendo.",
        "más leads calificados": "Día 30: los leads dejan de gotear. Tumban la puerta.",
        "reduce costos": "Tu burn rate era una hoguera. Ahora es una vela de cumpleaños.",
        "difícil sin el producto": "Día 90: todavía pegando hojas de cálculo con cinta. Las grietas suben por las paredes.",
    },
    "plantillas_hook": [
        "¿Qué pasaría si ___?",
        "¿Qué pasa si haces ___ todos los días?",
        "¿Cuánto tiempo puedes ___ antes de ___?",
        "¿Qué pasa si NUNCA ___?",
        "¿Cuántos ___ hacen falta para ___?",
    ],
    # Character Bibles VERBATIM — se pegan palabra por palabra en cada prompt.
    "character_bibles": {
        "bare_bones_cinematic": (
            "CHARACTER: A full anatomical skeleton with natural adult human proportions, "
            "tall and lanky, smooth ivory-cream bones with realistic bone detail (NOT "
            "toy-smooth, NOT chibi, NOT scary), and large expressive cartoon eyes with "
            "white sclera and dark pupils set in the eye sockets, giving an emotive, "
            "surprised, lovable face. No clothing. Same character in every shot. "
            "STYLE: cinematic 3D animated render, photoreal [THEME] environment, warm "
            "[palette] color grade, soft volumetric light with drifting steam/atmosphere, "
            "shallow depth of field. FORMAT: 9:16 vertical."
        ),
        "dressed_skeleton": (
            "CHARACTER: The same friendly skeleton (ivory bones, large expressive cartoon "
            "eyes with white sclera and dark pupils) wearing a complete [THEME-appropriate "
            "wardrobe]; skull, hands and any exposed bones still visible. Same character in "
            "every shot. STYLE: cinematic 3D animated render, photoreal [THEME] environment, "
            "warm [palette] color grade, soft volumetric light, shallow depth of field. "
            "FORMAT: 9:16 vertical."
        ),
        "xray_organs": (
            "CHARACTER: A translucent glowing anatomical human body revealing the full white "
            "skeleton PLUS visible internal organs (heart, lungs, intestines) glowing in red "
            "and orange through a blue-tinted translucent skin outline, with large expressive "
            "cartoon eyes. Same character in every shot. STYLE: clean sci-fi medical 3D "
            "render, cool blue translucent body with warm organ glow, soft rim light. "
            "FORMAT: 9:16 vertical."
        ),
        "cute_mascot": (
            "CHARACTER: A cute chibi cartoon skeleton with an oversized round skull, big "
            "adorable eyes, a small rounded body, and smooth toy-like bones; bright, friendly, "
            "non-scary. Same character in every shot. STYLE: playful Pixar-style 3D animated "
            "render, simple clean [pastel/theme] background, soft even studio lighting, glossy "
            "finish. FORMAT: 9:16 vertical."
        ),
    },
    "bible_por_defecto": "bare_bones_cinematic",
    "consistencia": [
        "Texto bloqueado: el Character Bible se pega verbatim en TODOS los prompts.",
        "Imagen héroe: se genera la imagen 1 primero; es la fuente visual de verdad.",
        "Cada imagen posterior referencia la HÉROE, nunca la imagen anterior — así no deriva.",
    ],
    "negativo_texto": "no text, no captions, no words, no letters, no watermark, no UI",
    "reglas_criticas": [
        "Nada de texto en las generaciones: los subtítulos se ponen en el editor, después.",
        "No cambiar la descripción del personaje entre planos — eso es lo que hace que el modelo lo re-renderice igual.",
        "Un solo movimiento de cámara y una sola acción por clip. No apilar.",
        "El diálogo hablado nunca va dentro del prompt de video: la voz se graba aparte en ElevenLabs.",
    ],
    "para_effix": {
        "hook": "¿Qué pasa si vas a Feria Effix y tu competencia no?",
        "arco": "costo_inaccion",
        "spine": "Semana 1 → Mes 3 → Año 2",
        "beats_ejemplo": [
            "Semana 1 después de Effix. Tienes tres contactos nuevos que resuelven lo que te tuvo frenado seis meses.",
            "Mes 3. Implementaste lo que aprendiste. Tu competencia todavía está probando lo que tú ya validaste.",
            "Año 2. Ellos siguen tomando cursos online. Tú ya eres el que otros buscan en los grupos.",
        ],
        "nota_datos": (
            "El borrador original traía 'conversiones subieron un 40%'. Se quitó: es una "
            "cifra sin fuente y la especificidad falsa es justo lo que destruye credibilidad."
        ),
    },
    "fps": 24,
}


# ===========================================================================
# ESTILO 3 — ZACK D FILMS (documental animado 3D)
# ===========================================================================

ZACK_FILMS: dict[str, Any] = {
    "nombre": "zack_films",
    "descripcion": (
        "Short animado 3D de 28-32 segundos, estilo documental. Abre un loop de "
        "curiosidad en el hook y lo cierra en el kicker con un reencuadre."
    ),
    "modelos": {
        "imagen": "seedream_v5_pro (bloqueado)",
        "video": "gemini_omni (bloqueado)",
        "voz": "seed_audio (bloqueado)",
    },
    "formula_angulo": (
        "Todos creen X — pero [historiadores/ingenieros/científicos] ahora piensan Y, "
        "y el mecanismo real es Z."
    ),
    "beats": {
        "1_mito": "Lo que todos creen — establecer la creencia popular",
        "2_giro": "El 'en realidad...' — la afirmación que voltea la historia",
        "3_mecanismo_a": "Cómo funciona la primera parte del mecanismo real",
        "4_mecanismo_b": "La segunda parte — escalando la revelación",
        "5_kicker": "El reencuadre final que cierra el loop del hook",
    },
    "duracion": {
        "segundos": "28-32",
        "palabras": "75-85",
        "ritmo": "~2.7 palabras por segundo",
        "bloques": "de 10s — N = ceil(duracion/10)",
    },
    "look_visual": (
        "3D estilizado-realista, glossy, sol cálido, cielo cobalto, materiales PBR"
    ),
    "anotaciones": {
        "verde_brillante": "revelación, 'mira aquí', cómo funciona — contornos, flechas, rectángulos",
        "rojo_intermitente": "peligro, física, impacto, error — trayectorias punteadas, grietas, estallidos",
    },
    "ritmo_edicion": {
        "cortes": "6-9 cortes duros por cada bloque de 10s (~1.0-1.6s por plano)",
        "zoom": "punch ~1.0→1.08 en 0.4s, en 3-6 momentos del beat map",
        "shake": "±1% de crop jitter, ~0.3s, en cada frontera de bloque y beat de impacto",
    },
    "reglas_criticas": [
        "Los personajes NUNCA hablan en pantalla — el narrador es externo, sin lip-sync. "
        "Cada prompt de video incluye 'characters only emote and gesture, they do NOT talk'.",
        "Sin texto en pantalla en las generaciones — las anotaciones son formas, no palabras.",
        "Sin nombres de marcas, estudios o IP reales en los prompts.",
        "Variar tamaño Y ángulo en cada corte.",
        "Mínimo un plano MACRO (ojo/detalle) por video.",
        "Un beat de 'gag': revelación deadpan, puf-desaparece.",
        "Consistencia por character sheets: todo lo que aparece en ≥2 planos se genera una vez y se referencia. "
        "El modelo no 'recuerda', VE.",
        "Subject-bleed (bug medido): el sujeto de la imagen ancla se cuela en las láminas de entorno. "
        "El prompt de entorno debe decir 'ENVIRONMENT SHEET — EMPTY LOCATION PLATE, take only the "
        "render style and palette from the reference image, NOT its subject' + 'ABSOLUTELY NO people, NO animals'.",
    ],
    "para_effix": {
        "angulo": (
            "Todos creen que el ecommerce LATAM es un juego de capital — pero los que "
            "escalan dicen que es un juego de información y de con quién estás."
        ),
        "beats_ejemplo": [
            "Mito: 'El que más invierte en ads gana'",
            "Giro: 'Los que más escalan no son los que más gastan en ads'",
            "Mecanismo A: 'Tienen acceso anticipado a qué está funcionando esta semana — antes de que llegue a YouTube'",
            "Mecanismo B: 'Ese acceso viene de estar en la misma sala que los referentes, no de seguirlos online'",
            "Kicker: 'Feria Effix es esa sala. Quince al diecinueve de octubre. Plaza Mayor, Medellín.'",
        ],
        "nota_datos": (
            "El borrador original afirmaba que 'los top sellers de LATAM gastan menos en ads "
            "que sus competidores'. Se reformuló: era una afirmación factual sin fuente, y en "
            "un formato que se apoya en sonar documental eso es especialmente peligroso."
        ),
    },
    "fps": 24,
}


# ===========================================================================
# ESTILO 4 — MICRO-DOCUMENTAL UGC
# ===========================================================================

MICRO_DOC_UGC: dict[str, Any] = {
    "nombre": "micro_doc_ugc",
    "descripcion": (
        "UGC donde el personaje ACTÚA la micro-situación, no la describe. Cámara de "
        "mano, luz natural, reacciones reales. El espectador se reconoce antes de que "
        "le hablen del producto."
    ),
    "modelos": {
        "imagen": "Nano Banana Pro · Seedream 4.5",
        "video": "Kling · Seedance · Veo (image-to-video)",
    },
    "estructura": {
        "0_3s": "El personaje EN el momento exacto (no hablando DE él)",
        "3_8s": "El síntoma observable — el personaje lo vive en cámara",
        "8_15s": "La reacción interna — habla directo a cámara, tono conversacional",
        "15_25s": "El giro — la explicación fallida que todos tienen, luego la real",
        "25_35s": "El mecanismo y la solución, específica y concreta",
        "35_44s": "CTA con micro-situación futura positiva: 'Imagínate que en octubre...'",
    },
    "reglas_de_actuacion": [
        "El personaje empieza DENTRO de la micro-situación, no frente a la cámara.",
        "La cámara lo 'encuentra' — no es una presentación preparada.",
        "Tono conversacional, como con un amigo. Nunca corporativo.",
        "Una auto-corrección o duda calculada por guión — humaniza.",
        "Un dato hiperespecífico: 'era martes a las once de la noche'.",
    ],
    "prefijo_prompt": (
        "iPhone handheld, authentic UGC, natural window light, casual setting,"
    ),
    "sufijo_prompt": (
        "real person, authentic micro-expressions, no studio lighting, visible pores, "
        "slight motion blur, candid, caught mid-moment"
    ),
    "negative": (
        "studio, professional lighting, teleprompter look, too polished, green screen, "
        "fake smile, posed to camera, presenter energy"
    ),
    "reglas_criticas": [
        "Prohibidas en el prompt: cinematic, professional, stunning, 8k, studio, perfect. "
        "Delatan el prompt y el clip deja de parecer grabado con teléfono.",
        "El bloque de audio cierra con 'no discernible speech': la voz entra por ElevenLabs.",
        "El beat es la ACCIÓN, no la explicación. Nunca filmar a alguien describiendo su dolor.",
    ],
    "modelo_fal": "fal-ai/kling-video/v2.1/standard/image-to-video",
    "fps": 24,
}


# ===========================================================================
# ESTILO 5 — OBJECT TALK (objeto antropomorfo Pixar)
# ===========================================================================

OBJECT_TALK: dict[str, Any] = {
    "nombre": "object_talk",
    "descripcion": (
        "Un objeto, ingrediente o concepto abstracto se convierte en personaje "
        "antropomorfo estilo Pixar que habla en primera persona. La gente recuerda "
        "personajes, no productos."
    ),
    "modelos": {
        "imagen": "GPT Image · Midjourney · Flux · Ideogram",
        "video": "Kling · Veo · Sora · Seedance · Runway · Pika · Hailuo",
    },
    "pipeline": "Objeto → Diseño de personaje → Prompt de imagen → Prompt de video",
    "formula_prompt_imagen": [
        "1. Estilo — 'Pixar-style cinematic 3D render'",
        "2. Personaje principal — objeto, material, escala, color, textura, silueta",
        "3. Rasgos faciales — ojos, cejas, boca, cada uno descrito por separado",
        "4. Brazos y lenguaje corporal — la pose debe implicar movimiento incluso en still",
        "5. Entorno — un lugar que le pertenezca al objeto, nunca fondo genérico",
        "6. Elementos de apoyo — partículas, luz; nunca sobrecargar",
        "7. Cámara — hero/medio/retrato/contrapicado, vertical 9:16",
        "8. Iluminación — obligatoria, comunica emoción",
        "9. Calidad de render — PBR, global illumination, subsurface scattering",
    ],
    "reglas_criticas": [
        "El personaje va ANTES del prompt. Definir identidad, personalidad y emoción primero.",
        "Una sola emoción dominante (opcionalmente una secundaria). Nunca emociones en conflicto.",
        "La audiencia debe entender el estado emocional ANTES de leer el diálogo.",
        "Respetar las propiedades del material: el metal refleja, el vidrio refracta, la tela cae.",
        "Poses animation-ready: que permitan mover cabeza, brazos, ojos y boca. "
        "Nada de poses complicadas que dejen al personaje trabado.",
        "Nunca rediseñar el personaje a mitad del pipeline.",
        "Para anatomía: entornos estilizados, no médicamente gráficos. Sin gore.",
    ],
    "para_effix": {
        "objeto_sugerido": "la escarapela del evento, o el carrito de compras de una tienda online",
        "nota": (
            "Effix es un evento, no un producto físico. El objeto que mejor antropomorfiza "
            "es algo que el avatar ya toca a diario — el carrito, el dashboard, la caja de envío."
        ),
    },
    "fps": 24,
}


# ===========================================================================
# Registro
# ===========================================================================

ESTILOS_ESPECIALES: dict[str, dict[str, Any]] = {
    "crochet": CROCHET,
    "skeleton": SKELETON,
    "zack_films": ZACK_FILMS,
    "micro_doc_ugc": MICRO_DOC_UGC,
    "object_talk": OBJECT_TALK,
}


def estilos_especiales_disponibles() -> list[str]:
    """Estilos con pipeline propio (fuera del SceneBuilder genérico)."""
    return sorted(ESTILOS_ESPECIALES)


def obtener(estilo: str) -> dict[str, Any]:
    """Devuelve el template completo de un estilo especial."""
    if estilo not in ESTILOS_ESPECIALES:
        disponibles = ", ".join(estilos_especiales_disponibles())
        raise KeyError(f"'{estilo}' no es un estilo especial. Hay: {disponibles}")
    return ESTILOS_ESPECIALES[estilo]
