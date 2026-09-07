# Feria Effix 2026 — 28 guiones Pixar con IA · ángulo .2 de cada público

*Locución narrada · siete estructuras narrativas distintas · 7 de septiembre de 2026 · para el equipo audiovisual*

---

## Qué es esto

Un video animado 3D estilo Pixar por cada uno de los veintiocho públicos de Feria Effix, sobre el **ángulo .2** de cada uno (el segundo dolor de su lista). Cada video vende **boletería**: cierra en la compra del ingreso, no en «conocer el evento».

Estos veintiocho son hermanos de los que ya existen, no repetición:

| Ángulo | Qué se hizo | Formato |
|---|---|---|
| .1 | 28 videos musicales | Canción como única voz, siete estilos visuales |
| **.2** | **Estos 28** | **Pixar 3D, locución narrada, siete estructuras narrativas** |
| .3 | 28 guiones para Sara | Grabación real a cámara, siete formatos de rodaje |

**Lo que cambia respecto al lote anterior de .2 (el de producción humana):** aquel tenía los veintiocho con la misma estructura de doce beats y se notaba al verlos seguidos. Este usa **siete estructuras narrativas distintas, cuatro guiones por estructura**, y las fechas, las cifras y el CTA ya no son beats aparte pegados al final: van metidos dentro de la historia de cada video.

**Los personajes los define el equipo.** Aquí va el *rol* que el objeto cumple en la historia y lo que tiene que poder hacer en cámara. El diseño, el nombre y la personalidad son decisión de ustedes: lo único que pedimos es que respeten las cuatro reglas duras de la sección «Reglas Pixar que no se negocian».

---

## Las siete estructuras

Cuatro guiones por estructura. Están agrupadas así en el documento, no por número de público, para que puedan producir de a cuatro con la misma cabeza puesta.

| # | Estructura | Cómo funciona | Dónde cae la campaña |
|---|---|---|---|
| **E1** | **Monólogo del objeto** | El objeto habla en primera persona de lo que ve todos los días. Íntimo, sin prisa, una sola voz. La locución ES la voz del objeto. | El objeto anuncia su propia fecha de salida: «el quince de octubre me sacan de aquí». |
| **E2** | **Dos objetos conversan** | Dos objetos del mismo mundo: uno resignado, otro que ya cambió. Réplicas cortas, alternadas. La misma voz hace los dos con timbre distinto. | El que ya cambió cuenta dónde lo aprendió. |
| **E3** | **La escalada** | Algo crece en cámara —una barra, una pila, un contador— mientras el resultado se queda quieto. Repetición con variación. | La escalada se rompe: el corte a la feria es el único cambio de plano que no escala. |
| **E4** | **Mundo espejo** | La misma escena dos veces: como está y como podría estar. El corte entre las dos es el argumento. | El mundo B es el de quien ya fue. |
| **E5** | **Preguntas al espectador** | El objeto se gira a cámara y pregunta. Silencio real después de cada pregunta —el espectador contesta en su cabeza— y el video confirma. | La última pregunta la contesta la feria. |
| **E6** | **Reloj** | Cada beat arranca con una hora, un día o un segundo. Cortes secos entre marcas de tiempo. | La última marca de tiempo es el quince de octubre. |
| **E7** | **El viaje** | El objeto sale del sitio donde está atascado y llega al recinto. Continuidad espacial: cada plano avanza en el mismo camino. | El destino ES la feria. |

---

## Reglas Pixar que no se negocian

Estas cuatro salieron de plata perdida en los ads que ya se produjeron. No son gusto:

**1. Nunca le pidan a un objeto una acción que necesita manos humanas.** «El libro teclea», «el carrito levanta los papeles». El modelo no falla: resuelve la acción imposible **metiendo una persona en el plano**. Costó dos clips rehechos en el ad de abogados. Si el objeto necesita mover algo, que lo haga con el cuerpo que tiene: se inclina, empuja, rebota, se ilumina, cae.

**2. La hoja de personaje va en un solo cuadro.** Pedir «character sheet» a nano-banana devuelve una grilla de contactos, y como cada escena se edita **desde** esa imagen, las doce heredan el error. Pidan `single full-frame image`, repítanlo en el system prompt, y **miren la imagen antes de generar las escenas**: es el punto de control más barato del pipeline.

**3. El recinto es un centro de convenciones, no una plaza de mercado.** `hundreds of colourful stands` y `at a stand` se leen como mercado. Va: `modern convention hall, corporate exhibition booths, backlit display walls, carpeted aisles, lanyards`, y veto explícito de puesto de mercado.

**4. Prohibido `slow`, `deliberate`, `slow motion` en los prompts de video.** Sale cámara lenta real y arreglarla en post cuesta calidad. El ritmo se construye en el montaje.

**Y una quinta que no cuesta plata pero sí credibilidad:** nada de texto dentro de la imagen. El modelo inventa letras. Los carteles del fondo se piden como `plain panels with bold abstract geometric shapes only, absolutely no letters, no words, no writing anywhere`. Todo el texto que se lee lo pone edición.

---

## Cómo se ve y cómo suena

**Estilo.** Pixar 3D: ojos grandes expresivos, proporciones redondeadas, materiales creíbles, luz de película animada, silueta clara. Nunca realismo inquietante. El espectador tiene que entender el estado emocional del objeto **antes** de escuchar la frase.

**Marca.** Feria Effix es **blanco y negro estricto, sin color de acento**, Montserrat. El mundo 3D del problema puede tener color —es la casa, la oficina, la bodega del personaje—; **el recinto de la feria va en blanco, negro y gris**, y ese contraste es parte del argumento: se pasa del ruido de color al orden en blanco y negro. Logo desde el primer segundo, puesto por edición.

**Voz.** Locución en off, voz latina, `speed 1.15`, respiro de doce centésimas entre réplicas. A **3,69 palabras por segundo** medidas. En el monólogo (E1) y en el diálogo (E2) la locución es la voz del objeto: **no hace falta lipsync**. Si quieren labios sincronizados, solo en uno o dos planos y **después** de generar el clip, nunca antes.

**Ritmo.** El corte visual cae **cada 1,5 a 2,5 segundos**, con piso duro de 1,25. Una línea de cinco segundos no es un plano de cinco segundos: son dos o tres planos del **mismo clip** reencuadrado (`full`, `punch`, `lateral`, `contra`, sin repetir dos seguidos, zoom máximo 1,25x). No generen clips extra para tener más cortes: el reencuadre no cuesta nada y el presupuesto es de cinco a seis dólares por video.

**Música.** De la librería (`assets/audio/soundtracks`), mood `alegre` para todo lo animado. Ducking real, master a −14 LUFS. La textura del ambiente va pedida dentro del prompt de video y **todo prompt de audio cierra con `no discernible speech`**.

**Duración.** Todos los guiones de aquí están entre ciento treinta y ciento setenta palabras, que a 3,69 palabras por segundo son entre treinta y seis y cuarenta y cinco segundos de locución. Con el aire entre réplicas y el cierre, cada video queda entre cuarenta y cincuenta segundos: dentro del rango de treinta a sesenta que pide el formato.

---

## Lo que se dice y lo que no

**Cifras autorizadas, ninguna otra:** más de trescientas cincuenta empresas · más de sesenta mil asistentes · más de doscientas ponencias · más de doscientos ponentes · cinco países · cinco ediciones.

⚠️ **«Más de sesenta mil asistentes» está sin fuente pública verificada.** Es cifra que dio Alexander. Confirmar con Effix antes de pautar cualquiera de estos videos.

**Fechas:** del quince al diecinueve de octubre, Plaza Mayor, Medellín. El **Pasaporte da tres días**; el evento dura cinco. Por eso las letras hablan de las fechas del evento y **nunca prometen cinco días de acceso**.

**CTA único:** «Compra tu ingreso dando clic en el botón». Sin URL —el mismo video va a landing y a WhatsApp—, sin descuento, sin código, sin la palabra «taller».

**En la locución los números van en letras** («trescientas cincuenta», «quince al diecinueve»). En el **texto en pantalla** sí van en dígitos (`+350 EMPRESAS`, `15–19 OCT`): se lee, no se pronuncia, y así se produjeron los ads que ya están renderizados.

**Se describe la situación, no la persona.** Nada de estados de salud, de dinero ni de ánimo atribuidos al espectador. El oficio sí se puede nombrar de frente («eres contador») — eso es Meta-seguro y quita ambigüedad.

**Texto en pantalla: máximo siete palabras** y tiene que funcionar sin sonido.

---

## Orden de producción por video

No es negociable y ahorra plata:

1. **Hoja de personaje** en un solo cuadro → **mírenla** antes de seguir.
2. **Voz** con la locución corrida completa → **midan el mp3 real**.
3. **Plan de planos desde el audio medido**, no desde el guion escrito.
4. Imágenes de escena editadas **desde la hoja de personaje**, nunca desde el clip anterior.
5. Clips.
6. Montaje: cortes cada 1,5–2,5 s, overlays Montserrat, música con ducking, master a −14 LUFS.
7. QA: duración entre treinta y sesenta segundos, ningún plano por debajo de 1,25 s, sin clipping.

**El audio manda.** Primero la voz, después los clips.

---

## Índice

| # | Público | Ángulo .2 | Título | Estructura | Dur. |
|---|---|---|---|---|---|
| 01 | 🔥 Emprendedores que empiezan en e-commerce | Elegir qué producto vender | Soy la lista que nunca se cierra | E1 Monólogo | ~41 s |
| 02 | 🔥 Dueños de tiendas online | Carritos abandonados | Dos carritos | E2 Diálogo | ~38 s |
| 03 | 🔥 Empresarios de e-commerce en crecimiento | Escalar publicidad | La barra que sube y la que no | E3 Escalada | ~42 s |
| 04 | 🔥 Vendedores de redes sociales | Responder manualmente | Las once de la noche, en dos casas | E4 Espejo | ~40 s |
| 05 | 🔥 Dropshippers | Encontrar proveedores confiables | ¿Cuántos días llevas esperando? | E5 Preguntas | ~38 s |
| 06 | 🔥 Marcas, fabricantes e importadores | Vender directamente al consumidor | El producto que se fue por otro camino | E7 Viaje | ~43 s |
| 07 | 🔥 Mayoristas y distribuidores | Conseguir nuevos clientes | Enero, junio, diciembre: los mismos | E6 Reloj | ~37 s |
| 08 | 🔥 Marketing, publicidad y adquisición digital | CPM cada vez más caro | Soy el número que sube | E1 Monólogo | ~42 s |
| 09 | 🔥 Creadores de contenido que venden | Monetizar seguidores | El contador y la alcancía | E2 Diálogo | ~38 s |
| 10 | 🔥 Consultores independientes de e-commerce | Demostrar experiencia | Ocho años sin público | E3 Escalada | ~40 s |
| 11 | 🔥 Tecnología y soluciones para e-commerce | Inteligencia artificial | La demo en la pantalla y la demo en el stand | E4 Espejo | ~45 s |
| 12 | 🔥 Medios de pago y Fintech | Carritos abandonados por pago | ¿Cuántos se van en el último paso? | E5 Preguntas | ~37 s |
| 13 | 🔥 Logística, fulfillment y última milla | Entregas tardías | El paquete, hora por hora | E6 Reloj | ~39 s |
| 14 | 🔥 Proveedores de dropshipping | Encontrar nuevos clientes | La caja que salió a buscar vendedores | E7 Viaje | ~36 s |
| 15 | 🔥 Empresas de empaques y packaging | Empaque que vende | Soy la caja que nadie graba | E1 Monólogo | ~41 s |
| 16 | 🔥 Marketplaces | Aumentar ventas | El estante lleno y el estante vacío | E2 Diálogo | ~37 s |
| 17 | 🟡 Internacionalización y expansión | Primer mercado internacional | El pedido que cruzó la frontera | E7 Viaje | ~38 s |
| 18 | 🟡 Negocios físicos que quieren vender online | Crear primera tienda online | El sábado que llovió | E4 Espejo | ~45 s |
| 19 | 🟡 Retail | E-commerce | El cinco por ciento | E3 Escalada | ~38 s |
| 20 | 🟡 Atención al cliente y Customer Experience | Responder rápido | ¿A qué hora respondiste? | E5 Preguntas | ~39 s |
| 21 | 🟡 Contenido para e-commerce | Videos para anuncios | Segundo uno, segundo dos, segundo tres | E6 Reloj | ~37 s |
| 22 | 🟡 Desarrollo, programación e integraciones | Integraciones | La hoja de cálculo y el cable | E2 Diálogo | ~40 s |
| 23 | 🟡 Ciberseguridad y prevención de fraude | Robo de cuentas | Viernes, siete de la noche | E6 Reloj | ~41 s |
| 24 | 🟡 Servicios profesionales para e-commerce | Contabilidad | Soy los movimientos que no cuadran | E1 Monólogo | ~44 s |
| 25 | 🟡 Educación y formación en e-commerce | Emprender | La pila de cuadernos | E3 Escalada | ~40 s |
| 26 | 🟡 Ejecutivos y líderes de transformación | IA en la empresa | La diapositiva y el proceso | E4 Espejo | ~41 s |
| 27 | 🧊 Empresarios que buscan networking y alianzas | Encontrar proveedores | ¿Cuándo agregaste el último contacto? | E5 Preguntas | ~36 s |
| 28 | 🧊 Personas que quieren ser referentes del sector | Ser reconocido en el sector | El nombre que faltaba en la lista | E7 Viaje | ~39 s |

**Una aclaración sobre las cifras que dicen los personajes.** Cuando un objeto habla de su propio mundo —«tengo cuarenta y siete productos guardados», «hoy entraron veinte carritos»— es detalle narrativo, no un dato de mercado. Las únicas cifras que afirman algo sobre la feria son las seis autorizadas de arriba.

---

# E1 · Monólogo del objeto

*Videos 01, 08, 15 y 24*

El objeto habla en primera persona de lo que ve todos los días. Una sola voz, tono de confidencia, sin prisa. **La locución ES la voz del objeto**, así que no hace falta lipsync: el personaje transmite con cuerpo, ojos y cejas, y la cámara se le acerca cuando la frase pesa. Es la estructura más íntima de las siete; el ritmo lo ponen los cortes, no la voz.

**Cómo se dirige:** el objeto nunca actúa lo que dice —no señala, no ilustra—. Reacciona. La cámara hace el trabajo: se abre cuando el objeto está solo, se cierra cuando confiesa.

---

## 01 · Emprendedores que están comenzando en e-commerce 🔥
**Ángulo 1.2 — Elegir qué producto vender** · E1 Monólogo · ~41 s · 153 palabras

**Objeto protagonista:** la lista de productos guardados en el celular. Vive dentro de la pantalla, se abre y se cierra sola, y está cansada de crecer. El equipo decide si es una libreta digital, una pila de tarjetas o una carpeta con ojos.
**Escenario:** mesa del comedor de noche, portátil cerrado, luz de una lámpara.
**Hilo visual:** cada vez que aparece, la lista tiene un renglón más.

**Locución corrida:**

