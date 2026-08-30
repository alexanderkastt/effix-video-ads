# GUIONES — Video IA Ads

Archivo acumulativo. Cada guion nuevo se agrega al final.

---

## 2026-08-28 — Feria Effix 2026 · Ad Pixar · Nicho IA · Reel 45s

**Cliente:** Feria Effix (Medellín, 15–19 oct 2026)
**Objetivo:** registro / asistencia
**Estilo:** Pixar 3D · **Formato:** 9:16, 45s, 6 clips
**Modelo:** Seedance 2.0 (std, 1080p, 9:16)
**Pack completo:** `prompts-listos/pixar/effix-2026-ia-45s.md`

### Personaje
EFFI — caja de envío de cartón antropomórfica con delantal (el emprendedor
ecommerce). BIT — asistente IA esférico flotante, luz cyan. Dos personajes
trackeados, dentro del límite de 3 de Seedance. Objeto antropomórfico elegido
a propósito para esquivar la regla age-blind del motor.

### Estructura narrativa (6 beats)

| # | Beat | Dur | Contenido |
|---|---|---|---|
| 1 | Hook | 7s | EFFI ahogada en pedidos sin despachar, bodega caótica. Wide static. |
| 2 | Problema | 8s | Ve el anuncio de la feria en el celular. Se endereza. MCU handheld. |
| 3 | Llegada | 8s | Puertas de Plaza Mayor se abren, revelación del pabellón. BIT aparece. Medium tracking. |
| 4 | Descubrimiento | 7s | El clic de entender la IA. ECU static sobre el rostro. |
| 5 | Escala | 8s | Aéreo sobre 350+ stands. Extreme wide aerial. |
| 6 | Transformación | 7s | Sale con escarapela y confianza. Crane up, espacio para CTA. |

### ⚠️ VERSIÓN FINAL PRODUCIDA — 36s (68 palabras)

El ad quedó en **35.7s**, no 45s: el plan de Higgsfield no permite clips de 10s en
Hailuo, así que los 6 clips son de ~6s. Guion recortado a 68 palabras.

| Clip | Timing | Línea |
|---|---|---|
| 1 | 0:00–0:06 | Tu tienda no para. Los pedidos tampoco. Y sientes que la inteligencia artificial te está dejando atrás. |
| 2 | 0:06–0:12 | No es que no sirvas para esto. Nadie te ha mostrado cómo usarla. |
| 3 | 0:12–0:18 | Del quince al diecinueve de octubre, Plaza Mayor Medellín. |
| 4 | 0:18–0:24 | Más de doscientas conferencias de inteligencia artificial y ecommerce. |
| 5 | 0:24–0:30 | Trescientos cincuenta stands. La feria de ecommerce más grande del mundo. |
| 6 | 0:30–0:36 | Feria Effix. Asegura tu entrada en feriaeffix punto com. |

Texto corrido para ElevenLabs:

```
Tu tienda no para. Los pedidos tampoco. Y sientes que la inteligencia artificial te está dejando atrás. No es que no sirvas para esto. Nadie te ha mostrado cómo usarla. Del quince al diecinueve de octubre, Plaza Mayor Medellín. Más de doscientas conferencias de inteligencia artificial y ecommerce. Trescientos cincuenta stands. La feria de ecommerce más grande del mundo. Feria Effix. Asegura tu entrada en feriaeffix punto com.
```

---

### Guion original de 45s — ElevenLabs (98 palabras)

Guardado por si se produce una versión larga más adelante.

Voz: "Cristian Sanchez" (paisa). Español neutro colombiano, sin voseo.
Base generada con Kreoon `generate_script` modo 2, adaptada.

> Tu tienda no para. Los pedidos tampoco. Y sientes que la inteligencia artificial te está dejando atrás.
>
> No es que no sirvas para esto. Es que nadie te ha mostrado cómo usarla de verdad.
>
> Del quince al diecinueve de octubre, Plaza Mayor Medellín. La feria de ecommerce más grande del mundo.
>
> Más de doscientas conferencias de inteligencia artificial, marketing y estrategia. Todo en un solo lugar.
>
> Trescientos cincuenta stands. Doscientos speakers. Y la comunidad de ecommerce más grande de Latinoamérica esperándote.
>
> Feria Effix, dos mil veintiséis. Asegura tu entrada en feriaeffix punto com.

**Línea de EFFI con lipsync (clip 4):** "Ah... ahora sí." — voz secundaria, más aguda.

### Arquitectura de audio
1. Textura (SFX/ambiente) → generada por Seedance dentro del prompt, sin habla
2. Voz en off → ElevenLabs, toma corrida, se corta en CapCut
3. Música → librería, sube en el clip 5

