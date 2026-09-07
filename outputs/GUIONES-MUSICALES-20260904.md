# Guiones musicales — 14 nichos · guion 1 · sync musical

*Generado el 4 de septiembre de 2026 · Feria Effix 2026 · para aprobar antes de producir · v2 (ajustes de Alexander)*

Un guion por nicho, en modo **musical sync**: la canción (MiniMax Music 2.6) es la única voz, se transcribe con whisper, se recorta al tramo cantado y el montaje corta en los golpes. Sin locución. Tres formatos rotados para que ningún nicho consecutivo repita estética.

**Cambios v2 (2026-09-04):** coro con «más de trescientas cincuenta empresas / más de sesenta mil asistentes» · CTA cantado y en pantalla «Compra tu ingreso dando clic en el botón» (mismo ad para landing y WhatsApp, sin URL) · #01 abogados reescrito con estructura explícita **dolor (1–5) → giro (6) → solución en Effix (7–12)**, con la misma tienda-cliente como hilo visual. Los otros 13 llevan el coro y el CTA nuevos; su estructura dolor→solución se afina después de aprobar el #01.

⚠️ «Más de sesenta mil asistentes» es dato de Alexander, no está en brand_dna ni en el sitio: confirmar con Effix antes de pautar. Queda declarado en `datos_sin_verificar` de los 14 JSON.

## Cómo aprobar y producir

1. Lee la letra y las 12 escenas. Lo que se cambia es la **letra** (lo que canta) y el **plano** (lo que se ve). Los prompts se regeneran solos.
2. Abre el JSON, cambia `"estado": "por_aprobar"` → `"aprobado"`, y renombra el archivo de `_por-aprobar.json` a `_aprobado.json`.
3. En Claude Code, dentro del repo:

```
produce scripts/guiones/<archivo>_aprobado.json
```

Claude Code valida, estima el costo con parámetros reales, muestra el veredicto y **espera tu OK** antes de gastar. Protocolo en `CLAUDE.md` §4b y `docs/FORMATO-GUION.md`.

**Costo estimado por ad: ~4,55 USD** (canción 0,15 + héroe 0,08 + 12 escenas × 0,08 + 12 clips × 5s × 0,056). Cada regeneración de canción suma 0,15: MiniMax canta mal «Feria Effix» más o menos una de cada tres veces.

## Índice

| # | Nicho | Título | Formato | Personaje | Archivo |
|---|---|---|---|---|---|
| 01 | `abogados` | Tus próximos clientes están en Feria Effix | Pixar 3D | CODIGO | `scripts/guiones/effix_pixar_abogados-musical_20260904_por-aprobar.json` |
| 02 | `agencias_contenido` | Tus próximos clientes no llegan por referido | Skeleton | SKELETON | `scripts/guiones/effix_skeleton_agencias-contenido-musical_20260904_por-aprobar.json` |
| 03 | `agencias_pauta` | Sabes pautar, pero nadie lo sabe | Crochet | TEO | `scripts/guiones/effix_crochet_agencias-pauta-musical_20260904_por-aprobar.json` |
| 04 | `contadores` | Los clientes de ecommerce necesitan contador | Pixar 3D | CALCU | `scripts/guiones/effix_pixar_contadores-musical_20260904_por-aprobar.json` |
| 05 | `dropshipping` | El martes que contesta | Skeleton | SKELETON | `scripts/guiones/effix_skeleton_dropshipping-musical_20260904_por-aprobar.json` |
| 06 | `ecommerce` | Sara y el mismo número | Crochet | SARA | `scripts/guiones/effix_crochet_ecommerce-musical_20260904_por-aprobar.json` |
| 07 | `ia` | Effi copia pedidos a mano | Pixar 3D | EFFI | `scripts/guiones/effix_pixar_ia-musical_20260904_por-aprobar.json` |
| 08 | `importadores` | El contenedor que no rota | Skeleton | SKELETON | `scripts/guiones/effix_skeleton_importadores-musical_20260904_por-aprobar.json` |
| 09 | `laboratorios` | Don Rubén y el precio ajeno | Crochet | RUBEN | `scripts/guiones/effix_crochet_laboratorios-musical_20260904_por-aprobar.json` |
| 10 | `logistica` | Ruta a media máquina | Pixar 3D | RUTA | `scripts/guiones/effix_pixar_logistica-musical_20260904_por-aprobar.json` |
| 11 | `networking` | Los mismos cinco | Skeleton | SKELETON | `scripts/guiones/effix_skeleton_networking-musical_20260904_por-aprobar.json` |
| 12 | `referentes` | Tripi y la silla del fondo | Pixar 3D | TRIPI | `scripts/guiones/effix_pixar_referentes-musical_20260904_por-aprobar.json` |
| 13 | `sin_arrancar` | Lana y el pedido de la prima | Crochet | LANA | `scripts/guiones/effix_crochet_sin-arrancar-musical_20260904_por-aprobar.json` |
| 14 | `tienda_ropa` | Rosa y la vitrina mojada | Crochet | ROSA | `scripts/guiones/effix_crochet_tienda-ropa-musical_20260904_por-aprobar.json` |

### Reglas que cumplen los 14

- Canción entre 30 y 60 s de tramo cantado (18 líneas, ~55 s a 96–104 BPM) · corte visual en el golpe, 12 clips de 5 s reencuadrados por `ritmo.py`.
- Coro fijo: «Feria Effix, dieciséis al dieciocho / Plaza Mayor, Medellín / Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / + la línea loop del nicho». La marca se canta completa, nunca fonética.
- Callout de audiencia en las primeras cuatro líneas (describe la situación, nunca a la persona). Sin descuentos, sin código, sin taller, sin URL. Nunca se promete tarima, ni cinco días con el pase de 3.
- Verbatim por estilo: Universal positivo/negativo + cierre I2V de crochet; Character Bible bare-bones de skeleton con héroe → edit; Pixar con objeto antropomórfico (regla age-blind). Encuadres distintos en los 12 planos.
- Ningún prompt pide `slow`/`deliberate`; todos cierran con `no discernible speech`. Texto en pantalla ≤ 7 palabras, en post con Montserrat.

---

## 01 · Tus próximos clientes están en Feria Effix  —  `abogados` · Pixar 3D

**Personaje:** CODIGO — CÓDIGO, un libro de derecho con ojos: es el abogado. TIENDA, un carrito de compras con ojos: es la tienda online que necesita abogado. Objetos a propósito (regla age-blind).  
**Gancho:** callout#36 · callout, dejar_de_ganar · **Música:** upbeat orchestral pop, playful pizzicato strings, bright brass hits · 104 BPM

**Micro-situación**  
*Momento.* Ves una consulta sobre términos y condiciones de una tienda online, y te das cuenta de que no sabes ni por dónde cotizarla.  
*Síntoma.* No es que no sepas derecho. Es que ese modelo tiene preguntas que en la facultad nunca aparecieron.  
*Explicación fallida.* Te dices que es un nicho pequeño, que todavía no justifica meterse.  
*Patrón.* Pero cada año hay más tiendas, más pasarelas, más plata moviéndose sin abogado que la acompañe.  
*Causa raíz.* No es un nicho pequeño. Es un nicho al que no has ido a mostrarte.  
*Mecanismo.* Trescientas cincuenta empresas digitales en un recinto, y casi ninguna tiene abogado propio.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Eres abogado, y te escribe una tienda online
Necesita contratos, y no sabes ni qué cobrarle
Si eres abogado y todavía no tienes clientes de ecommerce
Este video es para ti

