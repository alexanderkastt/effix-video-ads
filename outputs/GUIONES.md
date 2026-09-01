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

---

## 2026-08-30 — Feria Effix 2026 · Skeleton musical sync · Nicho `sin_arrancar` · 56s

**Entregable:** `assets/renders/EFFIX-SKELETON-sin-arrancar-musical.mp4` — 56.2s · 720x1280 · 16 MB
**Guión:** `scripts/guiones/effix_skeleton_sin-arrancar-v2-musical_20260830_215911_director.json`
**Nicho nuevo:** `sin_arrancar` — el que lo intentó todo y no ha vendido (en `nichos_effix.py` + `narracion_effix.py`)
**Ancla:** noventa días de tienda abierta y el único pedido lo hizo tu prima (vuelve 5 veces)

### Por qué no repite al ad de LANA
Mismo territorio (no logra vender online), **otro ángulo**: allá era narración
emocional en plano-secuencia de crochet; aquí es una canción con progresión
escalada en segunda persona sobre el arco cuarto cerrado → umbral → feria. Ni
una línea de narración coincide.

### Letra (MiniMax Music 2.6 · latin urban pop · 96 BPM)

| Sección | Línea |
|---|---|
| Verso 1 | Tu tienda lleva noventa días abierta / Y el único pedido lo hizo tu prima |
| Callout | Si vendes por internet y aún no llega un desconocido / Esto es para ti, treinta segundos |
| Verso 2 | Publicas todos los días, cero ventas / Entonces dices que te falta pauta / Pusiste pauta, y el pedido, otra vez familiar |
| Pre-coro | No te falta producto ni plata / Te falta que alguien que ya vendió te vea el negocio |
| Coro | Feria Effix, dieciséis al dieciocho / Plaza Mayor, Medellín / Trescientas cincuenta empresas / Y el próximo pedido no es de tu prima |
| Verso 3 | Doscientos ponentes que viven de vender por internet / Cinco ediciones, quien va una vez, vuelve |
| Outro | Compra tu pasaporte, clic en el enlace / El próximo pedido no es de tu prima |

El beat de **CALLOUT** entre MOMENTO y SÍNTOMA es nuevo: la estructura de 12
beats de `guiones_effix.py` no lo trae y el ad tiene que nombrar a su audiencia
en los primeros segundos.

### Producción
- **Canción:** `fal-ai/minimax-music/v2.6` ($0.15). Devuelve ~100s con intro larga;
  el tramo cantado útil es 21.66→77.86 y es lo que se monta.
- **Imágenes:** `fal-ai/nano-banana-2` (héroe) + `/edit` con la héroe como referencia
  en las 13 escenas. Character Bible Bare-Bones Cinematic verbatim en todas.
- **Video:** `fal-ai/kling-video/v2.1/standard/image-to-video`, 13 clips de 5s.
- **Cortes:** `librosa.beat.beat_track` sobre la canción recortada; cada corte cae
  en el golpe más cercano al reparto teórico si está a menos de 0.6s.
- **Overlays:** Montserrat Black, contorno sticker, pegados a las líneas reales
  de la letra (timestamps de `fal-ai/whisper`). La marca aparece escrita completa
  dos veces: en el coro (`Feria Effix · 16–18 oct`) y como cierre de marca en los
  últimos 2.4s.

### Aprendizajes
- **El director de skeleton genera prompts casi idénticos** para los 13 beats:
  solo cambia el marcador de escalada. Salieron 13 planos iguales. Hubo que
  escribir los encuadres a mano (wide → close → cenital → umbral → establishing →
  two-shot → hero) y regenerar. Costó $1.04 de imágenes tiradas.
- **MiniMax no acepta duración:** siempre devuelve ~100s con intro instrumental
  larga (21s en la v2). Hay que transcribir para saber dónde entra la voz.
- **La marca canta mal:** whisper transcribió "feria fix" y "serie fix". Escribir
  La marca se escribe SIEMPRE "Feria Effix", completa: nada de grafías
  fonéticas para ayudarle al modelo. Si canta mal, se regenera.
- El negativo de texto no siempre basta: una escena metió "New Order" en la
  pantalla de un teléfono. Se resuelve pidiendo explícitamente iconos sin texto.

### Costo real
| Concepto | USD |
|---|---|
| Canción v1 (descartada, sin callout) | 0.15 |
| Canción v3 (descartada, 40s de intro «la-la-la») | 0.15 |
| Canción v2 | 0.15 |
| Whisper ×2 | ~0.02 |
| Imagen héroe | 0.08 |
| Escenas v1 (descartadas, planos repetidos) | 1.04 |
| Escenas v2 + regeneración de la 11 | 1.12 |
| 13 clips Kling 2.1 std (5s c/u) | 3.64 |
| **Total** | **≈ 6.36** |

---

## 2026-08-31 — Feria Effix 2026 · Nicho `tienda_ropa` · TRES VARIACIONES

**Nicho nuevo:** `tienda_ropa` — el almacén de ropa con local que vende por
mostrador y WhatsApp y nunca ha vendido por internet. No es `sin_arrancar` (ese
lo intentó online y no vendió): este **nunca empezó**. Vende bien, pero su techo
lo pone la geografía.