### Copy en pantalla (post-producción)
- 0:02 — Vender online en 2026 sin IA es competir con una mano atada
- 0:10 — 16–18 de octubre · Medellín
- 0:19 — Plaza Mayor · 350+ stands
- 0:25 — 200+ conferencias sobre IA, ecommerce y marketing
- 0:33 — La feria de comercio electrónico más grande del mundo
- 0:40 — FERIA EFFIX 2026
- 0:43 — Asegura tu entrada → feriaeffix.com

### Decisiones técnicas
- Todo el texto va en post: el renderizado de texto es alto riesgo en Seedance.
- Character sheet obligatoria antes de los clips, como `image_reference` en los 6.
- Regla de doble contraste verificada: ningún corte repite tamaño de plano ni
  carácter de cámara.
- Paleta hex es propuesta, no el brand kit oficial de Effix — pendiente confirmar.

### Pendiente
- Confirmar colores oficiales de Effix y reemplazar los hex en los 6 prompts.
- Validar si el personaje mascota se aprueba o el cliente prefiere humanos Pixar.

---

---

## 2026-08-28 — Feria Effix 2026 · Ad Crochet "LANA" · 45s · CONCEPTO B "El pasillo"

**Nicho:** emprendedor que NO ha logrado arrancar a vender por internet
**Entregable:** `outputs/claymation/EFFIX-LANA-45s-FINAL.mp4` — 45.3s · 1080x1920
**Modelo:** Seedance 1.5 Pro con keyframes encadenados · Voz: Valentina Santos (colombiana)

### Guion locutado (74 palabras)

| Clip | Timing | Línea |
|---|---|---|
| 1 | 0:00-0:07 | Tienes el producto listo hace meses. Y ni una sola venta. |
| 2 | 0:07-0:14 | Lo intentaste sola. Viste los tutoriales. Nada funcionó. |
| 3 | 0:14-0:22 | No es que no sirvas para esto. Es que nadie te ha mostrado el camino. |
| 4 | 0:22-0:30 | Doscientas conferencias. Trescientos cincuenta stands. Y gente que ya lo logró, dispuesta a decirte cómo. |
| 5 | 0:30-0:38 | La feria de comercio electrónico más grande del mundo. Del quince al diecinueve de octubre, Plaza Mayor Medellín. |
| 6 | 0:38-0:45 | Da el primer paso. El resto aparece. |

### Concepto visual
Plano secuencia continuo. Un cuarto sin salida visible se abre en pasillo a medida
que ella camina. LANA, amigurumi a medio tejer, empieza monocroma y gana color
conforme se completa. El mundo permanece en blanco y negro de marca; ella es la
única fuente de color.

### Aprendizajes
- **Color selectivo:** decir "warm colour" no funciona. Hay que nombrar colores
  concretos (mostaza, terracota, teal) Y declarar el fondo como "strict pure
  greyscale with zero colour information". Con eso sale perfecto.
- **Banners sin texto:** pedir "no legible text" da texto inventado igual. Lo que
  funciona: "plain solid black panels with bold white abstract geometric shapes
  only, absolutely no letters, no words, no writing anywhere".
- **Keyframes encadenados:** el end de cada clip como start del siguiente da
  continuidad total. Verificado frame a frame — los pares son idénticos.

### VERSIÓN 2 FINAL — 37s (la buena)

`outputs/claymation/EFFIX-LANA-v2-FINAL.mp4` · 37s · 1080x1920 · 38 MB · −14 LUFS

Cambios sobre la v1:
- **Voz Norah Salgado (id 642)**, latina mexicana neutra, en `eleven_turbo_v2_5`
  (mitad de precio que `eleven_v3`). La v1 usaba Valentina Santos, que salió con
  acento español pese a estar catalogada como colombiana.
- **Ritmo acelerado 1.4x con ffmpeg** — los clips originales quedaron en cámara
  lenta porque los prompts pedían "slowest possible push", "slow", "deliberate".
  Corregido en post, sin regenerar (habría costado 9.900 créditos).
- **Subtítulos animados** en Montserrat real (descargada de Google Fonts), con fade
  y pulso de escala. Frases clave más grandes y en amarillo.
- **Cierre con material real** de la Feria Effix 2025: 4.7s de fotos de la galería
  oficial con movimiento Ken Burns.
- Música reutilizada de la v1, cero créditos nuevos.

Guion locutado v2 (56 palabras, 6 líneas):

| Clip | Inicio voz | Línea |
|---|---|---|
| 1 | 0.4s | Tienes el producto listo hace meses. Y ni una venta. |
| 2 | 5.3s | Lo intentaste sola. Nada funcionó. |
| 3 | 10.4s | No es que no sirvas. Nadie te ha mostrado el camino. |
| 4 | 16.1s | Doscientas conferencias. Trescientos cincuenta stands. Gente que ya lo logró. |
| 5 | 22.0s | La feria de ecommerce más grande del mundo. Quince al diecinueve de octubre, Medellín. |
| 6 | 27.6s | Da el primer paso. El resto aparece. |

Costo v2: **37 créditos** (solo la voz). Todo lo demás reutilizado o hecho con ffmpeg.