[Verso 2]
Cada día abren más tiendas por internet
Necesitan contratos, términos y todo en regla
Y casi ninguna tiene abogado

[Pre-coro]
Esos clientes existen
Solo tienes que ir a donde están

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Ahí están tus próximos clientes

[Verso 3]
Ahí están las tiendas que hoy no tienen abogado
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Ahí están tus próximos clientes
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Eres abogado, y te escribe una tienda online / Necesita contratos, y no sabes ni qué cobrarle | Una tienda te pide ayuda | PROBLEMA · Una tienda online le pide ayuda al abogado y él no sabe qué cobrar | gentle push-in |
| 02 | CALLOUT | Si eres abogado y todavía no tienes clientes de ecommerce / Este video es para ti | ¿Eres abogado? | A QUIÉN LE HABLA · Abogados sin clientes de ecommerce | locked |
| 03 | SINTOMA | Cada día abren más tiendas por internet | Cada día abren más tiendas | PROBLEMA · Cada día abren más tiendas online | locked |
| 04 | EXPL_FALLIDA | Necesitan contratos, términos y todo en regla | Necesitan contratos y términos | PROBLEMA · Necesitan contratos, términos y todo en regla | locked |
| 05 | PATRON | Y casi ninguna tiene abogado | Casi ninguna tiene abogado | PROBLEMA · Casi ninguna tienda tiene abogado | gentle aerial drift forward |
| 06 | CAUSA_RAIZ | Esos clientes existen / Solo tienes que ir a donde están | Ve a donde están | GIRO · Esos clientes existen, hay que ir a donde están | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct · Medellín | SOLUCIÓN · Feria Effix, Plaza Mayor Medellín, 15 al 19 de octubre | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Ahí están tus próximos clientes | +350 empresas · +60.000 asistentes | SOLUCIÓN · Más de 350 empresas y más de 60.000 asistentes | gentle aerial drift forward |
| 09 | MECANISMO | Ahí están las tiendas que hoy no tienen abogado | Ahí están tus próximos clientes | SOLUCIÓN · Las tiendas que no tienen abogado están ahí, y te buscan | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | SOLUCIÓN · Más de 200 ponencias para aprender de los que ya tienen resultados | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA · Compra tu ingreso dando clic en el botón | locked |
| 12 | LOOP | Ahí están tus próximos clientes | Tus clientes están en Feria Effix | CIERRE · Ahora tiene clientes de ecommerce | gentle push-in |

**Notas de producción.** Historia en una frase: un abogado (CÓDIGO) recibe una tienda online (TIENDA) que necesita contratos y no sabe qué cobrarle; cada día abren más tiendas y casi ninguna tiene abogado; en Feria Effix están esas tiendas, hacen fila en su stand y él aprende del gremio en las ponencias. Escenas 1-5 problema, 6 giro, 7-12 solución. TIENDA aparece en 1, 2, 4, 7, 8, 9 y 12: es el hilo. Pixar con objetos (regla age-blind). Cantado, sin voz en off. CTA botón, sin URL. Fechas: las del EVENTO (15-19 oct), factual; la letra no menciona el pase de 3 días, así no se promete duración. 'Eres abogado' es callout de oficio, permitido por Meta (la regla de no describir a la persona aplica a atributos sensibles).

**Producir:** `produce scripts/guiones/effix_pixar_abogados-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 02 · Tus próximos clientes no llegan por referido  —  `agencias_contenido` · Skeleton

**Personaje:** SKELETON — El esqueleto es el dueño de una agencia de contenido (o filmmaker) que vive de que lo recomienden.  
**Gancho:** callout#36 · callout, inclusion · **Música:** latin urban pop, reggaeton groove, dark synth bass · 96 BPM

**Micro-situación**  
*Momento.* Entregas un trabajo del que estás orgulloso, el cliente queda feliz, y aun así no sabes de dónde va a salir el siguiente.  
*Síntoma.* Tu agenda depende de que alguien te recomiende, y eso no lo controlas tú.  
*Explicación fallida.* Te dices que si el trabajo es bueno, los clientes van a llegar solos.  
*Patrón.* Pero llevas años con el trabajo bueno y los meses siguen siendo impredecibles.  
*Causa raíz.* El portafolio no consigue clientes. Los consigue estar en la sala donde ellos deciden.  
*Mecanismo.* Trescientas cincuenta marcas en un recinto, todas necesitando contenido que venda.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Haces videos para marcas, y te quedan muy bien
Pero el próximo cliente solo llega si alguien te recomienda
Si tienes agencia de contenido y vives de referidos
Este video es para ti

[Verso 2]
Un mes tienes tres clientes, y el otro ninguno
Y no puedes planear nada
Porque no controlas quién te recomienda

[Pre-coro]
Las marcas que necesitan videos existen
Solo tienes que estar donde ellas eligen

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Ahí están las marcas que necesitan tus videos

[Verso 3]
Más de trescientas cincuenta marcas buscando quién les haga contenido
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Ahí están las marcas que necesitan tus videos
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Haces videos para marcas, y te quedan muy bien / Pero el próximo cliente solo llega si alguien te recomienda | Quedó bien. ¿Y el próximo cliente? | PROBLEMA · Entrega un video que quedó muy bien y el teléfono no suena | gentle push-in |
| 02 | CALLOUT | Si tienes agencia de contenido y vives de referidos / Este video es para ti | ¿Tienes agencia de contenido? | A QUIÉN LE HABLA · Agencias de contenido que viven de referidos | locked |
| 03 | SINTOMA | Un mes tienes tres clientes, y el otro ninguno | Un mes tres clientes. El otro, ninguno | PROBLEMA · Un mes tres clientes, el otro ninguno | locked |
| 04 | EXPL_FALLIDA | Y no puedes planear nada | No puedes planear | PROBLEMA · No puede planear nada | gentle pull-back |
| 05 | PATRON | Porque no controlas quién te recomienda | No controlas quién te recomienda | PROBLEMA · No controla quién lo recomienda | locked |
| 06 | CAUSA_RAIZ | Las marcas que necesitan videos existen / Solo tienes que estar donde ellas eligen | Ve a donde ellas eligen | GIRO · Las marcas existen, hay que estar donde eligen | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct · Medellín | SOLUCIÓN · Feria Effix, Plaza Mayor, 15 al 19 de octubre | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Ahí están las marcas que necesitan tus videos | +350 empresas · +60.000 asistentes | SOLUCIÓN · Más de 350 empresas y más de 60.000 asistentes | gentle aerial drift forward |
| 09 | MECANISMO | Más de trescientas cincuenta marcas buscando quién les haga contenido | Marcas buscando quién les haga videos | SOLUCIÓN · Marcas buscando quién les haga contenido, de frente | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | SOLUCIÓN · Más de 200 ponencias para aprender de los que ya tienen resultados | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA · Compra tu ingreso dando clic en el botón | locked |
| 12 | LOOP | Ahí están las marcas que necesitan tus videos | Tus clientes están en Feria Effix | CIERRE · Agenda llena sin depender del referido | gentle push-in |

**Notas de producción.** Historia en una frase: una agencia de contenido hace buen trabajo pero solo consigue clientes si alguien la recomienda, así que un mes tiene tres y otro ninguno; en Feria Effix están más de 350 marcas buscando quién les haga contenido, y las ve de frente. Escenas 1-5 problema, 6 giro, 7-12 solución. Skeleton: Character Bible bare_bones verbatim, héroe primero, cada escena referencia la héroe con nano-banana-2/edit, encuadres distintos por plano. Cantado, sin voz en off. CTA botón, sin URL.

**Producir:** `produce scripts/guiones/effix_skeleton_agencias-contenido-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 03 · Sabes pautar, pero nadie lo sabe  —  `agencias_pauta` · Crochet

