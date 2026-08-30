# MASTER CONTEXT — Video IA Ads (Alexander / Kreoon / UGC Colombia)

## Marcas activas
- Alexander (@alexemprendee) — dark luxury, amarillo, emprendimiento LATAM
- Mile (@militougc) — wellness elegante, anti-aging
- Kreoon (@kreoon.latam) — dual morado/amarillo, SaaS de contenido

## Modelos de video disponibles (sin Arcads)
| Herramienta | Acceso | Mejor para |
|---|---|---|
| Higgsfield | higgsfield.ai | Seedance 2.5, Kling 3.0, Sora 2, Veo 3.1 |
| Hailuo / Minimax | hailuoai.com | Estilo anime, Pixar look |
| Pollo.ai | pollo.ai | Pixar nativo directo |
| Revid.ai | revid.ai | Disney/Pixar animado |
| Kling | klingai.com | Motion control, b-roll |
| Runway | runwayml.com | Cinematic, product hero |

## Reglas críticas de prompting UGC (Seedance 2.0)
- NUNCA usar: cinematic, professional, stunning, 8k, studio, perfect
- SÍ usar: handheld, authentic, natural light, candid, iPhone-shot
- Longitud ideal prompt: 100-260 palabras
- Human motion cues obligatorios (3-4 por prompt): breaking eye contact,
  head tilt, weight shift, grip adjustment
- Imperfection block: motion blur, grain, lens distortion, off-center framing

## Fórmula MCSLA (para todos los modelos)
M = Model (qué modelo usar)
C = Camera (framing + movimiento: wide, medium, close-up, dolly-in, handheld)
S = Subject (quién/qué: edad, ropa, expresión, postura)
L = Look (tone visual: iluminación, color grade, atmósfera)
A = Action (qué pasa: presente, un movimiento primario por shot)

## Estructura de 5 etapas (ai-shortfilm-prompts)
1. Opening hook (0-2s): gancho visual o situación
2. Problem/tension (2-5s): el conflicto o dolor
3. Discovery (5-8s): el producto o solución aparece
4. Transformation (8-12s): el cambio / beneficio
5. CTA close (12-15s): llamado a la acción

## Pipeline Pixar-style (sin Arcads)
1. ChatGPT (gpt-image-1 o dalle-3): genera storyboard stills secuenciales
2. Hailuo o Pollo.ai: anima cada still en 4-8s de video
3. CapCut o ffmpeg: une los clips + captions
Tiempo estimado por ad: 45-90 minutos

## Pipeline UGC auténtico
1. Define personaje (edad, look, setting)
2. Genera still con Nano Banana o Midjourney
3. Anima con Veo 3.1 (startFrame) en Higgsfield
4. Agrega audio con ElevenLabs
5. Captions con CapCut / HyperFrames

## ⭐ MODELO MÁS ECONÓMICO: Kling 2.5 (medido 2026-08-28 en Magnific)

Mismo trabajo — clip 9:16 con keyframes start+end encadenados:

| Modelo | Config | Créditos | Por segundo |
|---|---|---|---|
| **Kling 2.5** | **10s · 1080p · start+end** | **650** | **65** |
| Kling 2.5 | 5s · 720p · solo start | 140 | 28 |
| Seedance Fast 2.0 | 8s · 480p · start+end | 960 | 120 |
| Seedance Mini 2.0 | 8s · 720p · start+end | 1.120 | 140 |
| Seedance 1.5 Pro | 8s · 1080p · start+end | 1.760 | 220 |

**Kling 2.5 es 3.4x más barato por segundo que Seedance 1.5 Pro, en la MISMA
resolución 1080p y con los mismos keyframes encadenados.** Además permite clips de
10s, así que un ad de 45s necesita menos clips y tiene menos cortes.

Ad de 45s: **~2.750 créditos con Kling** vs **9.900 con Seedance 1.5 Pro**. 72% menos.

⚠️ Limitación: en Kling 2.5 el `end` keyframe está **prohibido a 720p**. Para
encadenar keyframes hay que ir a 1080p (que igual sale más barato que Seedance).

⚠️ Kling 2.5 no genera audio (`supportsSoundEffects: false`). Da igual: la regla de
esta casa es que el audio va aparte.