> Soy la lista de productos que guardas cada noche. Tengo cuarenta y siete adentro, y ninguno se ha vendido. Todas las noches me abres, me agregas uno más, y me cierras. Me dices que cuando aparezca el perfecto, arrancamos. Llevas siete meses diciéndome eso. Yo he visto listas como yo en otros teléfonos. Las abrieron una vez, eligieron uno, lo probaron, y no volvieron a abrirme. Esos ya están vendiendo. No te falta un producto mejor. Te falta ver cómo eligen los que ya venden. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas con los productos que sí se están moviendo, y los emprendedores que ya los venden, en el mismo sitio. Y más de doscientas ponencias donde cuentan cómo eligieron. Ese quince de octubre yo me quedo cerrada. Y tú sales de ahí con uno elegido. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Soy la lista de productos que guardas cada noche. | — | La lista, sola en el centro de la pantalla apagada, se despliega hacia la cámara. Comedor de noche al fondo, desenfocado. | Primer plano cerrado. Que la primera imagen sea el personaje, no el escenario. |
| 2 | Tengo cuarenta y siete adentro, y ninguno se ha vendido. | Cuarenta y siete guardados | La lista se estira hacia abajo hasta salir del cuadro por el borde inferior. | El estirón es el chiste visual. Que se pase de largo. |
| 3 | Todas las noches me abres, me agregas uno más, y me cierras. | — | Tres aperturas y cierres seguidos, con la lámpara cambiando de ángulo entre una y otra. | Tres cortes secos: son tres noches distintas, no una animación continua. |
| 4 | Me dices que cuando aparezca el perfecto, arrancamos. | «Cuando aparezca el perfecto» | La lista se encoge un poco, resignada, y mira hacia el portátil cerrado. | El portátil cerrado es el segundo personaje mudo del video. |
| 5 | Llevas siete meses diciéndome eso. | Siete meses | La lámpara del comedor se apaga y se enciende siete veces, la lista quieta en el centro. | Cambio de luz, no de plano. El paso del tiempo lo hace la lámpara. |
| 6 | Yo he visto listas como yo en otros teléfonos. Las abrieron una vez, eligieron uno, lo probaron, y no volvieron a abrirme. Esos ya están vendiendo. | Abrieron una vez y eligieron | Otra mesa, otro teléfono: una lista idéntica pero con un solo renglón, y cajas de pedido saliendo alrededor. | Es la primera vez que salimos de la casa. Que se note el cambio de mundo. |
| 7 | No te falta un producto mejor. Te falta ver cómo eligen los que ya venden. | No te falta producto | Vuelta al comedor, la lista de frente a cámara por primera vez. | La única frase que el objeto dice mirando al espectador. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas con los productos que sí se están moviendo, y los emprendedores que ya los venden, en el mismo sitio. | 15–19 OCT · +350 EMPRESAS | Recinto en blanco, negro y gris: pasillos alfombrados, stands corporativos, paneles retroiluminados. La lista, pequeña, entra por el pasillo. | El salto de color a blanco y negro es el argumento. Nada de puestos de mercado. |
| 9 | Y más de doscientas ponencias donde cuentan cómo eligieron. | +200 PONENCIAS | Auditorio en gris, sillas llenas, una tarima al fondo. | Plano ancho: el único del video. Da escala. |
| 10 | Ese quince de octubre yo me quedo cerrada. Y tú sales de ahí con uno elegido. | Sales con uno elegido | La lista se cierra sola sobre la mesa, tranquila, y la pantalla se apaga. | Es un final feliz, no una despedida triste. Que se cierre relajada. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | Sin URL. Sin descuento. |

**Recomendación de producción:** este es el guion más barato de los cuatro de E1 —dos escenarios y un solo personaje—. Úsenlo para calibrar la hoja de personaje del lote: si la lista sale bien en un solo cuadro, los otros tres objetos salen igual.

---

## 08 · Marketing, publicidad y adquisición digital 🔥
**Ángulo 8.2 — CPM cada vez más caro** · E1 Monólogo · ~42 s · 155 palabras

**Objeto protagonista:** el número del CPM. Un número que vive en el panel de anuncios, que sube sin querer y lo sabe. Culpable pero inocente. El equipo decide si es un dígito con cara, un medidor o una flecha.
**Escenario:** oficina de agencia de madrugada, dos monitores encendidos, café frío.
**Hilo visual:** el número, siempre un poco más arriba que en el plano anterior.

**Locución corrida:**

> Soy el número que abres primero cada mañana. Y sí: subí otra vez. Mismo anuncio, misma audiencia, más caro. No lo hago por molestarte. Yo solo mido lo que cuesta que alguien te vea, y cada vez somos más los que queremos ser vistos. Tú me miras y le dices al cliente que la plataforma está imposible. Y algo de razón tienes. Pero yo también subí en las cuentas de las agencias que están al lado, y ellas siguen dando resultado con el mismo presupuesto. Ahí está la diferencia: yo subí para todos. El creativo, el canal y el método solo cambiaron para algunas. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están esas agencias, y más de doscientas ponencias sobre creativos, canales nuevos e inteligencia artificial aplicada a la pauta. Yo voy a seguir subiendo. Lo que puede cambiar es lo que haces conmigo. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Soy el número que abres primero cada mañana. | — | El número solo, brillando en un monitor a oscuras. Oficina vacía detrás. | Empezar a oscuras. La luz del monitor es la única fuente. |
| 2 | Y sí: subí otra vez. | Subió otra vez | El número se estira un peldaño hacia arriba, incómodo, mirando a un lado. | Que la subida se vea como algo que le pasa, no algo que hace. |
| 3 | Mismo anuncio, misma audiencia, más caro. | — | Tres tarjetas idénticas se apilan detrás del número; la tercera con el número más grande. | Tres cortes rápidos. Es la única enumeración del guion. |
| 4 | No lo hago por molestarte. Yo solo mido lo que cuesta que alguien te vea, y cada vez somos más los que queremos ser vistos. | Cada vez somos más | El monitor se llena de números iguales, apretados, empujándose entre ellos. | La multitud de números es literal. Sin personas. |
| 5 | Tú me miras y le dices al cliente que la plataforma está imposible. Y algo de razón tienes. | «Está imposible» | El número mira hacia una silla vacía frente al monitor. | La silla vacía sustituye al humano. Nunca metan una persona. |
| 6 | Pero yo también subí en las cuentas de las agencias que están al lado, y ellas siguen dando resultado con el mismo presupuesto. | Subió para todos | Otra oficina, otro monitor con el mismo número arriba, y a su lado una barra de resultados que sí crece. | Cambio de oficina con corte seco. Mismo número, otro resultado. |
| 7 | Ahí está la diferencia: yo subí para todos. El creativo, el canal y el método solo cambiaron para algunas. | No es la plataforma | El número se aparta a un lado del cuadro y deja ver lo que había detrás. | El objeto literalmente se quita del medio. Es la causa raíz. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están esas agencias, y más de doscientas ponencias sobre creativos, canales nuevos e inteligencia artificial aplicada a la pauta. | 15–19 OCT · +200 PONENCIAS | Recinto en blanco y negro, stands corporativos, paneles retroiluminados, pasillo alfombrado. | Sin color. Sin letras legibles en los paneles del fondo. |
| 9 | Yo voy a seguir subiendo. Lo que puede cambiar es lo que haces conmigo. | Lo que cambia eres tú | El número, ahora en gris sobre el recinto, ya no molesta: es solo un dato en una pared. | Mismo objeto, otro contexto. Ese es todo el remate. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** un número con cara es el personaje más difícil del lote —tiende a salir como un ícono plano—. Denle volumen, material (metal cepillado, plástico pulido) y un peso que se note cuando se apoya. Si a la segunda hoja de personaje sigue saliendo plano, cámbienlo por un medidor de aguja: cuenta lo mismo y es más fácil de animar.

---

## 15 · Empresas de empaques y packaging 🔥
**Ángulo 15.2 — Empaque que vende** · E1 Monólogo · ~41 s · 151 palabras

**Objeto protagonista:** una caja de envío café, genérica, sin marca. Humilde, resignada, con dignidad. El equipo decide la cara y el gesto.
**Escenario:** mesa de despacho de una tienda online, cinta, rollo de burbuja, pedidos apilados.
**Hilo visual:** el momento en que alguien abre la caja — siempre fuera de cuadro, siempre sin manos humanas: la tapa se abre sola.

**Locución corrida:**

> Soy la caja en la que despachas mil pedidos al mes. Café, sin nada escrito, igual a las de todo el mundo. Yo soy lo único de tu marca que tu cliente toca. Y cuando llego, se me abre la tapa, sacan lo de adentro, y me botan sin mirarme. Nadie me graba. Nadie me muestra. Tú dices que yo soy un costo, y que el cliente compra el producto, no el empaque. Pero las marcas que crecen se gastan la plata en mí, porque saben que el video que el cliente sube es el de abrirme a mí. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas que despachan todos los días, y ahí una caja se puede tocar. Yo no te pido más presupuesto. Te pido que dejes de esconderme. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Soy la caja en la que despachas mil pedidos al mes. | — | La caja sola en la mesa de despacho, cinta y burbuja alrededor. | Luz de bodega, cálida. El mundo del problema tiene color. |
| 2 | Café, sin nada escrito, igual a las de todo el mundo. | — | La cámara retrocede y aparecen veinte cajas idénticas detrás. | El retroceso es el único movimiento de cámara grande del video. |
| 3 | Yo soy lo único de tu marca que tu cliente toca. | Lo único que toca | Primer plano de la caja, quieta, de frente. | La frase más importante va en el plano más cerrado. |
| 4 | Y cuando llego, se me abre la tapa, sacan lo de adentro, y me botan sin mirarme. | — | La tapa se abre sola, el contenido sale volando fuera de cuadro, la caja cae de lado. | **Sin manos.** Todo se mueve solo: es una caja que cuenta lo que le pasa. |
| 5 | Nadie me graba. Nadie me muestra. | Nadie la graba | La caja tirada junto a un celular apagado, en el piso. | El celular apagado es el remate mudo. |
| 6 | Tú dices que yo soy un costo, y que el cliente compra el producto, no el empaque. | «Es un costo» | La caja de nuevo en la mesa, encogida. | Volver al escenario uno. Que se sienta el bucle. |
| 7 | Pero las marcas que crecen se gastan la plata en mí, porque saben que el video que el cliente sube es el de abrirme a mí. | La caja es el video | Otra caja, con marca, abriéndose sola frente a un celular en trípode que sí está grabando. | Aquí sí hay color y diseño. El contraste con el plano 4 es todo. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas que despachan todos los días, y ahí una caja se puede tocar. | 15–19 OCT · +350 EMPRESAS | Recinto en blanco y negro: stands corporativos, paneles retroiluminados, pasillos alfombrados. La caja sobre un pedestal. | La caja en pedestal, iluminada como producto. Es su momento. |
| 9 | Yo no te pido más presupuesto. Te pido que dejes de esconderme. | Deja de esconderla | Primer plano de la caja, ahora con la tapa entreabierta y luz saliendo de adentro. | La luz de adentro es lo único que cambia. Nada de efectos. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** una caja tiene cero rasgos, así que toda la actuación está en la tapa y las solapas. Trátenlas como cejas y hombros: tapa medio abierta es duda, solapas caídas es derrota, tapa abierta con luz adentro es orgullo. Definan esos tres estados en la hoja de personaje y el resto sale solo.

---

## 24 · Servicios profesionales para e-commerce 🟡
**Ángulo 24.2 — Contabilidad** · E1 Monólogo · ~44 s · 161 palabras

**Objeto protagonista:** el extracto de una tienda online —una hoja larga de movimientos que no cuadran—. Nerviosa, honesta, quiere ayudar pero nadie la entiende. El equipo decide si es una hoja, un libro contable o una cinta de caja registradora.
**Escenario:** oficina de contador, archivadores, calculadora, escritorio ordenado.
**Hilo visual:** la hoja se enrolla y se desenrolla; cada vez sale un renglón raro nuevo.

**Locución corrida:**

> Soy el extracto de una tienda que vende por internet. Me trajeron a tu oficina y llevo ahí tres semanas. En mí hay pasarelas de pago, envíos a otros países, devoluciones y comisiones. Tú los cuadras igual, resolviendo sobre la marcha, y te sale. Pero te toma el triple. Te dices que cuando baje la temporada te vas a sentar a estudiar este modelo. La temporada no baja. Y cada mes abren más tiendas como esta, que necesitan un contador que las entienda. No es que te falte estudiar. Es que ese modelo no se aprende leyéndome a mí: se aprende donde están las tiendas, y no están en tu oficina. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas que necesitan quién les cuadre los números, y más de doscientas ponencias para entender el modelo. Yo me quedo aquí. Ve tú. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Soy el extracto de una tienda que vende por internet. | — | La hoja enrollada sobre el escritorio, un poco abierta, mirando alrededor. | Oficina ordenada y quieta: el contraste con lo que trae la hoja. |
| 2 | Me trajeron a tu oficina y llevo ahí tres semanas. | Tres semanas ahí | La hoja bajo una capa de polvo fina, junto a la calculadora apagada. | El polvo cuenta el tiempo sin decirlo. |
| 3 | En mí hay pasarelas de pago, envíos a otros países, devoluciones y comisiones. | — | La hoja se desenrolla de golpe y cruza todo el escritorio hasta el piso. | El desenrollado es el momento de energía del video. Cuatro cortes rápidos dentro del mismo clip. |
| 4 | Tú los cuadras igual, resolviendo sobre la marcha, y te sale. Pero te toma el triple. | Sale, pero tarda | La calculadora al lado se enciende, trabaja, y echa humito por un costado. | El humito es el único gag. Uno solo, y basta. |
| 5 | Te dices que cuando baje la temporada te vas a sentar a estudiar este modelo. | «Cuando baje la temporada» | La hoja mira un calendario de pared que pasa páginas solo. | El calendario que se pasa solo es el hilo del tiempo. |
| 6 | La temporada no baja. Y cada mes abren más tiendas como esta, que necesitan un contador que las entienda. | La temporada no baja | Detrás de la hoja aparecen otras hojas iguales, apiladas, cada una asomando. | La pila crece hacia atrás, no hacia arriba: cabe mejor en vertical. |
| 7 | No es que te falte estudiar. Es que ese modelo no se aprende leyéndome a mí: se aprende donde están las tiendas, y no están en tu oficina. | No están en tu oficina | La hoja se aparta y detrás se ve la puerta de la oficina, cerrada. | La puerta cerrada anticipa el corte siguiente. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas que necesitan quién les cuadre los números, | 15–19 OCT · +350 EMPRESAS | La puerta se abre a un recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | El corte de oficina con color a recinto en gris es el mismo recurso del lote. Consistencia. |
| 9 | y más de doscientas ponencias para entender el modelo. | +200 PONENCIAS | Auditorio gris, sillas llenas, tarima al fondo. | — |
| 10 | Yo me quedo aquí. Ve tú. | Ve tú | La hoja, sola en el escritorio, se enrolla tranquila. La puerta queda abierta. | La puerta abierta es el CTA visual. No la cierren. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este y el 01 comparten estructura y tono. Prodúzcanlos con la misma voz y el mismo mood de música, pero **cambien el ritmo del montaje**: el 01 respira, este corre. Si salen igual de rápidos, se van a leer como el mismo video.

---

# E2 · Dos objetos conversan

*Videos 02, 09, 16 y 22*

Dos objetos del mismo mundo hablan. Uno está resignado; el otro ya cambió y no presume: cuenta. Réplicas cortas, alternadas, con medio segundo de aire entre una y otra. **La misma voz hace los dos personajes**, diferenciados por timbre y ritmo —uno más grave y lento, otro más claro y ágil—; si quieren, se graban en dos pistas y se intercalan.

**Cómo se dirige:** cada objeto tiene su lado del cuadro y no lo cambia en todo el video. Cuando uno habla, la cámara está de su lado; cuando responde el otro, corta al lado opuesto. Ese ping-pong es lo que da ritmo sin generar más clips: **son dos clips largos y muchos reencuadres**.

**Lipsync:** no hace falta. Si lo quieren, úsenlo solo en las dos réplicas del giro, y siempre después de generar el clip.

---

## 02 · Dueños de tiendas online 🔥
**Ángulo 2.2 — Carritos abandonados** · E2 Diálogo · ~38 s · 142 palabras

**Objetos protagonistas:** un carrito de compras lleno hasta el tope, plantado en mitad de una tienda online vacía · y otro carrito, más ligero, que ya pasó por la caja. El equipo decide el diseño.
**Escenario:** el interior de una tienda online, imaginado como un pasillo de supermercado hecho de tarjetas de producto flotantes.
**Hilo visual:** la línea blanca del piso que lleva hasta la caja. El carrito lleno nunca la pisa.

**Locución corrida:**