**Personaje:** TEO — TEO, amigurumi de un trafficker que maneja pauta muy bien y no consigue clientes grandes. Único elemento con color en un mundo blanco y negro de marca.  
**Gancho:** dolor_nombrado#39 · dolor_nombrado, ego · **Música:** acoustic indie pop, ukulele and handclaps, warm and cozy · 100 BPM

**Micro-situación**  
*Momento.* Sacas un resultado bueno de verdad en una cuenta, lo publicas, y no pasa absolutamente nada.  
*Síntoma.* Sabes que manejas el pauta mejor que muchos que facturan el triple, y no logras que eso se note.  
*Explicación fallida.* Te dices que te falta contenido, que hay que publicar más seguido.  
*Patrón.* Pero llevas meses publicando resultados y las cuentas siguen llegando de a una.  
*Causa raíz.* Los que reparten presupuestos grandes no te están viendo el feed. Están en otro lado.  
*Mecanismo.* Trescientas cincuenta empresas en un recinto, muchas decidiendo con quién pautan el año que viene.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Eres trafficker, manejas pauta y logras resultados
Pero las cuentas grandes nunca te llaman
Si manejas pauta y tus clientes siguen siendo pequeños
Este video es para ti

[Verso 2]
Publicas tus resultados, y no pasa nada
Porque los que tienen presupuesto no te ven en redes
Están en otro lado

[Pre-coro]
Las empresas que pautan en grande existen
Solo tienes que estar donde ellas deciden

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Ahí están las cuentas que buscas

[Verso 3]
Más de trescientas cincuenta empresas decidiendo con quién pautan este año
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Ahí están las cuentas que buscas
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Eres trafficker, manejas pauta y logras resultados / Pero las cuentas grandes nunca te llaman | Resultados sí. Cuentas grandes, no | PROBLEMA · Logra resultados y las cuentas grandes no llaman | gentle push |
| 02 | CALLOUT | Si manejas pauta y tus clientes siguen siendo pequeños / Este video es para ti | ¿Manejas pauta? | A QUIÉN LE HABLA · Traffickers con clientes pequeños | locked |
| 03 | SINTOMA | Publicas tus resultados, y no pasa nada | Publicas y no pasa nada | PROBLEMA · Publica sus resultados y no pasa nada | locked |
| 04 | EXPL_FALLIDA | Porque los que tienen presupuesto no te ven en redes | Los grandes no te ven en redes | PROBLEMA · Los que tienen presupuesto no lo ven en redes | gentle pull |
| 05 | PATRON | Están en otro lado | Están en otro lado | PROBLEMA · Están en otro lado | locked |
| 06 | CAUSA_RAIZ | Las empresas que pautan en grande existen / Solo tienes que estar donde ellas deciden | Ve a donde deciden | GIRO · Estar donde ellas deciden | gentle push |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct · Medellín | SOLUCIÓN · Feria Effix, Plaza Mayor, 15 al 19 de octubre | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Ahí están las cuentas que buscas | +350 empresas · +60.000 asistentes | SOLUCIÓN · Más de 350 empresas y más de 60.000 asistentes | gentle drift forward |
| 09 | MECANISMO | Más de trescientas cincuenta empresas decidiendo con quién pautan este año | Deciden con quién pautan. Estás ahí | SOLUCIÓN · Las empresas que deciden con quién pautan, de frente | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | SOLUCIÓN · Más de 200 ponencias para aprender de los que ya tienen resultados | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA · Compra tu ingreso dando clic en el botón | locked |
| 12 | LOOP | Ahí están las cuentas que buscas | Tus cuentas están en Feria Effix | CIERRE · Ahora tiene las cuentas que buscaba | gentle push |

**Notas de producción.** Historia en una frase: un trafficker logra resultados pero las cuentas grandes no lo llaman porque quien tiene presupuesto no lo ve en redes; en Feria Effix esas empresas están de frente decidiendo con quién pautan. Los tres 'de traje' son el hilo: aparecen en 4, 5, 9 y 12. Crochet: mundo diorama B&N estricto (marca), TEO única fuente de color; poses simples, sin dedos; verbatim positivo/negativo/cierre I2V. Cantado, sin voz en off. CTA botón, sin URL. 'Eres trafficker' es callout de oficio.

**Producir:** `produce scripts/guiones/effix_crochet_agencias-pauta-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 04 · Los clientes de ecommerce necesitan contador  —  `contadores` · Pixar 3D

**Personaje:** CALCU — CALCU, una calculadora de escritorio con ojos: es el contador. TIENDA, un carrito de compras con ojos: es la tienda online que necesita contador.  
**Gancho:** dolor_nombrado#33 · dolor_nombrado, dejar_de_ganar · **Música:** upbeat orchestral pop, playful pizzicato strings, bright brass hits · 104 BPM

**Micro-situación**  
*Momento.* Te llega un cliente que vende por internet, te muestra sus movimientos, y por dentro sabes que ese modelo no lo manejas todavía.  
*Síntoma.* Lo atiendes igual, pero te queda la sensación de estar cobrando por algo que estás resolviendo sobre la marcha.  
*Explicación fallida.* Te dices que ya vas a estudiar el tema, cuando baje la temporada.  
*Patrón.* Pero la temporada nunca baja, y cada mes entran más negocios digitales al mercado.  
*Causa raíz.* No te falta estudiar. Te falta estar donde están ellos, y ellos no están en tu oficina.  
*Mecanismo.* Trescientas cincuenta empresas digitales en un solo recinto, todas necesitando quien les cuadre los números.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Eres contador, y te llega un cliente que vende por internet
Te muestra sus ventas, y ese modelo no lo conoces
Si eres contador y todavía no tienes clientes de ecommerce
Este video es para ti

[Verso 2]
Cada día abren más tiendas por internet
Facturan, pagan pasarelas, envían a otros países
Y necesitan quién les cuadre los números

[Pre-coro]
Esos clientes existen
Solo tienes que ir a donde están

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Ahí están tus próximos clientes

[Verso 3]
Ahí están las tiendas que hoy no tienen contador
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Ahí están tus próximos clientes
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Eres contador, y te llega un cliente que vende por internet / Te muestra sus ventas, y ese modelo no lo conoces | Una tienda te trae sus números | PROBLEMA · Una tienda online le trae sus ventas y él no conoce el modelo | gentle push-in |
| 02 | CALLOUT | Si eres contador y todavía no tienes clientes de ecommerce / Este video es para ti | ¿Eres contador? | A QUIÉN LE HABLA · Contadores sin clientes de ecommerce | locked |
| 03 | SINTOMA | Cada día abren más tiendas por internet | Cada día abren más tiendas | PROBLEMA · Cada día abren más tiendas online | locked |
| 04 | EXPL_FALLIDA | Facturan, pagan pasarelas, envían a otros países | Pasarelas, envíos, facturas | PROBLEMA · Facturan, pagan pasarelas, envían a otros países | locked |
| 05 | PATRON | Y necesitan quién les cuadre los números | Necesitan quién les cuadre los números | PROBLEMA · Casi ninguna tiene contador | gentle aerial drift forward |
| 06 | CAUSA_RAIZ | Esos clientes existen / Solo tienes que ir a donde están | Ve a donde están | GIRO · Esos clientes existen, hay que ir a donde están | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct · Medellín | SOLUCIÓN · Feria Effix, Plaza Mayor, 15 al 19 de octubre | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Ahí están tus próximos clientes | +350 empresas · +60.000 asistentes | SOLUCIÓN · Más de 350 empresas y más de 60.000 asistentes | gentle aerial drift forward |
| 09 | MECANISMO | Ahí están las tiendas que hoy no tienen contador | Ahí están tus próximos clientes | SOLUCIÓN · Las tiendas sin contador están ahí y hacen fila | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | SOLUCIÓN · Más de 200 ponencias para aprender de los que ya tienen resultados | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA · Compra tu ingreso dando clic en el botón | locked |
| 12 | LOOP | Ahí están tus próximos clientes | Tus clientes están en Feria Effix | CIERRE · Ahora tiene clientes de ecommerce | gentle push-in |

**Notas de producción.** Historia en una frase: un contador recibe una tienda online cuyo modelo no conoce (pasarelas, envíos, facturación); cada día abren más tiendas y casi ninguna tiene contador; en Feria Effix están esas tiendas y hacen fila en su stand. Misma estructura que #01 (mismo avatar de oficio, misma TIENDA como hilo). Pixar con objetos (age-blind). Cantado, sin voz en off. CTA botón, sin URL.

**Producir:** `produce scripts/guiones/effix_pixar_contadores-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 05 · El martes que contesta  —  `dropshipping` · Skeleton

