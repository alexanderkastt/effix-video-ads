# 28 prompts individuales — ángulo .1 v2 (musical)

Cada bloque se pega solo en Claude Code, dentro del repo `skills-video-ads`. Todos empiezan
igual: leen `outputs/REGLAS-ANGULO1-V2.md`, que trae las reglas duras, el reparto de formatos
y la prohibición de producir. Ninguno de estos prompts gasta un peso.

Orden sugerido: hacer primero uno de cada formato (01, 02, 04, 06, 09, 10, 12) para revisar
los siete moldes antes de soltar los veintiuno restantes.

> **Actualizado el 7 de septiembre de 2026.** Los JSON ya no los escribe Claude Code: los escribe Cowork y quedan
> en `scripts/guiones/*_v2_por-aprobar.json`. Estos bloques quedan como **brief de cada guion** — formato de canción,
> micro-situación y las tres apariciones — para revisar o pedir cambios. Los siete moldes (01, 02, 04, 06, 09, 10, 12)
> ya tienen su JSON escrito; los veintiuno restantes se escriben cuando Alexander apruebe los moldes.
> Para producir, usa el prompt de tanda del final de este archivo.

---

## F6 · DOS VOCES — 01, 07, 19, 23

### 01 · Emprendedores que empiezan

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 01 del ángulo .1.
Público: emprendedores que están comenzando en ecommerce · Ángulo 1.1: cómo empezar a vender por internet.
Estilo visual: Pixar 3D, objeto antropomórfico (NUBE, una nube de ideas) · Latin pop alegre.
Formato: F6 DOS VOCES — el que se excusa contra el que ya arrancó. Se interrumpen; la segunda voz
nunca regaña, solo cuenta lo que hizo.
Micro-situación: abre el portátil, hay tantas opciones que lo cierra sin hacer nada. Excusa: «me falta un curso más».
Tres apariciones: CRUDA la tapa del portátil que se cierra (0-5 s, en imagen) · AGRAVADA la misma tapa
otro día, con la libreta más llena de ideas tachadas (en imagen) · RESUELTA la misma tapa abierta, una sola
tienda en pantalla y el primer pedido.
Entregables: sección 01 del doc v2 + scripts/guiones/effix_pixar_p01-empezar-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 07 · Mayoristas y distribuidores

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 07 del ángulo .1.
Público: mayoristas y distribuidores · Ángulo 7.1: digitalizar ventas mayoristas.
Estilo visual: Animado 2D (DOÑA GLORIA, mayorista de teléfono y cuaderno) · Salsa urbana / champeta.
Formato: F6 DOS VOCES — doña Gloria contra el cliente que ya pide de noche por una página. Las dos voces
tienen razón en algo; el que gana es el que muestra el pedido entrando solo.
Micro-situación: el mismo pedido dictado por teléfono, pasado a Excel y digitado otra vez. Tres veces el mismo pedido.
Excusa: «mis clientes no van a pedir por una página».
Tres apariciones: CRUDA el cuaderno y el teléfono al hombro (0-5 s, en imagen) · AGRAVADA el día que la del
teléfono no llegó y el cuaderno está vacío (en imagen) · RESUELTA el mismo mostrador, el cuaderno cerrado y
los pedidos entrando solos.
Entregables: sección 07 del doc v2 + scripts/guiones/effix_animado_2d_p07-mayorista-digital-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 19 · Retail / omnicanalidad

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 19 del ángulo .1.
Público: retail · Ángulo 19.1: omnicanalidad.
Estilo visual: Anime (VALERIA, gerente de retail) · Latin pop electrónico.
Formato: F6 DOS VOCES — la tienda física y la tienda online cantan como dos personas que no se hablan.
Literal: cada una defiende su versión del mismo cliente.
Micro-situación: el cliente compra en la página, va a cambiarlo al local y le dicen «eso es de internet».
Tres apariciones: CRUDA el mostrador y la frase «eso es de internet» (0-5 s, en imagen) · AGRAVADA el mismo
cliente saliendo con la bolsa sin resolver, la vendedora encogiéndose de hombros (en imagen) · RESUELTA el
mismo mostrador, el cambio hecho, las dos voces cantando la misma línea por primera vez.
Entregables: sección 19 del doc v2 + scripts/guiones/effix_anime_p19-omnicanal-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 23 · Ciberseguridad y prevención de fraude

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 23 del ángulo .1.
Público: ciberseguridad y prevención de fraude (le venden a las tiendas) · Ángulo 23.1: fraude en pagos.
Estilo visual: Skeleton (bible verbatim, el esqueleto es la empresa de prevención) · Reggaetón.
Formato: F6 DOS VOCES — la tienda que dice «después lo vemos» contra la empresa que ya vio el contracargo
llegar. La segunda voz no dice «te lo dije»: dice qué pasa el día quince.
Micro-situación: aprueban el pago, despachan, y a los quince días llega el contracargo: era fraude.
El público objetivo es el proveedor de seguridad, no la tienda: el dolor es que solo lo buscan después de perder.
Tres apariciones: CRUDA el pago aprobado en verde (0-5 s, en imagen) · AGRAVADA el mismo pago, quince días
después, marcado como contracargo (en imagen) · RESUELTA la misma pantalla con el pago frenado antes de despachar.
Entregables: sección 23 del doc v2 + scripts/guiones/effix_skeleton_p23-fraude-pagos-musical_v2_por-aprobar.json.
No produzcas nada. Ojo: quita «sesenta mil asistentes» del mecanismo, va cifra verificable.
```

---

## F7 · JINGLE-LOOP — 02, 03, 15, 21

### 02 · Dueños de tiendas online

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 02 del ángulo .1.
Público: dueños de tiendas online · Ángulo 2.1: pocas ventas.
Estilo visual: Skeleton (Character Bible verbatim, encuadres distintos por plano) · Reggaetón.
Formato: F7 JINGLE-LOOP — «tres ventas» vuelve como cuña de radio cada vez más corta, con versos de dos
líneas entre repeticiones. La última vez la cuña se rompe y cambia el número.
Micro-situación: abre el panel y hay tres ventas. Igual que ayer. Igual que hace un mes.
Tres apariciones: CRUDA el panel con tres ventas (0-5 s, en imagen) · AGRAVADA el mismo panel, otro mes,
mismas tres (en imagen) · RESUELTA el mismo panel con la cifra subiendo mientras suena la última cuña.
Entregables: sección 02 del doc v2 + scripts/guiones/effix_skeleton_p02-pocas-ventas-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 03 · Ecommerce en crecimiento

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 03 del ángulo .1.
Público: empresarios de ecommerce en crecimiento · Ángulo 3.1: pasar de diez a cien pedidos diarios.
Estilo visual: Crochet, mundo B&N estricto, solo LEO con color (universal positivo/negativo y cierre I2V
verbatim) · Cumbia pop.
Formato: F7 JINGLE-LOOP — «diez, diez, diez» como cuña machacona; los versos entre repeticiones son lo que
se rompe cada vez que intenta crecer (pauta, proveedor, despacho). El loop se rompe con «cien».
Micro-situación: empaca diez pedidos al día, todos los días, sabiendo que podrían ser cien.
Tres apariciones: CRUDA la pila de diez cajas (0-5 s, en imagen) · AGRAVADA la misma pila con algo roto al
lado en cada intento (en imagen) · RESUELTA la mesa desbordada de cajas y el loop cambiado.
Entregables: sección 03 del doc v2 + scripts/guiones/effix_crochet_p03-diez-a-cien-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 15 · Empaques y packaging

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 15 del ángulo .1.
Público: empresas de empaques y packaging (le venden a las tiendas) · Ángulo 15.1: empaque que protege.
Estilo visual: Pixar 3D, objeto antropomórfico (CAJITA, caja de envío) · Latin pop alegre.
Formato: F7 JINGLE-LOOP — «llegó roto» como cuña de dos palabras que vuelve cada vez que se abre un paquete.
Entre cuña y cuña, versos cortos de la tienda contando devoluciones.
Micro-situación: una tienda despacha mil pedidos al mes y una parte llega golpeada, con la caja de otro.
El dolor es del fabricante de empaques: tiene la caja que sí protege y esa tienda no sabe que existe.
Tres apariciones: CRUDA la caja abriéndose con el producto partido (0-5 s, en imagen) · AGRAVADA la pila de
devoluciones creciendo en el mismo rincón (en imagen) · RESUELTA la misma caja abriéndose entera.
Entregables: sección 15 del doc v2 + scripts/guiones/effix_pixar_p15-empaque-protege-musical_v2_por-aprobar.json.
No produzcas nada. Ojo: quita «sesenta mil asistentes», va cifra verificable.
```