**Regla de presupuesto:** hacer `simulate_cost` con los parámetros REALES (duración
final, resolución final, con keyframes) antes de lanzar. Un preflight a 6s sin
keyframes subestimó el costo real en más del doble.

## Costos reales en Higgsfield (medidos 2026-08-28, plan ultra)

Clip vertical 9:16. Preflight con `get_cost: true` antes de generar, SIEMPRE.

| Modelo | Config | Créditos | 6 clips |
|---|---|---|---|
| minimax_hailuo | 6s · 768p | **6** | 36 |
| seedance_2_0 | 4s · 480p fast | 6 | 36 |
| seedance_2_0 | 8s · 480p fast | 12 | 72 |
| seedance_2_0_mini | 8s · 720p | 20 | 120 |
| seedance_2_0 | 8s · 720p fast | 28 | 168 |
| seedance_2_0 | 8s · 1080p std | **72** | **432** |
| nano_banana_pro | imagen 2K | 2 | — |

**Lección:** un ad de 45s en Seedance 1080p cuesta ~430 créditos. Los "drafts baratos"
en 480p cuestan 72 — no son baratos. Calcular el presupuesto ANTES de prometer un
pipeline, no después.

**Diferencia clave de referencias:**
- `seedance_2_0` acepta `image_references` → un solo character sheet sirve para todos
  los clips. Caro pero simple.
- `minimax_hailuo` solo acepta `start_image` / `end_image`, **no** `image_references`
  → hay que generar un still por clip (2 créditos c/u con Nano Banana) y animarlo.
  Más pasos, mucho más barato, y el still da control del aspect ratio que Hailuo no
  expone como parámetro.

## Audio — regla fija de todos los ads

TODOS los videos llevan voz en off de ElevenLabs. El video generado aporta solo
textura, nunca voz. Tres capas siempre:

1. **Textura** — SFX, ambiente y foley, generados dentro del prompt de video
2. **Voz en off** — ElevenLabs, voz "Cristian Sanchez" (paisa colombiano)
3. **Música** — librería, montada en post

**Obligatorio en cada prompt de video:** cerrar el bloque de Audio con
`no discernible speech` / `no speech`. Si el modelo genera murmullo con voces
reconocibles, choca con la voz en off y el mix suena sucio.

**Lipsync:** solo en clips puntuales, no en todos. Se aplica DESPUÉS de generar
el clip — nunca pedir movimiento de boca dentro del prompt y lipsync encima, sale
boca doble. Rutas: HyperFrames/HeyGen, Higgsfield `video_speak`, Magnific `video_speak`.
En personajes no humanos el lipsync puede fallar (modelos entrenados en caras
humanas) — plan B: reacción solo con ojos y la línea queda en off.

**Longitud de guion:** ~2.2 palabras por segundo de locución en español.
45s ≈ 98–110 palabras. Números escritos en letras, no en cifras.

## Guiones

Generarlos con **Kreoon MCP** (`generate_script` o `generate_content_block`).
- Si la marca está registrada → usar `product_id` / `content_id`
- Si no está → modo 2 con `brand_name` + `brand_description`
- Nunca inventar UUIDs: primero `list_clients` / `list_products`
- ⚠️ Kreoon devuelve voseo rioplatense ("sentís", "convertite", "quedés").
  Revisar y adaptar siempre a neutro colombiano o paisa según la audiencia.

## Entorno tecnico del proyecto

Todo vive en `skills-video-ads/`. No crear subproyectos aparte.

- **`python3` no existe en Windows** — el comando es `python` (3.13.5 aqui).
- Entorno Python en `venv/`. Activar: `venv\Scripts\activate`.
- Reinstalar dependencias: `pip install -r requirements.txt`.
- **No instalar el paquete `asyncio` de PyPI**: es stdlib desde Python 3.4 y el
  paquete de PyPI esta muerto — rompe los imports.
- `--break-system-packages` no aplica dentro de un venv.
- ffmpeg 7.1 y ffprobe 8.0.1 son builds distintos en este equipo. Funciona, pero
  conviene alinearlos para evitar diferencias al leer metadata.
- Un venv de Windows **no se puede mover de carpeta**: los `.exe` de `Scripts/`
  llevan rutas absolutas dentro. Si se mueve el proyecto, recrear el venv.

## Notas de aprendizaje (actualizar aquí)
-