**Personaje:** SKELETON — El esqueleto: el dropshipper atado a proveedores que no contestan.  
**Gancho:** dolor_nombrado#38 · dolor_nombrado, dejar_de_ganar · **Música:** latin urban pop, reggaeton groove, dark synth bass · 96 BPM

**Micro-situación**  
*Momento.* Le escribes al proveedor un martes para confirmar stock y te contesta el viernes. Ya se te cayó la campaña del fin de semana.  
*Síntoma.* Cada lanzamiento te toca hacerlo con los dedos cruzados, porque no sabes si el producto va a llegar como en la foto.  
*Explicación fallida.* Te dices que te tocó uno malo, que el siguiente va a ser distinto.  
*Patrón.* Pero es el cuarto proveedor del año y el ciclo es exactamente el mismo.  
*Causa raíz.* Los estás eligiendo por foto y por WhatsApp. Nunca le has visto la cara a ninguno.  
*Mecanismo.* En la feria están con stand, con muestra física, y les preguntas de frente lo que quieras.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Le escribes al proveedor un martes
Y te contesta el viernes, ya sin campaña
Si haces dropshipping y dependes de proveedores que fallan
Esto es para ti, quédate un minuto

[Verso 2]
Cada lanzamiento con los dedos cruzados
Dices que te tocó uno malo, que el próximo
Y es el cuarto del año con el mismo ciclo

[Pre-coro]
Los eliges por foto y por WhatsApp
Nunca le has visto la cara a ninguno

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y el próximo martes ya sabes quién contesta

[Verso 3]
En la feria están con stand y con muestra en la mano
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y el próximo martes ya sabes quién contesta
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Le escribes al proveedor un martes / Y te contesta el viernes, ya sin campaña | Contesta el viernes | Martes: escribe, nadie contesta | gentle push-in |
| 02 | CALLOUT | Si haces dropshipping y dependes de proveedores que fallan / Esto es para ti, quédate un minuto | ¿Proveedores que fallan? | Callout a cámara | locked |
| 03 | SINTOMA | Cada lanzamiento con los dedos cruzados | Dedos cruzados | Cada lanzamiento con los dedos cruzados | locked |
| 04 | EXPL_FALLIDA | Dices que te tocó uno malo, que el próximo | «Me tocó uno malo» | «Me tocó uno malo» | gentle pull-back |
| 05 | PATRON | Y es el cuarto del año con el mismo ciclo | El cuarto del año | El cuarto del año, mismo ciclo | locked |
| 06 | CAUSA_RAIZ | Los eliges por foto y por WhatsApp / Nunca le has visto la cara a ninguno | Nunca les viste la cara | El clic: nunca les has visto la cara | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y el próximo martes ya sabes quién contesta | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle aerial drift forward |
| 09 | MECANISMO | En la feria están con stand y con muestra en la mano | Con la muestra en la mano | El producto en la mano, el proveedor de frente | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y el próximo martes ya sabes quién contesta | Ya sabes quién contesta | Loop: el próximo martes ya sabes quién contesta | gentle push-in |

**Notas de producción.** Skeleton musical. Bible verbatim, héroe → edit. Encuadres variados a mano. Sin voz en off.

**Producir:** `produce scripts/guiones/effix_skeleton_dropshipping-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 06 · Sara y el mismo número  —  `ecommerce` · Crochet

**Personaje:** SARA — SARA, amigurumi de la dueña de tienda online estancada. Única con color.  
**Gancho:** callout#6 · callout, dejar_de_ganar · **Música:** acoustic indie pop, ukulele and handclaps, warm and cozy · 100 BPM

**Micro-situación**  
*Momento.* Cierras el mes, abres el panel, y el número se parece demasiado al del mes pasado. Y al del anterior.  
*Síntoma.* No es que la tienda esté mal. Es que hiciste todo lo que sabías hacer y ya no se te ocurre qué más mover.  
*Explicación fallida.* Le echas la culpa al mercado, a la competencia, a que el producto ya se quemó.  
*Patrón.* Pero ves otras tiendas con tu mismo producto creciendo, y esa explicación deja de servirte.  
*Causa raíz.* Lo que te falta no está adentro de tu tienda. Está en las conversaciones a las que no has llegado.  
*Mecanismo.* Más de trescientas cincuenta empresas en un recinto: proveedores, software, logística, agencias.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Cierras el mes, abres el panel
Y el número se parece al del mes pasado
Si tu tienda vende pero lleva meses en el mismo número
Esto es para ti, quédate un minuto

[Verso 2]
Hiciste todo lo que sabías y no se te ocurre qué más
Le echas la culpa al mercado, al producto
Y ves otras tiendas con lo mismo creciendo

[Pre-coro]
Lo que te falta no está adentro de tu tienda
Está en las conversaciones a las que no has llegado

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y el próximo cierre ya no se parece

[Verso 3]
Trescientas cincuenta empresas: proveedores, software, logística, agencias
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y el próximo cierre ya no se parece
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Cierras el mes, abres el panel / Y el número se parece al del mes pasado | El mismo número | El número se parece al del mes pasado | gentle push |
| 02 | CALLOUT | Si tu tienda vende pero lleva meses en el mismo número / Esto es para ti, quédate un minuto | ¿Meses en el mismo número? | Callout | locked |
| 03 | SINTOMA | Hiciste todo lo que sabías y no se te ocurre qué más | ¿Qué más mover? | Ya no se te ocurre qué más | locked |
| 04 | EXPL_FALLIDA | Le echas la culpa al mercado, al producto | «Es el mercado» | «Es el mercado, es el producto» | gentle pull |
| 05 | PATRON | Y ves otras tiendas con lo mismo creciendo | Las otras sí crecen | Otras tiendas con lo mismo, creciendo | locked |
| 06 | CAUSA_RAIZ | Lo que te falta no está adentro de tu tienda / Está en las conversaciones a las que no has llegado | Conversaciones que no has tenido | El clic: conversaciones a las que no has llegado | gentle push |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y el próximo cierre ya no se parece | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle drift forward |
| 09 | MECANISMO | Trescientas cincuenta empresas: proveedores, software, logística, agencias | Proveedores · software · logística | Proveedores, software, logística, agencias | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y el próximo cierre ya no se parece | Ya no se parece | Loop: el próximo cierre ya no se parece | gentle push |

**Notas de producción.** Crochet B&N + SARA en color. Poses simples. Sin voz en off. Verbatim de crochet en todos los prompts.

**Producir:** `produce scripts/guiones/effix_crochet_ecommerce-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 07 · Effi copia pedidos a mano  —  `ia` · Pixar 3D

