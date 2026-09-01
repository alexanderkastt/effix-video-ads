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

| Var | Banco | Hook |
|---|---|---|
| A | #39 `dolor_nombrado` | Llovió el sábado, no entró nadie, y el mes se te cayó. |
| B | #33 `callout` | Si vives de que la gente pase por el frente de tu almacén, quédate. |
| C | #11 `callout` | Tu ropa se vende bien. Pero solo a diez cuadras a la redonda. |

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
