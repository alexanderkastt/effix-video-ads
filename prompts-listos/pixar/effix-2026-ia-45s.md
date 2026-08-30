# Feria Effix 2026 — Ad Pixar · Nicho IA · Reel vertical

## ✅ PRODUCIDO — 2026-08-28

**Entregable:** `outputs/pixar-disney/EFFIX-2026-pixar-36s-FINAL.mp4`
**35.7s · 1080×1920 · 30fps · voz + música + ambiente mezclados**

| Archivo | Qué es |
|---|---|
| `EFFIX-2026-pixar-36s-FINAL.mp4` | **El ad.** Video + voz + música + ambiente |
| `EFFIX-2026-pixar-36s-CON-VOZ.mp4` | Sin música, por si quieres poner otra |
| `EFFIX-2026-pixar-36s-SIN-VOZ.mp4` | Solo video + ambiente, base limpia |
| `voz/vo-1..6.mp3` | Las 6 líneas sueltas, para recortar en CapCut |
| `voz/effi-linea.mp3` | "Ah... ahora sí." de EFFI |
| `voz/musica-v2.mp3` | La música usada |
| `voz/musica.mp3` | Primera versión, descartada (tenía huecos) |

### Mezcla de audio

- **Voz:** Ernesto Calderón (ElevenLabs vía Magnific), latino neutro. **No es
  Cristian Sanchez** — esa voz vive en tu cuenta de ElevenLabs y no es accesible
  desde acá. Los 6 mp3 sueltos están para que los reemplaces uno a uno.
- **Ducking activo:** la música baja sola cuando entra la voz (sidechain compressor).
- **Niveles medidos:** mean −16.4 dB, max −1.0 dB. Dentro del estándar de
  Instagram/TikTok, sin clipping.
- La línea de EFFI entra a los 21.9s, dentro del clip 4.

### Pendiente

1. **Textos en pantalla** — en CapCut, ver la tabla de copys más abajo
2. **Lipsync visual del clip 4** — el audio de EFFI ya está en la mezcla, pero la
   boca no se mueve sincronizada. Requiere pasar el clip 4 por HyperFrames/HeyGen
   con `voz/effi-linea.mp3`
3. Opcional: reemplazar la voz por Cristian Sanchez

### Dos cosas aprendidas en el montaje

- **`sidechaincompress` de ffmpeg corta la salida cuando se acaba la señal de
  sidechain.** La música moría a los 34.0s exactos porque la última línea de voz
  terminaba ahí. Se arregla con `apad=whole_dur=<duración total>` en la cadena del
  sidechain antes del `asplit`.
- **ElevenLabs Music interpreta "sparse" y "sit underneath" muy literal** y devuelve
  pistas con silencios reales. Hay que pedir explícitamente "no silence, no empty
  bars, every second has audible instrumentation, even dynamics".

### Qué se generó y dónde

| Clip | Archivo | Modelo | Estado |
|---|---|---|---|
| 1 caos | `clip-01-caos.mp4` | Hailuo (Higgsfield) | OK |
| 2 chispa | `clip-02-chispa.mp4` | Hailuo (Higgsfield) | OK — el entorno derivó a taller |
| 3 llegada | `clip-03-llegada.mp4` | Seedance Mini (Magnific) | OK |
| 4 clic | `clip-04-clic.mp4` | Hailuo (Higgsfield) | **El mejor** — la expresión construye |
| 5 aéreo | `clip-05-aereo.mp4` | Seedance Mini (Magnific) | OK |
| 6 CTA | `clip-06-cta.mp4` | Seedance Mini (Magnific) | OK — rehecho |
| 6 descartado | `clip-06-cta-HAILUO-descartado.mp4` | Hailuo | Falló: personaje lejano, BIT pegado al pecho |

### Por qué 36s y no 45s