> —¿Y tú por qué estás lleno ahí parado? —Me llenaron hace tres horas y se fueron. —A mí también me llenaron hace tres horas. Yo ya pasé. —¿Y cómo pasaste? —Alguien se dio cuenta de que yo estaba aquí y me fue a buscar. —A mí nadie me busca. Mi dueño dice que en internet todos los carritos se abandonan, que es normal. —No es normal. Es que a mí me recuperaron y a ti no. —¿Y eso cómo se hace? —Con herramientas. Y con gente que ya sabe cuáles. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas, las pasarelas y las agencias que recuperan carritos como tú, con stand, para preguntarles de frente. —¿Y si mi dueño no va? —Entonces mañana estamos los dos aquí. Y pasado también. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | —¿Y tú por qué estás lleno ahí parado? | — | Carrito lleno, quieto en mitad del pasillo. Entra la voz del otro desde fuera de cuadro. | Empezar por el que pregunta sin mostrarlo: se gana un plano. |
| 2 | —Me llenaron hace tres horas y se fueron. | Tres horas ahí | Primer plano del carrito lleno, hombros caídos, productos asomando. | Su lado del cuadro es el izquierdo. No se mueve en todo el video. |
| 3 | —A mí también me llenaron hace tres horas. Yo ya pasé. | Ya pasó | Contra: el segundo carrito, del lado derecho, junto a la caja, ligero. | El corte de lado a lado es el latido del formato. |
| 4 | —¿Y cómo pasaste? —Alguien se dio cuenta de que yo estaba aquí y me fue a buscar. | Alguien lo fue a buscar | Punch al carrito ligero; detrás, la línea blanca del piso llega hasta él. | La línea del piso aparece por primera vez. Que se note. |
| 5 | —A mí nadie me busca. | — | Carrito lleno; la línea blanca pasa a su lado y él está fuera de ella. | Composición, no diálogo: él está al lado del camino, no en el camino. |
| 6 | —Mi dueño dice que en internet todos los carritos se abandonan, que es normal. | «Es normal» | Plano abierto del pasillo: diez carritos llenos y quietos, todos fuera de la línea. | El plano ancho del problema. Solo uno en todo el video. |
| 7 | —No es normal. Es que a mí me recuperaron y a ti no. | No es normal | Punch al carrito ligero, de frente, firme. | Es la causa raíz y la dice el otro, no el protagonista. Eso es lo que la hace pasar. |
| 8 | —¿Y eso cómo se hace? —Con herramientas. Y con gente que ya sabe cuáles. | — | Los dos carritos en el mismo cuadro por primera vez, uno a cada lado. | Primer plano compartido del video. Guardarlo hasta aquí. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas, las pasarelas y las agencias que recuperan carritos como tú, con stand, para preguntarles de frente. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco, negro y gris: stands corporativos, paneles retroiluminados, pasillos alfombrados. Los dos carritos entran juntos. | La línea blanca del piso ahora es el pasillo del recinto. Mismo hilo visual. |
| 10 | —¿Y si mi dueño no va? —Entonces mañana estamos los dos aquí. Y pasado también. | Mañana seguimos aquí | Vuelta al pasillo de la tienda: los dos carritos llenos y quietos. | Cierre en frío. La amenaza es no ir, y se ve, no se dice. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** el guion tiene dos escenarios y dos personajes, pero **son dos clips base**: uno del carrito lleno y otro del ligero, ambos largos, más el del recinto. Todo el ping-pong sale de reencuadrar esos dos. Si generan un clip por réplica se van a los diez dólares y no hace falta.

---

## 09 · Creadores de contenido e influencers que venden 🔥
**Ángulo 9.2 — Monetizar seguidores** · E2 Diálogo · ~38 s · 142 palabras

**Objetos protagonistas:** el contador de seguidores —orgulloso, redondito, sube todos los días— y la alcancía, que lleva meses igual de liviana. El equipo decide el diseño.
**Escenario:** escritorio de creador: aro de luz apagado, trípode, celular en vertical.
**Hilo visual:** el contador sube un número cada vez que aparece; la alcancía suena igual de hueca cada vez que se mueve.

**Locución corrida:**

> —Subimos otra vez. Ya somos el doble del año pasado. —Yo sigo pesando lo mismo que el año pasado. —¿Y eso? Si nos escriben marcas todos los días. —Te escriben a ti. A mí me mandan canje. —Nuestro dueño dice que primero hay que crecer más, y después sí monetizar. —Hay alcancías más llenas que yo con la mitad de tus números. —¿Cómo hacen? —Venden algo. Producto propio, afiliados, contenido para marcas. Alguien les mostró qué se vende con una audiencia como la nuestra. —Entonces no nos faltan seguidores. —Nunca nos faltaron. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las marcas que buscan creadores, las plataformas de afiliados y los creadores que ya viven de esto, todos en el mismo sitio. —¿Y yo qué hago? —Tú sigue subiendo. Yo espero. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | —Subimos otra vez. Ya somos el doble del año pasado. | — | El contador en el lado izquierdo, girando cifras hacia arriba, feliz. | Energía alta desde el primer frame. El contraste llega en dos segundos. |
| 2 | —Yo sigo pesando lo mismo que el año pasado. | — | Contra: la alcancía, lado derecho, se inclina y suena hueca. | El sonido de hueco es el gancho real. Que se oiga limpio, sin música encima. |
| 3 | —¿Y eso? Si nos escriben marcas todos los días. | — | Punch al contador, desconcertado. | — |
| 4 | —Te escriben a ti. A mí me mandan canje. | Canje | Cajas de producto se apilan junto a la alcancía, tapándola. | El canje es visual: producto que se acumula y no cabe. |
| 5 | —Nuestro dueño dice que primero hay que crecer más, y después sí monetizar. | «Primero crecer» | Los dos en cuadro, el contador arriba, la alcancía abajo, hundida entre cajas. | Primer plano compartido. Composición vertical: arriba el número, abajo la plata. |
| 6 | —Hay alcancías más llenas que yo con la mitad de tus números. | Menos números, más llenas | Otro escritorio: contador pequeño, alcancía pesada que apenas se puede mover. | Cambio de mundo con corte seco. Mismo encuadre, otros objetos. |
| 7 | —¿Cómo hacen? —Venden algo. Producto propio, afiliados, contenido para marcas. Alguien les mostró qué se vende con una audiencia como la nuestra. | Alguien les mostró | Tres tarjetas se apoyan contra la alcancía llena, una por cada cosa. | Tres cortes de un mismo clip. No generen tres. |
| 8 | —Entonces no nos faltan seguidores. —Nunca nos faltaron. | No faltan seguidores | Vuelta al escritorio original, los dos de frente. | La causa raíz la dice la alcancía. El que sufre no diagnostica. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las marcas que buscan creadores, las plataformas de afiliados y los creadores que ya viven de esto, todos en el mismo sitio. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco y negro: stands corporativos, paneles retroiluminados, pasillos alfombrados. Contador y alcancía entran por el pasillo. | — |
| 10 | —¿Y yo qué hago? —Tú sigue subiendo. Yo espero. | Sigue subiendo | La alcancía, quieta, con la ranura de frente a cámara. | Remate seco y con humor. Sin música de cierre triunfal. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** el sonido hueco de la alcancía es el mejor activo de este video y **no lo va a dar el modelo**: pídanlo en el prompt como textura (`hollow ceramic thud, small room`) y refuércenlo en montaje. Y cierren el prompt de audio con `no discernible speech`, como en todos.

---

## 16 · Marketplaces 🔥
**Ángulo 16.2 — Aumentar ventas** · E2 Diálogo · ~37 s · 135 palabras

**Objetos protagonistas:** un estante casi vacío, con tres productos solitarios y mucha gente pasando · y un estante de otro marketplace, lleno hasta arriba. El equipo decide el diseño.
**Escenario:** un marketplace imaginado como una galería de estantes flotantes, con compradores representados como carritos que pasan de largo.
**Hilo visual:** los carritos que cruzan el cuadro sin parar. Son los compradores, y sobran.

**Locución corrida:**

> —Oye. ¿Tú por qué estás tan lleno? —Porque a mí me llegaron vendedores nuevos. —A mí me pasan compradores todo el día y no tengo qué ponerles. —¿Y no los buscas? —Pagamos pauta para atraer vendedores. Llegan de a uno, y con poco catálogo. —A los buenos no los traes con un anuncio. —Es que los buenos ya están en los marketplaces grandes. —Los buenos abren donde alguien los convence de frente. Nosotros fuimos a buscarlos. —¿A dónde? —Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de marcas, fabricantes y tiendas buscando dónde vender. Tres días de estar ahí y me llenaron. —¿Y si no vamos? —Entonces el año entrante seguimos igual: tú vacío, y ellos pasando. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | —Oye. ¿Tú por qué estás tan lleno? | — | Estante vacío en primer plano, izquierda; carritos cruzando el cuadro detrás, borrosos. | El movimiento de fondo desde el primer frame: hay demanda, sobra. |
| 2 | —Porque a mí me llegaron vendedores nuevos. | — | Contra: estante lleno, derecha, productos hasta arriba. | — |
| 3 | —A mí me pasan compradores todo el día y no tengo qué ponerles. | Compradores sí. Producto no. | Punch al estante vacío: tres productos separados en una repisa larga. | El vacío entre productos es la imagen del guion. Que sobre espacio. |
| 4 | —¿Y no los buscas? —Pagamos pauta para atraer vendedores. Llegan de a uno, y con poco catálogo. | Llegan de a uno | Un producto solitario aterriza en la repisa. Silencio. Otro, mucho después. | Dos aterrizajes con un hueco de tiempo entre ellos. El hueco es el chiste. |
| 5 | —A los buenos no los traes con un anuncio. | — | Estante lleno, de frente, tranquilo. | — |
| 6 | —Es que los buenos ya están en los marketplaces grandes. | «Ya están en los grandes» | Estante vacío mirando hacia arriba, a una silueta de estante gigante en gris. | La sombra del grande, nunca su marca. Sin letras. |
| 7 | —Los buenos abren donde alguien los convence de frente. Nosotros fuimos a buscarlos. | Los convencieron de frente | Punch al estante lleno; sus productos se acomodan solos, orgullosos. | La causa raíz la trae el que ya cambió. |
| 8 | —¿A dónde? —Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de marcas, fabricantes y tiendas buscando dónde vender. | 15–19 OCT · +350 EMPRESAS | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | — |
| 9 | Tres días de estar ahí y me llenaron. | Tres días | El estante lleno, en el recinto, recibiendo producto que entra por los lados. | «Tres días» es lo que da el Pasaporte. No prometan más. |
| 10 | —¿Y si no vamos? —Entonces el año entrante seguimos igual: tú vacío, y ellos pasando. | Tú vacío, ellos pasando | Estante vacío, quieto, con carritos cruzando detrás cada vez más rápido. | Acelerar el fondo en el último plano. Nada más cambia. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** los carritos del fondo son el hilo y **van desenfocados siempre**. Si el modelo los pone nítidos, el video se lee como una tienda y no como un marketplace lleno de tráfico. Pidan `shallow depth of field, background carts blurred in motion`.

---

## 22 · Desarrollo, programación e integraciones 🟡
**Ángulo 22.2 — Integraciones** · E2 Diálogo · ~40 s · 148 palabras

**Objetos protagonistas:** una hoja de cálculo agotada, que lleva años copiando pedidos a mano · y un cable de integración, con dos puntas, que no encuentra dónde enchufarse. El equipo decide el diseño.
**Escenario:** un cuarto de servidores pequeño, tibio, con tres máquinas que no se miran entre ellas.
**Hilo visual:** las tres máquinas —plataforma, pasarela, logística— de espaldas unas a otras.

**Locución corrida:**

> —¿Otra vez copiando pedidos? —Doscientos hoy. Uno por uno. —Yo tengo dos puntas y ninguna encaja con estas máquinas. —Es que aquí cada una habla su idioma. —Nuestro dueño dice que en ecommerce cada tienda es un mundo, y que toca hacer todo a la medida. —Pero las plataformas, las pasarelas y las logísticas del ecommerce latino se cuentan con los dedos. Y todas tienen equipo técnico. —¿Y por qué no hablamos con ellos? —Porque nunca les hemos visto la cara. —Ahí está. No nos falta código. Nos falta conocer a los que están del otro lado. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están con stand las plataformas, las pasarelas, las logísticas y sus equipos técnicos, y las tiendas que necesitan que alguien las conecte. —Entonces guarda la hoja. —Guárdala tú. Yo llevo años esperando esto. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | —¿Otra vez copiando pedidos? | — | La hoja de cálculo, izquierda, con celdas que se llenan solas, fila tras fila. | Las celdas se llenan solas. **Sin manos.** |
| 2 | —Doscientos hoy. Uno por uno. | Uno por uno | Punch a la hoja: las filas ya no caben y se desbordan por el borde inferior. | — |
| 3 | —Yo tengo dos puntas y ninguna encaja con estas máquinas. | — | Contra: el cable, derecha, con las dos puntas levantadas, buscando. | El cable busca girando sobre sí mismo, sin tocar nada. |
| 4 | —Es que aquí cada una habla su idioma. | — | Plano abierto: tres máquinas de espaldas unas a otras, cada una con su luz de otro color. | El único plano ancho. Tres colores distintos que no se mezclan. |
| 5 | —Nuestro dueño dice que en ecommerce cada tienda es un mundo, y que toca hacer todo a la medida. | «Cada tienda es un mundo» | La hoja, resignada, junto a una pila de hojas idénticas. | — |
| 6 | —Pero las plataformas, las pasarelas y las logísticas del ecommerce latino se cuentan con los dedos. Y todas tienen equipo técnico. | Se cuentan con los dedos | El cable se estira y toca, una por una, tres siluetas de máquina en gris. | El estirón del cable es el movimiento clave. Que llegue lejos. |
| 7 | —¿Y por qué no hablamos con ellos? —Porque nunca les hemos visto la cara. | Nunca les vimos la cara | Las tres máquinas siguen de espaldas. El cable, quieto en el centro. | Beat de silencio visual. Todo quieto medio segundo. |
| 8 | —Ahí está. No nos falta código. Nos falta conocer a los que están del otro lado. | No falta código | Punch al cable, de frente, con las dos puntas encendidas. | Causa raíz. La dice el cable, no la hoja. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están con stand las plataformas, las pasarelas, las logísticas y sus equipos técnicos, y las tiendas que necesitan que alguien las conecte. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco y negro. Las tres máquinas, ahora de frente, alineadas en stands corporativos. | Las máquinas se giran. Es el único cambio y lo dice todo. |
| 10 | —Entonces guarda la hoja. —Guárdala tú. Yo llevo años esperando esto. | Guarda la hoja | La hoja se dobla sola, contenta, y el cable conecta dos puntas por primera vez. | Que la conexión haga un chasquido limpio. Un solo sonido. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** ojo con el cuarto de servidores: si piden `server room` a secas sale frío, azul y con luces parpadeando, y este video no es de terror. Pidan `warm small utility room, soft practical lights, cozy` y **veten** `dark, blue lighting, blinking LEDs, horror`.

---

# E3 · La escalada

*Videos 03, 10, 19 y 25*

Algo crece en cámara —una barra, una pila, un porcentaje, un montón de cuadernos— mientras el resultado se queda exactamente donde estaba. La estructura es **repetición con variación**: la misma frase vuelve tres o cuatro veces con un número distinto, y el espectador se queda esperando el cambio que no llega.

**Cómo se dirige:** el encuadre es casi el mismo en los escalones —misma cámara, mismo eje— para que lo único que cambie sea lo que crece. Eso hace el efecto. **El primer plano que rompe el eje es el de la feria**, y por eso se siente distinto.

**Cuidado con el ritmo:** la repetición aburre si los escalones duran lo mismo. Que cada escalón sea un poco **más corto** que el anterior: acelera solo, y cuando llega el freno se nota.

---

## 03 · Empresarios de e-commerce en crecimiento 🔥
**Ángulo 3.2 — Escalar publicidad** · E3 Escalada · ~42 s · 155 palabras

**Objeto protagonista:** dos barras de un gráfico que viven una al lado de la otra: la del presupuesto, que sube encantada, y la de las ventas, que no se mueve. El equipo decide el diseño.
**Escenario:** un panel de anuncios convertido en habitación: piso de cuadrícula, paredes de gráfico.
**Hilo visual:** la línea de tope, arriba, que la barra de ventas nunca toca.

**Locución corrida:**