**Personaje:** EFFI — EFFI, la caja de cartón antropomórfica del ad Pixar de 2026-08-28 (continuidad de personaje). BIT, esfera de IA cyan, secundario.  
**Gancho:** dolor_nombrado#14 · dolor_nombrado, aprendizaje · **Música:** upbeat orchestral pop, playful pizzicato strings, bright brass hits · 104 BPM

**Micro-situación**  
*Momento.* Abres LinkedIn y el tercer post seguido es de alguien que automatizó algo con inteligencia artificial. Cierras la app y vuelves a copiar pedidos a mano.  
*Síntoma.* No es que no entiendas la tecnología. Es que cada vez que te sientas a probarla no sabes por dónde empezar y terminas usándola para escribir textos.  
*Explicación fallida.* Te dices que primero tienes que ordenar el negocio, y después sí te metes con eso.  
*Patrón.* Pero llevas todo el año diciéndolo, y en ese año salieron tres herramientas que ya usa medio mercado.  
*Causa raíz.* El problema no es la herramienta. Es que nadie te ha sentado cuatro horas a montarla contigo, desde cero, en tu negocio.  
*Mecanismo.* En la feria están las agencias de inteligencia artificial que ya la aplican para vender, y te muestran cómo lo hacen.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Abres el celular y el tercer post es de inteligencia artificial
Lo cierras y vuelves a copiar pedidos a mano
Si vendes por internet y la IA te está dejando atrás
Esto es para ti, quédate un minuto

[Verso 2]
No es que no entiendas, es que no sabes por dónde empezar
Dices que primero ordenas el negocio
Y en ese año salieron tres herramientas que ya usa medio mercado

[Pre-coro]
El problema no es la herramienta
Es que nadie se ha sentado contigo a montarla

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y el próximo post ya no te duele

[Verso 3]
Las agencias que ya venden con inteligencia artificial te muestran cómo
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y el próximo post ya no te duele
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Abres el celular y el tercer post es de inteligencia artificial / Lo cierras y vuelves a copiar pedidos a mano | Copiando pedidos a mano | Effi ve el post de IA y vuelve a copiar a mano | gentle push-in |
| 02 | CALLOUT | Si vendes por internet y la IA te está dejando atrás / Esto es para ti, quédate un minuto | ¿La IA te deja atrás? | Callout a cámara | locked |
| 03 | SINTOMA | No es que no entiendas, es que no sabes por dónde empezar | ¿Por dónde empezar? | No sabe por dónde empezar | locked |
| 04 | EXPL_FALLIDA | Dices que primero ordenas el negocio | «Primero ordeno el negocio» | «Primero ordeno el negocio» | gentle pull-back |
| 05 | PATRON | Y en ese año salieron tres herramientas que ya usa medio mercado | Tres herramientas ya | Tres herramientas que ya usa medio mercado | locked |
| 06 | CAUSA_RAIZ | El problema no es la herramienta / Es que nadie se ha sentado contigo a montarla | Nadie se ha sentado contigo | El clic: nadie se ha sentado contigo | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y el próximo post ya no te duele | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle aerial drift forward |
| 09 | MECANISMO | Las agencias que ya venden con inteligencia artificial te muestran cómo | Te muestran cómo | Le muestran cómo lo hacen | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y el próximo post ya no te duele | Ya no te duele | Loop: el próximo post ya no duele | gentle push-in |

**Notas de producción.** Continuidad de EFFI y BIT del ad Pixar del 2026-08-28: usar el character sheet en referencias/personajes/ como imagen héroe. Cantado, sin voz en off. El laptop del stand es el tercer personaje: límite de Seedance (3), OK en Kling.

**Producir:** `produce scripts/guiones/effix_pixar_ia-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 08 · El contenedor que no rota  —  `importadores` · Skeleton

**Personaje:** SKELETON — El esqueleto: el importador con bodega llena y dos clientes.  
**Gancho:** dolor_nombrado#33 · dolor_nombrado, dejar_de_ganar · **Música:** latin urban pop, reggaeton groove, dark synth bass · 96 BPM

**Micro-situación**  
*Momento.* Llega el contenedor, entra a bodega, y todavía no sabes con seguridad quién te va a rotar la mitad de eso.  
*Síntoma.* Dependes de dos o tres clientes de siempre, y si uno se demora, se te queda la plata quieta en el piso.  
*Explicación fallida.* Te dices que es normal en este negocio, que así funciona para todos.  
*Patrón.* Pero llevas trimestres con inventario parado mientras hay tiendas buscando exactamente lo que tienes.  
*Causa raíz.* No te falta producto ni te falta precio. Te faltan compradores, y están todos en el mismo sitio tres días.  
*Mecanismo.* Trescientas cincuenta empresas, muchas comprando producto para vender por internet.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Llega el contenedor, entra a bodega
Y no sabes quién te rota la mitad
Si importas y dependes de dos o tres clientes
Esto es para ti, quédate un minuto

[Verso 2]
Si uno se demora, la plata se queda en el piso
Dices que es normal, que así es este negocio
Y hay tiendas buscando justo lo que tienes

[Pre-coro]
No te falta producto ni precio
Te faltan compradores, y están todos ahí

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y el próximo contenedor ya sabes quién lo mueve

[Verso 3]
Trescientas cincuenta empresas comprando producto para vender online
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y el próximo contenedor ya sabes quién lo mueve
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Llega el contenedor, entra a bodega / Y no sabes quién te rota la mitad | ¿Quién rota la mitad? | Llega el contenedor, no hay quién lo rote | gentle push-in |
| 02 | CALLOUT | Si importas y dependes de dos o tres clientes / Esto es para ti, quédate un minuto | ¿Dependes de dos clientes? | Callout a cámara | locked |
| 03 | SINTOMA | Si uno se demora, la plata se queda en el piso | Plata quieta en el piso | La plata quieta en el piso | locked |
| 04 | EXPL_FALLIDA | Dices que es normal, que así es este negocio | «Así es este negocio» | «Así es este negocio» | gentle pull-back |
| 05 | PATRON | Y hay tiendas buscando justo lo que tienes | Tiendas buscando lo tuyo | Hay tiendas buscando lo que tienes | locked |
| 06 | CAUSA_RAIZ | No te falta producto ni precio / Te faltan compradores, y están todos ahí | Están todos ahí | El clic: los compradores están todos ahí | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y el próximo contenedor ya sabes quién lo mueve | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle aerial drift forward |
| 09 | MECANISMO | Trescientas cincuenta empresas comprando producto para vender online | Compran para vender online | Compradores que venden online | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y el próximo contenedor ya sabes quién lo mueve | Ya sabes quién lo mueve | Loop: el próximo contenedor ya tiene quién | gentle push-in |

**Notas de producción.** Skeleton musical. Bible verbatim, héroe → edit, encuadres a mano. Sin voz en off. Cuidado: 'Nadie compra en la feria' es el defecto del nicho — la escena 9 muestra interés y muestras, no compra cerrada.

**Producir:** `produce scripts/guiones/effix_skeleton_importadores-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 09 · Don Rubén y el precio ajeno  —  `laboratorios` · Crochet

