# Reglas del lote .1 v2 (musical) — leer antes de cada guion

Este archivo es el preámbulo común de los 28 prompts individuales de
`outputs/PROMPTS-INDIVIDUALES-ANGULO1-V2.md`. Cada prompt dice «aplica este archivo».

## Qué se está corrigiendo

El lote v1 (`outputs/GUIONES-MUSICALES-28-publicos-angulo1.md`) tiene los 28 videos con la
misma estructura de canción (Verso 1 → Coro → Verso 2 → Coro → Puente → Outro) y las mismas
12 escenas con los mismos beats. Se leen como el mismo video 28 veces. El v2 mantiene lo
musical y cambia la forma: siete formatos de canción, cuatro públicos cada uno.

## Regla 1 — la micro-situación aparece 3 veces, con función distinta cada vez

No es repetir la misma frase. Son tres apariciones:

- **Cruda** — la escena literal, en los primeros cinco segundos.
- **Agravada** — la misma escena con una vuelta más: otro día, lo que le dijo alguien, lo que
  ya le costó, lo que se dice a sí mismo.
- **Resuelta** — la misma escena al final, invertida, con el mecanismo puesto.

Mínimo **dos de las tres se ven en imagen**: sin sonido, el espectador reconoce que es el
mismo momento tres veces (mismo lugar, mismo objeto, misma acción, distinto resultado).

Antes de escribir letra: construye la micro-situación de siete pasos con la skill
`microsituaciones` (momento → síntoma → reacción → explicación fallida → patrón → causa raíz
→ mecanismo). La base del v1 sirve como punto de partida, no como copia.

## Regla 2 — los siete formatos de canción

- **F1 · PREGÓN Y RESPUESTA** — una voz lanza el dolor, un coro le contesta. La
  micro-situación va en la llamada; la respuesta cambia las tres veces.
- **F2 · CONTEO** — la canción enumera (uno, dos, tres…) lo que ya intentó o lo que se le
  acumula. La micro-situación es el número que se repite hasta que la cuenta se rompe.
- **F3 · RELATO EN TERCERA** — le canta la historia de otro («hay un man que…») y solo al
  final se descubre que es el espectador.
- **F4 · CARTA CANTADA** — le canta a alguien o a algo: a su yo de hace un año, a su marca,
  al cliente que no volvió a escribir. Segunda persona todo el tiempo.
- **F5 · CORO MUTANTE** — el mismo estribillo, misma melodía, tres letras distintas: dolor,
  duda, resuelto.
- **F6 · DOS VOCES** — el que pone excusas contra el que ya lo resolvió. Se interrumpen. La
  micro-situación se ve desde los dos lados.
- **F7 · JINGLE-LOOP** — una frase-gancho cortísima que vuelve como cuña de radio, con versos
  cortos entre repeticiones.

Cada formato lleva su propia arquitectura: dónde entra el estribillo (segundo 6, 10 o 15),
si el CTA se canta o se dice hablado al final, cuántas escenas (10 a 12, nunca más) y la
duración (30 a 60 s). Dos guiones del mismo formato tampoco pueden tener la misma
arquitectura: cambia el punto de entrada del estribillo y el número de escenas.

## Regla 3 — lo que no cambia

- Datos verificables y solo esos: **quince al diecinueve de octubre**, **Plaza Mayor
  Medellín**, **más de trescientas cincuenta empresas**, **más de doscientas conferencias**,
  **más de doscientos ponentes**.
- **«Sesenta mil personas» NO se usa.** Sigue en `datos_sin_verificar` hasta que Effix la
  confirme. El v1 la metió en los públicos 10, 11, 12, 15 y 23: en el v2 se reemplaza por una
  cifra verificable o se saca.
- Números en letras. Español neutro colombiano, nunca voseo.
- Describir la situación, nunca a la persona (regla de Meta).
- Sin descuentos, sin taller de IA. El CTA cierra en compra.
- Texto en pantalla: máximo siete palabras, tiene que funcionar sin sonido.
- Nunca prometer más días de los que da el pase (Pasaporte tres días, evento cinco).
- Reglas de cada estilo visual: las del JSON y de `src/estilos_especiales.py`, verbatim
  (bibles de crochet y skeleton, prohibido «slow»/«deliberate», UGC sin
  cinematic/professional/8k).