**Ancla:** la vitrina. Su facturación depende del clima y del andén.
**Estado:** ⏸️ BORRADOR — las tres esperan aprobación. Nada producido.

### Hooks — del banco de 320, filtrados por (problem, conversión)

Se citan como `categoría#n`: el `n` del banco no es único, se repite en cada
categoría (320 ganchos, 45 valores de `n`), así que el número solo no identifica
un gancho.

| Var | Banco | Hook |
|---|---|---|
| A | `dolor_nombrado#39` | Llovió el sábado, no entró nadie, y el mes se te cayó. |
| B | `callout#33` | Si vives de que la gente pase por el frente de tu almacén, quédate. |
| C | `callout#11` | Tu ropa se vende bien. Pero solo a diez cuadras a la redonda. |

Los tres atacan el mismo techo desde ángulos distintos. El dolor del hook A se
puede filmar —lluvia en el vidrio, acera vacía, ropa impecable que nadie vio—,
que es el test de Caples. "Las blusas siguen colgadas", el hook que se escribió
primero a mano, se descartó: es una tarde floja que le pasa a cualquier comercio,
no el techo de este micronicho.

---

## VARIACIÓN 1 — Narrada · Pixar 3D · DOÑA CLARA · 60s

**Formato:** micro-situación de 12 beats (`guiones_effix.py`) + voz en off
**Estructura:** los siete pasos del framework más los cinco de venta
**Personaje:** Doña Clara, dueña del almacén, cincuenta y pico, delantal sobre la
ropa que ella misma vende. Personaje Pixar de rasgos cálidos y manos ocupadas.
**Motor:** `NICHOS["tienda_ropa"]` · hook A · pase 3 días

| Clip | t | Beat | Voz | Overlay |
|---|---|---|---|---|
| 01 | 0–4 | MOMENTO | Llovió el sábado, no entró nadie, y el mes se te cayó. | Llovió. Y no entró nadie |
| 02 | 4–8 | CALLOUT | Tienes almacén de ropa y no vendes por internet: esto es para ti. | ¿Almacén de ropa? |
| 03 | 8–12 | SÍNTOMA | Mandas la foto al grupo de siempre, y contesta la de siempre. | Las mismas clientas de siempre |
| 04 | 12–16 | REACCIÓN | Y ya te acostumbraste: tu almacén vende hasta la esquina. | Vendes hasta la esquina |
| 05 | 16–20 | EXPL. FALLIDA | Total, tú dices que tu ropa se vende es viéndola. | «Se vende es viéndola» |
| 06 | 20–24 | PATRÓN | **Pero** la del local de al lado ya despacha para otra ciudad. | La del lado vende en otra ciudad |
| 07 | 24–32 | CAUSA RAÍZ | Así que no es que tu ropa no sirva para internet: es que nadie te ha mostrado cómo. | No es tu ropa |
| 09 | 32–36 | MECANISMO | En la feria está quien te monta la tienda y quien despacha. | 350 empresas en un recinto |
| 10 | 36–40 | FECHAS | Dieciséis al dieciocho de octubre, en Plaza Mayor. | 16–18 oct · Plaza Mayor |
| 11 | 40–44 | PRUEBA | Doscientos ponentes que viven de vender por internet. | 200 ponentes que ya venden |
| 12 | 44–48 | VISUALIZACIÓN | Imagínate empacando un pedido para alguien de otra ciudad. | Un pedido de otra ciudad |
| 13 | 48–52 | CTA | Compra tu pasaporte a la Feria Effix en feriaeffix punto com. Te toma un minuto. | Compra en feriaeffix.com |
| 14 | 52–56 | DEFECTO | No sales con la tienda montada: sales sabiendo qué te falta. | Sales sabiendo qué te falta |
| 15 | 56–60 | LOOP | Porque la próxima venta no la va a hacer la vitrina. | La vitrina ya no vende sola |

Texto corrido para ElevenLabs (161 palabras · 54,4s):

```
Llovió el sábado, no entró nadie, y el mes se te cayó. Tienes almacén de ropa y no vendes por internet: esto es para ti. Mandas la foto al grupo de siempre, y contesta la de siempre. Y ya te acostumbraste: tu almacén vende hasta la esquina. Total, tú dices que tu ropa se vende es viéndola. Pero la del local de al lado ya despacha para otra ciudad. Así que no es que tu ropa no sirva para internet: es que nadie te ha mostrado cómo. En la feria está quien te monta la tienda y quien despacha. Dieciséis al dieciocho de octubre, en Plaza Mayor. Doscientos ponentes que viven de vender por internet. Imagínate empacando un pedido para alguien de otra ciudad. Compra tu pasaporte a la Feria Effix en feriaeffix punto com. Te toma un minuto. No sales con la tienda montada: sales sabiendo qué te falta. Porque la próxima venta no la va a hacer la vitrina.
```

**Pipeline:** nano-banana-2 (héroe + 15 escenas con la héroe de referencia) →
Kling 2.1 std → voz ElevenLabs → overlays Montserrat Black.
**Costo estimado:** ~$5,60 (15 clips $4,20 · imágenes $1,28 · voz $0,10)
**Requiere:** `DURACION_CLIP_S=4` en el `.env` (con 5s el video se va a 75s).

---