### 21 · Contenido para ecommerce

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 21 del ángulo .1.
Público: contenido para ecommerce · Ángulo 21.1: fotos que no venden.
Estilo visual: Animado 2D (bible flat 2D verbatim del ad «La acera», CAMI hace sus propias fotos) ·
Salsa urbana / champeta.
Formato: F7 JINGLE-LOOP — «nadie pregunta» como cuña que entra después de cada foto publicada. Corta,
seca, tres veces, y la cuarta no alcanza a sonar porque ya escribieron.
Micro-situación: sube la foto del producto, la ven trescientas personas, nadie pregunta el precio.
Tres apariciones: CRUDA la foto subida y el chat quieto (0-5 s, en imagen) · AGRAVADA otra foto, más bonita,
el mismo chat quieto (en imagen) · RESUELTA la misma pantalla con mensajes entrando.
Entregables: sección 21 del doc v2 + scripts/guiones/effix_animado_2d_p21-fotos-musical_v2_por-aprobar.json.
No produzcas nada.
```

---

## F2 · CONTEO — 04, 05, 16, 20

### 04 · Vendedores de redes sociales

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 04 del ángulo .1.
Público: vendedores por redes sociales · Ángulo 4.1: demasiados mensajes en WhatsApp.
Estilo visual: Claymation (MARCE, plastilina con huellas, 12 fps, estética Aardman) · Merengue urbano.
Formato: F2 CONTEO — la canción cuenta mensajes sin responder y va acelerando con el conteo: uno, diez,
cien, trescientos. La cuenta se rompe cuando algo empieza a responder por ella.
Micro-situación: once de la noche, trescientos mensajes sin responder, todos preguntando lo mismo.
Tres apariciones: CRUDA el celular en la mano a las once de la noche (0-5 s, en imagen) · AGRAVADA el mismo
celular al otro día con el cliente diciendo que ya compró en otro lado (en imagen) · RESUELTA el mismo celular
boca abajo sobre la mesa mientras entran pedidos.
Entregables: sección 04 del doc v2 + scripts/guiones/effix_claymation_p04-whatsapp-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 05 · Dropshippers

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 05 del ángulo .1.
Público: dropshippers · Ángulo 5.1: encontrar productos ganadores.
Estilo visual: Anime (KAI, cel shading, timing anime de hold y snap) · Latin pop electrónico.
Formato: F2 CONTEO — cuenta los productos que probó y no ganaron: uno, dos… ocho. Cada número es medio verso.
En el noveno la cuenta cambia de sentido porque el producto llega antes que el conteo.
Micro-situación: dos meses buscando el producto ganador, ocho probados que no ganaron.
Tres apariciones: CRUDA el producto probado que no vendió (0-5 s, en imagen) · AGRAVADA la fila de productos
descartados acumulándose, todos iguales de quemados (en imagen) · RESUELTA el producto nuevo en la mano de un
proveedor, antes de que salga en los videos.
Entregables: sección 05 del doc v2 + scripts/guiones/effix_anime_p05-producto-ganador-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 16 · Marketplaces

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 16 del ángulo .1.
Público: marketplaces que necesitan vendedores · Ángulo 16.1: conseguir vendedores.
Estilo visual: Skeleton (bible verbatim) · Reggaetón.
Formato: F2 CONTEO — literal: cuenta con los dedos de una mano los vendedores nuevos del mes. Cinco dedos,
cinco medias líneas. Al final la mano no alcanza.
Micro-situación: abre el panel y los vendedores nuevos del mes se cuentan con una mano.
Tres apariciones: CRUDA la mano contando (0-5 s, en imagen) · AGRAVADA la misma mano el mes siguiente, con
menos dedos levantados y la pauta corriendo (en imagen) · RESUELTA la misma mano que se rinde porque ya no
alcanza a contar.
Entregables: sección 16 del doc v2 + scripts/guiones/effix_skeleton_p16-marketplace-vendedores-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 20 · Atención al cliente

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 20 del ángulo .1.
Público: atención al cliente y customer experience · Ángulo 20.1: demasiados chats.
Estilo visual: Cyberpunk (NICO, neón y lluvia, letreros solo como formas abstractas, nunca texto) ·
Reggaetón oscuro / trap latino.
Formato: F2 CONTEO — cuenta horas, no mensajes: preguntó a las diez, respondiste a las dos. El conteo es un
reloj que avanza en la letra. Se rompe cuando la respuesta sale en segundos.
Micro-situación: el cliente pregunta a las diez, le responde a las dos, y ya compró en otro lado.
Tres apariciones: CRUDA el chat sin responder con la hora encima (0-5 s, en imagen) · AGRAVADA la fila de
chats fríos, todos con horas distintas (en imagen) · RESUELTA el mismo chat respondido al instante.
Entregables: sección 20 del doc v2 + scripts/guiones/effix_cyberpunk_p20-chats-musical_v2_por-aprobar.json.
No produzcas nada.
```