> Subes el presupuesto. La barra del gasto sube. La de las ventas se queda. Subes otra vez. El gasto sube. Las ventas se quedan. Subes el doble. El gasto se va al techo. Las ventas se quedan. Y te dices que ya tocaste el techo del mercado. El techo lo tocó tu barra, no el mercado. Hay tiendas de tu mismo tamaño pasando de diez a cien pedidos diarios con la misma plataforma, la misma pauta y el mismo país. No es el mercado. Es que escalar tiene un método, y nadie te lo ha mostrado dentro de tu cuenta. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las agencias y los traffickers que escalan cuentas todos los días, y más de doscientas ponencias donde lo explican con números en pantalla. La próxima vez que subas el presupuesto, que suba también la otra barra. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Subes el presupuesto. La barra del gasto sube. La de las ventas se queda. | — | Las dos barras de frente, mismo eje. La de la izquierda crece un peldaño. | Establecer el eje. No se mueve hasta el plano 8. |
| 2 | Subes otra vez. El gasto sube. Las ventas se quedan. | — | Mismo encuadre. La barra del gasto crece otro peldaño, más rápido. | Mismo plano, otro tamaño. Que el corte sea invisible salvo por la barra. |
| 3 | Subes el doble. El gasto se va al techo. Las ventas se quedan. | El gasto sube. Las ventas no. | La barra del gasto se dispara hasta la línea de tope y se aplasta contra ella. | Tercer escalón más corto que el segundo. Acelerar. |
| 4 | Y te dices que ya tocaste el techo del mercado. | «Ya tocamos el techo» | La barra del gasto, apretada contra el techo, mira hacia abajo a la otra. | El único momento en que las dos barras se miran. |
| 5 | El techo lo tocó tu barra, no el mercado. | El techo es tuyo | Punch a la línea de tope: no es un techo, es una línea pintada en el aire. | Que se vea que la línea no sostiene nada. Es idea, no pared. |
| 6 | Hay tiendas de tu mismo tamaño pasando de diez a cien pedidos diarios con la misma plataforma, la misma pauta y el mismo país. | De diez a cien | Otro panel-habitación: dos barras subiendo juntas, en paralelo. | Primer cambio de mundo. Corte seco, mismo encuadre. |
| 7 | No es el mercado. Es que escalar tiene un método, y nadie te lo ha mostrado dentro de tu cuenta. | Escalar tiene método | Vuelta a las dos barras originales, quietas. | — |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las agencias y los traffickers que escalan cuentas todos los días, y más de doscientas ponencias donde lo explican con números en pantalla. | 15–19 OCT · +200 PONENCIAS | **Se rompe el eje**: cámara lateral, recinto en blanco y negro, stands corporativos, pasillos alfombrados, auditorio al fondo. | Este es el plano que cambia de lenguaje. Que se note el golpe. |
| 9 | La próxima vez que subas el presupuesto, que suba también la otra barra. | Que suban las dos | Las dos barras, ahora en gris, subiendo juntas y saliendo por arriba del cuadro. | Salen del cuadro. No hay techo. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** las barras son geometría pura y ahí el modelo se pone perezoso. Denles material y peso —caucho, plástico inflado, madera pintada— y una física clara: la que sube rebota al llegar arriba, la que no se mueve tiembla un poco cuando la otra crece. **Sin material, esto sale como una infografía y no como Pixar.**

---

## 10 · Consultores y profesionales independientes de e-commerce 🔥
**Ángulo 10.2 — Demostrar experiencia** · E3 Escalada · ~40 s · 149 palabras

**Objeto protagonista:** una pila de carpetas de casos resueltos, que crece cada año y que nadie ha abierto nunca. El equipo decide el diseño.
**Escenario:** oficina pequeña de consultor, una silla vacía al frente del escritorio.
**Hilo visual:** la silla del cliente, siempre vacía, hasta el final.

**Locución corrida:**

> Primer año: una carpeta. Un cliente que resolviste bien. Tercer año: cinco carpetas. Ninguna la ha abierto nadie. Quinto año: doce carpetas. La silla del frente sigue vacía la mitad de la semana. Octavo año: la pila no cabe en el escritorio, y la llamada termina otra vez en «lo voy a pensar». Te dices que la experiencia se demuestra trabajando. Pero los consultores que sí cierran la demuestran antes de que los contraten: en un escenario, en un caso público, en alguien que los recomienda de frente. No te falta experiencia. Te falta un lugar donde la gente del sector te vea demostrarla. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes y más de trescientas cincuenta empresas que necesitan quién les resuelva esto. Tres días para que dejen de tener que creerte. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Primer año: una carpeta. Un cliente que resolviste bien. | Año uno | Una carpeta sola en el escritorio, cerrada, orgullosa. Silla vacía detrás, desenfocada. | La silla vacía entra desde el primer plano, sin señalarla. |
| 2 | Tercer año: cinco carpetas. Ninguna la ha abierto nadie. | Año tres | Mismo encuadre: cinco carpetas apiladas, todas cerradas. | Mismo eje. Solo cambia la pila. |
| 3 | Quinto año: doce carpetas. La silla del frente sigue vacía la mitad de la semana. | Año cinco | Mismo encuadre, pila más alta. La silla ahora enfocada, vacía. | El foco pasa de la pila a la silla sin cortar. |
| 4 | Octavo año: la pila no cabe en el escritorio, y la llamada termina otra vez en «lo voy a pensar». | «Lo voy a pensar» | La pila se inclina, pasa del borde del escritorio y queda a punto de caer. | Escalón más corto. El desequilibrio es el clímax del problema. |
| 5 | Te dices que la experiencia se demuestra trabajando. | — | Punch a la carpeta de arriba: cerrada, con polvo en el canto. | El polvo cuenta que nadie la abrió. |
| 6 | Pero los consultores que sí cierran la demuestran antes de que los contraten: en un escenario, en un caso público, en alguien que los recomienda de frente. | La demuestran antes | Otra oficina: una sola carpeta, abierta, con las hojas de pie como si hablaran. | La carpeta abierta contra ocho años de carpetas cerradas. |
| 7 | No te falta experiencia. Te falta un lugar donde la gente del sector te vea demostrarla. | No te falta experiencia | Vuelta a la pila, quieta, y la silla vacía al lado. | — |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes y más de trescientas cincuenta empresas que necesitan quién les resuelva esto. | 15–19 OCT · +60.000 ASISTENTES | Se rompe el eje: recinto en blanco y negro, pasillos alfombrados, stands corporativos, sillas ocupadas hasta el fondo. | El contraplano de la silla vacía son sillas llenas. Ahí está el remate. |
| 9 | Tres días para que dejen de tener que creerte. | Tres días | La pila de carpetas, abierta y desplegada como un abanico, sobre una mesa del recinto. | «Tres días» es el Pasaporte. No prometan más. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este guion vive de que la pila crezca **en el mismo sitio exacto**. Generen un solo clip base de la oficina y editen la pila por escena desde la hoja de personaje, no desde el clip anterior: si encadenan clip con clip, el escritorio se les mueve y se pierde el efecto.

---

## 19 · Retail 🟡
**Ángulo 19.2 — E-commerce** · E3 Escalada · ~38 s · 140 palabras

**Objeto protagonista:** una porción de gráfico circular —la tajada del canal online— pequeña, seria, que lleva dos años sin crecer. El equipo decide el diseño.
**Escenario:** sala de junta convertida en mundo: mesa larga, pantalla de presentación, sillas grandes.
**Hilo visual:** la misma diapositiva de resultados, trimestre tras trimestre, con la misma tajada.

**Locución corrida:**

> Primer trimestre: el canal online es el cinco por ciento. Segundo trimestre: cinco por ciento. Tercero: cinco por ciento. Dos años después: cinco por ciento. Tienes tiendas, tienes marca, tienes inventario, tienes equipo. Y esa tajada no se mueve. Te dices que tu cliente prefiere ir a la tienda. Ese mismo cliente le compra por internet a otra marca esta misma semana. Solo que no a ti. No es tu cliente. Es que el ecommerce se opera distinto, y tu equipo no ha visto de cerca a los que lo hacen bien. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas, la logística, las agencias y más de doscientas ponencias de marcas y retailers que ya movieron esa tajada. Lleva al equipo. Que la próxima diapositiva sea distinta. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Primer trimestre: el canal online es el cinco por ciento. | Trimestre uno | La tajada pequeña, en el centro de la pantalla de la sala de junta. | Establecer el encuadre. Frontal, simétrico. |
| 2 | Segundo trimestre: cinco por ciento. | Trimestre dos | Mismo encuadre, misma tajada, otra luz de sala. | Solo cambia la hora del día por la ventana. |
| 3 | Tercero: cinco por ciento. | Trimestre tres | Mismo encuadre, misma tajada. La tajada mira a cámara. | Que mire a cámara solo aquí. Es el guiño al espectador. |
| 4 | Dos años después: cinco por ciento. | Dos años | Mismo encuadre. Ahora la sala tiene sillas nuevas y la tajada es idéntica. | Cambiar el mundo alrededor y no el dato. Ese es el chiste. |
| 5 | Tienes tiendas, tienes marca, tienes inventario, tienes equipo. Y esa tajada no se mueve. | Todo lo tienes | Cuatro objetos entran al cuadro y se alinean alrededor de la tajada. | Cuatro cortes rápidos de un mismo clip. |
| 6 | Te dices que tu cliente prefiere ir a la tienda. | «Prefiere la tienda» | La tajada mira hacia una puerta de local iluminada. | — |
| 7 | Ese mismo cliente le compra por internet a otra marca esta misma semana. Solo que no a ti. | Le compra a otros | Un carrito de compras cruza el cuadro por detrás y sale por el otro lado, sin parar. | El carrito que pasa de largo. Un solo paso, sin volver. |
| 8 | No es tu cliente. Es que el ecommerce se opera distinto, y tu equipo no ha visto de cerca a los que lo hacen bien. | Se opera distinto | Punch a la tajada, sola, en la pantalla apagada. | — |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas, la logística, las agencias y más de doscientas ponencias de marcas y retailers que ya movieron esa tajada. | 15–19 OCT · +200 PONENCIAS | Se rompe el eje: recinto en blanco y negro, auditorio lleno, stands corporativos, pasillos alfombrados. | — |
| 10 | Lleva al equipo. Que la próxima diapositiva sea distinta. | Lleva al equipo | La tajada, ahora grande, ocupando media pantalla de la sala de junta. | El cambio de tamaño es el final. Sin animación de celebración. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** es el único guion del lote dirigido a alguien que decide en comité, y por eso el CTA es «lleva al equipo». Si van a pautarlo, apunten a cargos, no a emprendedores: el mensaje solo funciona si quien lo ve puede comprar más de una entrada.

---

## 25 · Educación y formación en e-commerce 🟡
**Ángulo 25.2 — Emprender** · E3 Escalada · ~40 s · 149 palabras

**Objeto protagonista:** una libreta de ideas de negocio. Entusiasta, se llena rápido, y nunca la abren dos veces. El equipo decide el diseño.
**Escenario:** cuarto de alguien que estudia o trabaja y quiere emprender: cama, escritorio, celular en soporte reproduciendo videos.
**Hilo visual:** la pila de libretas iguales que crece en el rincón.

**Locución corrida:**

> Video uno: una idea. La escribes en la primera hoja. Video doce: otra idea. La anterior se quedó en la hoja de atrás. Video cincuenta: idea nueva, libreta nueva. La de antes ya está en el rincón. Un año de videos, y ni un producto vendido. Te dices que te falta un curso más, el que sí te explique todo. Los que ya emprendieron no aprendieron en un curso más. Aprendieron viendo el negocio real funcionando y hablando con el que lo opera. No te falta información. Te sobra, y sin nadie que te la ordene. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas del ecommerce con sus dueños en el stand, y más de doscientas ponencias de gente que ya tiene resultados. Tres días viendo cómo funciona por dentro. Deja la libreta. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Video uno: una idea. La escribes en la primera hoja. | Video uno | La libreta abierta en la primera hoja, sobre la cama, luz de celular. | La luz del celular es la única fuente. Azulada, de noche. |
| 2 | Video doce: otra idea. La anterior se quedó en la hoja de atrás. | Video doce | Mismo encuadre: la libreta pasa página sola, la anterior queda debajo. | Mismo eje. Solo cambia la página. |
| 3 | Video cincuenta: idea nueva, libreta nueva. La de antes ya está en el rincón. | Video cincuenta | Mismo encuadre. Al fondo, en el rincón, tres libretas apiladas. | Aquí aparece el hilo visual. No lo señalen: que se vea de reojo. |
| 4 | Un año de videos, y ni un producto vendido. | Un año | La pila del rincón, ahora de doce libretas, apoyada en la pared. | Escalón corto. Solo la pila. |
| 5 | Te dices que te falta un curso más, el que sí te explique todo. | «Un curso más» | La libreta abierta, esperando, con la hoja en blanco. | La hoja en blanco es el símbolo. Que dure. |
| 6 | Los que ya emprendieron no aprendieron en un curso más. Aprendieron viendo el negocio real funcionando y hablando con el que lo opera. | Vieron el negocio real | Otro cuarto: una sola libreta, muy usada, abierta junto a una caja de producto con guía de envío. | La caja con guía es la prueba de que ahí sí se vendió. |
| 7 | No te falta información. Te sobra, y sin nadie que te la ordene. | Te sobra información | Vuelta a la pila del rincón, que se tambalea. | — |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas del ecommerce con sus dueños en el stand, y más de doscientas ponencias de gente que ya tiene resultados. | 15–19 OCT · +350 EMPRESAS | Se rompe el eje: recinto en blanco y negro, stands corporativos, paneles retroiluminados, pasillos alfombrados. | — |
| 9 | Tres días viendo cómo funciona por dentro. Deja la libreta. | Deja la libreta | La libreta, cerrada, apoyada contra la pared del recinto, tranquila. | «Tres días» es el Pasaporte. Cerrar la libreta, no botarla. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este es el guion del lote con el público más frío en intención de compra, y **no puede sonar a regaño**. La libreta es simpática, no patética: se emociona con cada idea. Si el personaje da lástima, el video no vende entradas — culpa a quien lo ve.

---

# E4 · Mundo espejo

*Videos 04, 11, 18 y 26*

La misma escena, dos veces: como está y como podría estar. **El corte entre las dos ES el argumento** — no hay que explicarlo, se ve. Nadie dialoga: la locución va en off, en tercera persona, y describe los dos mundos con la misma frialdad.

**Cómo se dirige:** los dos mundos comparten encuadre, hora y composición, y se diferencian por **una sola variable** (una luz encendida, un objeto de más, un color). Cuanto más iguales sean, más fuerte pega el corte. El mundo A tiene color; el mundo B empieza con color y **termina en el blanco y negro del recinto**, que es de donde salió.

**Un truco que ahorra plata:** el mundo B se genera editando la imagen del mundo A, no desde cero. Misma habitación, misma cámara, un elemento distinto. Sale más barato y queda más parecido.

---

## 04 · Vendedores de redes sociales 🔥
**Ángulo 4.2 — Responder manualmente** · E4 Espejo · ~40 s · 148 palabras

**Objeto protagonista:** un celular con la bandeja de mensajes desbordada. En el mundo B, el mismo celular, tranquilo. El equipo decide el diseño.
**Escenario:** dos cocinas idénticas a las once de la noche, luz de nevera y de pantalla.
**Hilo visual:** el contador de mensajes sin leer. En A crece; en B se queda quieto.

**Locución corrida:**

> Once de la noche. En esta cocina, un celular lleva cuatro horas contestando lo mismo: precio, envío, disponibilidad. Once de la noche. En esta otra cocina, el mismo celular ya contestó eso hace horas, solo. En la primera, cada mensaje respondido destapa dos nuevos. En la segunda, los tres que quedan son los que van a comprar. En la primera, el dueño dice que la atención personal es lo que lo diferencia. En la segunda también atienden personal. Solo que no a mano. No te falta atención. Te falta automatizar lo repetido para poder atender lo que cierra. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las herramientas de automatización de WhatsApp y las tiendas que ya las usan, con stand y demostración en vivo. Las dos cocinas son iguales. Lo que cambia está en el celular. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Once de la noche. En esta cocina, un celular lleva cuatro horas contestando lo mismo: precio, envío, disponibilidad. | 11:00 p. m. | Mundo A: celular en la mesa de la cocina, notificaciones apiladas encima como platos sucios. | Las notificaciones son objetos físicos que se acumulan. Ese es todo el diseño. |
| 2 | Once de la noche. En esta otra cocina, el mismo celular ya contestó eso hace horas, solo. | 11:00 p. m. | Mundo B: **encuadre idéntico**, misma mesa, mismo celular, mesa despejada. | Idéntico de verdad: misma cámara, misma luz, mismo ángulo. Solo cambia la mesa. |
| 3 | En la primera, cada mensaje respondido destapa dos nuevos. | Uno cae, entran dos | Mundo A: una notificación se apaga y caen dos encima. | El gag mecánico del video. Uno, dos. Sin exagerar. |
| 4 | En la segunda, los tres que quedan son los que van a comprar. | Quedan tres | Mundo B: tres notificaciones separadas, ordenadas, con un brillo suave. | Tres, con aire entre ellas. El vacío es la riqueza. |
| 5 | En la primera, el dueño dice que la atención personal es lo que lo diferencia. | «Atención personal» | Mundo A: la pila de notificaciones tapa el celular por completo. | El personaje desaparece bajo su propio trabajo. |
| 6 | En la segunda también atienden personal. Solo que no a mano. | No a mano | Mundo B: el celular, de frente, con una sola conversación abierta y activa. | — |
| 7 | No te falta atención. Te falta automatizar lo repetido para poder atender lo que cierra. | No te falta atención | **Único plano partido del video**: la cocina A arriba, la cocina B abajo, misma composición. | Partición horizontal, no vertical: en nueve dieciséis es lo que se lee. Un solo plano así. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las herramientas de automatización de WhatsApp y las tiendas que ya las usan, con stand y demostración en vivo. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco y negro: stands corporativos, paneles retroiluminados, pasillos alfombrados. | De aquí sale el mundo B. Que se entienda sin decirlo. |
| 9 | Las dos cocinas son iguales. Lo que cambia está en el celular. | Las cocinas son iguales | Mundo B otra vez, la cocina en calma, la luz de la nevera apagándose. | Cierre tranquilo. Que dé ganas de ese silencio. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** generen **una sola** cocina y editen desde ahí las dos versiones. Si generan dos cocinas distintas, el espejo se rompe y el video se vuelve una comparación cualquiera. La regla es: misma imagen base, una variable cambiada.