## VARIACIÓN 2 — Cantada · Stop-motion de tela · KEILA · 55s

**Formato:** canción sincronizada a los golpes (MiniMax Music 2.6)
**Estructura:** letra de canción (verso · callout · pre-coro · coro · verso ·
puente · outro), no los 12 beats. El coro carga la marca y las fechas.
**Personaje:** Keila, veintidós años, la hija que atiende el almacén los sábados
y ve el techo antes que su mamá. No es la que decide: es la que empuja.
**Estilo visual:** stop-motion de tela y fieltro — el almacén, la calle y el
recinto construidos con retazos. Distinto del Pixar de la V1 a propósito.

| Sección | Letra |
|---|---|
| Verso 1 | Llovió todo el sábado y no entró nadie / Mi mamá acomoda las blusas otra vez |
| Callout | Si tu negocio vive del que pasa por el frente / Esto es para ti, treinta segundos |
| Verso 2 | La ropa está buena, el precio está bueno / Pero el mundo entero pasa de largo / Y solo compran las de siempre |
| Pre-coro | No es la ropa, no es el precio / Es que tu tienda no existe en el celular de nadie |
| Coro | Feria Effix, dieciséis al dieciocho / Plaza Mayor, Medellín / Trescientas cincuenta empresas / Y tu ropa saliendo de la ciudad |
| Verso 3 | Doscientos ponentes que viven de vender por internet / Cinco ediciones, quien va una vez, vuelve |
| Puente | Imagínate la caja con una dirección que no conoces |
| Outro | Compra tu pasaporte en feriaeffix punto com / Que la próxima venta no la haga la vitrina |

**Pipeline:** MiniMax Music 2.6 → whisper para los tiempos reales de la voz →
`librosa.beat_track` para cortar en el golpe → 12 clips Kling 2.1 → overlays
pegados a las líneas cantadas. Mismo camino que el ad de `sin_arrancar`.
**Costo estimado:** ~$4,80 (canción $0,15 más reintentos · whisper $0,02 ·
imágenes $1,04 · 12 clips $3,36)
**Riesgo conocido:** MiniMax devuelve ~100s con intro instrumental larga y a
veces canta mal la marca. Si canta "feria fix", se regenera — la marca se
escribe siempre "Feria Effix" completa, nunca fonética.

---

## VARIACIÓN 3 — Object talk · Pixar · EL MANIQUÍ · 25s

**Formato:** monólogo en primera persona del objeto (skill `object-talk`)
**Estructura:** declaración de apertura → mensaje central → dato → cierre. Cuatro
tomas, no doce beats. El más corto y el más raro de los tres.
**Personaje:** el maniquí de la vitrina. Cuatro años parado en el mismo metro
cuadrado viendo pasar gente que no entra. Orgulloso de la ropa que le ponen,
resignado a que solo lo vea el que pasa por el frente. Ojos grandes y cansados,
hombros de plástico levemente caídos, una mano que señala la calle.

| Toma | t | Voz del maniquí | Cámara |
|---|---|---|---|
| 1 | 0–7 | Llevo cuatro años parado en esta vitrina. Y solo me ve el que pasa por el frente. | Medium estático, lluvia en el vidrio |
| 2 | 7–14 | La ropa que me ponen es buena. Buenísima. Pero yo no puedo salir a buscar a nadie. | Close-up, push-in lento |
| 3 | 14–20 | Tú sí. Feria Effix, dieciséis al dieciocho de octubre, Plaza Mayor. | Contrapicado, la calle detrás |
| 4 | 20–25 | Compra tu pasaporte en feriaeffix punto com. Y sácame de esta vitrina. | Medium, mirada a cámara |

**Voz:** masculina, madura, con textura, resignada pero cálida. Colombiano
neutro, ritmo pausado. Nada de energía de locutor.
**Lipsync:** se aplica DESPUÉS de generar el clip, nunca pidiendo movimiento de
boca dentro del prompt. En un maniquí puede fallar (los modelos están entrenados
en caras humanas): plan B, la boca no se mueve y la línea queda en off, con los
ojos haciendo la actuación.
**Costo estimado:** ~$1,60 (4 clips $1,12 · imágenes $0,32 · voz $0,05)

---

### Cambios de motor que trajo esta tanda

- **`codas`** (`guiones_effix.py`) — beat opcional que le pone voz al segundo
  clip de los beats con aire, que antes quedaba mudo. Resuelve el callout de
  identidad (que la estructura de 12 beats no traía) y las fechas del evento
  (que el CTA del pase no decía). Los otros diez nichos quedan idénticos.
- **`techo_de_palabras()`** (`narracion_effix.py`) — el techo de palabras por
  clip se calcula desde la ventana del `.env` en vez de estar escrito a mano.
  Estaba en 8, calibrado para 2,2 palabras por segundo, cuando la locución real
  medida es 2,96: cada línea llenaba 2,7s de un clip de 4s y dejaba 1,3s de
  silencio. **Eso era lo que hacía sonar los guiones a telegrama** — el motor,
  no la redacción. `FACTOR_DESBORDE` deja que la voz cruce el corte a propósito.
- **CTA de compra** — los cinco pases decían "clic en el enlace", que pide un
  gesto y no dice dónde. Ahora dicen qué se compra, dónde (feriaeffix punto com)
  y con qué esfuerzo ("te toma un minuto", el sacrificio negado). Aplica a los
  once nichos.