---

## F3 · RELATO EN TERCERA — 10, 18, 27, 28

### 10 · Consultores independientes

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 10 del ángulo .1.
Público: consultores y profesionales independientes de ecommerce · Ángulo 10.1: conseguir clientes.
Estilo visual: Crochet, mundo B&N, solo ANA con color (universal y cierre I2V verbatim) · Cumbia pop.
Formato: F3 RELATO EN TERCERA — «hay una que sabe más que todos y nadie la contrata». Se cuenta como
historia de otra persona; en el último tercio el «ella» se vuelve «tú».
Micro-situación: termina la llamada y el cliente dice que lo va a pensar. Otra vez.
Tres apariciones: CRUDA la llamada colgando (0-5 s, en imagen) · AGRAVADA la misma pantalla con tres llamadas
seguidas terminadas igual (en imagen) · RESUELTA la misma llamada cerrando trato, con la propuesta aceptada.
Entregables: sección 10 del doc v2 + scripts/guiones/effix_crochet_p10-consultor-clientes-musical_v2_por-aprobar.json.
No produzcas nada. Ojo: quita «sesenta mil asistentes» del mecanismo, va cifra verificable.
```

### 18 · Negocios físicos que quieren vender online

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 18 del ángulo .1.
Público: comerciantes y negocios físicos · Ángulo 18.1: tengo tienda física pero no vendo online.
Estilo visual: Claymation (ROSA, continuidad del personaje del ad «La acera») · Merengue urbano.
Formato: F3 RELATO EN TERCERA — «hay una señora en un local de esquina». Tono de cuento de barrio, casi
crónica cantada. El «ella» se vuelve «usted» en el último tercio.
Micro-situación: llovió todo el sábado, no entró nadie, y el mes depende del clima y del andén.
Tres apariciones: CRUDA la puerta del local y la lluvia (0-5 s, en imagen) · AGRAVADA la misma puerta otro
sábado, con el local de al lado despachando cajas (en imagen) · RESUELTA la misma puerta, ahora con pedidos
saliendo aunque llueva.
Entregables: sección 18 del doc v2 + scripts/guiones/effix_claymation_p18-tienda-fisica-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 27 · Networking y alianzas

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 27 del ángulo .1.
Público: empresarios que buscan networking y alianzas · Ángulo 27.1: encontrar socios.
Estilo visual: Cyberpunk (SANTIAGO, neón y lluvia, sin texto en letreros) · Reggaetón oscuro / trap latino.
Formato: F3 RELATO EN TERCERA — «conozco a uno al que le llegó el negocio de su vida». Historia contada de
lejos, con distancia, hasta que en el cierre se descubre que el que escucha es el mismo.
Micro-situación: le llega un negocio grande, lo mira, y sabe que solo no lo puede coger.
Tres apariciones: CRUDA el negocio sobre la mesa y una sola silla (0-5 s, en imagen) · AGRAVADA la misma mesa
con la lista de posibles socios y todos los nombres tachados menos familia (en imagen) · RESUELTA la misma mesa
con dos sillas ocupadas.
Entregables: sección 27 del doc v2 + scripts/guiones/effix_cyberpunk_p27-socios-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 28 · Futuros referentes del ecommerce

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 28 del ángulo .1.
Público: personas que quieren convertirse en referentes del ecommerce · Ángulo 28.1: construir marca personal.
Estilo visual: Animado 2D (bible flat 2D verbatim, JULIÁN) · Salsa urbana / champeta.
Formato: F3 RELATO EN TERCERA — «hay uno que sabe y nadie lo sabe». El relato lo cuenta alguien que lo
conoce y se sorprende. Giro final: el que canta es él mismo.
Micro-situación: alguien le pregunta a qué se dedica, lo explica bien, y le dicen que nunca lo había visto
hablar de eso.
Tres apariciones: CRUDA la conversación y la cara de sorpresa del otro (0-5 s, en imagen) · AGRAVADA su perfil
con fotos de la vida y ningún rastro de lo que sabe (en imagen) · RESUELTA a él hablando frente a una cámara,
con gente escuchando.
Entregables: sección 28 del doc v2 + scripts/guiones/effix_animado_2d_p28-marca-personal-musical_v2_por-aprobar.json.
No produzcas nada.
```