El plan de Higgsfield **no permite clips de 10s en Hailuo** ("Requires basic plan or
higher"). Solo 6s. Con 6 clips de 6s el ad quedó en 35.7s. El guion se recortó de 98
a 68 palabras — ver `outputs/GUIONES.md`.

### Costos reales de esta producción

| Concepto | Plataforma | Créditos |
|---|---|---|
| Character sheet (2 variantes) | Higgsfield | 4 |
| 6 stills 9:16 | Higgsfield | 12 |
| 4 clips Hailuo | Higgsfield | ~77 |
| 3 clips Seedance Mini | Magnific | 2.520 |

⚠️ **Higgsfield quedó en 4 créditos y plan `free`.** Empezó en 97 con plan ultra.
Los clips de Hailuo costaron bastante más de lo que el preflight indicaba. Antes de
la próxima producción, revisar el estado real del plan.
Magnific quedó con ~35.000 de 37.685.

### Pendiente para cerrar el ad

1. Grabar la voz en off en ElevenLabs (guion de 36s en `outputs/GUIONES.md`)
2. Lipsync del clip 4 con la línea "Ah... ahora sí."
3. Música de fondo, sube en el clip 5
4. Textos en pantalla en CapCut
5. Bajar el volumen del audio ambiente para que no compita con la voz

---

## Documentación original del pack (45s)

**Objetivo:** registro / asistencia
**Formato:** 9:16, 45s exactos, 6 clips
**Modelo video:** Seedance 2.0 (`std`, 1080p, 9:16)
**Voz:** ElevenLabs — "Cristian Sanchez" (paisa colombiano)
**Fecha:** 2026-08-28 · Guion base generado con Kreoon (`generate_script`, modo 2)

---

## ARQUITECTURA DE AUDIO — 3 CAPAS

El video generado **no trae voz**. Trae solo textura. La voz se monta en post.

| Capa | Origen | Qué contiene |
|---|---|---|
| 1 · Textura | Seedance (dentro del prompt) | SFX, ambiente, foley. **Sin habla inteligible.** |
| 2 · Voz en off | ElevenLabs | El guion completo, locutado |
| 3 · Música | Librería | Bed instrumental, sube en clip 5 |

⚠️ **Regla crítica:** los prompts de audio de abajo dicen explícitamente
`no discernible speech`. Si dejas que Seedance genere murmullo de multitud con voces,
choca con la voz en off y suena sucio. Ya está corregido en los 6 prompts.

---

## GUION PARA ELEVENLABS

**98 palabras · ~45s a ritmo de ad.** Deja aire para pausas y respiración.
Español neutro colombiano (sin voseo). Base: variantes 1 y 3 de Kreoon, reescritas.

### Texto corrido para pegar en ElevenLabs

```
Tu tienda no para. Los pedidos tampoco. Y sientes que la inteligencia artificial te está dejando atrás.

No es que no sirvas para esto. Es que nadie te ha mostrado cómo usarla de verdad.

Del quince al diecinueve de octubre, Plaza Mayor Medellín. La feria de ecommerce más grande del mundo.

Más de doscientas conferencias de inteligencia artificial, marketing y estrategia. Todo en un solo lugar.

Trescientos cincuenta stands. Doscientos speakers. Y la comunidad de ecommerce más grande de Latinoamérica esperándote.

Feria Effix, dos mil veintiséis. Asegura tu entrada en feriaeffix punto com.
```

### Distribución por clip

| Clip | Timing | Palabras | Línea |
|---|---|---|---|
| 1 | 0:00–0:07 | 17 | Tu tienda no para. Los pedidos tampoco. Y sientes que la inteligencia artificial te está dejando atrás. |
| 2 | 0:07–0:15 | 18 | No es que no sirvas para esto. Es que nadie te ha mostrado cómo usarla de verdad. |
| 3 | 0:15–0:23 | 18 | Del quince al diecinueve de octubre, Plaza Mayor Medellín. La feria de ecommerce más grande del mundo. |
| 4 | 0:23–0:30 | 16 | Más de doscientas conferencias de inteligencia artificial, marketing y estrategia. Todo en un solo lugar. |
| 5 | 0:30–0:38 | 16 | Trescientos cincuenta stands. Doscientos speakers. Y la comunidad de ecommerce más grande de Latinoamérica esperándote. |
| 6 | 0:38–0:45 | 13 | Feria Effix, dos mil veintiséis. Asegura tu entrada en feriaeffix punto com. |

### Ajustes de ElevenLabs

- **Stability:** 40–50 (deja subir la emoción sin que se quiebre)
- **Similarity:** 75
- **Style exaggeration:** 30–40
- Los números van **escritos en letras** en el texto de arriba — si pones "350"
  la voz puede leerlo mal. Ya está corregido.
- Graba **una sola toma corrida**, no clip por clip. Suena más natural y luego
  cortas en CapCut sobre los timings de la tabla.

---

## LIPSYNC — dónde sí y dónde no

EFFI es una caja de cartón: tiene ojos y boca en el panel frontal. Puede hablar.

**Recomendación: narrador en off para los 6 clips, más UNA línea de EFFI con
lipsync en el clip 4.** Ese es el beat del "clic" — que el personaje hable justo
ahí es lo que lo vuelve un personaje y no un objeto animado.

| Clip | Voz | Lipsync |
|---|---|---|
| 1, 2, 3, 5, 6 | Narrador en off | No — EFFI no mueve boca |
| 4 | Narrador **+ EFFI** | **Sí** — EFFI dice su línea |

**Línea de EFFI (clip 4), 2 palabras:**
```
Ah... ahora sí.
```

Va justo después de que el narrador termina su línea del clip 4. Voz distinta a
la del narrador — más aguda, más cálida. Segunda voz de ElevenLabs.

### Cómo hacer el lipsync

1. Genera el clip 4 normal en Seedance con el prompt de abajo.
2. Graba la línea de EFFI en ElevenLabs (voz secundaria).
3. Pasa video + audio por una herramienta de lipsync. Tienes tres rutas:
   - **HyperFrames / HeyGen** (ya lo tienes conectado)
   - **Higgsfield** → herramienta `video_speak`
   - **Magnific** → `video_speak`
4. Si el lipsync sale raro en un personaje no-humano (pasa: los modelos están
   entrenados en caras humanas), plan B: no muevas la boca — que EFFI reaccione
   solo con los ojos y deja la línea en off. El clip ya funciona así.

⚠️ El prompt del clip 4 abajo **no** incluye movimiento de boca. Si vas por
lipsync, generas primero y el lipsync lo agrega después. No pidas las dos cosas.

---

## DATOS VERIFICADOS DEL EVENTO

| Dato | Valor |
|---|---|
| Fechas | 15–19 oct 2026 (Black/VIP) · 16–18 oct (general) |
| Sede | Centro de Convenciones Plaza Mayor, Medellín (Calle 41 # 55-80) |
| Claim oficial | "el evento de comercio electrónico MÁS GRANDE DEL MUNDO" |
| Stands | 350+ |
| Conferencias | 200+ conferencias, paneles y talleres · 200+ speakers |
| Entradas | Black (5 días) · VIP (5 días) · Pasaporte 3 días |

Fuente: feriaeffix.com. **Sin verificar:** "50.000 asistentes" y "380 marcas"
aparecen en directorios de terceros pero no en la web oficial — fuera del ad.

⚠️ Hoy es 28 ago 2026 → faltan ~7 semanas.

---

## PERSONAJE — "EFFI" (propuesta)

Caja de envío de cartón antropomórfica con delantal. Representa al emprendedor
ecommerce. La acompaña **BIT**, asistente IA flotante.

Dos personajes trackeados → dentro del límite de 3 de Seedance.

**Regla age-blind (obligatoria en Seedance):** nunca describir por edad. Por eso
el personaje es un objeto antropomórfico — elimina el problema de raíz.

### Identity Block (copiar VERBATIM en los 6 prompts)

```
EFFI: an anthropomorphic corrugated cardboard shipping box character, rounded
corners, two expressive eyes on the front panel, short stubby cardboard arms,
wearing a canvas work apron with a single chest pocket, packing tape strip across
one corner like a scar. BIT: a small floating spherical assistant, matte white
shell, single soft cyan light-ring for a face, hovers at shoulder height.
```

### Visual DNA

- **Palette:** `#F4A300` ámbar · `#1B2A4A` azul profundo · `#C9772F` cartón ·
  `#E8E2D5` crema · `#3DD6C4` cyan (solo la luz de BIT)
- **Lighting:** práctica cálida en interiores, luz de ventana suave, key lateral
- **Materials:** cartón corrugado, lona, plástico mate, concreto pulido
- **Refs de look:** *Wall-E*, *Luca*, *Big Hero 6* (Baymax → BIT)

**FORBIDDEN LIST:**
> NO neón cyberpunk. NO teal-and-orange genérico. NO robots humanoides metálicos.
> NO rostros humanos fotorrealistas. NO negro puro en sombras — usar azul profundo.
> NO superficies impecables. NO texto renderizado dentro del video.

⚠️ **Los hex son propuesta mía, no el brand kit de Effix.** Si tienes los oficiales,
reemplázalos en los 6 prompts antes de generar.

---

## PIPELINE COMPLETO

1. **Character sheet** (paso 0, prompt abajo) → `referencias/personajes/`
2. **6 clips** en Seedance 2.0 con la sheet como `image_reference`
3. **Voz en off** en ElevenLabs — una toma corrida
4. **Lipsync** del clip 4 (opcional)
5. **Montaje** en CapCut: video + voz + música + textos
6. Todo el texto en pantalla va en post — Seedance renderiza letras rotas

---

## PASO 0 — CHARACTER SHEET (genera esto PRIMERO)

Modelo: GPT Image 2 o Nano Banana Pro. Sin esto, los 6 clips no son el mismo personaje.

```
Character model sheet on a plain flat neutral grey background. Pixar-grade 3D
animation render.

EFFI: an anthropomorphic corrugated cardboard shipping box character, rounded
corners, two expressive eyes on the front panel, short stubby cardboard arms,
wearing a canvas work apron with a single chest pocket, packing tape strip across
one corner like a scar.

Layout: full-body front view, full-body three-quarter view, full-body side view,
plus two head close-ups side by side — one with the mouth open mid-speech, one with
the mouth closed neutral.

Beside EFFI at correct relative scale: BIT, a small floating spherical assistant,
matte white shell, single soft cyan light-ring for a face, sized to hover at EFFI's
shoulder height.

Palette locked to amber #F4A300, deep blue #1B2A4A, cardboard brown #C9772F, cream
#E8E2D5, and cyan #3DD6C4 on BIT's ring only. Even flat studio lighting, sharp focus
throughout, deep depth of field, no cast shadows on the background.
```

> Las dos cabezas (boca abierta / boca cerrada) no son decorativas — son lo que
> permite el lipsync del clip 4. No las quites.

Guarda en `referencias/personajes/character-sheet-effi.png`.

### ✅ YA GENERADA — 2026-08-28

| Archivo | Estado |
|---|---|
| `referencias/personajes/character-sheet-effi.png` | **Oficial** (copia de v1) |
| `referencias/personajes/effi-sheet-v1.png` | Variante 1 — la elegida |
| `referencias/personajes/effi-sheet-v2.png` | Variante 2 — descartada |

Generada con Higgsfield `nano_banana_pro`, 16:9, 2752×1536, 2 créditos por variante.
Siguió el workflow oficial `character-sheet` de Higgsfield, preset `3d-stylized`.

**Por qué la v1 y no la v2:** en la v2, BIT salió con **dos ojos** en vez del anillo
cyan único del spec. La v1 respeta el diseño.

**Lo que salió bien:** las 3 vistas de cuerpo completo, las 2 cabezas
(boca abierta / boca cerrada) que alimentan el lipsync, el delantal con bolsillo,
la cinta en la esquina, el fluting del cartón visible en los bordes. El subsurface
scattering en el cartón se lee de verdad. Bonus no pedido: le salieron cejas, y
funcionan — dan mucha expresividad al clip 4.

⚠️ **Un defecto que debes vigilar:** en la sheet **BIT aparece duplicado** (una esfera
junto a la vista frontal y otra junto a la 3/4). Al usarla como `image_reference`,
Seedance puede renderizar dos BITs. Mitigación: los prompts de los clips 3, 4, 5 y 6
ya dicen `BIT, a small floating spherical assistant` en **singular**. Si aun así salen
dos en el draft de 480p, agrega al prompt `exactly one floating sphere assistant`.

⚠️ EFFI salió más alto y esbelto que una caja cuadrada — se lee más como paquete
vertical. Tiene personalidad y funciona, pero si querías la caja cúbica clásica hay
que regenerar con `wide cubic proportions` en vez de `upright rectangular body`.

---

## LOS 6 PROMPTS

Doble contraste aplicado: cada corte cambia tamaño de plano **y** carácter de cámara.

---

### CLIP 1 — Hook · 7s · El caos (0:00–0:07)

**Archetype:** Atmosphere · **Cámara:** Wide, static locked

```
Locked-off static wide shot. EFFI, an anthropomorphic corrugated cardboard box
character in a canvas work apron, stands surrounded by toppling stacks of unshipped
parcels in a cramped home warehouse. Order notifications pile up on a cracked monitor
behind, glow flickering across the boxes. EFFI's shoulders sag, one cardboard arm
lifts slowly and drops. Dust drifts through a single shaft of late afternoon window
light from the left. Pixar-grade 3D animation, subsurface scattering on cardboard
fibers, warm amber #F4A300 key against deep blue #1B2A4A shadows, shallow depth of
field, sharp focus on EFFI throughout.

Audio: the low hum of a tired laptop fan, a plastic notification chime repeating,
a parcel sliding and thudding to the floor. Ambient texture only, no speech, no music.
```

---

### CLIP 2 — Problema · 8s · La chispa (0:07–0:15)

**Archetype:** Reveal · **Cámara:** MCU, handheld

```
Handheld medium close-up, subtle breath-like float. EFFI tilts the cardboard face
down toward a phone screen resting on a packing table. The screen light throws a
warm amber wash across the box front. EFFI's eyes widen deliberately, then the whole
body straightens — packing tape corner catching the light as posture shifts. One
stubby arm rises and grips the table edge. Late afternoon window light from the left,
practical desk lamp warm pool. Pixar-grade 3D animation, subsurface scattering on
cardboard, amber #F4A300 and deep blue #1B2A4A, subject in sharp focus, background
falling into soft bokeh.

Audio: a single bright notification tone, the creak of cardboard flexing, a slow
inhale, distant traffic through a window. Ambient texture only, no speech, no music.
```

---

### CLIP 3 — Llegada · 8s · Se abre el mundo (0:15–0:23)

**Archetype:** Reveal · **Cámara:** Medium, stabilized tracking

```
Stabilized tracking shot pushing forward behind EFFI, moving left to right. Wide
convention centre doors part ahead, revealing a vast exhibition hall stretching back
in rows of bright stands, banners rippling from a ceiling truss. EFFI walks in, arms
swinging, cardboard head turning up and back as the ceiling height registers. BIT, a
small floating spherical assistant with a soft cyan light-ring face, drifts into frame
at shoulder height and settles alongside. Bright even daylight from overhead glazing,
warm amber accent lighting on the stands. Pixar-grade 3D animation, deep focus through
the hall, cream #E8E2D5 architecture against amber #F4A300 signage.

Audio: a broad reverberant hall ambience with no discernible speech, footsteps on
polished concrete, a soft electronic chirp as BIT arrives. No music.
```

---

### CLIP 4 — Descubrimiento IA · 7s · El clic (0:23–0:30)

**Archetype:** Reveal · **Cámara:** ECU, static · **← clip del lipsync**

```
Static extreme close-up on EFFI's cardboard face, filling the frame at a slight
low angle. BIT's cyan light-ring reflects across the corrugated surface as it pulses
twice. EFFI's eyes shift focus deliberately from left to right, pupils dilating, then
the eyes crease upward — the expression building slowly rather than snapping. A brief
focus hunt on the packing-tape corner before it locks. Warm practical stand lighting
from the right, cyan #3DD6C4 rim from BIT on the left cheek. Pixar-grade 3D animation,
subsurface scattering, deep blue #1B2A4A background falling into soft bokeh.

Audio: a rising three-note synth motif, the soft whir of BIT hovering, distant hall
ambience with no discernible speech.
```

> Nota: el prompt **no** pide movimiento de boca a propósito. El lipsync se aplica
> encima del clip ya generado. Si pides las dos cosas, la boca sale doble.

---

### CLIP 5 — Escala · 8s · La feria completa (0:30–0:38)

**Archetype:** Journey · **Cámara:** Extreme wide, aerial

```
Slow aerial crane shot drifting forward high above the exhibition floor. Hundreds of
stands laid out in ordered rows below, crowds flowing between them like current,
banners and truss lighting receding toward the far wall. EFFI and BIT are two small
figures moving steadily through the centre aisle, tracked from above. Bright overhead
glazing daylight, amber #F4A300 stand lighting pooling across the floor. Pixar-grade
3D animation, sharp focus throughout, deep depth of field, cream #E8E2D5 and amber
palette, large-scale architectural sweep.

Audio: a wide reverberant hall ambience, non-verbal crowd murmur with no discernible
speech, distant footfall. No music.
```

---

### CLIP 6 — Transformación · 7s · Salida + CTA (0:38–0:45)

**Archetype:** Reveal · **Cámara:** MCU, crane up

```
Crane shot rising from a medium close-up on EFFI walking toward camera, moving right
to left, then lifting to reveal the hall behind. EFFI's apron now carries a lanyard,
posture squared, arms swinging with intent, packing-tape corner catching golden light.
BIT circles once around EFFI's head and settles at shoulder height, cyan ring steady.
The upper third of the frame opens to clean negative space against the hall ceiling.
Golden hour light spilling through the entrance glazing behind, warm backlight rimming
the cardboard edges. Pixar-grade 3D animation, subsurface scattering, amber #F4A300
backlight against deep blue #1B2A4A, subject in sharp focus.

Audio: confident footsteps on concrete, a warm sustained tone resolving, hall ambience
fading back with no discernible speech.
```

---

## TABLA DE CONTINUIDAD — verificación de doble contraste

| Clip | Tamaño | Cámara | Dirección | Dur | Voz |
|---|---|---|---|---|---|
| 1 | Wide | Static locked | — | 7s | Off |
| 2 | MCU | Handheld | — | 8s | Off |
| 3 | Medium | Stabilized tracking | izq → der | 8s | Off |
| 4 | ECU | Static | — | 7s | Off + EFFI (lipsync) |
| 5 | Extreme wide | Aerial | avance | 8s | Off |
| 6 | MCU | Crane | der → izq | 7s | Off |

Ningún corte repite tamaño ni carácter de cámara. **Total: 45s exactos.**

---

## TEXTO EN POST (CapCut)

El texto **refuerza** la voz, no la repite palabra por palabra.

| Momento | Texto en pantalla |
|---|---|
| 0:04 | La IA no te va a reemplazar. Te va a dejar atrás si no la usas. |
| 0:16 | 15–19 OCTUBRE · MEDELLÍN |
| 0:20 | Plaza Mayor |
| 0:26 | +200 conferencias |
| 0:32 | +350 stands · +200 speakers |
| 0:40 | FERIA EFFIX 2026 |
| 0:43 | feriaeffix.com |

---

## PARÁMETROS EN HIGGSFIELD

```
model: seedance_2_0
mode: std
resolution: 1080p
aspect_ratio: 9:16
duration: por clip (7 / 8 / 8 / 7 / 8 / 7)
image_references: [character-sheet-effi.png]
```

**Antes de gastar créditos:** genera los 6 en `mode=fast`, `480p`. El draft valida
el prompt, no la toma. Si el personaje deriva, el problema es la character sheet.

---

## VARIANTES PARA TESTEAR

- **Hook alterno (clip 1):** EFFI mirando una gráfica de ventas plana. Más directo
  al dolor de negocio que el caos de bodega.
- **Versión B2B (vender stands):** cambia el clip 4 — EFFI atendiendo su propio
  stand con fila de visitantes.
- **Corte 30s:** elimina clips 1 y 5 → 8+7+8+7 = 30s. Recorta el guion a las
  líneas 2, 3, 4 y 6.
- **Variante de voz:** el guion está en neutro colombiano. Si el ad es solo para
  Antioquia, la versión paisa con voseo ("mirá", "vení", "dejá") conecta más fuerte.
  Kreoon la devolvió así de origen.