### Pendiente antes de producir cualquiera de las tres

1. **Fechas.** `config/brand_dna.json` dice 15 al 19 de octubre; los nichos y
   todo lo publicado dicen 16 al 18. Confirmar cuál es la buena y unificar.
2. **`DURACION_CLIP_S`.** La V1 necesita 4s. Con 5s el video se va a 75s.
3. `test_integracion_creativa.py` imprime "12 clips × 4s = 60s" y en la línea
   siguiente "todos los clips duran 5s": está leyendo dos constantes distintas
   y se contradice solo.

---

## 2026-08-31 — `tienda_ropa` · Los tres estilos: skeleton · pixar · animado 2D

Tres guiones distintos, uno por estilo. **No es el mismo guión en tres estilos**:
cada uno tiene su estructura, su personaje y su arco. El de Pixar es el de la
tanda anterior (Doña Clara, micro-situación de 12 beats); los otros dos son
nuevos. Ninguno comparte una línea con otro.

| Estilo | Estructura | Personaje | Dur |
|---|---|---|---|
| Skeleton | Escalada temporal (Día 1 → Día 365) | El esqueleto comerciante | 40s |
| Pixar 3D | Micro-situación de 12 beats | Doña Clara, la dueña | 60s |
| Animado 2D | Diálogo a dos voces en la acera | Rosa y Marce, vecinas de local | 38s |

---

## ESTILO SKELETON — "Un año en la vitrina" · 47s  ✅ PRODUCIDO (2026-09-01)

**Formato:** skeleton ad (skill `skeleton-ads`) · narración en segunda persona
**Ángulo:** costo de la inacción + escalada de tiempo. El producto no se usa: se
deja de usar, y el precio de eso se ve crecer día a día.
**Loop de curiosidad:** ¿qué le pasa a la ropa que nunca sale de la vitrina?
**El turn:** beat 6, cuando se sube al bus. Antes de eso, solo se acumula el costo.
**Personaje:** el esqueleto comerciante, Bare-Bones Cinematic. Va **sin ropa**
rodeado de ropa que nadie compra — la ironía es el concepto: tiene el producto
encima y no le sirve de nada mientras dependa de quien pase por el frente.
**Character Bible:** el bloque Bare-Bones Cinematic, verbatim en los 9 prompts,
con `[THEME]` = almacén de ropa de barrio colombiano y palette cálida desaturada.
**Registro:** voseo paisa — es el cambio que aprobó Alexander sobre el borrador
en tuteo: `colgás`, `le bajás`, `te montás`, `volvés`, `comprá`, `completica`.

| # | VO | Escena | Overlay |
|---|---|---|---|
| 1 | ¿Y si tu ropa nunca sale de esa vitrina, qué? | Wide del local desde la acera, el esqueleto acomodando un maniquí | ¿Y si nunca sale de ahí? |
| 2 | Día uno: colgás la colección nueva. Quedó divina. La ve… el que pasa por el frente. | Medium, orgulloso, colgando ropa nueva → el rack lleno y él mirando la puerta vacía | Día 1 |
| 3 | Día treinta: llovió tres sábados seguidos. La colección sigue completica. | El esqueleto mirando la lluvia por el vidrio, brazos cruzados | Día 30 |
| 4 | Día noventa: le bajás el precio. Ahora la ve el mismo que pasa por el frente, pero más barata. | Close-up de manos huesudas amarrando una etiqueta roja → el rack entero con etiquetas | Día 90 |
| 5 | Día trescientos sesenta y cinco: la misma ropa, un año de arriendo, el mismo andén. | Wide, el local intacto, el esqueleto sentado en el mostrador | Día 365 |
| 6 | Hasta que un octubre te montás en un bus pa' Medellín. | Contrapicado subiendo al bus → el bus en la carretera de montaña al amanecer | Un octubre |
| 7 | Feria Effix. Trescientas cincuenta empresas y doscientos ponentes que viven de vender por internet. | Establishing del recinto, el esqueleto pequeño entre stands | FERIA EFFIX · 350 empresas |
| 8 | Y volvés con la tienda montada y con quién te la despache. | Entregando cajas a un mensajero → el mensajero arrancando en la moto | Con quién te la despache |
| 9 | Comprá tu pasaporte en feriaeffix punto com. | Hero final: el esqueleto tras el mostrador con el celular y las cajas listas | feriaeffix.com |

Texto corrido para ElevenLabs:

```
¿Y si tu ropa nunca sale de esa vitrina, qué? Día uno: colgás la colección nueva. Quedó divina. La ve… el que pasa por el frente. Día treinta: llovió tres sábados seguidos. La colección sigue completica. Día noventa: le bajás el precio. Ahora la ve el mismo que pasa por el frente, pero más barata. Día trescientos sesenta y cinco: la misma ropa, un año de arriendo, el mismo andén. Hasta que un octubre te montás en un bus pa' Medellín. Feria Effix. Trescientas cincuenta empresas y doscientos ponentes que viven de vender por internet. Y volvés con la tienda montada y con quién te la despache. Comprá tu pasaporte en feriaeffix punto com.
```

