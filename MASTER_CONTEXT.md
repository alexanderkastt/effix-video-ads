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

## 💵 Presupuesto por video — regla fija (2026-09-01)

**Cada ad se planifica para caber en 5 USD en promedio.** Todo incluido: video,
imágenes, locución y música. Tope por video: **6 USD**, y sólo si el guión lo
justifica y otro ad de la tanda queda por debajo. Por encima del tope se avisa
y se propone el recorte **antes** de gastar, nunca después.

El objetivo vive en `config/costos.json` → `presupuesto`, y `cost_estimator.py`
lo aplica: `estimar()` devuelve el veredicto y `formatear()` lo imprime con ✅,
⚠️ o 🛑. No bloquea la corrida — el que decide si un ad vale seis dólares es
Alexander; lo que no puede pasar es que se entere cuando ya está pagado.

Las imágenes **cuentan**: un ad de nueve planos con keyframes lleva diecisiete,
y son 1,36 USD — la quinta parte del presupuesto. Pasar `n_imagenes` al estimar.

**Palancas para bajar, en orden de rendimiento:**
1. Menos segundos de video: es el 70% del costo (Kling o1 standard, 0,084 USD/s).
2. Keyframe final donde la frase no cabe en 5s: **sin frame final Kling sólo
   vende 5 o 10 segundos**, así que una línea de 6s sin keyframe se factura como
   10s. La imagen extra cuesta 0,08 y ahorra cuatro segundos (0,34).
3. Las imágenes son baratas frente al video: preferir un plano más corto y bien
   encuadrado antes que un clip largo.
4. La música son 0,20 fijos por pista, no por minuto: no se recorta por ahí.

**Referencia real:** el skeleton "Un año en la vitrina" (47s, 9 clips, 17
imágenes) costó 6,30 USD — se pasó del tope. Un ad de 6 clips de 5s con 8
imágenes sale en 3,43.

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
3. **Música** — de la librería del repo, mezclada en post

**La música no es opcional.** Estuvo enunciada aquí como "capa siempre" mientras
en el código el default era `musica=None`, así que ningún ad salía con fondo. Ya
no: `video_assembler.ensamblar()` toma por defecto la pista que le toca al estilo
y solo se apaga con `musica=False`, que es para el modo `musical_sync` —ahí la
canción ya es la pista principal—.

- **Librería:** `assets/audio/soundtracks/<mood>.mp3`, indexada en
  `config/soundtracks.json`. Seis moods: energetico, emotivo, aspiracional,
  alegre, tenso, epico. Se generaron una vez por 1.20 USD y se reusan gratis.
  Componer pista nueva por ad sería 0.20 recurrentes por un fondo que nadie va a
  distinguir del anterior. Para rehacerlas: `python scripts/generar_soundtracks.py`.
- **Mezcla:** una sola implementación, `src/mezcla.py`. Ducking real con
  `sidechaincompress` —la música se hunde sola cuando alguien habla y vuelve a
  subir en los silencios—, fade-out derivado de la duración real y `loudnorm` a
  **−14 LUFS** en el master, que es lo que piden Instagram, TikTok y YouTube.
  Antes había tres mezclas distintas en tres archivos, con volúmenes distintos y
  un fade escrito a mano en el segundo 48.
- **Volumen:** `MUSICA_VOLUMEN=0.18` en el `.env`. Con el sidechain no hay que
  elegir entre que se oiga y que no tape la voz.

**Obligatorio en cada prompt de video:** cerrar el bloque de Audio con
`no discernible speech` / `no speech`. Si el modelo genera murmullo con voces
reconocibles, choca con la voz en off y el mix suena sucio.

**Lipsync:** solo en clips puntuales, no en todos. Se aplica DESPUÉS de generar
el clip — nunca pedir movimiento de boca dentro del prompt y lipsync encima, sale
boca doble. Rutas: HyperFrames/HeyGen, Higgsfield `video_speak`, Magnific `video_speak`.
En personajes no humanos el lipsync puede fallar (modelos entrenados en caras
humanas) — plan B: reacción solo con ojos y la línea queda en off.

**Longitud de guion:** la voz real corre a **3.69 palabras por segundo** (medido
el 2026-09-02 con "Medellin - Conversational and Intense" a `speed 1.15`). 45s ≈
166 palabras. Números escritos en letras, no en cifras.