---

## 11 · Tecnología y soluciones para e-commerce 🔥
**Ángulo 11.2 — Inteligencia artificial** · E4 Espejo · ~45 s · 167 palabras

**Objeto protagonista:** una demo —una ventana de software con cara— que se explica perfecto y nadie entiende. El equipo decide el diseño.
**Escenario:** mundo A, una videollamada: la demo hablándole a una pantalla. Mundo B, un stand de feria: la demo funcionando sobre el caso de una tienda que está ahí.
**Hilo visual:** la ventana de la demo, idéntica en los dos mundos. Lo que cambia es lo que tiene al frente.

**Locución corrida:**

> Mundo uno: la demo se explica sola frente a una pantalla. Dice todo bien. Al otro lado contestan que está muy bueno, y no vuelven a escribir. Mundo dos: la misma demo, funcionando encima de los datos de una tienda que está ahí parada, mirando. Mundo uno: la tienda entiende que el producto sirve. Mundo dos: la tienda entiende que le sirve a ella. En el primero se dice que el mercado todavía no está listo para la inteligencia artificial. En el segundo las tiendas ya están comprando. Le compran a quien se las muestra funcionando en su propio negocio. No te falta producto. Te falta estar donde la tienda te ve resolverle su caso, en vivo. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes del ecommerce buscando herramientas, y un stand donde tu demo se hace con el cliente al frente. Es la misma demo. Cambia quién la está viendo. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Mundo uno: la demo se explica sola frente a una pantalla. Dice todo bien. | — | Mundo A: la ventana-demo, sola, frente a una pantalla apagada con un punto de cámara. | La pantalla apagada con la lucecita: eso es una videollamada sin nadie. |
| 2 | Al otro lado contestan que está muy bueno, y no vuelven a escribir. | «Está muy bueno» | Mundo A: la demo se queda quieta esperando. La lucecita se apaga. | El apagado de la lucecita es el corte emocional. |
| 3 | Mundo dos: la misma demo, funcionando encima de los datos de una tienda que está ahí parada, mirando. | — | Mundo B: la misma ventana-demo, mismo tamaño, con una tienda-personaje al lado, atenta. | Misma ventana, mismo encuadre. Solo cambia quién está al lado. |
| 4 | Mundo uno: la tienda entiende que el producto sirve. | Sirve | Mundo A: una tienda-personaje pequeñita al otro lado del cristal de la pantalla, borrosa. | Detrás del cristal: presente pero inalcanzable. |
| 5 | Mundo dos: la tienda entiende que le sirve a ella. | Le sirve a ella | Mundo B: la tienda-personaje se acerca a la ventana y su reflejo aparece dentro. | El reflejo dentro de la demo es la imagen clave del video. |
| 6 | En el primero se dice que el mercado todavía no está listo para la inteligencia artificial. | «No está listo» | Mundo A: la demo apagada sobre un escritorio vacío. | — |
| 7 | En el segundo las tiendas ya están comprando. Le compran a quien se las muestra funcionando en su propio negocio. | Ya están comprando | Mundo B: tres tiendas-personaje haciendo fila junto a la demo. | Fila corta y ordenada. Tres, no una multitud. |
| 8 | No te falta producto. Te falta estar donde la tienda te ve resolverle su caso, en vivo. | No te falta producto | Los dos mundos en un plano partido horizontal: arriba la pantalla apagada, abajo la fila. | Único plano partido. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes del ecommerce buscando herramientas, y un stand donde tu demo se hace con el cliente al frente. | 15–19 OCT · +60.000 ASISTENTES | Recinto en blanco y negro: stands corporativos, paneles retroiluminados, pasillos alfombrados llenos. | — |
| 10 | Es la misma demo. Cambia quién la está viendo. | Es la misma demo | Punch a la ventana-demo, encendida, con varios reflejos encima. | Cerrar en el objeto, no en el recinto. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** una ventana de software es un rectángulo, o sea el personaje más difícil del lote después del número del ocho. Denle marco físico —vidrio, borde de metal, un pie— y que su expresión viva en cómo se inclina. **Y nada de texto dentro de la ventana:** lo que se ve adentro son formas geométricas abstractas, o el modelo inventa letras.

---

## 18 · Comerciantes y negocios físicos que quieren vender online 🟡
**Ángulo 18.2 — Crear primera tienda online** · E4 Espejo · ~45 s · 167 palabras

**Objeto protagonista:** una vitrina de local, con toldo y puerta de vidrio. En el mundo B, la misma vitrina con una segunda puerta que da a otra parte. El equipo decide el diseño.
**Escenario:** una calle comercial bajo la lluvia, sábado.
**Hilo visual:** el agua que corre por el andén. En A es todo lo que pasa; en B pasa igual y no importa.

**Locución corrida:**

> Sábado, tres de la tarde. Llueve. En este local no ha entrado nadie en todo el día. Sábado, tres de la tarde. Llueve igual. En el local de al lado están empacando pedidos para otra ciudad. En el primero, el mes depende del clima y del andén. En el segundo, el andén es solo la mitad del negocio. En el primero, la dueña le manda la foto por WhatsApp a las mismas clientas de siempre, y ya sabe cuáles contestan. En el segundo, la misma foto la ve gente que nunca pasó por esa calle. Y dice que lo suyo se vende viéndolo, tocándolo. Eso también lo decía la de al lado. No es que tu producto no sirva para internet. Es que nadie te ha mostrado cómo montar la primera tienda. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas, las pasarelas, la logística y comerciantes que arrancaron desde un local como el tuyo. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Sábado, tres de la tarde. Llueve. En este local no ha entrado nadie en todo el día. | Sábado, 3 p. m. | Mundo A: la vitrina desde la calle, lluvia en el vidrio, luz encendida adentro. | La lluvia va en el vidrio, no delante de la cámara. Se lee mejor. |
| 2 | Sábado, tres de la tarde. Llueve igual. En el local de al lado están empacando pedidos para otra ciudad. | Sábado, 3 p. m. | Mundo B: **misma calle, misma lluvia**, la vitrina de al lado con cajas saliendo por una puerta lateral. | Idéntico encuadre, movido un local. Que se entienda que es la misma calle. |
| 3 | En el primero, el mes depende del clima y del andén. | Depende del clima | Mundo A: el toldo goteando sobre el andén vacío. | Plano de detalle. Un solo objeto: el gotero. |
| 4 | En el segundo, el andén es solo la mitad del negocio. | La mitad | Mundo B: la puerta lateral abierta; por ella salen cajas y entra luz. | La segunda puerta es todo el argumento visual. |
| 5 | En el primero, la dueña le manda la foto por WhatsApp a las mismas clientas de siempre, y ya sabe cuáles contestan. | Las de siempre | Mundo A: un celular en el mostrador, con cinco conversaciones y nada más. | Cinco. Que se puedan contar de un vistazo. |
| 6 | En el segundo, la misma foto la ve gente que nunca pasó por esa calle. | Gente de otra ciudad | Mundo B: el mismo celular, con la foto multiplicándose y saliendo del cuadro. | La misma foto: no cambien el producto. Cambia el alcance. |
| 7 | Y dice que lo suyo se vende viéndolo, tocándolo. Eso también lo decía la de al lado. | «Se vende viéndolo» | Plano partido horizontal: arriba la vitrina A, abajo la vitrina B, misma lluvia. | Único plano partido del video. |
| 8 | No es que tu producto no sirva para internet. Es que nadie te ha mostrado cómo montar la primera tienda. | Nadie te ha mostrado | Mundo A: la vitrina, de frente, con la puerta cerrada. | — |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas, las pasarelas, la logística y comerciantes que arrancaron desde un local como el tuyo. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. Sin lluvia. | Que se note que aquí adentro no llueve. Es el premio. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este público es el más sensible del lote a que lo traten de atrasado. La vitrina A no es tonta ni vieja: es **bonita, cuidada y con producto bueno**. Si la dibujan destartalada, el video insulta a quien lo está viendo. La diferencia es la segunda puerta, nada más.

---

## 26 · Ejecutivos y líderes de transformación empresarial 🟡
**Ángulo 26.2 — IA en la empresa** · E4 Espejo · ~41 s · 152 palabras

**Objeto protagonista:** una diapositiva de presentación titulada «Inteligencia artificial», impecable, que lleva seis meses sin salir de la sala. En el mundo B, en su lugar, un proceso pequeño que sí está andando. El equipo decide el diseño.
**Escenario:** sala de junta corporativa, mesa larga, pantalla grande.
**Hilo visual:** el reloj de pared de la sala. Es el mismo en los dos mundos.

**Locución corrida:**

> Empresa uno: la junta aprueba implementar inteligencia artificial este año. Empresa dos: la junta aprueba lo mismo, el mismo día. Seis meses después. Empresa uno: hay una presentación muy buena y ningún proceso cambiado. Empresa dos: hay un proceso pequeño andando, y nadie hizo presentación. En la primera dicen que primero hay que ordenar los datos, y después sí. En la segunda empezaron por lo más aburrido que tenían, y funcionó. Ahí está la diferencia: una arrancó por la diapositiva y la otra por el proceso. No te falta estrategia. Te faltan casos reales de empresas como la tuya, contados por quien los implementó. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de doscientas ponencias de empresas que ya aplican inteligencia artificial en ventas, atención y operación, y los proveedores que se lo montaron. Las dos juntas aprobaron lo mismo. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Empresa uno: la junta aprueba implementar inteligencia artificial este año. | — | Mundo A: la diapositiva en la pantalla de la sala, nueva, brillante, sola. | Sin gente. Las sillas grandes y vacías cuentan la empresa. |
| 2 | Empresa dos: la junta aprueba lo mismo, el mismo día. | El mismo día | Mundo B: **encuadre idéntico**, misma sala, misma diapositiva, mismo reloj. | Idéntico. Aquí todavía no hay diferencia y así debe ser. |
| 3 | Seis meses después. | Seis meses | El reloj de pared girando; la sala se oscurece y se vuelve a iluminar. | Beat bisagra, corto y seco. Un solo plano. |
| 4 | Empresa uno: hay una presentación muy buena y ningún proceso cambiado. | Cero procesos | Mundo A: la misma diapositiva, con polvo, y la sala igual de vacía. | El polvo otra vez. Es el marcador de tiempo del lote. |
| 5 | Empresa dos: hay un proceso pequeño andando, y nadie hizo presentación. | Un proceso andando | Mundo B: la pantalla apagada, y en la mesa un engranaje pequeño girando solo. | El engranaje minúsculo contra la pantalla gigante. |
| 6 | En la primera dicen que primero hay que ordenar los datos, y después sí. | «Primero los datos» | Mundo A: cajas de archivo apiladas frente a la pantalla, tapándola. | — |
| 7 | En la segunda empezaron por lo más aburrido que tenían, y funcionó. | Empezaron por lo aburrido | Mundo B: el engranaje mueve otro engranaje, y otro. Tres, no más. | Tres engranajes. Crecimiento honesto, sin fuegos artificiales. |
| 8 | Ahí está la diferencia: una arrancó por la diapositiva y la otra por el proceso. No te falta estrategia. | No falta estrategia | Plano partido horizontal: arriba la diapositiva con polvo, abajo los engranajes girando. | Único plano partido. |
| 9 | Te faltan casos reales de empresas como la tuya, contados por quien los implementó. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de doscientas ponencias de empresas que ya aplican inteligencia artificial en ventas, atención y operación, y los proveedores que se lo montaron. | 15–19 OCT · +200 PONENCIAS | Recinto en blanco y negro: auditorio lleno, tarima, stands corporativos, pasillos alfombrados. | Beat largo. Que el montaje lo parta en tres o cuatro planos. |
| 10 | Las dos juntas aprobaron lo mismo. | Aprobaron lo mismo | La diapositiva del mundo A, sola en la pantalla apagada. | Remate frío. Sin música de cierre. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este es el guion más corporativo del lote y el que más fácil se vuelve aburrido. Compénsenlo en el montaje, no en el guion: cortes cortos, el reloj como puntuación y **el engranaje con sonido propio**. Si lo montan lento porque «es de ejecutivos», se muere.

---

# E5 · Preguntas al espectador

*Videos 05, 12, 20 y 27*

El objeto se gira a cámara y pregunta. Después de cada pregunta hay **silencio de verdad** —el personaje quieto, mirando— para que el espectador conteste en su cabeza. Luego el video confirma lo que ya pensó. Tres preguntas, una respuesta.

**Cómo se dirige:** los silencios son planos, no huecos. Duran entre ocho décimas y un segundo, el personaje **no se mueve** y la música no baja: ese contraste con el corte rápido del resto es lo que los hace incómodos, y ahí está la retención. Si el montaje los recorta, el formato se cae.

**Ojo con el TTS:** el silencio hay que dejarlo en el montaje, no pedírselo a la voz. Graben la locución sin las pausas y sepárenlas al montar; si meten puntos suspensivos en el prompt de voz, la locución sale rara.

---

## 05 · Dropshippers 🔥
**Ángulo 5.2 — Encontrar proveedores confiables** · E5 Preguntas · ~38 s · 142 palabras

**Objeto protagonista:** un chat de proveedor: un globo de mensaje enviado, con la palomita de «entregado» y sin respuesta. El equipo decide el diseño.
**Escenario:** cuarto de trabajo de dropshipper, escritorio con dos pantallas y una campaña corriendo.
**Hilo visual:** el globo del mensaje, cada vez más gris.

**Locución corrida:**

> Pregunta uno: ¿cuántos días llevas esperando que tu proveedor te confirme si hay stock? Le escribiste el martes. Contestó el viernes. Y la campaña ya se cayó. Pregunta dos: ¿cuántas veces has lanzado sin saber si el producto llega como en la foto? Cada lanzamiento con los dedos cruzados no es una estrategia. Es una apuesta. Pregunta tres: ¿cuántos proveedores llevas este año? Si es más de uno, no te tocó uno malo. Es el mismo ciclo. Y el ciclo se repite porque los eliges por foto y por WhatsApp. Nunca le has visto la cara a ninguno. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, los proveedores están con stand y con muestra física, y les preguntas de frente lo que quieras. Última pregunta: ¿qué le vas a preguntar al primero? Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Pregunta uno: ¿cuántos días llevas esperando que tu proveedor te confirme si hay stock? | ¿Cuántos días llevas? | El globo de mensaje, de frente a cámara, solo en la pantalla. | De frente desde el primer frame. Sin preámbulo. |
| 2 | *(silencio, un segundo)* | — | Mismo plano. El globo quieto. Nada se mueve. | **No cortar.** El silencio es el plano. |
| 3 | Le escribiste el martes. Contestó el viernes. Y la campaña ya se cayó. | Martes → viernes | Tres cortes: el globo enviado, el globo gris, una campaña que se apaga al fondo. | Tres planos del mismo clip. Rápido, para que el silencio anterior resalte. |
| 4 | Pregunta dos: ¿cuántas veces has lanzado sin saber si el producto llega como en la foto? | ¿Cuántas veces? | El globo de frente otra vez, junto a una foto de producto flotando. | Volver al eje de la pregunta uno. Es el ancla del formato. |
| 5 | *(silencio, un segundo)* | — | Mismo plano, quieto. | — |
| 6 | Cada lanzamiento con los dedos cruzados no es una estrategia. Es una apuesta. | Es una apuesta | Una moneda cae y gira sobre el escritorio, junto al globo. | La moneda girando sin caer del todo. Ese es el gesto. |
| 7 | Pregunta tres: ¿cuántos proveedores llevas este año? Si es más de uno, no te tocó uno malo. Es el mismo ciclo. | ¿Cuántos van este año? | Cuatro globos de mensaje iguales, en fila, todos grises. | Cuatro, sin decir cuatro. Que el espectador los cuente. |
| 8 | Y el ciclo se repite porque los eliges por foto y por WhatsApp. Nunca le has visto la cara a ninguno. | Nunca les viste la cara | Los cuatro globos se dan vuelta: por detrás no tienen nada. | El reverso vacío es la causa raíz hecha imagen. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, los proveedores están con stand y con muestra física, y les preguntas de frente lo que quieras. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco y negro: stands corporativos, muestras de producto sobre mesas, pasillos alfombrados. | Muestra física en la mesa: es el argumento del nicho. |
| 10 | Última pregunta: ¿qué le vas a preguntar al primero? | ¿Qué le vas a preguntar? | El globo de mensaje, ahora blanco y encendido, de frente. | Cerrar con pregunta abierta. Sin responderla. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** los dos silencios son el formato entero. Si el QA les marca «se siente largo», **no los quiten**: revisen primero que el resto esté cortado cada segundo y medio. Un silencio funciona por contraste; si todo el video respira, no hay silencio, hay lentitud.