**Producción:** audio primero — la locución real (44,1s en 9 mp3, voz masculina
*Carlos Aguilar*) fijó la duración de cada clip. Imagen HÉROE primero; las
otras dieciséis referencian la héroe, nunca la anterior. Siete de los nueve
beats llevan frame inicial **y** final: los cuatro que cambian de estado dentro
del plano (2, 4, 6, 8) y otros tres por una restricción del modelo — **Kling o1
sólo acepta 5 o 10 segundos cuando el clip no lleva frame final**, así que la
frase que no cabe en cinco segundos necesita keyframe, no un clip de diez
pagado a medias. Cero texto en la generación: los nueve overlays van en montaje.
**Voz:** el primer corte salió con voz femenina y Alexander la pidió masculina.
Rehacer la locución movió las duraciones, y por eso el montaje ahora estira un
plano hasta un 12% si la frase creció — por debajo de eso no se nota y evita
repagar el clip.
**Archivos:** guión `scripts/guiones/effix_skeleton_tienda-ropa-un-ano-en-la-vitrina_20260901_aprobado.json`
· corrida `scripts/_producir_skeleton_vitrina.py` · render
`assets/renders/EFFIX-tienda-ropa-skeleton-Un-ano-en-la-vitrina.mp4`
**Costo real:** ~$6,30 (9 clips Kling o1, 54s, ~$4,54 · 17 imágenes $1,36 ·
música $0,20 · locución ~$0,20 en dos corridas)

---

## ESTILO PIXAR 3D — "Doña Clara" · 60s  ⚠️ REEMPLAZADO (ver 2026-09-01)

Sin cambios: es el guión registrado más arriba en esta misma fecha (micro-
situación de 12 beats, hook A del banco, `codas` de callout y fechas). Se
mantiene como el guión Pixar de este nicho.

Resumen: `Llovió el sábado, no entró nadie, y el mes se te cayó.` → callout →
síntoma → reacción → explicación fallida → **pero** → causa raíz → mecanismo →
fechas → prueba → visualización → CTA → defecto → `Porque la próxima venta no la
va a hacer la vitrina.`

---

## ESTILO ANIMADO 2D — "La acera" · 38s

**Formato:** diálogo a dos voces, cartoon 2D plano, línea gruesa y color plano
**Estructura:** una sola escena continua en la acera entre dos locales vecinos.
No hay narrador: la venta la hace el diálogo. El espectador se reconoce en Rosa.
**Personajes:**
- **ROSA**, cincuenta y tantos, dueña del almacén de ropa. Vende bien, de mostrador.
- **MARCE**, cuarenta y tantos, la vecina de local. Vende lo mismo y despacha a
  todo el país. No es una gurú: es la de al lado.

| # | Quién | Línea | Escena |
|---|---|---|---|
| 1 | Rosa | Llovió otra vez. Hoy no entró nadie. | Rosa en la puerta, mirando la acera mojada |
| 2 | Marce | A mí tampoco entró nadie. Y despaché dieciocho. | Marce apilando cajas en el andén |
| 3 | Rosa | ¿Dieciocho? ¿A quién? | Rosa se acerca, cambia la postura |
| 4 | Marce | A gente que no conozco. De Pereira, de Cúcuta, de Neiva. | Insert: tres cajas con tres direcciones distintas |
| 5 | Rosa | Y eso cómo se hace. | Close-up de Rosa, la pregunta que abre todo |
| 6 | Marce | Yo tampoco sabía. Lo aprendí en la feria. | Marce se encoge de hombros, sin pose de experta |
| 7 | Marce | Feria Effix, dieciséis al dieciocho de octubre, Plaza Mayor. Trescientas cincuenta empresas. | Corte al recinto, dos segundos, y vuelta a la acera |
| 8 | Rosa | ¿Y sirve para ropa? | Rosa mira su propia vitrina |
| 9 | Marce | Sirve para lo que vendas. | Marce cerrando su camión |
| 10 | Voz | Compra tu pasaporte en feriaeffix punto com. Te toma un minuto. | Cierre de marca sobre la acera |
| 11 | Rosa | Mañana no espero a que llueva. | Rosa entra a su local, mira la ropa distinto |

**Producción:** dos hojas de personaje (Rosa y Marce) más una del local. Estilo
2D plano: contorno grueso, sombras de dos tonos, fondo con textura de papel.
El diálogo se graba con **dos voces distintas** de ElevenLabs, no una.
**Costo estimado:** ~$3,60 (11 clips $3,08 · hojas de personaje $0,24 · dos
voces $0,20)
**Riesgo:** el 2D plano con Kling tiende a "engordar" el trazo entre clips. Se
mitiga con la hoja de personaje como referencia en los once y trazo declarado
en el prompt (grosor constante, sin degradados).

---

El skeleton y el Pixar siguen en borrador. **El animado 2D se produjo el 2026-09-01** — ver el registro al final del documento.

---

## 2026-09-01 — `tienda_ropa` · ESTILO PIXAR v2 — "La venta que no fue" · 43s

**Reemplaza a Doña Clara** como el guión Pixar de este nicho. Doña Clara queda
archivada más arriba, sin producir: sirve como alternativa si se quiere el
formato de micro-situación clásica.