**Personaje:** RUBEN — DON RUBÉN, amigurumi del fabricante que vende por terceros. Único con color.  
**Gancho:** dolor_nombrado#33 · dolor_nombrado, dejar_de_ganar · **Música:** acoustic indie pop, ukulele and handclaps, warm and cozy · 100 BPM

**Micro-situación**  
*Momento.* Ves tu propio producto en una tienda online, a un precio que te sorprende, y esa diferencia no llega a tu cuenta.  
*Síntoma.* Fabricas bien. Cumples. Pero el que se queda con el margen es el que sabe vender por internet, no el que hace el producto.  
*Explicación fallida.* Te dices que lo tuyo es producir, que vender en línea es otro oficio.  
*Patrón.* Pero llevas años viendo cómo ese otro oficio se queda con la parte más grande.  
*Causa raíz.* No necesitas volverte experto en marketing. Necesitas a los que ya lo son, trabajando para ti.  
*Mecanismo.* Agencias de tráfico, creadores de contenido y operadores logísticos, todos en el mismo recinto.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Ves tu propio producto en una tienda online
A un precio que no llega a tu cuenta
Si fabricas y otro se queda con el margen
Esto es para ti, quédate un minuto

[Verso 2]
Fabricas bien, cumples, y el margen es del que vende
Dices que lo tuyo es producir, no vender en línea
Y llevas años viendo cómo ese oficio se lleva la parte grande

[Pre-coro]
No necesitas volverte experto en marketing
Necesitas a los que ya lo son, trabajando para ti

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y ese precio ya no te molesta

[Verso 3]
Agencias, creadores y logística en el mismo recinto
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y ese precio ya no te molesta
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Ves tu propio producto en una tienda online / A un precio que no llega a tu cuenta | Ese precio no llega a tu cuenta | Su producto, a otro precio | gentle push |
| 02 | CALLOUT | Si fabricas y otro se queda con el margen / Esto es para ti, quédate un minuto | ¿Otro se queda con tu margen? | Callout | locked |
| 03 | SINTOMA | Fabricas bien, cumples, y el margen es del que vende | El margen es del que vende | Fabricas bien y el margen se va | locked |
| 04 | EXPL_FALLIDA | Dices que lo tuyo es producir, no vender en línea | «Lo mío es producir» | «Lo mío es producir» | gentle pull |
| 05 | PATRON | Y llevas años viendo cómo ese oficio se lleva la parte grande | La parte grande, ajena | Años viendo la parte grande irse | locked |
| 06 | CAUSA_RAIZ | No necesitas volverte experto en marketing / Necesitas a los que ya lo son, trabajando para ti | Los que ya saben vender | El clic: los que ya lo son | gentle push |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y ese precio ya no te molesta | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle drift forward |
| 09 | MECANISMO | Agencias, creadores y logística en el mismo recinto | Agencias · creadores · logística | Agencias, creadores, logística | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y ese precio ya no te molesta | Ya no te molesta | Loop: ese precio ya no molesta | gentle push |

**Notas de producción.** Crochet B&N + DON RUBÉN en color. El mecanismo del nicho no es una cifra: son los tres oficios (agencia, creador, logística), por eso el stand tiene tres figuras con objeto. Sin voz en off.

**Producir:** `produce scripts/guiones/effix_crochet_laboratorios-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 10 · Ruta a media máquina  —  `logistica` · Pixar 3D

**Personaje:** RUTA — Una furgoneta de reparto antropomórfica: el operador logístico.  
**Gancho:** callout#36 · callout, inclusion · **Música:** upbeat orchestral pop, playful pizzicato strings, bright brass hits · 104 BPM

**Micro-situación**  
*Momento.* Tienes la flota, tienes la bodega, tienes el equipo listo. Y la operación va a media máquina.  
*Síntoma.* Los clientes que tienes están bien, pero son pocos y crecen despacio, y la capacidad instalada te está costando igual.  
*Explicación fallida.* Te dices que en este negocio los clientes llegan por recomendación, y hay que esperar.  
*Patrón.* Pero llevas trimestres esperando mientras las tiendas que crecen ya eligieron con quién despachan.  
*Causa raíz.* No se trata de esperar. Se trata de estar el fin de semana donde ellas deciden.  
*Mecanismo.* Trescientas cincuenta empresas en un recinto, casi todas despachando producto todos los días.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Tienes la flota, la bodega, el equipo listo
Y la operación va a media máquina
Si mueves paquetes y quieres mover más
Esto es para ti, quédate un minuto

[Verso 2]
Los clientes que tienes son pocos y crecen despacio
Dices que en esto se llega por recomendación
Y las tiendas que crecen ya eligieron con quién despachan

[Pre-coro]
No se trata de esperar
Se trata de estar donde ellas deciden

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y la flota deja de andar a media máquina

[Verso 3]
Trescientas cincuenta empresas despachando producto todos los días
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y la flota deja de andar a media máquina
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Tienes la flota, la bodega, el equipo listo / Y la operación va a media máquina | A media máquina | La bodega lista, la operación a media máquina | gentle push-in |
| 02 | CALLOUT | Si mueves paquetes y quieres mover más / Esto es para ti, quédate un minuto | ¿Mueves paquetes? | Callout a cámara | locked |
| 03 | SINTOMA | Los clientes que tienes son pocos y crecen despacio | Pocos y despacio | Pocos clientes que crecen despacio | tracking alongside |
| 04 | EXPL_FALLIDA | Dices que en esto se llega por recomendación | «Hay que esperar» | «Se llega por recomendación»: esperando | gentle pull-back |
| 05 | PATRON | Y las tiendas que crecen ya eligieron con quién despachan | Ya eligieron con quién | Las tiendas ya eligieron con quién | locked |
| 06 | CAUSA_RAIZ | No se trata de esperar / Se trata de estar donde ellas deciden | Estar donde deciden | El clic: estar donde deciden | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y la flota deja de andar a media máquina | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle aerial drift forward |
| 09 | MECANISMO | Trescientas cincuenta empresas despachando producto todos los días | Despachan todos los días | Tiendas que despachan todos los días | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y la flota deja de andar a media máquina | Máquina completa | Loop: la flota a máquina completa | gentle push-in |

**Notas de producción.** Pixar con vehículo antropomórfico. Héroe primero. Sin voz en off. Los carritos del stand son secundarios.

**Producir:** `produce scripts/guiones/effix_pixar_logistica-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 11 · Los mismos cinco  —  `networking` · Skeleton