---

## 12 · Medios de pago y Fintech 🔥
**Ángulo 12.2 — Carritos abandonados por problemas de pago** · E5 Preguntas · ~37 s · 136 palabras

**Objeto protagonista:** el botón de pagar. Vive en el último paso del checkout y ve pasar a todo el mundo. El equipo decide el diseño.
**Escenario:** el checkout como un pasillo estrecho que termina en una puerta: el botón.
**Hilo visual:** la puerta que se abre a medias y se cierra.

**Locución corrida:**

> Pregunta uno: ¿sabes cuántas tiendas pierden un cliente en el último paso, hoy, mientras ves esto? Muchas. Y casi ninguna sabe que existe otra forma de cobrar. Pregunta dos: ¿cuántas de esas tiendas te van a buscar a ti? Ninguna. Porque las tiendas no buscan pasarela. Se quedan con la primera que instalaron. Pregunta tres: entonces, ¿cuándo cambian? Cuando alguien les muestra otra de frente y les enseña cuánto están perdiendo. No te faltan funcionalidades. Te falta estar delante de miles de tiendas al mismo tiempo. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes y más de trescientas cincuenta empresas del ecommerce, y tres días para mostrar tu checkout en vivo. Última pregunta: ¿cuántos de esos últimos pasos quieres arreglar? Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Pregunta uno: ¿sabes cuántas tiendas pierden un cliente en el último paso, hoy, mientras ves esto? | ¿Cuántas, hoy? | El botón de pagar al final del pasillo, de frente a cámara. | Perspectiva de pasillo, punto de fuga en el botón. |
| 2 | *(silencio, un segundo)* | — | Mismo plano. Un carrito llega, se detiene, se devuelve. | El único movimiento durante el silencio. Fuera de foco. |
| 3 | Muchas. Y casi ninguna sabe que existe otra forma de cobrar. | No saben que hay otra | El botón parpadea; detrás de él se ve una segunda puerta cerrada. | La segunda puerta se planta aquí y se paga en el plano 8. |
| 4 | Pregunta dos: ¿cuántas de esas tiendas te van a buscar a ti? | ¿Cuántas te buscan? | Punch al botón, de frente. | — |
| 5 | *(silencio, un segundo)* | — | Mismo plano, quieto. | — |
| 6 | Ninguna. Porque las tiendas no buscan pasarela. Se quedan con la primera que instalaron. | Se quedan con la primera | Un botón viejo, gastado, atornillado y con óxido en los bordes. | El óxido y los tornillos: lleva años ahí y nadie lo toca. |
| 7 | Pregunta tres: entonces, ¿cuándo cambian? Cuando alguien les muestra otra de frente y les enseña cuánto están perdiendo. | Cuando alguien les muestra | Una tienda-personaje se acerca al botón viejo y mira hacia la segunda puerta. | — |
| 8 | No te faltan funcionalidades. Te falta estar delante de miles de tiendas al mismo tiempo. | Delante de miles | La segunda puerta se abre y la luz llena el pasillo. | El pago de la puerta del plano 3. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes y más de trescientas cincuenta empresas del ecommerce, y tres días para mostrar tu checkout en vivo. | 15–19 OCT · +60.000 ASISTENTES | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. Fila de tiendas-personaje. | «Tres días» es el Pasaporte. No prometan más. |
| 10 | Última pregunta: ¿cuántos de esos últimos pasos quieres arreglar? | ¿Cuántos quieres arreglar? | El botón, encendido, con muchos carritos cruzándolo. | Cerrar con la pregunta y el movimiento resuelto. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** cuidado con el chiste involuntario — el CTA dice «botón» y el personaje **es** un botón. Aprovéchenlo en vez de esquivarlo: que el último plano del personaje y el botón del anuncio rimen visualmente. Pero el botón-personaje **nunca** debe parecer un botón clicable de interfaz: es un objeto físico, con volumen y material.

---

## 20 · Atención al cliente y Customer Experience 🟡
**Ángulo 20.2 — Responder rápido** · E5 Preguntas · ~39 s · 145 palabras

**Objeto protagonista:** un mensaje que quedó en visto. Un globo de conversación pequeño, paciente, que se va enfriando. El equipo decide el diseño.
**Escenario:** una bandeja de entrada imaginada como una sala de espera con sillas.
**Hilo visual:** el vapor del mensaje: cuando llega echa humito; a las dos horas está frío.

**Locución corrida:**

> Pregunta uno: el mensaje que llegó a las diez de la mañana, ¿a qué hora lo contestaste? A las dos de la tarde ya había comprado en otro lado. Pregunta dos: ¿en qué orden contestas? Por orden de llegada. Y el que más plata traía llevaba tres horas enfriándose en la fila. Pregunta tres: ¿qué pensaste que necesitabas? Contratar a otra persona. Hay negocios con el triple de mensajes que responden en segundos con el mismo equipo. No les falta gente. Tienen un sistema que responde lo repetido y les deja a ellos lo que cierra ventas. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas de atención, los chatbots y los equipos que atienden miles de conversaciones al día, con demostración en stand. Última pregunta: ¿cuántos mensajes se te enfriaron esta semana? Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Pregunta uno: el mensaje que llegó a las diez de la mañana, ¿a qué hora lo contestaste? | ¿A qué hora contestaste? | El mensaje sentado en una silla de sala de espera, de frente, echando humito. | La sala de espera con sillas es todo el concepto. Establecerla ya. |
| 2 | *(silencio, un segundo)* | — | Mismo plano. El humito se apaga poco a poco. | Lo único que cambia durante el silencio. |
| 3 | A las dos de la tarde ya había comprado en otro lado. | 2:00 p. m. | La silla vacía. Al fondo, una puerta que se cierra. | El personaje se fue. Corte seco a la silla vacía. |
| 4 | Pregunta dos: ¿en qué orden contestas? | ¿En qué orden? | Fila de mensajes en sillas, todos mirando al frente. | — |
| 5 | *(silencio, un segundo)* | — | Mismo plano, quieto. | — |
| 6 | Por orden de llegada. Y el que más plata traía llevaba tres horas enfriándose en la fila. | Tres horas en la fila | Punch a un mensaje del fondo de la fila: es más grande que los demás y está frío. | El más grande al final de la fila. Se entiende sin explicar. |
| 7 | Pregunta tres: ¿qué pensaste que necesitabas? Contratar a otra persona. | «Contratar a alguien» | Una silla nueva aparece al lado de la fila. La fila crece igual. | La silla nueva no resuelve nada. Ese es el punto. |
| 8 | Hay negocios con el triple de mensajes que responden en segundos con el mismo equipo. No les falta gente. Tienen un sistema que responde lo repetido y les deja a ellos lo que cierra ventas. | No les falta gente | Otra sala: los mensajes entran y salen sin sentarse; tres se quedan y están calientes. | La sala que no se llena. Movimiento fluido, sin fila. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las plataformas de atención, los chatbots y los equipos que atienden miles de conversaciones al día, con demostración en stand. | 15–19 OCT · PLAZA MAYOR | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | — |
| 10 | Última pregunta: ¿cuántos mensajes se te enfriaron esta semana? | ¿Cuántos se enfriaron? | Una silla vacía, sola, en el recinto. | Cierre incómodo a propósito. La silla vacía cierra el círculo del plano 3. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** el humito es el termómetro del video y lo tiene que hacer el modelo, no el post. Pídanlo como `soft warm steam rising, thin wisps` y **veten** `smoke, fog, mist` — humo denso convierte una sala de espera en un incendio.

---

## 27 · Empresarios que buscan networking y alianzas 🧊
**Ángulo 27.2 — Encontrar proveedores** · E5 Preguntas · ~36 s · 134 palabras

**Objeto protagonista:** una agenda de contactos con cinco fichas adentro. Fiel, ordenada, y muy corta. El equipo decide el diseño.
**Escenario:** oficina de gerente, escritorio limpio, teléfono, ventana con vista a la ciudad.
**Hilo visual:** las cinco fichas, siempre las mismas cinco.

**Locución corrida:**

> Pregunta uno: ¿cuándo fue la última vez que agregaste un proveedor nuevo a tu agenda? Si tuviste que pensarlo, ya pasaron años. Pregunta dos: cuando necesitas cotizar algo, ¿a cuántos les escribes? A los mismos cinco. Y te cotizan lo mismo de siempre. Pregunta tres: ¿cuántas empresas que te servirían no sabes ni que existen? Todas las que nunca llegaron por referido. Y ahí está: no te faltan referidos. Llevas años buscando dentro de la misma agenda. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas de cinco países en un mismo recinto, buscando con quién hacer negocios. Tu competencia ya cerró una alianza con alguien que tú no conocías. Última pregunta: ¿cuántas fichas nuevas caben en tu agenda? Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Pregunta uno: ¿cuándo fue la última vez que agregaste un proveedor nuevo a tu agenda? | ¿Cuándo fue la última vez? | La agenda cerrada sobre el escritorio, de frente. | Establecer en plano medio, no en detalle. La oficina cuenta el cargo. |
| 2 | *(silencio, un segundo)* | — | Mismo plano. La agenda quieta. | — |
| 3 | Si tuviste que pensarlo, ya pasaron años. | Ya pasaron años | La agenda se abre sola: cinco fichas, y mucho espacio en blanco detrás. | El espacio vacío ocupa más cuadro que las fichas. |
| 4 | Pregunta dos: cuando necesitas cotizar algo, ¿a cuántos les escribes? | ¿A cuántos? | Punch a las cinco fichas, de frente. | — |
| 5 | *(silencio, un segundo)* | — | Mismo plano, quieto. | — |
| 6 | A los mismos cinco. Y te cotizan lo mismo de siempre. | Los mismos cinco | Las cinco fichas se levantan y muestran los cinco la misma cifra. | Que las cinco sean idénticas. Ni una distinta. |
| 7 | Pregunta tres: ¿cuántas empresas que te servirían no sabes ni que existen? | ¿Cuántas no conoces? | La ventana de la oficina: la ciudad afuera, con miles de luces. | La ciudad es la respuesta y llega antes que la locución. |
| 8 | Todas las que nunca llegaron por referido. Y ahí está: no te faltan referidos. Llevas años buscando dentro de la misma agenda. | No faltan referidos | La agenda, abierta, girada hacia la ventana. | El objeto mira hacia afuera por primera vez. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas de cinco países en un mismo recinto, buscando con quién hacer negocios. | 15–19 OCT · +350 EMPRESAS · 5 PAÍSES | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | — |
| 10 | Tu competencia ya cerró una alianza con alguien que tú no conocías. Última pregunta: ¿cuántas fichas nuevas caben en tu agenda? | ¿Cuántas fichas caben? | La agenda abierta, con las hojas en blanco pasando solas. | Las hojas en blanco pasando: espacio disponible, no vacío triste. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** público frío: no sabe que Effix existe ni por qué le importa. Por eso este guion **no menciona ecommerce en ninguna línea** — habla de proveedores y alianzas, que es su idioma. Si lo van a pautar, no lo mezclen en el mismo conjunto de anuncios que los guiones de dropshipping.

---

# E6 · Reloj

*Videos 07, 13, 21 y 23*

Cada beat arranca con una marca de tiempo —una hora, un día, un mes, un segundo— y los cortes entre marcas son secos. El espectador no sigue una historia: sigue un cronómetro, y eso mantiene la vista pegada porque siempre quiere saber qué viene en la marca siguiente.

**Cómo se dirige:** la marca de tiempo se dice **y** se pone en pantalla, siempre en el mismo sitio del cuadro, con el mismo tamaño. Es lo único repetido del video y funciona como latido. Los planos entre marcas pueden ser distintos entre sí; la marca los cose.

**La última marca de tiempo es siempre el quince de octubre.** Ahí se rompe la serie: es la única que está en el futuro y la única que el espectador puede cambiar.

---

## 07 · Mayoristas y distribuidores 🔥
**Ángulo 7.2 — Conseguir nuevos clientes** · E6 Reloj · ~37 s · 138 palabras

**Objeto protagonista:** un talonario de pedidos, con las mismas hojas escritas mes tras mes. El equipo decide el diseño.
**Escenario:** oficina de bodega: escritorio con vista a las estanterías, teléfono fijo, calendario de pared.
**Hilo visual:** las hojas del talonario, todas con los mismos nombres.

**Locución corrida:**

> Enero. Cierras el mes y revisas quién te compró. Junio. Cierras el mes. Los mismos nombres. Diciembre. Los mismos, otra vez. Un año entero de los mismos ocho clientes. Y cuando uno se demora en pagar, el mes entero se te mueve. Te dices que en este negocio los clientes llegan por recomendación, y que hay que esperar. Mientras esperas, cada día abren tiendas online que compran al por mayor, y no saben que existes. No te faltan clientes. Te falta estar donde ellos van a buscar proveedor. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas buscando a quién comprarle, en el mismo recinto. Quince de octubre. La única fecha de este video que todavía no ha pasado. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Enero. Cierras el mes y revisas quién te compró. | ENERO | El talonario abierto sobre el escritorio, con ocho renglones escritos. | La marca de tiempo va arriba a la izquierda. Ahí se queda todo el video. |
| 2 | Junio. Cierras el mes. Los mismos nombres. | JUNIO | Mismo encuadre, hoja nueva, mismos ocho renglones. | Mismo plano, otra hoja. El corte es seco. |
| 3 | Diciembre. Los mismos, otra vez. | DICIEMBRE | Mismo encuadre. Ahora el talonario está casi acabado. | Tercera repetición, más corta. Acelerar. |
| 4 | Un año entero de los mismos ocho clientes. | Ocho clientes | Las hojas del talonario pasan solas, todas iguales, como un flipbook. | El flipbook es el único movimiento rápido del video. |
| 5 | Y cuando uno se demora en pagar, el mes entero se te mueve. | Uno se demora y todo se mueve | Uno de los ocho renglones se despega y el talonario se inclina. | Un renglón mueve todo el objeto. Ahí está la fragilidad. |
| 6 | Te dices que en este negocio los clientes llegan por recomendación, y que hay que esperar. | «Llegan por recomendación» | El teléfono fijo, quieto, sin sonar. La bodega llena al fondo. | El teléfono que no suena es el plano más elocuente. Que dure. |
| 7 | Mientras esperas, cada día abren tiendas online que compran al por mayor, y no saben que existes. | No saben que existes | Fuera de la bodega: tiendas-personaje pequeñas caminando en otra dirección. | Van hacia otro lado. No están perdidas: están yendo a otra parte. |
| 8 | No te faltan clientes. Te falta estar donde ellos van a buscar proveedor. | No te faltan clientes | El talonario, de frente, con una hoja en blanco. | — |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas buscando a quién comprarle, en el mismo recinto. | 15–19 OCT · +350 EMPRESAS | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | — |
| 10 | Quince de octubre. La única fecha de este video que todavía no ha pasado. | 15 OCT | El talonario abierto, con renglones nuevos apareciendo solos. | La marca de tiempo cierra igual que abrió. Mismo sitio del cuadro. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** el remate del plano 10 —«la única fecha que todavía no ha pasado»— es el mejor cierre del lote entero y sirve para los cuatro videos de E6. Consérvenlo tal cual: es lo que convierte un formato de calendario en una razón para comprar hoy.