**Gancho base:** `dolor_nombrado#34` — "El cliente pregunta cuánto vale, le
respondés, y no vuelve a escribir." Adaptado a la venta que se pierde por no
tener canal.
**Estructura:** tres actos, no doce beats. Acto 1 cuenta una venta real desde
**la clienta**; el acto 2 la voltea contra el espectador; el acto 3 es el puente.
**Personaje:** **MILENA**, treinta y cuatro, en Neiva, a diez horas de bus de la
tienda. Pixar 3D, cálida, con el celular en la mano.

**Decisión de dirección:** a la dueña del almacén **nunca se le ve la cara**. Se
la ve de espaldas, fuera de foco, o solo las manos. El ad no muestra a la dueña
porque la dueña es quien está viendo el ad.

| # | t | Acto | Voz | Escena |
|---|---|---|---|---|
| 1 | 0–5 | Venta | Una mujer en Neiva vio tu blusa un martes, en una foto que le reenviaron. | Milena en su sala, la foto reenviada en el celular |
| 2 | 5–8 | Venta | Le escribió a la tienda: ¿hacen envíos? | Close-up del mensaje escribiéndose |
| 3 | 8–11 | Venta | Y ahí se acabó la conversación. | El chat sin respuesta, la luz del cuarto baja |
| 4 | 11–16 | Venta | No porque no quisiera comprarla. Sino porque nadie le supo responder. | Milena deja el celular boca abajo |
| 5 | 16–19 | Giro | Esa venta existió. **Pero** no fue tuya. | Corte seco al almacén, de noche, la vitrina encendida |
| 6 | 19–25 | Giro | Y pasa todos los días, a diez cuadras de tu vitrina y a diez horas de bus. | Cámara sale del local hacia la calle, la ciudad detrás |
| 7 | 25–30 | Puente | No te falta ropa ni clientas: te falta el camino entre las dos. | Manos de la dueña (sin rostro) doblando una blusa |
| 8 | 30–35 | Puente | Ese camino lo arman las trescientas cincuenta empresas que van a la feria. | Establishing del recinto, pasillos llenos |
| 9 | 35–39 | Puente | Feria Effix, dieciséis al dieciocho de octubre, en Plaza Mayor. | Fachada de Plaza Mayor |
| 10 | 39–42 | Puente | Y doscientos ponentes que ya lo recorrieron. | Auditorio, gente tomando nota |
| 11 | 42–47 | CTA | Compra tu pasaporte en feriaeffix punto com. Te toma un minuto. | Cierre de marca |
| 12 | 47–52 | Loop | Y la próxima vez que alguien pregunte si haces envíos, tienes qué responder. | Milena abre una caja en Neiva. Sonríe |

Texto corrido para ElevenLabs (126 palabras · 42,6s de locución):

```
Una mujer en Neiva vio tu blusa un martes, en una foto que le reenviaron. Le escribió a la tienda: ¿hacen envíos? Y ahí se acabó la conversación. No porque no quisiera comprarla. Sino porque nadie le supo responder. Esa venta existió. Pero no fue tuya. Y pasa todos los días, a diez cuadras de tu vitrina y a diez horas de bus. No te falta ropa ni clientas: te falta el camino entre las dos. Ese camino lo arman las trescientas cincuenta empresas que van a la feria. Feria Effix, dieciséis al dieciocho de octubre, en Plaza Mayor. Y doscientos ponentes que ya lo recorrieron. Compra tu pasaporte en feriaeffix punto com. Te toma un minuto. Y la próxima vez que alguien pregunte si haces envíos, tienes qué responder.
```

**Por qué es mejor que Doña Clara:** el dolor no se enumera, se **dramatiza**.
El espectador ve la venta perdida antes de saber que era suya, así que la frase
"pero no fue tuya" cae sobre una escena que ya vio, no sobre una afirmación. Y
el loop cierra con la misma pregunta que lo abrió — "¿hacen envíos?" — que es
literalmente la frase que el nicho recibe y no puede responder.

**Producción:** dos hojas de personaje (Milena y las manos de la dueña) más el
local y el recinto. Kling 2.1 std, 12 clips. La escena 12 usa a Milena de la
hoja 1 para cerrar el círculo visual.
**Costo estimado:** ~$4,20 (12 clips $3,36 · imágenes $0,72 · voz $0,10)

### Corrección de registro

Los hooks se citaban como "#39", "#33", "#11". El `n` del banco **no es único**:
se repite en cada categoría (320 ganchos, 45 valores de `n`), así que un número
suelto identifica siete ganchos distintos. Corregido a `categoría#n` acá y en el
campo `banco` de `nichos_effix.py`.

---

## 2026-09-01 — ✅ PRODUCIDO · `tienda_ropa` · Pixar "La venta que no fue" · 46s

**Entregable:** `assets/renders/EFFIX-tienda-ropa-pixar-La-venta-que-no-fue.mp4`
45,98s · 1080x1920 · 30 MB · h264 + aac
**Guión:** `scripts/guiones/effix_tienda-ropa_pixar-v2_APROBADO.json`
**Script de corrida:** `scripts/_producir_tienda_ropa_pixar.py` (hero · escenas · clips · montaje)

Registro tuteo colombiano, sin voseo y sin "parce" — Alexander editó el guión y
pidió quitarlo. Fechas: 16 al 18 de octubre.