---

## F4 · CARTA CANTADA — 06, 08, 11, 24

### 06 · Marcas, fabricantes e importadores

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 06 del ángulo .1.
Público: marcas, fabricantes e importadores · Ángulo 6.1: llevar una marca al mundo digital.
Estilo visual: Cyberpunk (DON RAMÓN, marca tradicional en mundo cyberpunk, sin texto en letreros) ·
Reggaetón oscuro / trap latino.
Formato: F4 CARTA CANTADA — le canta a su propia marca, como a alguien que quiere y que está desapareciendo.
Segunda persona todo el tiempo: «vos hiciste esto, y hoy no te encuentran».
Micro-situación: busca su marca en el celular y no aparece; la del competidor sí, con ventas online.
Tres apariciones: CRUDA la búsqueda sin resultados (0-5 s, en imagen) · AGRAVADA la misma búsqueda con la
marca del competidor llenando la pantalla (en imagen) · RESUELTA la misma búsqueda, ahora con su marca de primera.
Entregables: sección 06 del doc v2 + scripts/guiones/effix_cyberpunk_p06-marca-digital-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 08 · Marketing y adquisición digital

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 08 del ángulo .1.
Público: marketing, publicidad y adquisición digital · Ángulo 8.1: campañas que dejaron de funcionar.
Estilo visual: Pixar 3D, objeto antropomórfico (PÍXEL, un cuadrito de anuncio) · Latin pop alegre.
Formato: F4 CARTA CANTADA — le canta a la campaña que se le murió, como una despedida. «Vos me vendías
todos los días». Tono de duelo pequeño, no de drama.
Micro-situación: la campaña que vendía todos los días, un martes dejó de vender. Sin cambiar nada.
Tres apariciones: CRUDA la gráfica que cae un martes (0-5 s, en imagen) · AGRAVADA la misma gráfica plana
después de duplicar, cambiar públicos y subir presupuesto (en imagen) · RESUELTA otra gráfica subiendo, con
creativo nuevo, en la misma pantalla.
Entregables: sección 08 del doc v2 + scripts/guiones/effix_pixar_p08-campanas-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 11 · Tecnología y CRM

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 11 del ángulo .1.
Público: tecnología y soluciones para ecommerce (venden CRM) · Ángulo 11.1: CRM.
Estilo visual: Claymation (TOBI, plastilina con huellas, 12 fps) · Merengue urbano.
Formato: F4 CARTA CANTADA — le canta al cliente que hizo la demo, dijo «está muy bueno» y no volvió a
escribir. Es un mensaje que se escribe y no se manda.
Micro-situación: hace demos, le dicen que está muy bueno, y no vuelven a escribir.
Tres apariciones: CRUDA la pantalla de la demo terminando y el «está muy bueno» (0-5 s, en imagen) ·
AGRAVADA el chat sin respuesta semanas después, con el mensaje escrito y sin enviar (en imagen) · RESUELTA
el mismo chat contestando, pero desde un stand, con la tienda al frente.
Entregables: sección 11 del doc v2 + scripts/guiones/effix_claymation_p11-crm-musical_v2_por-aprobar.json.
No produzcas nada. Ojo: quita «sesenta mil asistentes», va cifra verificable.
```

### 24 · Servicios profesionales / impuestos

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 24 del ángulo .1.
Público: dueños de tienda que necesitan servicios profesionales · Ángulo 24.1: impuestos.
Estilo visual: Crochet, mundo B&N, solo DIEGO con color (universal y cierre I2V verbatim) · Cumbia pop.
Formato: F4 CARTA CANTADA — la canción es la respuesta a la carta de impuestos. Le canta a la carta.
Arranca formal, se le quiebra, termina resuelta.
Micro-situación: llega la carta de impuestos y no sabe si debe mucho, poco o nada. Vende bien y no tiene idea.
Tres apariciones: CRUDA la carta sobre la mesa sin abrir (0-5 s, en imagen) · AGRAVADA la misma carta abierta
al lado de tres pantallas con cifras que no cuadran (en imagen) · RESUELTA la misma mesa ordenada, un solo
número claro.
Entregables: sección 24 del doc v2 + scripts/guiones/effix_crochet_p24-impuestos-musical_v2_por-aprobar.json.
No produzcas nada.
```