- Ritmo: corte cada 1.5 a 2.5 s, piso 1.25 s. Encuadres sin repetir. Texto siempre en post,
  Montserrat.

## Regla 4 — nada de estribillo de marca repetido (corrección del 7 de septiembre de 2026)

La versión anterior de esta regla decía que los 28 cerraran con las mismas dos líneas de marca.
**Estaba mal y se anula.** Fijar el bloque de la feria y el cierre hizo que, del segundo veinte
en adelante, todos los videos sonaran iguales — el mismo «Feria Effix, del quince al diecinueve /
Plaza Mayor, Medellín, la cosa se mueve» y el mismo «compra tu ingreso, dale clic». Del público 07
en adelante:

- **Prohibido repetir el bloque de coro de marca.** Cada guion inventa su propia forma de decir
  cuándo, dónde y qué hay. Ninguna de las tres frases de la feria puede coincidir palabra por
  palabra con las de otro guion del lote.
- **La información entra dentro de la historia, dicha por alguien.** Un cliente que ya tiene su
  entrada, un vecino que fue el año pasado, una cuenta regresiva, una dirección que alguien da,
  una decisión que el personaje toma en voz alta. No un anuncio pegado en la mitad de la canción.
- **El CTA cambia de forma en cada guion, pero siempre cierra en compra.** Puede ser la decisión
  del personaje («compré la mía»), una invitación a otro personaje, un reto, una promesa. Lo que
  no cambia es que quede claro que se compra la entrada, y el overlay del CTA sí se mantiene
  igual en los 28 porque es la marca en pantalla, no la letra.
- **El punto donde entra la feria se mueve.** En unos guiones al cuarenta por ciento del video,
  en otros al sesenta o setenta. Nunca en el mismo segundo que el anterior.
- Lo único que se repite en los 28 es el **dato verificable**: quince al diecinueve de octubre,
  Plaza Mayor Medellín, más de trescientas cincuenta empresas, más de doscientas conferencias,
  más de doscientos ponentes. El nombre «Feria Effix» se canta al menos una vez, con tilde.

El video tiene que entenderse solo y vender: dolor reconocible → esto se resuelve viendo el
negocio real → eso está en la Feria Effix, estos días, en este lugar → compra la entrada.
Si al escucharlo sin ver la pantalla no queda claro qué se compra y para qué, el guion está mal.

## Regla 5 — no se produce nada

Estos prompts son de escritura. No llames fal, ElevenLabs ni ffmpeg, no corras `producir.py`,
no generes canción ni imágenes. Entregas texto: la sección del documento y el JSON. La
producción se pide aparte, después de que Alexander apruebe.

## Entregables por guion

1. Su sección en `outputs/GUIONES-MUSICALES-28-angulo1-v2.md` (crear el archivo en el primer
   guion, agrupado por formato, no por número de público). No tocar el v1.
2. Su JSON en `scripts/guiones/` como `*_v2_por-aprobar.json`, esquema de
   `docs/FORMATO-GUION.md` (formato `lineas`). No tocar los `_20260904_`.
3. Al cierre del guion: tabla de verificación de las tres apariciones (cruda / agravada /
   resuelta) diciendo cuáles se ven en imagen, y costo estimado con `cost_estimator` y
   parámetros reales.

## Reparto de formatos (fijo — no reasignar)

| Formato | Públicos |
|---|---|
| F1 · Pregón y respuesta | 09, 13, 25, 26 |
| F2 · Conteo | 04, 05, 16, 20 |
| F3 · Relato en tercera | 10, 18, 27, 28 |
| F4 · Carta cantada | 06, 08, 11, 24 |
| F5 · Coro mutante | 12, 14, 17, 22 |
| F6 · Dos voces | 01, 07, 19, 23 |
| F7 · Jingle-loop | 02, 03, 15, 21 |

Repartido por afinidad del dolor, y ningún par (estilo visual + formato) se repite en el lote.