### El audio mandó, y cambió el plan
La estimación de escritorio daba 52,4s de locución; el mp3 real dio **43,3s**.
Un 21% de diferencia, porque las 2,96 palabras/segundo del motor se midieron con
`ELEVENLABS_SPEED=0.83` y el `.env` está en 1.1. Con la estimación se habrían
comprado once clips de 5s (55s) para 43s de voz: doce segundos pagados y tirados.

### Keyframes y el modelo
Kling 2.1 standard **no acepta frame final** (su schema solo tiene `image_url`).
Se cambió a **`fal-ai/kling-video/o1/standard/image-to-video`**, que admite
`start_image_url` + `end_image_url` y duraciones enteras de 3 a 10s.

⚠️ **Con solo frame inicial, Kling O1 acepta únicamente 5 o 10 segundos.** Las
escenas 7, 8 y 9 (4s, 3s, 4s, sin end) fallaron con
`Duration only support 5 or 10 seconds when no refer image`. Se piden de 5s y el
montaje las recorta con `-t` a su duración real.

Siete de las diez escenas van encadenadas: el frame final de una es el inicial de
la siguiente dentro de cada bloque (Neiva 1→2→3, el almacén 4→5, la feria 6, el
cierre 10). Por eso son 15 imágenes y no 20.

### Los dos errores de continuidad que hubo que pagar dos veces
1. **La cara que no debía verse.** La 07 salió con el rostro de la dueña en el
   cuadro. El guión dice que nunca se le ve: el ad no la muestra porque la dueña
   es quien está viendo el ad. Se regeneró pidiendo el recorte explícito a la
   altura de las muñecas.
2. **Milena dentro de la feria.** La 10 la puso en primer plano en el pabellón.
   Ella es la clienta de Neiva y no va a la feria — rompía la narrativa entera.
   Causa: el prompt de `/edit` pedía "la misma mujer donde aparezca", y el modelo
   la metió donde no debía. Se resolvió diciendo explícitamente que NO aparece.
3. **El morphing del cierre.** La escena 10 tenía frame inicial con Milena
   arrodillada y blusa coral, y final de pie con la blusa mostaza puesta. Kling no
   puede interpolar un cambio de vestuario: salió un morphing incómodo y, encima,
   con cara triste en el momento de recompensa del ad. Se rehízo con la misma
   postura y la misma ropa — solo levanta la blusa y se ríe.

**Regla que queda:** entre dos keyframes el personaje puede moverse, no cambiarse
de ropa. Si cambia el vestuario, son dos escenas distintas.

### Costo real: $6,32

| Concepto | USD |
|---|---|
| Voz ElevenLabs (14 tomas, 794 caracteres) | 0,08 |
| Música Stable Audio 3 small (48s instrumental) | 0,02 |
| 20 imágenes nano-banana-2 (15 + 5 regeneradas) | 1,60 |
| 55s de video Kling O1 (46s usados) | 4,62 |
| **Total** | **6,32** |

Presupuestado: $5,26. El sobrecosto de $1,06 es enteramente de las cinco
regeneraciones y de los nueve segundos de clip que Kling obliga a comprar cuando
no hay frame final. Los tres clips que fallaron por duración inválida no se
cobraron.

La música salió por **$0,02** con Stable Audio 3 small, no los $0,20
presupuestados con MiniMax: para una cama instrumental de fondo no hace falta un
modelo de canción.

### Overlays
Uno por escena, Montserrat Black con contorno, quemados en el montaje (nunca en
la generación). La marca aparece completa —"FERIA EFFIX"— en el cierre, y
"16-18 oct · Plaza Mayor" y "feriaeffix.com" en los beats de logística.

### Pendiente
- Las fotos reales de la 5ª edición (`referencias/esteticas/feria-real/`) no se
  usaron: los escenarios de feria se generaron en Pixar. Sigue abierto el permiso
  de imagen para usarlas en pauta.
- Faltan por producir los otros dos guiones de la tanda: el skeleton y el
  animado 2D.

---

## 2026-09-01 — `tienda_ropa` · ANIMADO 2D — "La acera" · **PRODUCIDO** · 36s

`assets/renders/tienda-ropa-2d-la-acera.mp4` · 1080×1920 · 24 fps · 35,96s
Guion: `scripts/guiones/effix_animado2d_tienda-ropa-la-acera_20260901_aprobado.json`
Corrida: `scripts/_producir_animado2d_la_acera.py` (`voz · hojas · escenas · clips · lipsync · montaje`)

Diálogo a dos voces, sin narrador. Rosa vende de mostrador; Marce, la vecina de
local, despacha a todo el país. Quien convence no es un gurú: es la de al lado.