**Personaje:** SKELETON — El esqueleto: el empresario cuya agenda es la misma de hace tres años.  
**Gancho:** dolor_nombrado#33 · dolor_nombrado, auto_relevancia · **Música:** latin urban pop, reggaeton groove, dark synth bass · 96 BPM

**Micro-situación**  
*Momento.* Necesitas un proveedor nuevo, abres el WhatsApp, y son los mismos cinco contactos de hace tres años.  
*Síntoma.* Le escribes al de siempre, y te cotiza lo de siempre.  
*Explicación fallida.* Te dices que los buenos negocios salen por referidos, y que eso no se fuerza.  
*Patrón.* Pero tu competencia ya cerró alianza con una empresa que tú ni sabías que existía.  
*Causa raíz.* No es que te falten referidos. Es que llevas años buscando en la misma agenda.  
*Mecanismo.* En la feria están trescientas cincuenta empresas de cinco países, en el mismo recinto, buscando con quién hacer negocios.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Necesitas un proveedor nuevo, abres el WhatsApp
Y son los mismos cinco de hace tres años
Si tienes empresa y buscas aliados o clientes nuevos
Esto es para ti, quédate un minuto

[Verso 2]
Le escribes al de siempre y te cotiza lo de siempre
Dices que los negocios salen por referidos
Y tu competencia ya cerró con alguien que ni conocías

[Pre-coro]
No te faltan referidos
Llevas años buscando en la misma agenda

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y la próxima alianza no sale de tu WhatsApp

[Verso 3]
Trescientas cincuenta empresas de cinco países buscando con quién
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y la próxima alianza no sale de tu WhatsApp
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Necesitas un proveedor nuevo, abres el WhatsApp / Y son los mismos cinco de hace tres años | Los mismos cinco | Los mismos cinco contactos | gentle push-in |
| 02 | CALLOUT | Si tienes empresa y buscas aliados o clientes nuevos / Esto es para ti, quédate un minuto | ¿Buscas aliados nuevos? | Callout a cámara | locked |
| 03 | SINTOMA | Le escribes al de siempre y te cotiza lo de siempre | Lo de siempre | Te cotiza lo de siempre | locked |
| 04 | EXPL_FALLIDA | Dices que los negocios salen por referidos | «Salen por referidos» | «Salen por referidos» | gentle pull-back |
| 05 | PATRON | Y tu competencia ya cerró con alguien que ni conocías | Tu competencia ya cerró | La competencia ya cerró | locked |
| 06 | CAUSA_RAIZ | No te faltan referidos / Llevas años buscando en la misma agenda | La misma agenda | El clic: la misma agenda | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y la próxima alianza no sale de tu WhatsApp | +350 empresas · +60.000 asistentes | 350 empresas de 5 países | gentle aerial drift forward |
| 09 | MECANISMO | Trescientas cincuenta empresas de cinco países buscando con quién | Con quién hacer negocios | Buscando con quién hacer negocios | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y la próxima alianza no sale de tu WhatsApp | No sale de tu WhatsApp | Loop: la próxima alianza no sale del WhatsApp | locked |

**Notas de producción.** Skeleton musical del nicho 27 (ángulo 27.2). Complementa a 'La agenda' (micro_doc_ugc narrado). Bible verbatim, héroe → edit. Sin voz en off.

**Producir:** `produce scripts/guiones/effix_skeleton_networking-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 12 · Tripi y la silla del fondo  —  `referentes` · Pixar 3D

**Personaje:** TRIPI — Un celular en trípode antropomórfico: el que sabe y graba solo. NUNCA se le pone en tarima ni con micrófono.  
**Gancho:** dolor_nombrado#39 · dolor_nombrado, ego · **Música:** upbeat orchestral pop, playful pizzicato strings, bright brass hits · 104 BPM

**Micro-situación**  
*Momento.* Ves a alguien en tarima explicando lo que tú aplicas hace años, y la sala entera tomando nota.  
*Síntoma.* Grabas un video contando lo mismo, y lo ven los de siempre.  
*Explicación fallida.* Te dices que primero toca tener más resultados, y después mostrarse.  
*Patrón.* Pero el que está en tarima no sabe más que tú. Se puso donde lo vieran.  
*Causa raíz.* No te falta conocimiento. Te falta estar en el lugar donde están los que ya son referentes.  
*Mecanismo.* En la feria están doscientos ponentes de más de veinte países y trescientas cincuenta marcas, en el mismo recinto.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Ves a alguien en tarima diciendo lo que tú aplicas hace años
Y la sala entera tomando nota
Si sabes de ecommerce y nadie te conoce todavía
Esto es para ti, quédate un minuto

[Verso 2]
Grabas un video contando lo mismo, y lo ven los de siempre
Dices que primero toca tener más resultados
Pero el de la tarima se puso donde lo vieran

[Pre-coro]
No te falta conocimiento
Te falta estar donde están los que ya son

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Nadie se vuelve referente desde la silla

[Verso 3]
Doscientos ponentes de veinte países y trescientas cincuenta marcas
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Nadie se vuelve referente desde la silla
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Ves a alguien en tarima diciendo lo que tú aplicas hace años / Y la sala entera tomando nota | Tú lo aplicas hace años | Tripi en la silla del fondo | locked |
| 02 | CALLOUT | Si sabes de ecommerce y nadie te conoce todavía / Esto es para ti, quédate un minuto | ¿Sabes y no te conocen? | Callout a cámara | locked |
| 03 | SINTOMA | Grabas un video contando lo mismo, y lo ven los de siempre | Lo ven los de siempre | Lo ven los de siempre | gentle push-in |
| 04 | EXPL_FALLIDA | Dices que primero toca tener más resultados | «Primero más resultados» | «Primero más resultados» | gentle pull-back |
| 05 | PATRON | Pero el de la tarima se puso donde lo vieran | Se puso donde lo vieran | El de la tarima se puso donde lo vieran | locked |
| 06 | CAUSA_RAIZ | No te falta conocimiento / Te falta estar donde están los que ya son | Estar donde están | El clic: estar donde están | locked |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Nadie se vuelve referente desde la silla | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle aerial drift forward |
| 09 | MECANISMO | Doscientos ponentes de veinte países y trescientas cincuenta marcas | Con los que hoy sigues | Grabando con los que sigue (pasillo, no tarima) | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Nadie se vuelve referente desde la silla | Nadie es referente desde la silla | Loop: nadie es referente desde la silla | locked |

**Notas de producción.** REGLA: TRIPI nunca aparece EN tarima ni con micrófono (el pase es de asistente). En la escena 9 graba en pasillo, no en zona de contenido (eso es VIP). Pixar, cantado.

**Producir:** `produce scripts/guiones/effix_pixar_referentes-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 13 · Lana y el pedido de la prima  —  `sin_arrancar` · Crochet

**Personaje:** LANA — LANA, la amigurumi del ad crochet de 2026-08-28 (continuidad: mismo character sheet). Ahora cantado, otro ángulo: la prima.  
**Gancho:** dolor_nombrado#39 · dolor_nombrado, auto_relevancia · **Música:** acoustic indie pop, ukulele and handclaps, warm and cozy · 100 BPM