---

## F5 · CORO MUTANTE — 12, 14, 17, 22

### 12 · Medios de pago y fintech

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 12 del ángulo .1.
Público: medios de pago y fintech (le venden checkout a las tiendas) · Ángulo 12.1: checkout.
Estilo visual: Anime (MIA, cel shading, hold y snap) · Latin pop electrónico.
Formato: F5 CORO MUTANTE — misma melodía tres veces: «se van en el último paso» → «¿y si no era el precio?»
→ «se quedaron en el último paso». La letra cambia, la melodía no.
Micro-situación: una tienda pierde clientes en el pago, con otra pasarela, y no sabe que MIA existe.
Tres apariciones: CRUDA el carrito abandonado en el paso final (0-5 s, en imagen) · AGRAVADA la misma pantalla
repetida en varias tiendas a la vez (en imagen) · RESUELTA el mismo paso final completándose.
Entregables: sección 12 del doc v2 + scripts/guiones/effix_anime_p12-checkout-musical_v2_por-aprobar.json.
No produzcas nada. Ojo: quita «sesenta mil asistentes», va cifra verificable.
```

### 14 · Proveedores de dropshipping

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 14 del ángulo .1.
Público: proveedores de dropshipping · Ángulo 14.1: conseguir vendedores.
Estilo visual: Animado 2D (bible flat 2D verbatim, DON JAIME) · Salsa urbana / champeta.
Formato: F5 CORO MUTANTE — «vendedores de a uno» → «¿dónde están los que buscan?» → «vendedores de a cien».
Mismo estribillo, tres estados.
Micro-situación: bodega llena y catálogo listo, y los mismos veinte vendedores de siempre mueven la mitad.
Tres apariciones: CRUDA la bodega llena y un solo vendedor entrando (0-5 s, en imagen) · AGRAVADA el catálogo
publicado en grupos con un solo mensaje nuevo (en imagen) · RESUELTA la misma bodega con fila de vendedores.
Entregables: sección 14 del doc v2 + scripts/guiones/effix_animado_2d_p14-conseguir-vendedores-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 17 · Internacionalización

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 17 del ángulo .1.
Público: internacionalización y expansión · Ángulo 17.1: vender en otro país.
Estilo visual: Crochet, mundo B&N, solo PABLO con color (universal y cierre I2V verbatim) · Cumbia pop.
Formato: F5 CORO MUTANTE — «todavía no vendo allá» → «¿y si ya podía?» → «ya vendo allá». Mismo estribillo,
tres respuestas a la misma pregunta.
Micro-situación: le preguntan si vende en otro país y dice que todavía no, sin saber por dónde empezar.
Tres apariciones: CRUDA la pregunta y el «todavía no» (0-5 s, en imagen) · AGRAVADA la búsqueda de cómo
exportar llena de requisitos y ninguna persona (en imagen) · RESUELTA la misma pregunta con otra respuesta y
un aliado al lado.
Entregables: sección 17 del doc v2 + scripts/guiones/effix_crochet_p17-otro-pais-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 22 · Desarrollo e integraciones

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 22 del ángulo .1.
Público: desarrollo, programación e integraciones · Ángulo 22.1: APIs.
Estilo visual: Pixar 3D, objeto antropomórfico (ENCHUFE, un conector) · Latin pop alegre.
Formato: F5 CORO MUTANTE — «no se hablan» → «¿y si me presentan?» → «ya se hablan». Tres veces el mismo
estribillo, misma melodía.
Micro-situación: una tienda lo llama porque plataforma, pasarela y logística no se hablan, y alguien copia
pedidos a mano.
Tres apariciones: CRUDA los tres sistemas de espaldas y el pedido copiado a mano (0-5 s, en imagen) ·
AGRAVADA la misma escena con otro cliente y otras tres herramientas distintas (en imagen) · RESUELTA los
mismos tres conectados y el pedido pasando solo.
Entregables: sección 22 del doc v2 + scripts/guiones/effix_pixar_p22-apis-musical_v2_por-aprobar.json.
No produzcas nada.
```