---

## 13 · Logística, fulfillment y última milla 🔥
**Ángulo 13.2 — Entregas tardías** · E6 Reloj · ~39 s · 145 palabras

**Objeto protagonista:** un paquete que va tarde. No es tuyo: es del operador que sí tiene el cliente. El equipo decide el diseño.
**Escenario:** mundo A, una estantería de bodega ajena donde el paquete lleva días. Mundo B, tu bodega: ordenada, con capacidad de sobra.
**Hilo visual:** el reloj de pared de la bodega ajena, siempre en cuadro.

**Locución corrida:**

> Lunes, nueve de la mañana. Una tienda despacha un pedido. Miércoles, dos de la tarde. El paquete sigue en la misma estantería. Viernes. El cliente escribe preguntando dónde está su pedido. Lunes otra vez. El cliente pide la devolución y no vuelve a comprar. Ese paquete no es tuyo. Tú entregas a tiempo, tienes la flota, tienes la bodega, y tu operación va a media máquina. Te dices que en logística los clientes llegan por recomendación, y hay que esperar. Pero las tiendas que crecen ya eligieron con quién despachan, y lo eligieron donde lo vieron de frente. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas despachando producto todos los días. Quince de octubre. La única fecha de este video que todavía no ha pasado. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Lunes, nueve de la mañana. Una tienda despacha un pedido. | LUNES 9:00 a. m. | El paquete recién sellado, entusiasmado, en una banda transportadora. | Empezar con el paquete de buen ánimo. La caída se siente más. |
| 2 | Miércoles, dos de la tarde. El paquete sigue en la misma estantería. | MIÉRCOLES 2:00 p. m. | El paquete quieto en una estantería. Reloj de pared al fondo. | El reloj entra aquí y no se va hasta el plano 6. |
| 3 | Viernes. El cliente escribe preguntando dónde está su pedido. | VIERNES | El paquete, más apagado; a su lado un globo de mensaje que pregunta. | El globo llega hasta el paquete, no hasta una persona. |
| 4 | Lunes otra vez. El cliente pide la devolución y no vuelve a comprar. | LUNES OTRA VEZ | El paquete devuelto, con la etiqueta al revés, en una caneca de devoluciones. | La etiqueta al revés cuenta la devolución sin texto. |
| 5 | Ese paquete no es tuyo. | No es tuyo | Corte a tu bodega: limpia, ordenada, con la banda parada. | El giro del video. Cambio de mundo con corte duro. |
| 6 | Tú entregas a tiempo, tienes la flota, tienes la bodega, y tu operación va a media máquina. | A media máquina | Estanterías tuyas con la mitad de los espacios vacíos. | El vacío organizado, no el abandono. Es capacidad, no fracaso. |
| 7 | Te dices que en logística los clientes llegan por recomendación, y hay que esperar. | «Llegan por recomendación» | El teléfono de la bodega, quieto. | — |
| 8 | Pero las tiendas que crecen ya eligieron con quién despachan, y lo eligieron donde lo vieron de frente. | Ya eligieron | Tiendas-personaje caminando por un pasillo hacia stands. | Anticipa el recinto un plano antes. Suaviza la entrada. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de trescientas cincuenta empresas y miles de tiendas despachando producto todos los días. | 15–19 OCT · +350 EMPRESAS | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | — |
| 10 | Quince de octubre. La única fecha de este video que todavía no ha pasado. | 15 OCT | Tu bodega, con las estanterías llenándose solas. | Mismo remate del lote E6. Consistencia de campaña. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** el riesgo aquí es que el video se lea como un ataque a la competencia. No lo es: el paquete tarde **no tiene marca**, la bodega ajena no tiene logo, y el argumento es la capacidad ociosa propia. Si el equipo le pone identidad al operador que falla, hay que rehacerlo.

---

## 21 · Contenido para e-commerce 🟡
**Ángulo 21.2 — Videos para anuncios** · E6 Reloj · ~37 s · 135 palabras

**Objeto protagonista:** un video de producto —un rectángulo con cara, en vertical— que nadie ve completo. El equipo decide el diseño.
**Escenario:** el feed, imaginado como un tubo vertical por el que pasan videos a toda velocidad.
**Hilo visual:** el dedo que desliza. **Nunca se ve la mano**: es una sombra que barre desde arriba.

**Locución corrida:**

> Segundo uno. Tu video arranca. Se ve bien: buena luz, buena cámara. Segundo dos. Todavía estás mostrando el producto. Segundo tres. La sombra pasa y tu video se fue. Segundo cuatro no existe. Nadie llegó. Te dices que necesitas mejor cámara, mejor luz, mejor edición. Los videos que más venden se graban con celular. Lo que cambia es el guion y quién sale. No te falta producción. Te falta saber qué se dice en los primeros tres segundos. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las agencias de contenido, los creadores y más de doscientas ponencias donde muestran, cuadro por cuadro, los videos que sí venden y por qué. Quince de octubre. El único segundo de este video que todavía no ha pasado. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Segundo uno. Tu video arranca. Se ve bien: buena luz, buena cámara. | SEGUNDO 1 | El video-personaje entra al tubo del feed, iluminado, orgulloso. | La marca de tiempo arriba a la izquierda, igual que en los otros E6. |
| 2 | Segundo dos. Todavía estás mostrando el producto. | SEGUNDO 2 | El video-personaje sostiene un producto contra su propio cuerpo. | Que se note que va lento: es lo que estamos criticando. |
| 3 | Segundo tres. La sombra pasa y tu video se fue. | SEGUNDO 3 | Una sombra barre el cuadro de arriba abajo y el video-personaje sale disparado. | **Sin manos.** Es una sombra, y va rapidísimo. |
| 4 | Segundo cuatro no existe. Nadie llegó. | No hay segundo 4 | Cuadro vacío. Solo el tubo del feed y otro video entrando. | Medio segundo de vacío. El único hueco del video. |
| 5 | Te dices que necesitas mejor cámara, mejor luz, mejor edición. | «Mejor cámara» | Tres objetos —foco, cámara, mesa de edición— se apilan sobre el video-personaje. | Tres cortes rápidos. El personaje desaparece bajo el equipo. |
| 6 | Los videos que más venden se graban con celular. Lo que cambia es el guion y quién sale. | Es el guion | Otro video-personaje, más humilde, que en el segundo uno ya está diciendo algo. | El humilde arranca hablando. Ese es todo el contraste. |
| 7 | No te falta producción. Te falta saber qué se dice en los primeros tres segundos. | Los primeros tres segundos | El video-personaje humilde, quieto, con la sombra pasando por encima **sin llevárselo**. | La sombra que pasa y no se lo lleva: la retención hecha imagen. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las agencias de contenido, los creadores y más de doscientas ponencias donde muestran, cuadro por cuadro, los videos que sí venden y por qué. | 15–19 OCT · +200 PONENCIAS | Recinto en blanco y negro: auditorio lleno, pantalla grande, stands corporativos, pasillos alfombrados. | — |
| 9 | Quince de octubre. El único segundo de este video que todavía no ha pasado. | 15 OCT | El video-personaje, de frente, encendido, en el tubo del feed. | Variación del remate de E6: aquí es «segundo», no «fecha». |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este video es el más meta del lote —es un anuncio sobre por qué los anuncios no retienen— y por eso **tiene que ser el mejor montado de los veintiocho**. Si a este se le pasa un plano de tres segundos, el chiste se vuelve en contra. Móntenlo de último, cuando ya tengan mano con el formato.

---

## 23 · Ciberseguridad y prevención de fraude 🟡
**Ángulo 23.2 — Robo de cuentas** · E6 Reloj · ~41 s · 152 palabras

**Objeto protagonista:** un candado de una cuenta de anuncios. Despierto, atento, y sin trabajo porque nadie lo instaló. El equipo decide el diseño.
**Escenario:** un panel de anuncios visto como una casa pequeña con una puerta.
**Hilo visual:** la puerta del panel. Al principio está entreabierta y nadie la mira.

**Locución corrida:**

> Viernes, siete de la noche. La puerta de la cuenta de anuncios de una tienda queda entreabierta, como todos los días. Viernes, ocho y media. Alguien entra y el presupuesto del mes se va. Sábado. La tienda se da cuenta. Lunes, ocho de la mañana. Ahí sí te llaman a ti. Tú vendes protección. Y las tiendas solo te buscan después de perder. Te dices que la seguridad se vende después del susto. Pero las que ya crecieron contrataron antes, porque alguien les mostró el riesgo con casos reales, de frente. No te falta producto. Te falta estar delante de miles de tiendas antes del viernes. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes que manejan cuentas, pagos y datos de clientes. Quince de octubre. La única fecha de este video que todavía no ha pasado. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Viernes, siete de la noche. La puerta de la cuenta de anuncios de una tienda queda entreabierta, como todos los días. | VIERNES 7:00 p. m. | La casita-panel con la puerta entreabierta, luz adentro. El candado, aparte, en una repisa. | El candado está en la repisa desde el primer plano. Ahí está el drama. |
| 2 | Viernes, ocho y media. Alguien entra y el presupuesto del mes se va. | VIERNES 8:30 p. m. | La puerta se abre del todo y la luz de adentro se apaga de golpe. | **Sin figura humana, sin sombra amenazante.** Solo la luz que se va. |
| 3 | Sábado. La tienda se da cuenta. | SÁBADO | La casita a oscuras. El candado, en la repisa, mirando. | El candado mirando y sin poder hacer nada: la imagen del video. |
| 4 | Lunes, ocho de la mañana. Ahí sí te llaman a ti. | LUNES 8:00 a. m. | El candado suena y vibra en la repisa por primera vez. | Su único momento de acción llega tarde. |
| 5 | Tú vendes protección. Y las tiendas solo te buscan después de perder. | Te buscan después | Una repisa larga con muchos candados iguales, todos apagados. | La repisa llena es el inventario que no se mueve. |
| 6 | Te dices que la seguridad se vende después del susto. | «Después del susto» | Punch a un candado, cerrado, quieto. | — |
| 7 | Pero las que ya crecieron contrataron antes, porque alguien les mostró el riesgo con casos reales, de frente. | Contrataron antes | Otra casita: la puerta cerrada, el candado puesto, la luz encendida adentro. | La casa con luz encendida es el mundo deseado. Cálida, no fortificada. |
| 8 | No te falta producto. Te falta estar delante de miles de tiendas antes del viernes. | Antes del viernes | El candado, de frente, abierto, listo para ponerse. | — |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay más de sesenta mil asistentes que manejan cuentas, pagos y datos de clientes. | 15–19 OCT · +60.000 ASISTENTES | Recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. Casitas-panel haciendo fila. | — |
| 10 | Quince de octubre. La única fecha de este video que todavía no ha pasado. | 15 OCT | El candado cerrándose sobre una puerta, con un chasquido limpio. | El chasquido es el punto final. Un solo sonido, seco. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** ni sombras encapuchadas, ni calaveras, ni verde de matriz, ni candados rotos con chispas. **Nada de estética de hacker**: es un video Pixar sobre una casa a la que se le olvidó cerrar la puerta. Si da miedo, está mal dirigido — y además Meta castiga el creativo alarmista.

---

# E7 · El viaje

*Videos 06, 14, 17 y 28*

El objeto sale del sitio donde está atascado y se va, y el video lo sigue. Hay **continuidad espacial**: cada plano avanza por el mismo camino, en la misma dirección, y el destino es el recinto. Es la única de las siete estructuras donde el personaje se mueve de verdad, y por eso es la que mejor aguanta un montaje rápido.

**Cómo se dirige:** que el movimiento vaya **siempre hacia el mismo lado del cuadro** (de izquierda a derecha, por ejemplo) y no se invierta nunca. En el momento en que el personaje camina hacia el otro lado, el espectador siente que se devolvió. La única excepción es el plano del problema al principio, donde el objeto está quieto.

**Truco de continuidad:** encadenen keyframes —el último cuadro del clip N es el primero del clip N+1—. En este formato paga más que en los otros seis porque el camino tiene que verse continuo. En Kling 2.5 el keyframe final está prohibido a 720p: generen a 1080p.

---

## 06 · Marcas, fabricantes e importadores 🔥
**Ángulo 6.2 — Vender directamente al consumidor** · E7 Viaje · ~43 s · 157 palabras

**Objeto protagonista:** un producto de fábrica —recién hecho, con orgullo— que va a viajar. El equipo decide el diseño.
**Escenario:** el camino que va de la planta a la casa del cliente, con paradas.
**Hilo visual:** una etiqueta de precio que va cambiando en cada parada.

**Locución corrida:**

> Salgo de tu planta con la etiqueta que tú me pusiste. Primera parada: la bodega de un distribuidor. Mi etiqueta cambia. Segunda parada: una tienda online que no es tuya. Mi etiqueta cambia otra vez. Tercera parada: la casa del cliente, que paga el precio final y nunca supo quién me fabricó. Esa diferencia entre la primera etiqueta y la última no llega a tu cuenta. Te dices que lo tuyo es producir, y que vender directo es otro oficio. Es otro oficio. Y no tienes que aprenderlo: tienes que contratar a los que ya lo tienen. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las agencias, los creadores de contenido y los operadores logísticos que le montan el canal directo a marcas como la tuya, todos en el mismo recinto. Sigo saliendo de tu planta todos los días. Lo que puede cambiar es por dónde. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Salgo de tu planta con la etiqueta que tú me pusiste. | — | El producto en la banda de salida de la planta, etiqueta puesta, contento. | Movimiento de izquierda a derecha. Se mantiene todo el video. |
| 2 | Primera parada: la bodega de un distribuidor. Mi etiqueta cambia. | Parada uno | El producto se detiene en una bodega; la etiqueta gira y muestra otro número. | La etiqueta gira sola. **Sin manos.** |
| 3 | Segunda parada: una tienda online que no es tuya. Mi etiqueta cambia otra vez. | Parada dos | Sigue avanzando; la etiqueta gira de nuevo, más grande. | Mismo eje, mismo sentido. El camino no se corta. |
| 4 | Tercera parada: la casa del cliente, que paga el precio final y nunca supo quién me fabricó. | Parada tres | El producto llega a una puerta de casa; la etiqueta, ahora la más grande de todas. | — |
| 5 | Esa diferencia entre la primera etiqueta y la última no llega a tu cuenta. | La diferencia no llega | Las tres etiquetas alineadas en el aire, de menor a mayor. | El único plano gráfico del video. Corto. |
| 6 | Te dices que lo tuyo es producir, y que vender directo es otro oficio. | «Lo mío es producir» | La planta al fondo, con el producto de espaldas mirándola. | El único plano en que mira hacia atrás. Justificado: está recordando. |
| 7 | Es otro oficio. Y no tienes que aprenderlo: tienes que contratar a los que ya lo tienen. | No tienes que aprenderlo | El producto retoma el camino, ahora por una bifurcación que se abre a la derecha. | La bifurcación es la decisión. Que se vea el desvío. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están las agencias, los creadores de contenido y los operadores logísticos que le montan el canal directo a marcas como la tuya, todos en el mismo recinto. | 15–19 OCT · PLAZA MAYOR | El camino desemboca en el recinto en blanco y negro: stands corporativos, pasillos alfombrados, paneles retroiluminados. | El camino ENTRA al recinto. No corten: que se llegue. |
| 9 | Sigo saliendo de tu planta todos los días. Lo que puede cambiar es por dónde. | Cambia por dónde | El producto, en el recinto, con la etiqueta original puesta y sin girar. | La etiqueta que ya no cambia. Ese es el final. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** el producto **no puede ser reconocible**: nada de marcas, logos ni formas de producto real. Que sea una forma genérica bonita —una caja con tapa, un frasco liso— para que cualquier fabricante que lo vea se ponga a sí mismo ahí.

---

## 14 · Proveedores de dropshipping 🔥
**Ángulo 14.2 — Encontrar nuevos clientes** · E7 Viaje · ~36 s · 132 palabras

**Objeto protagonista:** una caja de catálogo llena de producto, que se cansó de esperar en la bodega y sale a buscar vendedores. El equipo decide el diseño.
**Escenario:** de la bodega a la calle, de la calle al recinto.
**Hilo visual:** el catálogo que la caja lleva encima como si fuera un sombrero.

**Locución corrida:**