**Micro-situación**  
*Momento.* Tu tienda lleva noventa días abierta y el único pedido lo hizo tu prima.  
*Síntoma.* Publicas todos los días, revisas el panel, y el contador de ventas no se mueve.  
*Explicación fallida.* Te dices que lo que falta es pauta, que con presupuesto sí arranca.  
*Patrón.* Pusiste la pauta. Y el único pedido volvió a ser de la familia.  
*Causa raíz.* No te falta producto ni presupuesto: te falta que alguien que ya vende te vea el negocio por dentro.  
*Mecanismo.* Trescientas cincuenta empresas y doscientos ponentes que viven de vender por internet, en un solo recinto.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Tu tienda lleva noventa días abierta
Y el único pedido lo hizo tu prima
Si vendes por internet y no llega un desconocido
Esto es para ti, quédate un minuto

[Verso 2]
Publicas todos los días y el contador no se mueve
Dices que falta pauta, que con plata arranca
Pusiste pauta y el pedido volvió a ser familiar

[Pre-coro]
No te falta producto ni presupuesto
Te falta que alguien que ya vende te vea el negocio

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y el próximo pedido no es de tu prima

[Verso 3]
Trescientas cincuenta empresas y doscientos ponentes que viven de vender
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y el próximo pedido no es de tu prima
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Tu tienda lleva noventa días abierta / Y el único pedido lo hizo tu prima | Y era tu prima | Un pedido, y era la prima | gentle push |
| 02 | CALLOUT | Si vendes por internet y no llega un desconocido / Esto es para ti, quédate un minuto | ¿Ningún desconocido compra? | Callout | locked |
| 03 | SINTOMA | Publicas todos los días y el contador no se mueve | El contador no se mueve | Publica y el contador no se mueve | locked |
| 04 | EXPL_FALLIDA | Dices que falta pauta, que con plata arranca | «Con pauta sí arranca» | «Con pauta sí arranca» | gentle pull |
| 05 | PATRON | Pusiste pauta y el pedido volvió a ser familiar | Otra vez familiar | El pedido volvió a ser familiar | locked |
| 06 | CAUSA_RAIZ | No te falta producto ni presupuesto / Te falta que alguien que ya vende te vea el negocio | Que alguien que ya vende te vea | El clic: que alguien que ya vende te vea | gentle push |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y el próximo pedido no es de tu prima | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle drift forward |
| 09 | MECANISMO | Trescientas cincuenta empresas y doscientos ponentes que viven de vender | Te ven el negocio por dentro | Alguien que ya vende le ve el negocio | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y el próximo pedido no es de tu prima | No es de tu prima | Loop: el próximo pedido no es de la prima | gentle push |

**Notas de producción.** Continuidad de LANA (character sheet en referencias/personajes/lana-sheet-v2.jpg). Mismo territorio que el skeleton musical de sin_arrancar pero en crochet y con la prima como ancla visual. Sin voz en off.

**Producir:** `produce scripts/guiones/effix_crochet_sin-arrancar-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*

---

## 14 · Rosa y la vitrina mojada  —  `tienda_ropa` · Crochet

**Personaje:** ROSA — ROSA, versión amigurumi de la dueña del almacén de ropa (personaje del ad 2D 'La acera'). Única con color.  
**Gancho:** dolor_nombrado#39 · dolor_nombrado, auto_relevancia · **Música:** acoustic indie pop, ukulele and handclaps, warm and cozy · 100 BPM

**Micro-situación**  
*Momento.* Llovió todo el sábado, no entró nadie, y ahí caes en cuenta de que tu mes depende del clima y del andén.  
*Síntoma.* Le mandas la foto por WhatsApp a las mismas clientas de siempre, y ya sabes cuáles te van a contestar.  
*Explicación fallida.* Te dices que tu ropa se vende es viéndola, tocándola, midiéndosela.  
*Patrón.* Pero la marca del local de al lado ya la están comprando en otra ciudad. Misma ropa, mismo precio.  
*Causa raíz.* No es que tu ropa no sirva para internet. Es que nadie te ha mostrado cómo se vende ropa por internet.  
*Mecanismo.* En la feria están las plataformas, las pasarelas de pago, la logística y las agencias que ya visten a las tiendas que sí venden online.  

**Letra completa (lo que se canta)**

```
[Verso 1]
Llovió todo el sábado, no entró nadie
Y tu mes depende del clima y del andén
Si tienes almacén de ropa y no vendes por internet
Esto es para ti, quédate un minuto

[Verso 2]
Mandas la foto al grupo de siempre y contesta la de siempre
Dices que tu ropa se vende es viéndola
Y la del local de al lado ya despacha a otra ciudad

[Pre-coro]
No es que tu ropa no sirva para internet
Es que nadie te ha mostrado cómo

[Coro]
Feria Effix, del quince al diecinueve de octubre
Plaza Mayor, Medellín
Más de trescientas cincuenta empresas
Más de sesenta mil asistentes
Y la próxima venta no la hace la vitrina

[Verso 3]
En la feria está quien te monta la tienda y quien despacha
Más de doscientas ponencias para aprender de los que ya tienen resultados

[Outro]
Compra tu ingreso dando clic en el botón
Y la próxima venta no la hace la vitrina
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Plano | Cámara |
|---|---|---|---|---|---|
| 01 | MOMENTO | Llovió todo el sábado, no entró nadie / Y tu mes depende del clima y del andén | Llovió. Y no entró nadie | Llovió y no entró nadie | gentle push |
| 02 | CALLOUT | Si tienes almacén de ropa y no vendes por internet / Esto es para ti, quédate un minuto | ¿Almacén de ropa sin internet? | Callout | locked |
| 03 | SINTOMA | Mandas la foto al grupo de siempre y contesta la de siempre | Contesta la de siempre | El grupo de siempre, la de siempre | locked |
| 04 | EXPL_FALLIDA | Dices que tu ropa se vende es viéndola | «Se vende es viéndola» | «Se vende es viéndola» | gentle pull |
| 05 | PATRON | Y la del local de al lado ya despacha a otra ciudad | La del lado ya despacha | La del lado ya despacha a otra ciudad | locked |
| 06 | CAUSA_RAIZ | No es que tu ropa no sirva para internet / Es que nadie te ha mostrado cómo | Nadie te ha mostrado cómo | El clic: nadie te ha mostrado cómo | gentle push |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve de octubre / Plaza Mayor, Medellín | Feria Effix · 15–19 oct | Llegada a Plaza Mayor | tracking from behind |
| 08 | CORO_FERIA | Más de trescientas cincuenta empresas / Más de sesenta mil asistentes / Y la próxima venta no la hace la vitrina | +350 empresas · +60.000 asistentes | Las 350 empresas | gentle drift forward |
| 09 | MECANISMO | En la feria está quien te monta la tienda y quien despacha | Quien te monta la tienda | Quien monta la tienda y quien despacha | locked |
| 10 | PRUEBA | Más de doscientas ponencias para aprender de los que ya tienen resultados | +200 ponencias: aprende de quien ya vende | 200 ponentes, 5 ediciones | gentle lateral drift |
| 11 | CTA | Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CTA cantado | locked |
| 12 | LOOP | Y la próxima venta no la hace la vitrina | La vitrina ya no vende sola | Loop: la próxima venta no la hace la vitrina | gentle push |

**Notas de producción.** Crochet B&N + ROSA en color (misma dueña del ad 2D 'La acera', en versión amigurumi). Poses simples. Sin voz en off.

**Producir:** `produce scripts/guiones/effix_crochet_tienda-ropa-musical_20260904_aprobado.json` *(tras renombrar y aprobar)*