---

## F1 · PREGÓN Y RESPUESTA — 09, 13, 25, 26

### 09 · Creadores que quieren vender

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 09 del ángulo .1.
Público: creadores de contenido e influencers que venden · Ángulo 9.1: convertir audiencia en ventas.
Estilo visual: Skeleton (bible verbatim) · Reggaetón.
Formato: F1 PREGÓN Y RESPUESTA — él lanza «cien mil vistas», el coro responde «cero ventas». Tres llamadas,
tres respuestas distintas; la tercera respuesta ya no es el reproche.
Micro-situación: sube un video, lo ven cien mil personas, y vende cero.
Tres apariciones: CRUDA el contador de vistas subiendo y el de ventas en cero (0-5 s, en imagen) · AGRAVADA
los comentarios de «qué lindo» y ningún pedido (en imagen) · RESUELTA la misma pantalla con el contador de
ventas moviéndose.
Entregables: sección 09 del doc v2 + scripts/guiones/effix_skeleton_p09-audiencia-ventas-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 13 · Logística y última milla

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 13 del ángulo .1.
Público: logística, fulfillment y última milla (buscan tiendas) · Ángulo 13.1: pedidos atrasados.
Estilo visual: Cyberpunk (RUTA, mensajera de última milla, neón y lluvia, sin texto) · Reggaetón oscuro /
trap latino.
Formato: F1 PREGÓN Y RESPUESTA — la ciudad pregunta «¿dónde está mi pedido?» y RUTA responde. Tres veces,
con la respuesta cada vez más corta hasta que es «ya llegó».
Micro-situación: una tienda pierde un cliente porque el pedido llegó tarde, con su operador, no con RUTA.
El dolor es de RUTA: entrega a tiempo, tiene flota y bodega, y opera a media máquina.
Tres apariciones: CRUDA el pedido tarde y el cliente que no vuelve (0-5 s, en imagen) · AGRAVADA la flota de
RUTA quieta mientras otra reparte mal (en imagen) · RESUELTA la misma puerta con la entrega a tiempo.
Entregables: sección 13 del doc v2 + scripts/guiones/effix_cyberpunk_p13-pedidos-atrasados-musical_v2_por-aprobar.json.
No produzcas nada.
```

### 25 · Educación y formación

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 25 del ángulo .1.
Público: personas que quieren aprender ecommerce · Ángulo 25.1: aprender ecommerce.
Estilo visual: Claymation (LUCÍA, plastilina con huellas, 12 fps) · Merengue urbano.
Formato: F1 PREGÓN Y RESPUESTA — ella pregunta «¿por dónde empiezo?» y le contestan mil voces distintas a la
vez, que es justo el problema. En la tercera vuelta le responde una sola voz.
Micro-situación: quiere aprender ecommerce, busca por dónde, y hay mil cursos, mil videos y ningún primer paso.
Tres apariciones: CRUDA la pantalla llena de cursos y ninguno empezado (0-5 s, en imagen) · AGRAVADA la
libreta llena de teoría y ninguna tienda vista por dentro (en imagen) · RESUELTA ella adentro de una tienda
real viendo cómo se opera.
Entregables: sección 25 del doc v2 + scripts/guiones/effix_claymation_p25-aprender-musical_v2_por-aprobar.json.
No produzcas nada. Ojo: este público y el 01 comparten dolor de «por dónde»: diferéncialos, aquí el foco es
aprender para trabajar en el sector, no montar tienda propia.
```