| # | t | Quién | Voz | Línea |
|---|---|---|---|---|
| 1 | 0,0 | ROSA | Medellín | Otra vez llovió. Hoy no me entró ni un alma. |
| 2 | 2,7 | MARCE | Valentina | A mí tampoco me entró nadie… y despaché dieciocho blusas. |
| 3 | 6,8 | ROSA | Medellín | ¿Cómo así que dieciocho? ¿A quién? |
| 4 | 9,3 | MARCE | Valentina | A gente que ni conozco. De Pereira, de Cúcuta, de Neiva. |
| 5 | 14,5 | ROSA | Medellín | ¿Y eso cómo se hace? |
| 6 | 16,2 | MARCE | Valentina | Yo tampoco sabía. Lo aprendí en la feria. |
| 7 | 20,1 | ROSA | Medellín | ¿Cuál feria? |
| 8 | 21,1 | MARCE (off) | Valentina | Feria Effix, del dieciséis al dieciocho de octubre, en Plaza Mayor. |
| 9 | 25,7 | ROSA | Medellín | ¿Y eso sirve pa ropa? |
| 10 | 27,5 | MARCE | Valentina | Eso sirve pa lo que vos vendás. |
| 11 | 29,5 | VOZ MARCA | Effi | Compra tu pasaporte en feriaeffix punto com. Te toma un minuto. |
| 12 | 33,3 | ROSA | Medellín | Mañana no me quedo esperando a que escampe. |

**Reparto de voces:** Rosa con `cercana_medellin`, Marce con `amiga`, el CTA con
`marca_femenina`. El contexto de ElevenLabs (`previous_text`/`next_text`) se pasa
sólo entre líneas del mismo hablante: darle a Rosa la frase de Marce la hace
imitar su entonación y el diálogo deja de sonar a dos personas.

**Dirección:** planos alternados, un hablante por clip — es lo único que el
lip-sync sincroniza bien, porque los modelos mueven una sola cara por video. El
beat 8 corta al recinto de la feria y la línea va en off; el 11 es un plano
abierto de los dos locales, con aire arriba para el logo.

### Lo que este ad le enseñó al motor

- **Kling o1 no acepta cualquier duración.** El schema dice 3–10s, pero el
  endpoint responde `Duration only support 5 or 10 seconds when no refer image`.
  Con frame de referencia sí acepta los enteros intermedios, así que en un plano
  de diálogo **el frame final es el mismo inicial**: la cara actúa y vuelve al
  encuadre. Eso desbloquea clips de 3s (una línea de 0,74s no paga 5s), no cuesta
  una imagen extra y de paso impide que el plano derive.
- **`sync_mode=cut_off` devuelve el clip cortado a la voz.** Pedirle después un
  cuarto de segundo más de video deja el video más corto que su audio y el
  diálogo se desfasa. El aire entre réplicas se saca con `tpad=stop_mode=clone`:
  la cara sostiene el gesto, que es lo que hace en una conversación real.
- **La bible con escenario adentro contamina los planos que no son de ese
  escenario.** La primera feria salió con las fachadas de la acera pegadas en el
  tercio inferior. Para los planos sin personaje viaja sólo la mitad de estilo
  de la bible, cortada en `Setting:`.
- **Verificar la locución con whisper antes de animar.** Dos defectos que no se
  ven en el texto: la línea 8 dijo "Plaza **Mayores**" y la 12 salió con un
  tartamudeo ("a que **la que** escampe"). Las dos se regeneraron con la misma
  ortografía —nunca deformando la marca— y se comprobaron transcribiendo. Cuesta
  centavos y evita descubrirlo con el clip y el lip-sync ya pagados.

**Costo real:** ~$5,4 · voz $0,06 · 16 imágenes $0,62 · 53s de clips $4,45 ·
lip-sync 13 pasadas $0,25 · whisper $0,04

### 2026-09-01 · Cambio de voz — "Medellin" reemplaza a Sara Montoya

Alexander descartó la voz con la que se locutó la primera versión: era
`Sara Montoya - clonación #5`, la clonada que estaba fijada en
`ELEVENLABS_VOICE_ID` del `.env`. El script cayó ahí por no pasarle `perfil`.

Se probaron seis voces profesionales del catálogo con la misma frase
(`assets/audio/pruebas-voz/`, $0,09) y quedó **"Medellin - Conversational and
Intense"**, latina y conversacional en vez de locutora. "Malena M" está
deshabilitada por su dueño y "Valentina" arrastra el acento español que ya se
había detectado en el ad de LANA.

También cambiaron los ajustes: `stability` de 0.28 a **0.45** y `speed` de 1.1 a
**1.0**. Esa combinación vieja atropellaba la frase y era la mitad de la
sensación robótica.

**La locución pasó de 43,3s a 53,9s** — casi diez segundos más, por la velocidad
y por la voz. Como los clips ya estaban comprados para 46s, el montaje los
ralentiza un **x1,179** con `setpts` en vez de regenerar video: en planos de
push-in lento no se nota, y regenerar habría costado otros $3,80. Es la misma
maniobra que en el ad de LANA, al revés (allá se aceleró 1.4x).

El montaje también cambió de criterio: antes alineaba cada frase al arranque de
su escena y rellenaba con silencio; ahora la voz corre de largo con respiros de
0,12s y la imagen corta por debajo. La frase ya no se parte donde corta el video.

⚠️ Detalle de ffmpeg que costó dos montajes: **`-t` va antes del `-i`**. Después
del `-i` recorta la salida ya ralentizada y anula el estirado — el video seguía
saliendo de 46s.

**Entregable final:** 53,85s · 1080x1920 · 33 MB
**Costo acumulado del ad: $6,49** (los $6,32 de producción más $0,17 de las
pruebas de voz y la relocución).