> Llevo meses en esta bodega, llena, con el catálogo listo. Los mismos veinte vendedores de siempre mueven la mitad de lo que hay aquí. Publicaste el catálogo en grupos, y los vendedores nuevos llegan de a uno. Te dices que los buenos dropshippers ya tienen proveedor y no cambian. Cambian. Cambian cada vez que uno les falla. Y cuando cambian, buscan al siguiente donde puedan verlo, tocar el producto y mirarlo a la cara. Ahí es donde no estás. Así que me salí. Voy a donde están buscando. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay miles de dropshippers de cinco países buscando proveedor confiable, y una mesa donde el producto se puede tocar. Yo llego el quince. Nos vemos allá. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Llevo meses en esta bodega, llena, con el catálogo listo. | — | La caja quieta entre estanterías, catálogo encima, luz de bodega. | Único plano quieto del video. A partir del 6 no para. |
| 2 | Los mismos veinte vendedores de siempre mueven la mitad de lo que hay aquí. | Los mismos veinte | Estantería con la mitad de los espacios llenos y la otra mitad intacta. | La mitad exacta. Que se lea de un vistazo. |
| 3 | Publicaste el catálogo en grupos, y los vendedores nuevos llegan de a uno. | Llegan de a uno | Un vendedor-personaje pequeño entra a la bodega, mira, y se va. | Uno solo, y se va. Sin drama. |
| 4 | Te dices que los buenos dropshippers ya tienen proveedor y no cambian. | «Ya tienen proveedor» | La caja mira la puerta de la bodega, cerrada. | La puerta cerrada anticipa la salida. |
| 5 | Cambian. Cambian cada vez que uno les falla. | Sí cambian | Afuera: vendedores-personaje caminando en fila, todos en la misma dirección. | Aquí arranca el movimiento de izquierda a derecha. Ya no para. |
| 6 | Y cuando cambian, buscan al siguiente donde puedan verlo, tocar el producto y mirarlo a la cara. | Quieren tocar el producto | La fila avanza; la cámara los sigue en travelling lateral. | Travelling, no corte. Un solo clip largo que se parte en tres planos. |
| 7 | Ahí es donde no estás. Así que me salí. Voy a donde están buscando. | Me salí | La caja sale por la puerta de la bodega y se mete en la fila. | El momento del video. Que el paso se sienta decidido. |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay miles de dropshippers de cinco países buscando proveedor confiable, y una mesa donde el producto se puede tocar. | 15–19 OCT · 5 PAÍSES | El recinto en blanco y negro: stands corporativos, pasillos alfombrados, mesa con muestras. | La mesa con muestra física es el argumento del nicho. |
| 9 | Yo llego el quince. Nos vemos allá. | Nos vemos el 15 | La caja sobre la mesa del stand, abierta, con el catálogo desplegado. | Cierre generoso: abierta, no cerrada. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** este y el 05 (dropshippers buscando proveedor) son **las dos caras del mismo pasillo**. Si los pautan en la misma semana, pueden montarse como pieza doble: uno busca y el otro sale a buscar. Nada más hay que cuidar que la mesa con muestra física se vea igual en los dos.

---

## 17 · Internacionalización y expansión de negocios 🟡
**Ángulo 17.2 — Primer mercado internacional** · E7 Viaje · ~38 s · 140 palabras

**Objeto protagonista:** un pedido —una caja con guía de envío— que quiere cruzar una frontera y no sabe cómo. El equipo decide el diseño.
**Escenario:** un mapa físico, con relieve, por el que la caja camina. La frontera es una línea marcada en el suelo.
**Hilo visual:** la línea de la frontera. Está en cuadro casi todo el video.

**Locución corrida:**

> Me preguntaron si vas a vender en Ecuador. Dijiste que todavía no. Yo estoy listo, empacado y con guía. Lo que no sé es cómo se cruza esta línea. Buscaste en internet cómo exportar, y te salieron requisitos. Ninguno de ellos es una persona. Te dices que para entrar a otro país hay que ser una empresa grande. Las empresas de tu tamaño que ya venden afuera no eran grandes. Tenían un aliado del otro lado. No te falta tamaño. Te falta conocer a alguien que ya esté vendiendo allá. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay empresas de cinco países y ponentes de más de veinte, en el mismo recinto. El aliado del otro lado está a un pasillo de distancia. Yo sigo empacado, esperando la línea. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Me preguntaron si vas a vender en Ecuador. Dijiste que todavía no. | — | La caja de pie sobre el mapa, frente a la línea de la frontera. | El mapa con relieve, iluminado como maqueta. Que se vea el volumen. |
| 2 | Yo estoy listo, empacado y con guía. Lo que no sé es cómo se cruza esta línea. | Listo. Y quieto. | Punch a la caja: guía pegada, cinta puesta, todo en orden. | Está impecable. El problema no es ella. |
| 3 | Buscaste en internet cómo exportar, y te salieron requisitos. Ninguno de ellos es una persona. | Requisitos, no personas | Hojas de papel caen sobre el mapa y forman un montón frente a la caja. | El montón de papel tapa la línea. Literal. |
| 4 | Te dices que para entrar a otro país hay que ser una empresa grande. | «Hay que ser grande» | La sombra de una caja enorme cae sobre la caja pequeña. | Sombra, no objeto. Es una idea, no un competidor. |
| 5 | Las empresas de tu tamaño que ya venden afuera no eran grandes. | No eran grandes | Al otro lado de la línea, tres cajas del mismo tamaño, ya instaladas. | Mismo tamaño exacto que la protagonista. Ese es el argumento. |
| 6 | Tenían un aliado del otro lado. | Un aliado del otro lado | Una de las tres cajas se acerca a la línea desde el otro lado. | El primer movimiento que viene de enfrente. Rompe la soledad. |
| 7 | No te falta tamaño. Te falta conocer a alguien que ya esté vendiendo allá. | No te falta tamaño | Las dos cajas, una a cada lado de la línea, de frente. | — |
| 8 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, hay empresas de cinco países y ponentes de más de veinte, en el mismo recinto. | 15–19 OCT · 5 PAÍSES · +20 PAÍSES DE PONENTES | La línea del mapa se convierte en el pasillo alfombrado del recinto en blanco y negro. | La transformación de la línea en pasillo es el mejor plano del video. Vale un clip propio. |
| 9 | El aliado del otro lado está a un pasillo de distancia. Yo sigo empacado, esperando la línea. | A un pasillo | La caja, en el pasillo, mirando hacia adelante. La línea ya no está. | La línea desaparece. Nada más hace falta. |
| 10 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** nada de banderas, mapas políticos reconocibles ni nombres de país escritos en el suelo. La frontera es **una línea abstracta** en un mapa de relieve. Ecuador se nombra en la locución, que es donde no puede salir mal, y en la imagen nunca.

---

## 28 · Personas que quieren convertirse en referentes del e-commerce 🧊
**Ángulo 28.2 — Ser reconocido en el sector** · E7 Viaje · ~39 s · 144 palabras

**Objeto protagonista:** una placa con un nombre grabado —el tuyo— que no está en ninguna lista. Digna, callada, con años encima. El equipo decide el diseño.
**Escenario:** de un escritorio en casa a un pasillo lleno de placas con nombres, hasta el recinto.
**Hilo visual:** el muro de placas. Al principio se ve de lejos; al final se camina por él.

**Locución corrida:**

> Publicaron la lista de los nombres que mueven el ecommerce en tu país. Yo me quedé en el escritorio. Reconoces a la mitad. De la otra mitad piensas que sabes más que ellos. Y puede que tengas razón. Te dices que esas listas son de contactos, no de mérito. El mérito que nadie ha visto pesa lo mismo que no tenerlo. No te falta mérito. Te falta que la gente del sector te haya visto en persona. Así que me bajé del escritorio y me fui caminando. Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están los más de doscientos ponentes y las más de trescientas cincuenta marcas que definen quién es quién en este sector. Tres días conversando de frente con ellos. Las listas del año entrante las escribe alguien que estuvo ahí. Compra tu ingreso dando clic en el botón.

| # | Locución | Texto en pantalla | Plano | Dirección |
|---|---|---|---|---|
| 1 | Publicaron la lista de los nombres que mueven el ecommerce en tu país. Yo me quedé en el escritorio. | — | La placa sobre un escritorio de casa. Al fondo, un muro de placas iluminadas, lejos. | El muro al fondo desde el primer plano. Es el destino y ya se ve. |
| 2 | Reconoces a la mitad. | — | El muro, más cerca: placas con formas grabadas, sin letras legibles. | **Sin letras.** Formas geométricas grabadas. El modelo inventa texto si lo dejan. |
| 3 | De la otra mitad piensas que sabes más que ellos. | — | Punch a tres placas del muro, brillantes, y a la protagonista, opaca, al lado. | El brillo es la única diferencia. No el tamaño. |
| 4 | Y puede que tengas razón. | Puede que tengas razón | La placa protagonista, de frente, quieta. | Beat corto de dignidad. Sin música encima. |
| 5 | Te dices que esas listas son de contactos, no de mérito. | «Son de contactos» | La placa se gira de espaldas al muro. | Único momento en que da la espalda al destino. |
| 6 | El mérito que nadie ha visto pesa lo mismo que no tenerlo. | Nadie lo ha visto | La placa en el cajón del escritorio, entre cosas guardadas. | El cajón: el fondo del video. Corto, no lastimero. |
| 7 | No te falta mérito. Te falta que la gente del sector te haya visto en persona. | No te falta mérito | La placa sale del cajón y se apoya de canto en el borde del escritorio. | Arranca el viaje. De aquí en adelante, siempre hacia la derecha. |
| 8 | Así que me bajé del escritorio y me fui caminando. | — | La placa cruzando el piso, en travelling lateral, hacia el muro. | Un clip largo, tres planos por reencuadre. |
| 9 | Del quince al diecinueve de octubre, en Plaza Mayor, Medellín, están los más de doscientos ponentes y las más de trescientas cincuenta marcas que definen quién es quién en este sector. | 15–19 OCT · +200 PONENTES | El muro se abre y se convierte en el pasillo del recinto en blanco y negro: stands corporativos, paneles retroiluminados. | El muro se vuelve pasillo. Mismo recurso de transformación que el 17. |
| 10 | Tres días conversando de frente con ellos. Las listas del año entrante las escribe alguien que estuvo ahí. | Tres días | La placa caminando por el pasillo, entre otras placas, de frente. | **Nunca en tarima.** El pase es de asistente. Que camine el pasillo, no que suba a hablar. |
| 11 | Compra tu ingreso dando clic en el botón. | Compra tu ingreso | Logo Effix en blanco sobre negro. | — |

**Recomendación de producción:** dos líneas rojas heredadas de los guiones anteriores de este público, y las dos son de riesgo comercial: **el personaje nunca aparece en tarima** y **no se promete cupo de ponente** — el pase que se vende es de asistente. Tampoco se prometen las zonas de creación de contenido: esas son del VIP.

---

# Recomendaciones para el equipo

## Por dónde empezar

No produzcan en orden numérico. **Produzcan por estructura**, cuatro a la vez: la segunda vez que se monta un formato cuesta la mitad de esfuerzo que la primera, y los cuatro salen parecidos entre ellos, que es lo que queremos.

Orden sugerido, de menor a mayor riesgo:

| Tanda | Estructura | Por qué en este orden |
|---|---|---|
| 1 | **E1 Monólogo** (01, 08, 15, 24) | Un personaje, dos escenarios, cero coreografía. Es donde se calibra la hoja de personaje del lote. |
| 2 | **E3 Escalada** (03, 10, 19, 25) | Mismo eje de cámara en casi todo el video: se reencuadra mucho y se genera poco. |
| 3 | **E5 Preguntas** (05, 12, 20, 27) | El riesgo está en el montaje, no en la generación. Buen sitio para probar los silencios. |
| 4 | **E4 Espejo** (04, 11, 18, 26) | Exige que dos imágenes sean casi idénticas. Se hace editando la imagen A, no generando dos. |
| 5 | **E2 Diálogo** (02, 09, 16, 22) | Dos personajes consistentes en el mismo mundo. Ahí empieza a costar. |
| 6 | **E6 Reloj** (07, 13, 21, 23) | Muchas marcas de tiempo y un overlay que tiene que caer siempre en el mismo sitio. |
| 7 | **E7 Viaje** (06, 14, 17, 28) | Continuidad espacial con keyframes encadenados: lo más caro y lo que peor perdona un error. |

**Empiecen por el 01.** Es el más barato del lote y el que menos cosas puede romper. Si sale bien, el pipeline está listo.

## Presupuesto

**Cinco dólares promedio por video, tope seis, todo incluido.** Si un video se va a pasar, avisen y propongan un recorte **antes** de gastar, no después.

Referencia de un video narrado con doce escenas: voz (menos de medio dólar) + hoja de personaje (ocho centavos) + doce imágenes de escena + doce clips de cinco segundos. La música sale de la librería y ya está pagada.

**Tres formas de gastar de más que ya conocemos:**

1. **Generar un clip por línea de guion.** No. Un clip por escena, y los planos extra salen de reencuadrar ese mismo clip. Es el punch-in de toda la vida y cuesta cero.
2. **No mirar la hoja de personaje antes de generar las escenas.** Un error en la hoja se hereda en las doce imágenes. Mirarla cuesta un minuto.
3. **Pedir acciones imposibles.** El modelo mete una persona para resolverlas, y el clip se rehace.

Kling cobra por tramos de cinco y diez segundos: un keyframe final (ocho centavos) suele ahorrar más de lo que cuesta, sobre todo en E7.

## QA antes de entregar cada video

- [ ] Duración entre treinta y sesenta segundos
- [ ] Ningún plano por debajo de 1,25 s
- [ ] Cortes cada 1,5–2,5 s en promedio
- [ ] Ningún encuadre repetido dos veces seguidas
- [ ] Ninguna persona humana en ningún clip
- [ ] Ninguna letra inventada por el modelo en ningún plano
- [ ] El recinto se lee como centro de convenciones, no como plaza de mercado
- [ ] Master a −14 LUFS, sin clipping en el archivo final (no solo en el WAV)
- [ ] Overlays centrados, dos renglones máximo, Montserrat, ≤ 7 palabras
- [ ] Logo Effix desde el primer segundo
- [ ] La locución dice los números en letras
- [ ] No aparece descuento, código, URL ni la palabra «taller»
- [ ] No se prometen más días de los que da el pase

## Errores que ya nos costaron plata

| Error | Qué pasó | Cómo se evita |
|---|---|---|
| «Character sheet» a nano-banana | Devolvió una grilla de contactos; las doce escenas heredaron el díptico | Pedir `single full-frame image` y repetirlo en el system prompt |
| Acción que necesita manos | El modelo metió humanos en dos clips | Solo acciones que el objeto puede hacer con el cuerpo que tiene |
| `hundreds of colourful stands` | El recinto salió como plaza de mercado | `modern convention hall, corporate exhibition booths, backlit display walls, carpeted aisles, lanyards` |
| `guidance_scale` alto | Degeneró una pista de audio entera | No aplica al narrado, pero vale el principio: no apretar los parámetros para forzar dicción |
| Limitador mal escrito | `alimiter` recibe amplitud lineal, no decibelios; ffmpeg no avisa | Limitar 1,5 dB por debajo, para que cumpla el archivo entregado y no solo la señal |

## Antes de pautar

⚠️ **Confirmar con Effix la cifra de «más de sesenta mil asistentes».** Está en seis de los veintiocho guiones (10, 11, 12, 23 y las variantes que la usen) y no tiene fuente pública. Si Effix no la confirma, se cambia por «miles de asistentes» y se vuelven a montar solo los overlays afectados — la locución sí habría que regrabarla, así que **es más barato preguntar ahora**.

Lo demás está verificado: más de trescientas cincuenta empresas, más de doscientas ponencias, más de doscientos ponentes, cinco países, cinco ediciones, del quince al diecinueve de octubre en Plaza Mayor, Medellín.

## Qué queda pendiente

- Los **ángulos .4 a .10** de cada público (doscientos veinticuatro guiones más) salen con el mismo molde cuando este lote se apruebe.
- **Personajes:** los define el equipo. Cuando estén definidos, vale la pena escribirlos en un documento aparte: si un objeto se repite entre nichos, la hoja de personaje se reutiliza y el lote siguiente cuesta menos.
- Si quieren producir estos veintiocho con el pipeline automático en vez de a mano, hay que pasarlos al formato JSON del repo. El contenido ya está: es trabajo de estructura, no creativo.

---

*Feria Effix 2026 · veintiocho guiones Pixar, ángulo .2 · 7 de septiembre de 2026*