### 26 · Ejecutivos y transformación digital

```
Lee outputs/REGLAS-ANGULO1-V2.md completo y aplícalo. Reescribe SOLO el público 26 del ángulo .1.
Público: ejecutivos y líderes de transformación empresarial · Ángulo 26.1: transformación digital.
Estilo visual: Anime (RICARDO, cel shading, hold y snap) · Latin pop electrónico.
Formato: F1 PREGÓN Y RESPUESTA — la junta pregunta «¿cómo vamos?» y él responde con la misma frase cada
trimestre. Tres preguntas, tres respuestas; la tercera por fin es distinta.
Micro-situación: la junta aprobó la transformación digital hace un año y lo único que hay es una presentación.
Tres apariciones: CRUDA la presentación proyectada en la sala (0-5 s, en imagen) · AGRAVADA la misma
diapositiva un año después, con la fecha cambiada (en imagen) · RESUELTA un proceso real funcionando en
pantalla en vez de la diapositiva.
Entregables: sección 26 del doc v2 + scripts/guiones/effix_anime_p26-transformacion-musical_v2_por-aprobar.json.
No produzcas nada.
```

---

## Prompt de producción (cuando el guion ya tiene JSON)

```
Lee CLAUDE.md §3 y §4b, docs/FORMATO-GUION.md y la última entrada de ESTADO.md.
Produce esta tanda de musicales v2, uno por uno, en este orden:
  1. scripts/guiones/<archivo 1>_v2_por-aprobar.json
  2. scripts/guiones/<archivo 2>_v2_por-aprobar.json
  3. scripts/guiones/<archivo 3>_v2_por-aprobar.json

Por cada uno: (a) renómbralo a _v2_aprobado.json y pon estado: aprobado, sin tocar letra,
planos ni prompts — la parte creativa viene cerrada desde Cowork; (b) valida las 6 reglas de
FORMATO-GUION.md y muéstrame el costo con parámetros reales (Seedance 1.5 Pro 1080p, clips de
4 s, nano-banana-2); espera mi OK; (c) fases separadas, parando después de cada una:
canción → whisper → me avisas si NO RIMA al oído, si canta mal «Feria Effix» o «quince al
diecinueve», si no alcanza a cantar el outro (el CTA), o si la intro instrumental pasa de 20 s;
héroe → la reviso yo; escenas → clips → montaje con cortes en los golpes (librosa), overlays
Montserrat con texto_pantalla, musica=False, −14 LUFS; (d) QA: 30–60 s, ningún plano < 1,25 s,
y las tres apariciones de la micro-situación reconocibles en imagen (campo
microsituacion_apariciones del JSON); (e) el mp4 se nombra con el campo `nombre_entrega` del
JSON, que ya viene numerado por público (P01_, P02_…): si nombre_de_entrega() no antepone ese
número, ajústala y actualiza CLAUDE.md en el mismo commit; (f) costo real en logs/ y entrega en
ESTADO.md. Solo entonces el siguiente. Presupuesto 5 USD promedio, tope 6 por video.
```