El número no se calcula, se mide: no escala lineal con el `speed`. Vive en
`PALABRAS_POR_SEGUNDO` del `.env` y se remide con `python scripts/calibrar_voz.py`
cada vez que cambia la voz o la velocidad. Los 2.2 y 2.75 que andaban sueltos por
el repo eran estimaciones de escritorio; el 2.96 fue una medición a `speed 0.83`
que quedó vieja.

## Ritmo y montaje — regla fija de todos los ads

**El corte visual cae cada 1.5–2.5 segundos.** No cada cuatro, y sobre todo no
"cuando termine la frase". Un ad donde el plano dura lo que dura la línea se lee
como lento aunque el guión sea bueno: en el feed, la línea de seis segundos es un
plano de seis segundos.

**Los planos extra no cuestan video generado.** Cuando una línea pide más de un
plano, el segundo sale del MISMO clip con otro encuadre: `trim` del tramo que toca
y un `crop` distinto. Es el punch-in de toda la vida — la misma toma vista más
cerca se lee como otra cámara. Generar dos clips por línea larga duplicaría el
gasto de video y rompería el tope de 6 USD.

Lo hace `src/ritmo.py`, y ningún montaje tiene que reimplementarlo:

- Una línea de hasta 2.5s es un plano. Más que eso se parte, redondeando hacia
  arriba: 3.6s son dos planos de 1.8s, no un plano de 3.6s.
- Piso duro de 1.25s por plano. Debajo de eso el ojo no alcanza a leer el
  encuadre y el corte se siente como un error. Es preferible un plano de 2.8s a
  dos de 1.4s cortados a mitad de palabra.
- Cuatro encuadres que alternan y nunca se repiten seguidos: `full`, `punch`
  (crop 0.80 subido al tercio superior, donde vive la cara), `lateral` y
  `contra`. El ciclo se arrastra entre líneas para que el corte también se note
  al pasar de una a la siguiente.
- Zoom máximo **1.25x**. Recortar al 80% de 1080x1920 y volver a escalar todavía
  aguanta; más que eso se empieza a ver el pixel.

**El aire entre réplicas son 0.12s** (`RESPIRO_S` en el `.env`). Eran 0.25, 0.35
y 0.12 hardcodeados en tres scripts, así que el mismo guión respiraba distinto
según por dónde se montara. Cada centésima de más es un hueco que se oye como
duda.

**La frase puede cruzar el corte, y debe.** `FACTOR_DESBORDE = 1.15` en
`src/plan_clips.py`. Ahora que la imagen corta cada 1.5–2.5s, el desborde es más
necesario, no menos: una locución que respeta el corte al milímetro suena a lista
de viñetas leída en voz alta.

**Sigue prohibido pedir "slow" o "deliberate"** en los prompts de video: sale
cámara lenta real. El ritmo se construye en el montaje, no pidiéndole velocidad
al modelo.

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

- **2026-09-02 — "Le falta dinámica" casi nunca es el guión.** Los tres ads de
  `tienda_ropa` se sentían lentos y el guión estaba bien. El problema era que la
  unidad de corte estaba atada a la unidad de habla: un plano por línea. Separar
  plano de línea, y sacar los planos extra del mismo clip por reencuadre, subió
  el ad de 12 planos a 19 sin gastar un peso más de video.
- **2026-09-02 — Un número medido se pudre.** `PALABRAS_POR_SEGUNDO` estaba en
  2.96 (medido a `speed 0.83`), 2.75 en `script_engine.py` y 2.2 en dos
  docstrings: cuatro verdades distintas para la misma cosa. Cualquier constante
  que salga de una medición va al `.env` con el script que la remide al lado.
- **2026-09-02 — Una regla que solo está escrita no existe.** "Música en todos
  los ads" llevaba meses en este archivo mientras el código tenía `musica=None`
  por defecto y `object-talk` la prohibía explícitamente. Si una regla es fija,
  el default del código tiene que serlo también.
- **2026-09-02 — El frontmatter de un SKILL.md se rompe con `": "`.** Una
  `description:` en escalar plano que contenga dos puntos y espacio no parsea
  como YAML, y el indexador cae al primer título del cuerpo: la skill deja de
  dispararse por sus triggers. `ganchos-y-retencion` y `storyboard-director`
  llevaban tiempo así. Descripción larga siempre en bloque `>-`.
