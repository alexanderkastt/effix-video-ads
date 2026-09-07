# Feria Effix 2026 — 28 videos musicales (ángulo .1 de cada público)

*Versión 1 · 4 de septiembre de 2026 · canciones latinas pegajosas · 7 estilos visuales · listos para Claude Code*

## Qué es esto

Un video musical por público, sobre el ángulo .1 de cada uno. La canción es la única voz: no hay locución. Cada letra rima, está escrita para cantarse, y menciona el dolor de la micro-situación exactamente tres veces (verso uno, verso dos y outro, ya resuelto). El coro y el puente son fijos en los 28 para que la marca suene igual en toda la campaña: fechas del quince al diecinueve, Plaza Mayor Medellín, más de trescientas cincuenta empresas, sesenta mil personas, doscientas ponencias, y el CTA «compra tu ingreso dando clic en el botón».

**Estructura de cada canción:** Verso 1 (dolor) → Coro → Verso 2 (excusa, patrón, causa, dolor) → Coro → Puente (cifras) → Outro (dolor resuelto + CTA). Doce escenas de cinco segundos: seis de problema, dos de coro (llegada y pabellón), una de mecanismo, una de puente, CTA y cierre.

**Los siete estilos y su música** (rotan en orden, cuatro videos por estilo):

| Estilo | Género | BPM | Regla que no se negocia |
|---|---|---|---|
| Pixar 3D | Latin pop alegre | 108 | Personaje = objeto antropomórfico (regla age-blind). Héroe primero. |
| Skeleton | Reggaetón | 96 | Character Bible verbatim en todos los prompts; héroe → edit; encuadres distintos por plano. |
| Crochet | Cumbia pop | 100 | Universal positivo/negativo y cierre I2V verbatim. Mundo B&N estricto, solo el personaje con color. Poses simples. |
| Claymation | Merengue urbano | 130 | Plastilina con huellas, 12 fps, estética Aardman. |
| Anime | Latin pop electrónico | 104 | Cel shading, timing anime (hold y snap). |
| Cyberpunk | Reggaetón oscuro / trap latino | 92 | Neón y lluvia; letreros solo como formas abstractas, nunca texto. |
| Animado 2D | Salsa urbana / champeta | 98 | Bible flat 2D verbatim del ad «La acera»: línea uniforme, sin gradientes. |

**Costo estimado por video: ~4,55 USD** (canción 0,15 + héroe 0,08 + 12 imágenes × 0,08 + 12 clips × 5 s × 0,056). Cada regeneración de canción suma 0,15. Los 28: ~127 USD más reintentos.

⚠️ «Sesenta mil personas» es dato de Alexander sin fuente pública; está en `datos_sin_verificar` de los 28 JSON. Confirmar con Effix antes de pautar.

## Cómo pedirlos a Claude Code

Los 28 JSON están en `scripts/guiones/` como `_por-aprobar.json`. Se producen de a tres con el `producir.py` construido para el primer musical. Prompt de tanda:

```
Lee CLAUDE.md §3 y §4b, docs/FORMATO-GUION.md y la última entrada de ESTADO.md.
Vamos a producir esta tanda de videos musicales, uno por uno, en este orden:
  1. scripts/guiones/<archivo 1>
  2. scripts/guiones/<archivo 2>
  3. scripts/guiones/<archivo 3>

Por cada uno: (a) renómbralo a _aprobado.json y pon estado: aprobado, sin tocar letra,
planos ni prompts; (b) valida las 6 reglas de FORMATO-GUION.md y muéstrame el costo con
parámetros reales; espera mi OK; (c) fases separadas, parando después de cada una:
canción → whisper → me avisas si NO RIMA al oído, si canta mal «Feria Effix», «sesenta mil»
o «quince al diecinueve», o si la intro instrumental pasa de 20 s (0.15 USD por reintento);
héroe → la reviso yo; escenas → clips → montaje con cortes en los golpes (librosa), overlays
Montserrat con texto_pantalla, musica=False, -14 LUFS; (d) QA: 30-60 s, ningún plano < 1.25 s;
(e) costo real en logs/ y entrega en ESTADO.md. Solo entonces el siguiente.
El estilo de cada JSON tiene reglas propias (campos bible, negative_prompt y notas_produccion):
el productor las lee del JSON, no las inventa. Para claymation, anime y cyberpunk usa el
prefijo/sufijo de src/scene_builder.py si existe; si no, el del JSON. Presupuesto 5 USD
promedio, tope 6 por video.
```

## Índice

| # | Público | Ángulo .1 | Título | Estilo | Género | Archivo |
|---|---|---|---|---|---|---|
| 01 | 🔥 Emprendedores que están comenzando en e-commerce | Cómo empezar a vender por Internet | Quiero vender y no sé por dónde | Pixar 3D (objeto antropomórfico) | Latin pop alegre | `effix_pixar_p01-empezar-musical_20260904_por-aprobar.json` |
| 02 | 🔥 Dueños de tiendas online | Pocas ventas | La tienda que vende poquito | Skeleton | Reggaetón | `effix_skeleton_p02-pocas-ventas-musical_20260904_por-aprobar.json` |
| 03 | 🔥 Empresarios de e-commerce en crecimiento | Pasar de 10 a 100 pedidos diarios | De diez a cien | Crochet (mundo B&N) | Cumbia pop | `effix_crochet_p03-diez-a-cien-musical_20260904_por-aprobar.json` |
| 04 | 🔥 Vendedores de redes sociales | Demasiados mensajes en WhatsApp | Mil mensajes en WhatsApp | Claymation | Merengue urbano | `effix_claymation_p04-whatsapp-musical_20260904_por-aprobar.json` |
| 05 | 🔥 Dropshippers | Encontrar productos ganadores | El producto ganador | Anime | Latin pop electrónico | `effix_anime_p05-producto-ganador-musical_20260904_por-aprobar.json` |
| 06 | 🔥 Marcas, fabricantes e importadores | Llevar una marca al mundo digital | Mi marca no existe en internet | Cyberpunk | Reggaetón oscuro / trap latino | `effix_cyberpunk_p06-marca-digital-musical_20260904_por-aprobar.json` |
| 07 | 🔥 Mayoristas y distribuidores | Digitalizar ventas mayoristas | Pedidos por teléfono | Animado 2D | Salsa urbana / champeta | `effix_animado_2d_p07-mayorista-digital-musical_20260904_por-aprobar.json` |
| 08 | 🔥 Marketing, publicidad y adquisición digital | Campañas que dejaron de funcionar | La campaña que dejó de funcionar | Pixar 3D (objeto antropomórfico) | Latin pop alegre | `effix_pixar_p08-campanas-musical_20260904_por-aprobar.json` |
| 09 | 🔥 Creadores de contenido e influencers que venden | Convertir audiencia en ventas | Muchos seguidores, cero ventas | Skeleton | Reggaetón | `effix_skeleton_p09-audiencia-ventas-musical_20260904_por-aprobar.json` |
| 10 | 🔥 Consultores y profesionales independientes de e-commerce | Conseguir clientes | Sé mucho y nadie me contrata | Crochet (mundo B&N) | Cumbia pop | `effix_crochet_p10-consultor-clientes-musical_20260904_por-aprobar.json` |
| 11 | 🔥 Tecnología y soluciones para e-commerce | CRM | Los clientes que se me pierden | Claymation | Merengue urbano | `effix_claymation_p11-crm-musical_20260904_por-aprobar.json` |
| 12 | 🔥 Medios de pago y Fintech | Checkout | Se van en el último paso | Anime | Latin pop electrónico | `effix_anime_p12-checkout-musical_20260904_por-aprobar.json` |
| 13 | 🔥 Logística, fulfillment y última milla | Pedidos atrasados | Los pedidos que llegan tarde | Cyberpunk | Reggaetón oscuro / trap latino | `effix_cyberpunk_p13-pedidos-atrasados-musical_20260904_por-aprobar.json` |
| 14 | 🔥 Proveedores de dropshipping | Conseguir vendedores | Bodega llena, vendedores de a uno | Animado 2D | Salsa urbana / champeta | `effix_animado_2d_p14-conseguir-vendedores-musical_20260904_por-aprobar.json` |
| 15 | 🔥 Empresas de empaques y packaging | Empaque que protege | Llegó roto | Pixar 3D (objeto antropomórfico) | Latin pop alegre | `effix_pixar_p15-empaque-protege-musical_20260904_por-aprobar.json` |
| 16 | 🔥 Marketplaces | Conseguir vendedores | El marketplace sin vendedores | Skeleton | Reggaetón | `effix_skeleton_p16-marketplace-vendedores-musical_20260904_por-aprobar.json` |
| 17 | 🟡 Internacionalización y expansión de negocios | Vender en otro país | Vender en otro país | Crochet (mundo B&N) | Cumbia pop | `effix_crochet_p17-otro-pais-musical_20260904_por-aprobar.json` |
| 18 | 🟡 Comerciantes y negocios físicos que quieren vender online | Tengo tienda física pero no vendo online | Tengo local y no vendo online | Claymation | Merengue urbano | `effix_claymation_p18-tienda-fisica-musical_20260904_por-aprobar.json` |
| 19 | 🟡 Retail | Omnicanalidad | Dos tiendas que no se hablan | Anime | Latin pop electrónico | `effix_anime_p19-omnicanal-musical_20260904_por-aprobar.json` |
| 20 | 🟡 Atención al cliente y Customer Experience | Demasiados chats | Demasiados chats | Cyberpunk | Reggaetón oscuro / trap latino | `effix_cyberpunk_p20-chats-musical_20260904_por-aprobar.json` |
| 21 | 🟡 Contenido para e-commerce | Fotos que no venden | Fotos que no venden | Animado 2D | Salsa urbana / champeta | `effix_animado_2d_p21-fotos-musical_20260904_por-aprobar.json` |
| 22 | 🟡 Desarrollo, programación e integraciones | APIs | Las plataformas que no se hablan | Pixar 3D (objeto antropomórfico) | Latin pop alegre | `effix_pixar_p22-apis-musical_20260904_por-aprobar.json` |
| 23 | 🟡 Ciberseguridad y prevención de fraude | Fraude en pagos | El pago que era fraude | Skeleton | Reggaetón | `effix_skeleton_p23-fraude-pagos-musical_20260904_por-aprobar.json` |
| 24 | 🟡 Servicios profesionales para e-commerce | Impuestos | Vendo y no sé cuánto debo | Crochet (mundo B&N) | Cumbia pop | `effix_crochet_p24-impuestos-musical_20260904_por-aprobar.json` |
| 25 | 🟡 Educación y formación en e-commerce | Aprender e-commerce | Quiero aprender ecommerce | Claymation | Merengue urbano | `effix_claymation_p25-aprender-musical_20260904_por-aprobar.json` |
| 26 | 🟡 Ejecutivos y líderes de transformación empresarial | Transformación digital | La transformación digital que no llega | Anime | Latin pop electrónico | `effix_anime_p26-transformacion-musical_20260904_por-aprobar.json` |
| 27 | 🔵 Empresarios que buscan networking y alianzas | Encontrar socios | Solo no lo puedo coger | Cyberpunk | Reggaetón oscuro / trap latino | `effix_cyberpunk_p27-socios-musical_20260904_por-aprobar.json` |
| 28 | 🔵 Personas que quieren convertirse en referentes del e-commerce | Construir marca personal | Nadie sabe lo que sé | Animado 2D | Salsa urbana / champeta | `effix_animado_2d_p28-marca-personal-musical_20260904_por-aprobar.json` |

---

## 01 · Quiero vender y no sé por dónde

**Público:** Emprendedores que están comenzando en e-commerce (🔥) · **Ángulo 1.1:** Cómo empezar a vender por Internet  
**Estilo:** Pixar 3D (objeto antropomórfico) · **Música:** Latin pop alegre, 108 BPM  
**Personaje:** NUBE, una nube de ideas antropomórfica: la persona que quiere empezar a vender por internet y no sabe por dónde.  
**Dolor (3 veces en la letra):** «por dónde»

**Micro-situación**  
*Momento.* Quieres vender por internet, abres el portátil, y hay tantas opciones que lo cierras sin hacer nada.  
*Síntoma.* Ves videos, tomas notas, y al final del día no has abierto ni una tienda.  
*Explicación fallida.* Te dices que te falta un curso más.  
*Patrón.* Pero los que ya venden empezaron sin saberlo todo, viendo a alguien hacerlo.  
*Causa raíz.* No te falta información. Te falta ver el negocio real y hablar con quien lo opera.  
*Mecanismo.* En Feria Effix están las plataformas, los proveedores y los que abrieron su tienda el año pasado, en un solo lugar.  

**Letra**

```
[Verso 1]
Quiero vender por internet y no sé por dónde
Abro el portátil y la idea se me esconde
Veo mil videos y ninguno me responde
Cierro la tapa, y otro día se me esconde

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí está el camino que hoy no ves
Entras sin saber, y sales sabiendo qué hacer

[Verso 2]
Me digo que me falta un curso, uno más
Pero el que vende empezó sin saber jamás
Vio a alguien hacerlo, y ahí arrancó de verdad
Yo sigo sin saber por dónde, y el tiempo va

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí está el camino que hoy no ves
Entras sin saber, y sales sabiendo qué hacer

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya sé por dónde, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Quiero vender por internet y no sé por dónde / Abro el portátil y la idea se me esconde | No sé por dónde | NUBE floats over a bedroom desk at night, a laptop open with dozens of tiny glowing tab shapes, lightning bolts popping out of the cloud, a  |
| 02 | CALLOUT | Veo mil videos y ninguno me responde / Cierro la tapa, y otro día se me esconde | ¿Quieres vender por internet? | NUBE turns to face the camera in a small bedroom desk at night with a laptop, a notebook full of crossed-out business ideas still visible. |
| 03 | SINTOMA | Me digo que me falta un curso, uno más | Mil videos, ninguna tienda | Close-up of the notebook: NUBE's tiny arm writes a new idea and immediately crosses it out; a phone beside plays an abstract video. |
| 04 | EXPL_FALLIDA | Pero el que vende empezó sin saber jamás | «Me falta un curso más» | NUBE from behind, watching a shelf where glowing course-box shapes pile up, one more being added. |
| 05 | PATRON | Vio a alguien hacerlo, y ahí arrancó de verdad | Empezaron sin saberlo todo | Low-angle wide: through the window, a neighbour's lit shop-front with a small delivery bike leaving; NUBE small at the glass. |
| 06 | CAUSA_RAIZ | Yo sigo sin saber por dónde, y el tiempo va | Ve el negocio real | Extreme close-up of NUBE's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | NUBE walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí está el camino que hoy no ves / Entras sin saber, y sales sabiendo qué hacer | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; NUBE small in the aisle looking |
| 09 | MECANISMO | Me digo que me falta un curso, uno más (repite el dolor en imagen) | Plataformas, proveedores y los que ya empezaron | At a fair stand, NUBE beside a friendly anthropomorphic laptop character showing a glowing storefront shape; a second exhibitor hands NUBE a |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of NUBE seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya sé por dónde, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | NUBE facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya sé por dónde, se acabó | Ya sabes por dónde | Bedroom desk again, daytime: the laptop shows one glowing storefront shape with a first order dot, the notebook closed, NUBE bright and stea |

**Notas de producción.** Pixar con objeto antropomórfico (nube de ideas). Dolor «no sé por dónde» 3 veces: v1, v2 y outro. Héroe primero. Cantado, sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_pixar_p01-empezar-musical_20260904_aprobado.json
(antes: renombrar effix_pixar_p01-empezar-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo pixar: Pixar con objeto antropomórfico (nube de ideas). Canción Latin pop alegre a 108 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 02 · La tienda que vende poquito

**Público:** Dueños de tiendas online (🔥) · **Ángulo 2.1:** Pocas ventas  
**Estilo:** Skeleton · **Música:** Reggaetón, 96 BPM  
**Personaje:** El esqueleto es el dueño de una tienda online que vende poco.  
**Dolor (3 veces en la letra):** «poquito»

**Micro-situación**  
*Momento.* Abres el panel y hay tres ventas. Igual que ayer. Igual que hace un mes.  
*Síntoma.* Publicas, pautas un poquito, y el número no se mueve.  
*Explicación fallida.* Te dices que el producto es de nicho.  
*Patrón.* Pero hay tiendas con tu mismo producto vendiendo treinta al día.  
*Causa raíz.* No es el producto. Es que nadie te ha mostrado por dentro una tienda que sí vende.  
*Mecanismo.* En Feria Effix están las tiendas que ya venden, las agencias y las plataformas, y les preguntas de frente qué hacen distinto.  

**Letra**

```
[Verso 1]
Abro el panel y otra vez vendo poquito
Tres ventas hoy, igual que ayer, lo mismito
Publico, pauto, y el número está quietico
Y el mes se va, y yo con el mismo numerito

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que venden todo el día
Y te muestran por dentro lo que tú no sabías

[Verso 2]
Me digo que mi producto es de nicho, que es así
Pero otra tienda con lo mismo vende treinta aquí
No es el producto, es que nadie me enseñó a mí
Y sigo vendiendo poquito, y no puedo seguir

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que venden todo el día
Y te muestran por dentro lo que tú no sabías

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no vendo poquito, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Abro el panel y otra vez vendo poquito / Tres ventas hoy, igual que ayer, lo mismito | Vendes poquito | The skeleton at a home desk at night, a laptop showing an abstract dashboard with a tiny bar and a small '3'-shaped dot cluster, coffee cold |
| 02 | CALLOUT | Publico, pauto, y el número está quietico / Y el mes se va, y yo con el mismo numerito | ¿Tienda online que vende poco? | the skeleton turns to face the camera in a small home office with a glowing store dashboard, the sales counter stuck on the same low number  |
| 03 | SINTOMA | Me digo que mi producto es de nicho, que es así | El número no se mueve | Close-up of bony hands posting on a phone and then checking the laptop bar; nothing changes. |
| 04 | EXPL_FALLIDA | Pero otra tienda con lo mismo vende treinta aquí | «Es de nicho» | The skeleton from behind, shrugging at a blurred friend, gesturing 'it's a niche thing' with open hands. |
| 05 | PATRON | No es el producto, es que nadie me enseñó a mí | Otras venden treinta al día | Low-angle wide: through the window, a neighbouring lit apartment where a blurred figure packs a tall stack of parcels; the skeleton small at |
| 06 | CAUSA_RAIZ | Y sigo vendiendo poquito, y no puedo seguir | Nadie te mostró una que vende | Extreme close-up of the skeleton's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | the skeleton walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las tiendas que venden todo el día / Y te muestran por dentro lo que tú no sabías | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; the skeleton small in the aisle |
| 09 | MECANISMO | Me digo que mi producto es de nicho, que es así (repite el dolor en imagen) | Pregúntales de frente | Two-shot at a fair stand: the skeleton showing its laptop dashboard to a blurred human-shaped exhibitor who points at the screen and gesture |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of the skeleton seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking not |
| 11 | CTA | Y ya no vendo poquito, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | the skeleton facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands be |
| 12 | LOOP | Y ya no vendo poquito, se acabó | Ya no vendes poquito | Home desk, daytime: the laptop dashboard with a tall bar and many order dots, the skeleton leaning back with a fresh coffee, notification do |

**Notas de producción.** Skeleton reggaetón. Bible verbatim, héroe → edit, encuadres distintos. Dolor «vendo poquito» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_skeleton_p02-pocas-ventas-musical_20260904_aprobado.json
(antes: renombrar effix_skeleton_p02-pocas-ventas-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo skeleton: Skeleton reggaetón. Canción Reggaetón a 96 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 03 · De diez a cien

**Público:** Empresarios de e-commerce en crecimiento (🔥) · **Ángulo 3.1:** Pasar de 10 a 100 pedidos diarios  
**Estilo:** Crochet (mundo B&N) · **Música:** Cumbia pop, 100 BPM  
**Personaje:** LEO, amigurumi del dueño de una tienda que ya vende y quiere pasar de diez a cien pedidos diarios. Único con color.  
**Dolor (3 veces en la letra):** «me quedé en diez»

**Micro-situación**  
*Momento.* Empacas diez pedidos al día, todos los días, y sabes que podrían ser cien.  
*Síntoma.* Cada vez que intentas crecer, algo se rompe: la pauta, el proveedor, el despacho.  
*Explicación fallida.* Te dices que para crecer hay que arriesgar mucho.  
*Patrón.* Pero las tiendas que ya despachan cien no arriesgaron: copiaron un sistema.  
*Causa raíz.* No te falta ganas. Te falta ver el sistema de los que ya pasaron de diez a cien.  
*Mecanismo.* En Feria Effix están los dueños que ya lo hicieron, las agencias que escalan y la logística que despacha cien al día.  

**Letra**

```
[Verso 1]
Diez pedidos hoy, y otra vez me quedé en diez
Empaco, despacho, y mañana vuelvo a ser diez
Quiero llegar a cien y no sé cómo se hace
Subo la pauta, y algo se me deshace

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que ya pasaron de diez a cien
Y te enseñan el sistema que te funcione bien

[Verso 2]
Me digo que crecer es arriesgar la plata
Pero el que ya está en cien no tiró la plata
Copió un sistema que otro le mostró de frente
Y yo me quedé en diez, mirando a la gente

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que ya pasaron de diez a cien
Y te enseñan el sistema que te funcione bien

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no me quedé en diez, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Diez pedidos hoy, y otra vez me quedé en diez / Empaco, despacho, y mañana vuelvo a ser diez | Te quedaste en diez | LEO in a greyscale knitted stockroom taping the tenth parcel of a stack of exactly ten, a knitted clock on the wall; he looks at the empty s |
| 02 | CALLOUT | Quiero llegar a cien y no sé cómo se hace / Subo la pauta, y algo se me deshace | ¿Vendes y quieres crecer? | LEO turns to face the camera in a small greyscale knitted stockroom with parcels, a knitted stack of exactly ten parcels still visible. |
| 03 | SINTOMA | Me digo que crecer es arriesgar la plata | Algo se rompe al crecer | Close-up of LEO's mitten-hand on a knitted laptop: a felt bar goes up one stitch and a felt warning shape pops; the hand pulls back. |
| 04 | EXPL_FALLIDA | Pero el que ya está en cien no tiró la plata | «Crecer es arriesgar» | LEO from behind at a knitted table counting felt coins into two piles, hesitating over the second pile. |
| 05 | PATRON | Copió un sistema que otro le mostró de frente | Copiaron un sistema | Low-angle wide of the knitted street: a grey knitted truck loads a hundred grey parcels from the shop next door; LEO small at his own door w |
| 06 | CAUSA_RAIZ | Y yo me quedé en diez, mirando a la gente | El sistema de los que crecieron | Extreme close-up of LEO's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | LEO walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. The whole fa |
| 08 | CORO_FERIA | Ahí están los que ya pasaron de diez a cien / Y te enseñan el sistema que te funcione bien | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; LEO small in the aisle looking  |
| 09 | MECANISMO | Me digo que crecer es arriesgar la plata (repite el dolor en imagen) | Los que pasaron de diez a cien | At a knitted fair stand, LEO with two grey knitted figures: one holds a felt chart climbing in steps, the other a knitted parcel with a tiny |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of LEO seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. The w |
| 11 | CTA | Y ya no me quedé en diez, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | LEO facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. The |
| 12 | LOOP | Y ya no me quedé en diez, se acabó | Ya no te quedas en diez | The knitted stockroom, now full: a hundred parcels in rows, a grey knitted helper taping, LEO checking a knitted list, calm. |

**Notas de producción.** Crochet cumbia. Mundo B&N estricto, LEO única fuente de color. Poses simples, sin dedos. Verbatim de crochet. Dolor «me quedé en diez» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_crochet_p03-diez-a-cien-musical_20260904_aprobado.json
(antes: renombrar effix_crochet_p03-diez-a-cien-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo crochet: Crochet cumbia. Canción Cumbia pop a 100 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 04 · Mil mensajes en WhatsApp

**Público:** Vendedores de redes sociales (🔥) · **Ángulo 4.1:** Demasiados mensajes en WhatsApp  
**Estilo:** Claymation · **Música:** Merengue urbano, 130 BPM  
**Personaje:** MARCE, personaje de plastilina: la vendedora por WhatsApp ahogada en mensajes.  
**Dolor (3 veces en la letra):** «mil mensajes»

**Micro-situación**  
*Momento.* Son las once de la noche y tienes trescientos mensajes sin responder, todos preguntando lo mismo.  
*Síntoma.* Respondes uno por uno, y cuando llegas, ya compraron en otro lado.  
*Explicación fallida.* Te dices que la atención personal es lo tuyo.  
*Patrón.* Pero los que venden diez veces más también atienden personal. Solo que no a mano.  
*Causa raíz.* No te falta atención. Te falta automatizar lo repetido.  
*Mecanismo.* En Feria Effix están las herramientas que responden por ti y los vendedores que ya las usan, con demostración en stand.  

**Letra**

```
[Verso 1]
Son las once y tengo mil mensajes en WhatsApp
Precio, envío, talla, y otra vez el mismo chat
Respondo uno y ya llegaron veinte más
Y ninguno de todos me deja descansar

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las herramientas que responden por ti
Y los que venden en grande te dicen cómo así

[Verso 2]
Me digo que lo mío es atender personal
Pero el que vende diez veces más responde igual
Solo que no a mano, lo hace un sistema
Y yo con mil mensajes, y el mismo problema

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las herramientas que responden por ti
Y los que venden en grande te dicen cómo así

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no son mil mensajes, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Son las once y tengo mil mensajes en WhatsApp / Precio, envío, talla, y otra vez el mismo chat | Mil mensajes sin responder | MARCE on a clay couch at night, the oversized clay phone showing a mountain of tiny clay message bubbles piling over the top, her eyes wide, |
| 02 | CALLOUT | Respondo uno y ya llegaron veinte más / Y ninguno de todos me deja descansar | ¿Vendes por WhatsApp? | MARCE turns to face the camera in a small clay living room with a couch and a phone, the clay phone with a mountain of message bubbles still |
| 03 | SINTOMA | Me digo que lo mío es atender personal | Ya compraron en otro lado | Close-up of the clay phone: MARCE's thumb answers one bubble and twenty new bubbles pop in; a small clay 'sold elsewhere' cart shape rolls a |
| 04 | EXPL_FALLIDA | Pero el que vende diez veces más responde igual | «Lo mío es atender personal» | MARCE from behind, hugging the phone to her chest proudly, a clay speech shape with a heart above her. |
| 05 | PATRON | Solo que no a mano, lo hace un sistema | Ellos tampoco responden a mano | Low-angle wide: a clay neighbour on a balcony sipping coffee while her phone answers by itself with tiny bubbles flying out in order; MARCE  |
| 06 | CAUSA_RAIZ | Y yo con mil mensajes, y el mismo problema | Automatiza lo repetido | Extreme close-up of MARCE's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | MARCE walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las herramientas que responden por ti / Y los que venden en grande te dicen cómo así | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; MARCE small in the aisle lookin |
| 09 | MECANISMO | Me digo que lo mío es atender personal (repite el dolor en imagen) | Herramientas que responden por ti | At a clay fair stand, MARCE watching a clay exhibitor tap once on a tablet and a line of bubbles answer themselves; her mouth opens. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of MARCE seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no son mil mensajes, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | MARCE facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no son mil mensajes, se acabó | Ya no son mil mensajes | Clay living room, daytime: MARCE on the couch with coffee, the phone on the table answering by itself with orderly bubbles, a small clay par |

**Notas de producción.** Claymation merengue. Estilo Aardman, 12fps, dedos visibles en la plastilina. Dolor «mil mensajes» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_claymation_p04-whatsapp-musical_20260904_aprobado.json
(antes: renombrar effix_claymation_p04-whatsapp-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo claymation: Claymation merengue. Canción Merengue urbano a 130 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 05 · El producto ganador

**Público:** Dropshippers (🔥) · **Ángulo 5.1:** Encontrar productos ganadores  
**Estilo:** Anime · **Música:** Latin pop electrónico, 104 BPM  
**Personaje:** KAI, personaje anime: el dropshipper que busca el producto ganador.  
**Dolor (3 veces en la letra):** «ninguno gana»

**Micro-situación**  
*Momento.* Llevas dos meses buscando el producto ganador, y ya probaste ocho que no ganaron.  
*Síntoma.* Cada semana un video promete el producto del momento, y cuando lo pautas ya está quemado.  
*Explicación fallida.* Te dices que te falta la herramienta correcta para encontrarlo.  
*Patrón.* Pero los que sí venden no lo encontraron en una herramienta: lo vieron en la mano de un proveedor antes que todos.  
*Causa raíz.* No te falta herramienta. Te falta ver el producto antes de que sea tendencia.  
*Mecanismo.* En Feria Effix están los proveedores con los productos que van a vender en los próximos meses, en la mano, antes de que salgan en los videos.  

**Letra**

```
[Verso 1]
Ocho productos y ninguno gana
Lo veo en un video y lo pauto mañana
Y cuando llega, ya lo quemó la semana
Ocho productos, y ninguno gana

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí está el producto antes de la tendencia
En la mano del proveedor, no en la pantalla, con paciencia

[Verso 2]
Me digo que me falta la herramienta correcta
Pero el que gana lo vio primero, en una mesa
Se lo mostró un proveedor antes que a todos
Y yo con ocho productos, y ninguno gana

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí está el producto antes de la tendencia
En la mano del proveedor, no en la pantalla, con paciencia

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y el noveno sí gana, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Ocho productos y ninguno gana / Lo veo en un video y lo pauto mañana | Ocho productos, ninguno gana | KAI at a desk with two monitors, behind him a wall of pinned product screenshots with eight crossed with red tape, energy drink cans, night. |
| 02 | CALLOUT | Y cuando llega, ya lo quemó la semana / Ocho productos, y ninguno gana | ¿Buscas el producto ganador? | KAI turns to face the camera in a small apartment desk with two monitors, a wall covered in product screenshots pinned like a detective boar |
| 03 | SINTOMA | Me digo que me falta la herramienta correcta | Cuando lo pautas, ya está quemado | Close-up of a phone playing an abstract 'winning product' video; KAI's hand taps to a laptop ad panel where a small flame icon fades to grey |
| 04 | EXPL_FALLIDA | Pero el que gana lo vio primero, en una mesa | «Me falta la herramienta» | KAI from behind scrolling a glowing tool dashboard with dozens of tiny product cards, pointing at one after another. |
| 05 | PATRON | Se lo mostró un proveedor antes que a todos | Lo vieron antes que todos | Low-angle wide: in a bright wholesale hall a supplier hands a small product to a smiling seller across a table; KAI watches from the doorway |
| 06 | CAUSA_RAIZ | Y yo con ocho productos, y ninguno gana | Ve el producto antes de la tendencia | Extreme close-up of KAI's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | KAI walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí está el producto antes de la tendencia / En la mano del proveedor, no en la pantalla, con paciencia | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; KAI small in the aisle looking  |
| 09 | MECANISMO | Me digo que me falta la herramienta correcta (repite el dolor en imagen) | Proveedores con el producto en la mano | At a fair stand, KAI holding a product sample in both hands, turning it, a supplier explaining across the counter, a second sample waiting. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of KAI seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y el noveno sí gana, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | KAI facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y el noveno sí gana, se acabó | El noveno sí gana | Apartment desk, daytime: the wall now has one screenshot circled in green, the laptop shows a rising bar, KAI leaning back with a satisfied  |

**Notas de producción.** Anime latin pop electrónico. Cel shading, timing anime (hold y snap). Dolor «ocho productos y ninguno gana» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_anime_p05-producto-ganador-musical_20260904_aprobado.json
(antes: renombrar effix_anime_p05-producto-ganador-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo anime: Anime latin pop electrónico. Canción Latin pop electrónico a 104 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 06 · Mi marca no existe en internet

**Público:** Marcas, fabricantes e importadores (🔥) · **Ángulo 6.1:** Llevar una marca al mundo digital  
**Estilo:** Cyberpunk · **Música:** Reggaetón oscuro / trap latino, 92 BPM  
**Personaje:** DON RAMÓN, dueño de una marca tradicional que no existe en el mundo digital, en un mundo cyberpunk.  
**Dolor (3 veces en la letra):** «mi marca no existe en internet»

**Micro-situación**  
*Momento.* Buscas tu marca en el celular y no aparece. Y la de tu competidor sí, con ventas online.  
*Síntoma.* Tienes fábrica, calidad y años, y en internet no existes.  
*Explicación fallida.* Te dices que tu cliente es tradicional y compra en tienda.  
*Patrón.* Pero tu cliente ya compra por internet todo lo demás. Solo tu marca no la encuentra.  
*Causa raíz.* No te falta marca. Te falta el canal digital, y los que lo montan.  
*Mecanismo.* En Feria Effix están las agencias, las plataformas y la logística que llevan marcas tradicionales a internet, y los fabricantes que ya lo hicieron.  

**Letra**

```
[Verso 1]
Mi marca no existe en internet
La busco en el celular y no está, y la de él sí se ve
Tengo fábrica, calidad, y años de hacerlo bien
Pero mi marca no existe en internet

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que llevan tu marca a la red
Agencias y plataformas, y quien lo hizo ayer, ¿ves?

[Verso 2]
Me digo que mi cliente compra en tienda, es tradicional
Pero en internet compra todo lo demás, igual
Solo mi marca es la que no puede encontrar
Mi marca no existe en internet, y eso va a cambiar

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que llevan tu marca a la red
Agencias y plataformas, y quien lo hizo ayer, ¿ves?

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y mi marca ya existe, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Mi marca no existe en internet / La busco en el celular y no está, y la de él sí se ve | Tu marca no existe en internet | DON RAMON standing in the rain on a neon street, phone in hand showing an empty search result shape, while a giant holographic competitor lo |
| 02 | CALLOUT | Tengo fábrica, calidad, y años de hacerlo bien / Pero mi marca no existe en internet | ¿Fabricas y no vendes online? | DON RAMÓN turns to face the camera in a neon-lit rainy street of holographic shops, his printed paper catalogue that nobody looks at still v |
| 03 | SINTOMA | Me digo que mi cliente compra en tienda, es tradicional | Fábrica, calidad, años. Y nada | Close-up of DON RAMON's hands holding a paper catalogue, rain soaking it, neon reflections on the wet cover; passers-by with glowing phones  |
| 04 | EXPL_FALLIDA | Pero en internet compra todo lo demás, igual | «Mi cliente es tradicional» | DON RAMON from behind, gesturing at an old-fashioned physical shop-front with a warm light, arms open as if to say 'this is enough'. |
| 05 | PATRON | Solo mi marca es la que no puede encontrar | Ya compra todo por internet | Low-angle wide: a delivery drone drops a glowing parcel with the competitor's shape onto a balcony; DON RAMON small below looking up. |
| 06 | CAUSA_RAIZ | Mi marca no existe en internet, y eso va a cambiar | Te falta el canal digital | Extreme close-up of DON RAMÓN's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | DON RAMÓN walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que llevan tu marca a la red / Agencias y plataformas, y quien lo hizo ayer, ¿ves? | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; DON RAMÓN small in the aisle lo |
| 09 | MECANISMO | Me digo que mi cliente compra en tienda, es tradicional (repite el dolor en imagen) | Los que llevan marcas a internet | At a fair stand under neon, DON RAMON with three figures: one holding a glowing storefront hologram, one a parcel, one a tablet with a risin |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of DON RAMÓN seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y mi marca ya existe, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | DON RAMÓN facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behin |
| 12 | LOOP | Y mi marca ya existe, se acabó | Tu marca ya existe | The neon street again: DON RAMON's own brand-shape now glows as a hologram beside the competitor's, a delivery drone lifting a parcel from h |

**Notas de producción.** Cyberpunk reggaetón oscuro. El contraste es traje clásico contra neón. Logos y letreros como formas abstractas, nunca texto. Dolor «mi marca no existe en internet» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_cyberpunk_p06-marca-digital-musical_20260904_aprobado.json
(antes: renombrar effix_cyberpunk_p06-marca-digital-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo cyberpunk: Cyberpunk reggaetón oscuro. Canción Reggaetón oscuro / trap latino a 92 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 07 · Pedidos por teléfono

**Público:** Mayoristas y distribuidores (🔥) · **Ángulo 7.1:** Digitalizar ventas mayoristas  
**Estilo:** Animado 2D · **Música:** Salsa urbana / champeta, 98 BPM  
**Personaje:** DOÑA GLORIA, mayorista que toma pedidos por teléfono y cuaderno, en animación 2D.  
**Dolor (3 veces en la letra):** «el pedido por teléfono»

**Micro-situación**  
*Momento.* Un cliente llama, dictas el pedido en un cuaderno, alguien lo pasa a Excel, y otro lo digita. Tres veces el mismo pedido.  
*Síntoma.* Cuando la del teléfono se enferma, ese día no se vende.  
*Explicación fallida.* Te dices que tus clientes no van a pedir por una página.  
*Patrón.* Pero tus clientes ya compran todo lo demás por internet.  
*Causa raíz.* No es que no quieran. Es que no les has dado un canal para pedir a cualquier hora.  
*Mecanismo.* En Feria Effix están las plataformas de venta mayorista online y los distribuidores que ya reciben la mitad de sus pedidos sin tocar el teléfono.  

**Letra**

```
[Verso 1]
Suena el teléfono y anoto el pedido en el cuaderno
Lo pasan al Excel, lo digitan, y es eterno
El mismo pedido tres veces, todo el día
El pedido por teléfono me quita la alegría

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los mayoristas que ya venden sin llamar
Y las plataformas donde el cliente pide sin esperar

[Verso 2]
Me digo que mi gente no va a pedir por internet
Pero por internet compra todo, hasta el café
Solo a mí me llama, porque no le di otro lugar
El pedido por teléfono ya no va a durar

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los mayoristas que ya venden sin llamar
Y las plataformas donde el cliente pide sin esperar

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y el pedido por teléfono se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Suena el teléfono y anoto el pedido en el cuaderno / Lo pasan al Excel, lo digitan, y es eterno | El pedido, tres veces | DONA GLORIA in a warehouse office with the landline between ear and shoulder, writing in a paper notebook, behind her a second worker typing |
| 02 | CALLOUT | El mismo pedido tres veces, todo el día / El pedido por teléfono me quita la alegría | ¿Mayorista que vende por teléfono? | DOÑA GLORIA turns to face the camera in a wholesale warehouse office with a landline and a paper notebook, the paper order notebook still vi |
| 03 | SINTOMA | Me digo que mi gente no va a pedir por internet | Sin la del teléfono no hay venta | Close-up of the empty desk with the landline off the hook and the notebook closed; a wall clock; the warehouse shelves full behind. |
| 04 | EXPL_FALLIDA | Pero por internet compra todo, hasta el café | «No van a pedir por página» | DONA GLORIA from behind, waving a hand at a laptop a young worker offers, turning back to the landline. |
| 05 | PATRON | Solo a mí me llama, porque no le di otro lugar | Ya compran todo por internet | Low-angle wide: outside the warehouse, a retail client on a scooter taps a phone and a parcel-shape from a competitor warehouse flies out; D |
| 06 | CAUSA_RAIZ | El pedido por teléfono ya no va a durar | Un canal a cualquier hora | Extreme close-up of DOÑA GLORIA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | DOÑA GLORIA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los mayoristas que ya venden sin llamar / Y las plataformas donde el cliente pide sin esperar | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; DOÑA GLORIA small in the aisle  |
| 09 | MECANISMO | Me digo que mi gente no va a pedir por internet (repite el dolor en imagen) | Mayoristas que venden sin llamar | At a fair stand, DONA GLORIA looking at a tablet where order shapes arrive by themselves into a list, a distributor beside her pointing at i |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of DOÑA GLORIA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking note |
| 11 | CTA | Y el pedido por teléfono se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | DOÑA GLORIA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands beh |
| 12 | LOOP | Y el pedido por teléfono se acabó | El pedido entra solo | The warehouse office, early morning, lights off except a tablet on the desk where order shapes arrive by themselves; the landline unplugged; |

**Notas de producción.** Animado 2D salsa urbana. Bible flat 2D verbatim del ad 'La acera'. Dolor «el pedido por teléfono» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_animado_2d_p07-mayorista-digital-musical_20260904_aprobado.json
(antes: renombrar effix_animado_2d_p07-mayorista-digital-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo animado_2d: Animado 2D salsa urbana. Canción Salsa urbana / champeta a 98 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 08 · La campaña que dejó de funcionar

**Público:** Marketing, publicidad y adquisición digital (🔥) · **Ángulo 8.1:** Campañas que dejaron de funcionar  
**Estilo:** Pixar 3D (objeto antropomórfico) · **Música:** Latin pop alegre, 108 BPM  
**Personaje:** PÍXEL, un cuadrito de anuncio antropomórfico: la campaña que un día dejó de vender.  
**Dolor (3 veces en la letra):** «dejó de funcionar»

**Micro-situación**  
*Momento.* La campaña que te vendía todos los días, un martes dejó de vender. Sin cambiar nada.  
*Síntoma.* Duplicas, cambias públicos, subes presupuesto, y nada la revive.  
*Explicación fallida.* Te dices que la plataforma cambió el algoritmo.  
*Patrón.* Pero hay cuentas creciendo ahora mismo con creativos nuevos, canales nuevos y método nuevo.  
*Causa raíz.* No es el algoritmo. Es que estás pautando igual que hace dos años.  
*Mecanismo.* En Feria Effix hay más de doscientas ponencias de pauta, creativos e inteligencia artificial, y las agencias que sí sostienen resultados.  

**Letra**

```
[Verso 1]
Mi campaña un martes dejó de funcionar
Sin tocar nada, se dejó de vender, así no más
Duplico, cambio público, subo, y nada
Dejó de funcionar, y no sé qué le pasa

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que pautan y hoy sí venden
Con creativos nuevos que la gente entiende

[Verso 2]
Me digo que fue el algoritmo, que cambió
Pero hay cuentas creciendo con un método mejor
Estoy pautando como hace dos años, ya sé
Dejó de funcionar porque yo no cambié

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que pautan y hoy sí venden
Con creativos nuevos que la gente entiende

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y vuelve a funcionar, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Mi campaña un martes dejó de funcionar / Sin tocar nada, se dejó de vender, así no más | Dejó de funcionar | PIXEL on a media buyer's desk beside a laptop with an abstract chart that climbs and then goes flat; PIXEL's chest light dims, eyes drooping |
| 02 | CALLOUT | Duplico, cambio público, subo, y nada / Dejó de funcionar, y no sé qué le pasa | ¿Tu campaña dejó de vender? | PIXEL turns to face the camera in a media buyer's desk with an ads dashboard, the campaign chart that turned flat still visible. |
| 03 | SINTOMA | Me digo que fue el algoritmo, que cambió | Nada la revive | Close-up of the laptop: a hand duplicates PIXEL into three copies, changes an audience shape, raises a budget slider; all three copies stay  |
| 04 | EXPL_FALLIDA | Pero hay cuentas creciendo con un método mejor | «Fue el algoritmo» | PIXEL from behind, shaking its tiny fist at a giant floating abstract platform logo-shape in the sky. |
| 05 | PATRON | Estoy pautando como hace dos años, ya sé | Cuentas creciendo ahora mismo | Low-angle wide: on the next desk, a bright new ad-card character with a glowing chest light rides a rising chart; PIXEL small, dim, watching |
| 06 | CAUSA_RAIZ | Dejó de funcionar porque yo no cambié | Pautas como hace dos años | Extreme close-up of PIXEL's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | PIXEL walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que pautan y hoy sí venden / Con creativos nuevos que la gente entiende | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; PIXEL small in the aisle lookin |
| 09 | MECANISMO | Me digo que fue el algoritmo, que cambió (repite el dolor en imagen) | Ponencias de pauta, creativos e IA | At a fair stand, PIXEL beside a media buyer showing three new creative cards; a speaker shape in the background gestures; PIXEL's chest ligh |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of PIXEL seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y vuelve a funcionar, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | PIXEL facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y vuelve a funcionar, se acabó | Vuelve a funcionar | The desk again: the laptop chart rising, PIXEL glowing bright with three new cards behind it, the buyer leaning back with coffee. |

**Notas de producción.** Pixar latin pop con objeto antropomórfico (tarjeta de anuncio). Dolor «dejó de funcionar» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_pixar_p08-campanas-musical_20260904_aprobado.json
(antes: renombrar effix_pixar_p08-campanas-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo pixar: Pixar latin pop con objeto antropomórfico (tarjeta de anuncio). Canción Latin pop alegre a 108 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 09 · Muchos seguidores, cero ventas

**Público:** Creadores de contenido e influencers que venden (🔥) · **Ángulo 9.1:** Convertir audiencia en ventas  
**Estilo:** Skeleton · **Música:** Reggaetón, 96 BPM  
**Personaje:** El esqueleto es el creador con audiencia que no vende.  
**Dolor (3 veces en la letra):** «cero ventas»

**Micro-situación**  
*Momento.* Subes un video, lo ven cien mil personas, y vendes cero.  
*Síntoma.* Te escriben «qué lindo», te siguen, y nadie compra.  
*Explicación fallida.* Te dices que tu audiencia no está para comprar todavía.  
*Patrón.* Pero creadores con la mitad de tus seguidores ya venden todos los días.  
*Causa raíz.* No te falta audiencia. Te falta saber qué venderle y cómo.  
*Mecanismo.* En Feria Effix están las marcas que buscan creadores, los proveedores que hacen producto propio y los creadores que ya viven de esto.  

**Letra**

```
[Verso 1]
Cien mil vistas y cero ventas
Me escriben «qué lindo» y nadie paga la cuenta
Subo otro video y la gente lo comenta
Cien mil vistas, y cero ventas

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las marcas que buscan a alguien como tú
Y los que ya venden con menos gente que tú

[Verso 2]
Me digo que mi audiencia no compra todavía
Pero uno con la mitad vende todos los días
No me falta gente, me falta qué vender
Cien mil vistas, cero ventas, y eso va a ceder

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las marcas que buscan a alguien como tú
Y los que ya venden con menos gente que tú

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y las vistas ya venden, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Cien mil vistas y cero ventas / Me escriben «qué lindo» y nadie paga la cuenta | Cien mil vistas, cero ventas | The skeleton in a home studio with a ring light, phone on a tripod, a laptop showing a huge view-count bar next to an empty sales panel; the |
| 02 | CALLOUT | Subo otro video y la gente lo comenta / Cien mil vistas, y cero ventas | ¿Creador con audiencia? | the skeleton turns to face the camera in a home creator studio with a ring light and a phone on a tripod, the follower counter next to an em |
| 03 | SINTOMA | Me digo que mi audiencia no compra todavía | «Qué lindo» y nadie compra | Close-up of a phone with floating heart and comment shapes pouring in; beneath it a wallet-shaped icon stays flat. |
| 04 | EXPL_FALLIDA | Pero uno con la mitad vende todos los días | «Mi audiencia no compra» | The skeleton from behind, waving off a floating shop-bag icon and turning back to the ring light. |
| 05 | PATRON | No me falta gente, me falta qué vender | Con la mitad, ya venden | Low-angle wide: on a giant screen a smaller creator figure with a smaller view bar and a tall sales bar; the skeleton small below looking up |
| 06 | CAUSA_RAIZ | Cien mil vistas, cero ventas, y eso va a ceder | Te falta qué vender | Extreme close-up of the skeleton's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | the skeleton walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las marcas que buscan a alguien como tú / Y los que ya venden con menos gente que tú | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; the skeleton small in the aisle |
| 09 | MECANISMO | Me digo que mi audiencia no compra todavía (repite el dolor en imagen) | Marcas, proveedores y creadores que ya venden | Two-shot at a fair stand: the skeleton beside a blurred brand exhibitor holding a product with the skeleton's own abstract logo-shape on it; |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of the skeleton seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking not |
| 11 | CTA | Y las vistas ya venden, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | the skeleton facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands be |
| 12 | LOOP | Y las vistas ya venden, se acabó | Las vistas ya venden | The home studio, daytime: the laptop now shows a view bar AND a sales bar, a stack of parcels with the skeleton's logo-shape beside the trip |

**Notas de producción.** Skeleton reggaetón. Bible verbatim, héroe → edit. Dolor «cien mil vistas y cero ventas» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_skeleton_p09-audiencia-ventas-musical_20260904_aprobado.json
(antes: renombrar effix_skeleton_p09-audiencia-ventas-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo skeleton: Skeleton reggaetón. Canción Reggaetón a 96 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 10 · Sé mucho y nadie me contrata

**Público:** Consultores y profesionales independientes de e-commerce (🔥) · **Ángulo 10.1:** Conseguir clientes  
**Estilo:** Crochet (mundo B&N) · **Música:** Cumbia pop, 100 BPM  
**Personaje:** ANA, amigurumi de la consultora de ecommerce sin clientes nuevos. Única con color.  
**Dolor (3 veces en la letra):** «lo voy a pensar»

**Micro-situación**  
*Momento.* Terminas la llamada y el cliente dice que lo va a pensar. Otra vez.  
*Síntoma.* Sabes resolver el problema, y no tienes cómo demostrarlo antes de que te contraten.  
*Explicación fallida.* Te dices que la experiencia se demuestra trabajando.  
*Patrón.* Pero los consultores que sí cierran la demuestran antes: en escenarios, en casos, en la gente que los recomienda.  
*Causa raíz.* No te falta experiencia. Te falta un lugar donde el sector te vea demostrarla.  
*Mecanismo.* En Feria Effix hay más de sesenta mil asistentes y trescientas cincuenta empresas que necesitan consultores, y tres días para conversar de frente.  

**Letra**

```
[Verso 1]
Termina la llamada y me dice «lo voy a pensar»
Sé resolverlo, pero no lo puedo mostrar
Otra semana, otra llamada, y nada más
Y otra vez el «lo voy a pensar»

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas que necesitan a alguien así
Y en tres días te ven de frente, y te dicen que sí

[Verso 2]
Me digo que la experiencia se demuestra en el trabajo
Pero el que cierra la demuestra antes, y yo abajo
Le falta un lugar donde el sector me vea
«Lo voy a pensar» es lo único que me queda

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas que necesitan a alguien así
Y en tres días te ven de frente, y te dicen que sí

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya nadie lo piensa, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Termina la llamada y me dice «lo voy a pensar» / Sé resolverlo, pero no lo puedo mostrar | «Lo voy a pensar» | ANA at a greyscale knitted desk closing a knitted laptop after a video call, a knitted calendar on the wall with empty squares, her mitten-h |
| 02 | CALLOUT | Otra semana, otra llamada, y nada más / Y otra vez el «lo voy a pensar» | ¿Consultora sin clientes nuevos? | ANA turns to face the camera in a small greyscale knitted home office with a video-call laptop, a knitted calendar with empty squares still  |
| 03 | SINTOMA | Me digo que la experiencia se demuestra en el trabajo | No tienes cómo mostrarlo | Close-up of ANA's mitten-hands holding a knitted folder of felt case studies; beside it the knitted phone shows a grey chat with no reply. |
| 04 | EXPL_FALLIDA | Pero el que cierra la demuestra antes, y yo abajo | «Se demuestra trabajando» | ANA from behind at the desk working hard, head down, while through the grey knitted window a small grey stage with a grey speaker is lit far |
| 05 | PATRON | Le falta un lugar donde el sector me vea | Ellos la demuestran antes | Low-angle wide of the knitted street: a grey knitted consultant figure shaking hands with three grey clients outside a building; ANA small a |
| 06 | CAUSA_RAIZ | «Lo voy a pensar» es lo único que me queda | Donde el sector te vea | Extreme close-up of ANA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | ANA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. The whole fa |
| 08 | CORO_FERIA | Ahí están las empresas que necesitan a alguien así / Y en tres días te ven de frente, y te dicen que sí | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; ANA small in the aisle looking  |
| 09 | MECANISMO | Me digo que la experiencia se demuestra en el trabajo (repite el dolor en imagen) | Empresas que necesitan consultores | At a knitted fair stand, ANA explaining with a felt chart to two grey knitted figures leaning in; a third one waits behind them. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of ANA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. The w |
| 11 | CTA | Y ya nadie lo piensa, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | ANA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. The |
| 12 | LOOP | Y ya nadie lo piensa, se acabó | Ya nadie lo piensa | The knitted home office again: the calendar now full of coloured felt squares, the laptop open with a call, ANA smiling with a stitch. |

**Notas de producción.** Crochet cumbia. Mundo B&N, ANA única con color. Verbatim de crochet. Dolor «lo voy a pensar» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_crochet_p10-consultor-clientes-musical_20260904_aprobado.json
(antes: renombrar effix_crochet_p10-consultor-clientes-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo crochet: Crochet cumbia. Canción Cumbia pop a 100 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 11 · Los clientes que se me pierden

**Público:** Tecnología y soluciones para e-commerce (🔥) · **Ángulo 11.1:** CRM  
**Estilo:** Claymation · **Música:** Merengue urbano, 130 BPM  
**Personaje:** TOBI, personaje de plastilina: dueño de una empresa de software CRM que no consigue tiendas.  
**Dolor (3 veces en la letra):** «dicen que está muy bueno»

**Micro-situación**  
*Momento.* Vendes un CRM que ordena clientes, y las tiendas siguen anotando clientes en un cuaderno.  
*Síntoma.* Haces demos, dicen que está muy bueno, y no vuelven a escribir.  
*Explicación fallida.* Te dices que las tiendas pequeñas no son tu mercado.  
*Patrón.* Pero las tiendas compran CRM el mes que empiezan a perder clientes, y se lo compran a quien tenían cerca.  
*Causa raíz.* No te falta producto. Te falta estar cerca de miles de tiendas en el momento en que pierden clientes.  
*Mecanismo.* En Feria Effix hay más de sesenta mil asistentes del ecommerce, y un stand para mostrar tu CRM con el caso de cada uno.  

**Letra**

```
[Verso 1]
Hago la demo y dicen que está muy bueno
Y después de eso ni un mensaje, ni un «lo veo»
Vendo el sistema que ordena a sus clientes
Y dicen que está muy bueno, y se van, indiferentes

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que hoy pierden clientes
Y te compran a ti si te tienen enfrente

[Verso 2]
Me digo que la tienda pequeña no es mi mercado
Pero compra el mes que se le pierde un contacto
Y le compra a quien tenía cerca ese día
Dicen que está muy bueno, y yo sin compañía

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que hoy pierden clientes
Y te compran a ti si te tienen enfrente

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ahora sí me compran, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Hago la demo y dicen que está muy bueno / Y después de eso ni un mensaje, ni un «lo veo» | «Está muy bueno» y no vuelven | TOBI in a clay startup office finishing a demo on a clay tablet to a clay shop-owner who nods with a clay thumbs-up and then walks out the d |
| 02 | CALLOUT | Vendo el sistema que ordena a sus clientes / Y dicen que está muy bueno, y se van, indiferentes | ¿Vendes software a tiendas? | TOBI turns to face the camera in a small clay startup office with a whiteboard, a clay tablet with a demo that never gets clicked still visi |
| 03 | SINTOMA | Me digo que la tienda pequeña no es mi mercado | Ni un mensaje después | Close-up of TOBI's clay phone: a chat with the owner, one grey bubble from TOBI, no reply; the clay clock hand moves. |
| 04 | EXPL_FALLIDA | Pero compra el mes que se le pierde un contacto | «No son mi mercado» | TOBI from behind at the whiteboard erasing a small clay shop icon and drawing a big clay building icon instead. |
| 05 | PATRON | Y le compra a quien tenía cerca ese día | Compran a quien tenían cerca | Low-angle wide: a clay shop-owner across the street drops a clay notebook full of client names in the rain; a competitor's clay van pulls up |
| 06 | CAUSA_RAIZ | Dicen que está muy bueno, y yo sin compañía | Cerca cuando pierden clientes | Extreme close-up of TOBI's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | TOBI walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las tiendas que hoy pierden clientes / Y te compran a ti si te tienen enfrente | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; TOBI small in the aisle looking |
| 09 | MECANISMO | Me digo que la tienda pequeña no es mi mercado (repite el dolor en imagen) | Tu CRM con su caso | At a clay fair stand, TOBI showing his tablet to a line of clay shop-owners; the first one's name-list turns into an orderly grid on the scr |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of TOBI seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ahora sí me compran, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | TOBI facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ahora sí me compran, se acabó | Ahora sí te compran | The clay office again: the whiteboard covered in small shop icons with clay check marks, TOBI's phone buzzing with bubbles, coffee in hand. |

**Notas de producción.** Claymation merengue. Dolor «dicen que está muy bueno» 3 veces. B2B: la solución es exponerse a las tiendas. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_claymation_p11-crm-musical_20260904_aprobado.json
(antes: renombrar effix_claymation_p11-crm-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo claymation: Claymation merengue. Canción Merengue urbano a 130 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 12 · Se van en el último paso

**Público:** Medios de pago y Fintech (🔥) · **Ángulo 12.1:** Checkout  
**Estilo:** Anime · **Música:** Latin pop electrónico, 104 BPM  
**Personaje:** MIA, personaje anime: fundadora de una pasarela de pagos que quiere más tiendas.  
**Dolor (3 veces en la letra):** «se van en el último paso»

**Micro-situación**  
*Momento.* Una tienda pierde uno de cada tres clientes en el pago. Con otra pasarela. Y tú tienes justo el checkout que lo evita.  
*Síntoma.* Las tiendas pierden ventas en el último paso todos los días y no saben que existes.  
*Explicación fallida.* Te dices que las tiendas te van a encontrar cuando busquen pasarela.  
*Patrón.* Pero las tiendas no buscan pasarela: se quedan con la primera hasta que alguien les muestra otra de frente.  
*Causa raíz.* No te faltan funciones. Te falta estar delante de miles de tiendas con su caso en la mano.  
*Mecanismo.* En Feria Effix hay más de sesenta mil asistentes que cobran por internet, y tres días para mostrar tu checkout en vivo.  

**Letra**

```
[Verso 1]
Llegan al pago y se van en el último paso
Uno de cada tres, y la tienda ni hace caso
Yo tengo el checkout que lo evita, lo sé
Pero se van en el último paso, y ella no lo ve

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que hoy pierden el pago
Y tú les muestras en vivo cómo cerrarlo, y no en vano

[Verso 2]
Me digo que me buscan cuando busquen pasarela
Pero nadie busca, se quedan con la que llega
Hasta que alguien de frente les muestra otra
Se van en el último paso, y yo sin mostrarla

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que hoy pierden el pago
Y tú les muestras en vivo cómo cerrarlo, y no en vano

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no se van, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Llegan al pago y se van en el último paso / Uno de cada tres, y la tienda ni hace caso | Se van en el último paso | MIA in a fintech office in front of a huge glowing funnel on the wall; at the last step the light blinks out and small cart shapes fall away |
| 02 | CALLOUT | Yo tengo el checkout que lo evita, lo sé / Pero se van en el último paso, y ella no lo ve | ¿Tienes una pasarela de pagos? | MIA turns to face the camera in a fintech office with a big glowing funnel on the wall, the last step of the funnel where the light goes out |
| 03 | SINTOMA | Me digo que me buscan cuando busquen pasarela | No saben que existes | Close-up of MIA's tablet showing a clean glowing checkout with a big check mark; beside it a phone with a store's chat showing no reply. |
| 04 | EXPL_FALLIDA | Pero nadie busca, se quedan con la que llega | «Me van a encontrar» | MIA from behind, leaning back in a chair with arms crossed, watching a search-bar shape float above the desk with nothing typed in it. |
| 05 | PATRON | Hasta que alguien de frente les muestra otra | Se quedan con la primera | Low-angle wide: a store owner at a counter shrugs at an old clunky payment terminal shape while customers walk away; MIA small in the doorwa |
| 06 | CAUSA_RAIZ | Se van en el último paso, y yo sin mostrarla | Con su caso en la mano | Extreme close-up of MIA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | MIA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las tiendas que hoy pierden el pago / Y tú les muestras en vivo cómo cerrarlo, y no en vano | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; MIA small in the aisle looking  |
| 09 | MECANISMO | Me digo que me buscan cuando busquen pasarela (repite el dolor en imagen) | Tu checkout en vivo | At a fair stand, MIA holding her tablet toward a store owner, a live checkout completing with a bright check mark; a small crowd gathers. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of MIA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no se van, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | MIA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no se van, se acabó | Ya no se van | The fintech office again: the wall funnel now glowing to the very last step, cart shapes flowing through, MIA smiling at the tablet. |

**Notas de producción.** Anime latin pop electrónico. B2B: la solución es mostrar el checkout a las tiendas. Dolor «se van en el último paso» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_anime_p12-checkout-musical_20260904_aprobado.json
(antes: renombrar effix_anime_p12-checkout-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo anime: Anime latin pop electrónico. Canción Latin pop electrónico a 104 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 13 · Los pedidos que llegan tarde

**Público:** Logística, fulfillment y última milla (🔥) · **Ángulo 13.1:** Pedidos atrasados  
**Estilo:** Cyberpunk · **Música:** Reggaetón oscuro / trap latino, 92 BPM  
**Personaje:** RUTA, mensajera de última milla en una ciudad cyberpunk: el operador logístico que quiere más tiendas.  
**Dolor (3 veces en la letra):** «llegó tarde»

**Micro-situación**  
*Momento.* Una tienda pierde un cliente porque el pedido llegó tarde. Con su operador. No contigo.  
*Síntoma.* Tú entregas a tiempo, tienes la flota y la bodega, y la operación va a media máquina.  
*Explicación fallida.* Te dices que en logística los clientes llegan por recomendación.  
*Patrón.* Pero las tiendas que crecen ya eligieron operador, y lo eligieron donde lo vieron de frente.  
*Causa raíz.* No se trata de esperar. Se trata de estar donde las tiendas deciden con quién despachar.  
*Mecanismo.* En Feria Effix hay miles de tiendas despachando todos los días y más de trescientas cincuenta empresas, en un mismo recinto.  

**Letra**

```
[Verso 1]
El pedido de esa tienda otra vez llegó tarde
Con su operador, no conmigo, y el cliente se parte
Yo entrego a tiempo, tengo flota y bodega
Pero el que llegó tarde fue otro, y ella no me llega

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que despachan cada día
Y eligen de frente a quien les da garantía

[Verso 2]
Me digo que en logística se llega por recomendado
Pero la que crece ya eligió, y eligió a su lado
A quien vio de frente, no a quien esperó
Otro llegó tarde, y a mí nadie me llamó

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que despachan cada día
Y eligen de frente a quien les da garantía

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no llega tarde, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | El pedido de esa tienda otra vez llegó tarde / Con su operador, no conmigo, y el cliente se parte | Llegó tarde. No contigo | RUTA at a neon delivery hub watching a giant holographic map where one parcel-shape blinks red 'late' far across the city, not from her hub; |
| 02 | CALLOUT | Yo entrego a tiempo, tengo flota y bodega / Pero el que llegó tarde fue otro, y ella no me llega | ¿Mueves paquetes de tiendas? | RUTA turns to face the camera in a neon-lit rainy delivery hub with conveyor belts, a parcel with a blinking red 'late' light still visible. |
| 03 | SINTOMA | Me digo que en logística se llega por recomendado | A media máquina | Close-up of RUTA's conveyor belt moving with wide gaps between parcels; her scanner beeps on nothing. |
| 04 | EXPL_FALLIDA | Pero la que crece ya eligió, y eligió a su lado | «Llegan por recomendación» | RUTA from behind, sitting on her bike waiting under a neon sign-shape, helmet on the handlebar, rain falling. |
| 05 | PATRON | A quien vio de frente, no a quien esperó | Eligen a quien vieron de frente | Low-angle wide: a bright store-front where a shop owner shakes hands with a competitor courier under neon; RUTA small across the street. |
| 06 | CAUSA_RAIZ | Otro llegó tarde, y a mí nadie me llamó | Donde deciden con quién despachar | Extreme close-up of RUTA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | RUTA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las tiendas que despachan cada día / Y eligen de frente a quien les da garantía | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; RUTA small in the aisle looking |
| 09 | MECANISMO | Me digo que en logística se llega por recomendado (repite el dolor en imagen) | Miles de tiendas despachando | At a fair stand under neon, RUTA showing her wrist scanner to a line of store owners, a hologram showing a parcel tracked live along a route |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of RUTA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no llega tarde, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | RUTA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no llega tarde, se acabó | Ya no llega tarde | The delivery hub again: the conveyor packed with parcels, three couriers loading bikes, RUTA's holographic map full of green dots. |

**Notas de producción.** Cyberpunk reggaetón oscuro. B2B logística. Dolor «llegó tarde» 3 veces. Sin voz en off.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_cyberpunk_p13-pedidos-atrasados-musical_20260904_aprobado.json
(antes: renombrar effix_cyberpunk_p13-pedidos-atrasados-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo cyberpunk: Cyberpunk reggaetón oscuro. Canción Reggaetón oscuro / trap latino a 92 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 14 · Bodega llena, vendedores de a uno

**Público:** Proveedores de dropshipping (🔥) · **Ángulo 14.1:** Conseguir vendedores  
**Estilo:** Animado 2D · **Música:** Salsa urbana / champeta, 98 BPM  
**Personaje:** DON JAIME, proveedor de dropshipping en animación 2D.  
**Dolor (3 veces en la letra):** «vendedores de a uno»

**Micro-situación**  
*Momento.* Tienes bodega llena y catálogo listo, y los mismos veinte vendedores de siempre mueven la mitad.  
*Síntoma.* Publicas el catálogo en grupos y los vendedores nuevos llegan de a uno.  
*Explicación fallida.* Te dices que los buenos dropshippers ya tienen proveedor.  
*Patrón.* Pero los dropshippers cambian de proveedor cada vez que uno les falla, y buscan al siguiente donde puedan verlo.  
*Causa raíz.* No te faltan productos. Te falta estar delante de los vendedores cuando buscan proveedor.  
*Mecanismo.* En Feria Effix están miles de dropshippers de cinco países buscando proveedor, y tú con stand y muestra física.  

**Letra**

```
[Verso 1]
Bodega llena y vendedores de a uno
Publico el catálogo en veinte grupos, y ninguno
Los mismos veinte de siempre mueven la mitad
Y los vendedores de a uno, nada más

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los dropshippers de cinco países
Buscando proveedor, y tú con la muestra, sin disfraces

[Verso 2]
Me digo que los buenos ya tienen proveedor
Pero cambian cuando uno les falla, y buscan mejor
Buscan donde puedan verlo, con producto en la mano
Vendedores de a uno, y yo sin acercarlo

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los dropshippers de cinco países
Buscando proveedor, y tú con la muestra, sin disfraces

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y llegan de a cientos, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Bodega llena y vendedores de a uno / Publico el catálogo en veinte grupos, y ninguno | Vendedores de a uno | DON JAIME in a full warehouse holding a phone with a catalogue image posted into a long list of group chats, only one small reply bubble; sh |
| 02 | CALLOUT | Los mismos veinte de siempre mueven la mitad / Y los vendedores de a uno, nada más | ¿Proveedor de dropshipping? | DON JAIME turns to face the camera in a dropshipping warehouse with shelves and a packing table, the phone catalogue posted in twenty groups |
| 03 | SINTOMA | Me digo que los buenos ya tienen proveedor | Los mismos veinte de siempre | Close-up of the packing table: a short list of twenty names on a clipboard, half the parcels boxed, half the shelf untouched. |
| 04 | EXPL_FALLIDA | Pero cambian cuando uno les falla, y buscan mejor | «Ya tienen proveedor» | DON JAIME from behind, waving a hand dismissively at a poster-shape of a big supplier, turning back to his boxes. |
| 05 | PATRON | Buscan donde puedan verlo, con producto en la mano | Cambian cuando uno falla | Low-angle wide: outside a competitor warehouse, a line of young sellers holding product samples and taking photos; DON JAIME small across th |
| 06 | CAUSA_RAIZ | Vendedores de a uno, y yo sin acercarlo | Cuando buscan proveedor | Extreme close-up of DON JAIME's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | DON JAIME walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los dropshippers de cinco países / Buscando proveedor, y tú con la muestra, sin disfraces | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; DON JAIME small in the aisle lo |
| 09 | MECANISMO | Me digo que los buenos ya tienen proveedor (repite el dolor en imagen) | Dropshippers de cinco países | At a fair stand, DON JAIME handing a product sample to the first of a long line of young sellers with lanyards, a second sample already in h |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of DON JAIME seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y llegan de a cientos, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | DON JAIME facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behin |
| 12 | LOOP | Y llegan de a cientos, se acabó | Llegan de a cientos | The warehouse again: three packers at the table, the clipboard list now several pages long, DON JAIME on the phone smiling at a flood of bub |

**Notas de producción.** Animado 2D salsa urbana. Bible flat 2D verbatim. B2B proveedor. Dolor «vendedores de a uno» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_animado_2d_p14-conseguir-vendedores-musical_20260904_aprobado.json
(antes: renombrar effix_animado_2d_p14-conseguir-vendedores-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo animado_2d: Animado 2D salsa urbana. Canción Salsa urbana / champeta a 98 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 15 · Llegó roto

**Público:** Empresas de empaques y packaging (🔥) · **Ángulo 15.1:** Empaque que protege  
**Estilo:** Pixar 3D (objeto antropomórfico) · **Música:** Latin pop alegre, 108 BPM  
**Personaje:** CAJITA, una caja de envío antropomórfica: la empresa de empaques que quiere venderle a las tiendas.  
**Dolor (3 veces en la letra):** «llegó roto»

**Micro-situación**  
*Momento.* Una tienda despacha mil pedidos al mes y el veinte por ciento llega golpeado. Con la caja de otro.  
*Síntoma.* Tú tienes el empaque que sí protege, y esa tienda no sabe que existes.  
*Explicación fallida.* Te dices que las tiendas compran la caja más barata.  
*Patrón.* Pero las tiendas que crecen pagan más por la caja el día que cuentan cuánto pierden en devoluciones.  
*Causa raíz.* No te falta producto. Te falta poner tu caja en las manos de las tiendas que hoy pierden pedidos.  
*Mecanismo.* En Feria Effix hay más de sesenta mil asistentes del ecommerce y trescientas cincuenta empresas, y un stand donde tu caja se toca.  

**Letra**

```
[Verso 1]
Otro pedido de esa tienda llegó roto
Con la caja de otro, y el cliente puso la foto
Yo tengo el empaque que protege de verdad
Pero llegó roto, y ella a mí no me va a buscar

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que hoy pierden pedidos
Y tu caja en sus manos, eso es lo que no han tenido

[Verso 2]
Me digo que compran la caja más barata
Pero la que crece paga más cuando ve lo que gasta
En devoluciones, en clientes que se van
Llegó roto otra vez, y yo sin mostrar

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que hoy pierden pedidos
Y tu caja en sus manos, eso es lo que no han tenido

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no llega roto, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Otro pedido de esa tienda llegó roto / Con la caja de otro, y el cliente puso la foto | Llegó roto | CAJITA on a packaging factory floor looking at a phone showing a photo of a crushed generic parcel with a sad face shape; a pile of sturdy s |
| 02 | CALLOUT | Yo tengo el empaque que protege de verdad / Pero llegó roto, y ella a mí no me va a buscar | ¿Fabricas empaques? | CAJITA turns to face the camera in a packaging factory floor with sample boxes, a crushed generic parcel with a sad face still visible. |
| 03 | SINTOMA | Me digo que compran la caja más barata | No saben que existes | Close-up of CAJITA's arms holding a perfect reinforced box while, on a screen behind, a store's chat with a message from CAJITA sits unread. |
| 04 | EXPL_FALLIDA | Pero la que crece paga más cuando ve lo que gasta | «Compran la más barata» | CAJITA from behind, shrugging at a price tag shape hanging on a thin flimsy box on a shelf. |
| 05 | PATRON | En devoluciones, en clientes que se van | Pagan más cuando cuentan devoluciones | Low-angle wide: a store owner at a desk buried under returned crushed parcels, counting coin shapes that fly away; CAJITA small at the door. |
| 06 | CAUSA_RAIZ | Llegó roto otra vez, y yo sin mostrar | Tu caja en sus manos | Extreme close-up of CAJITA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | CAJITA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las tiendas que hoy pierden pedidos / Y tu caja en sus manos, eso es lo que no han tenido | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; CAJITA small in the aisle looki |
| 09 | MECANISMO | Me digo que compran la caja más barata (repite el dolor en imagen) | Donde tu caja se toca | At a fair stand, CAJITA letting a store owner press and drop a reinforced box on the counter; it bounces intact; a small crowd leans in. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of CAJITA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no llega roto, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CAJITA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no llega roto, se acabó | Ya no llega roto | The factory floor again: a conveyor of reinforced boxes with a store's abstract logo-shape, a delivery van loading, CAJITA proud at the fron |

**Notas de producción.** Pixar latin pop, objeto antropomórfico. B2B empaques. Dolor «llegó roto» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_pixar_p15-empaque-protege-musical_20260904_aprobado.json
(antes: renombrar effix_pixar_p15-empaque-protege-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo pixar: Pixar latin pop, objeto antropomórfico. Canción Latin pop alegre a 108 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 16 · El marketplace sin vendedores

**Público:** Marketplaces (🔥) · **Ángulo 16.1:** Conseguir vendedores  
**Estilo:** Skeleton · **Música:** Reggaetón, 96 BPM  
**Personaje:** El esqueleto dirige un marketplace que no consigue vendedores.  
**Dolor (3 veces en la letra):** «con una mano los cuento»

**Micro-situación**  
*Momento.* Abres el panel y los vendedores nuevos del mes se cuentan con una mano.  
*Síntoma.* Inviertes en pauta para atraer vendedores y llegan de a uno, con poco catálogo.  
*Explicación fallida.* Te dices que los vendedores buenos ya están en los grandes.  
*Patrón.* Pero cada día abren marcas y tiendas buscando dónde vender, y eligen al marketplace que conocieron de frente.  
*Causa raíz.* No te faltan compradores. Te falta estar donde los vendedores deciden dónde vender.  
*Mecanismo.* En Feria Effix hay más de trescientas cincuenta empresas y miles de vendedores buscando canal, y tres días para reclutarlos de frente.  

**Letra**

```
[Verso 1]
Vendedores nuevos este mes: con una mano los cuento
Compradores tengo, pero vendedores, lo lamento
Pauto para atraerlos y llegan de a uno
Con una mano los cuento, y no llega ninguno

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los vendedores buscando un canal
Y eligen al que de frente les dijo cómo ganar

[Verso 2]
Me digo que los buenos ya están con los grandes
Pero cada día abren tiendas que buscan dónde
Y se van con el que les habló de frente un día
Con una mano los cuento, y la mano vacía

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los vendedores buscando un canal
Y eligen al que de frente les dijo cómo ganar

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no me alcanza la mano, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Vendedores nuevos este mes: con una mano los cuento / Compradores tengo, pero vendedores, lo lamento | Con una mano los cuentas | The skeleton in a marketplace office in front of a big screen: a buyers bar towering and a sellers bar tiny; one bony hand raised counting o |
| 02 | CALLOUT | Pauto para atraerlos y llegan de a uno / Con una mano los cuento, y no llega ninguno | ¿Tienes un marketplace? | the skeleton turns to face the camera in a marketplace office with a big screen of seller counts, the empty seller sign-up counter still vis |
| 03 | SINTOMA | Me digo que los buenos ya están con los grandes | Llegan de a uno | Close-up of a laptop: an ad spend slider goes up, a seller sign-up counter ticks once, a tiny catalogue with two items appears. |
| 04 | EXPL_FALLIDA | Pero cada día abren tiendas que buscan dónde | «Ya están con los grandes» | The skeleton from behind, looking at a wall of giant marketplace logo-shapes, shrugging. |
| 05 | PATRON | Y se van con el que les habló de frente un día | Eligen a quien les habló de frente | Low-angle wide: a street of new small shops opening their shutters one after another, each owner holding a phone looking for where to sell;  |
| 06 | CAUSA_RAIZ | Con una mano los cuento, y la mano vacía | Donde deciden dónde vender | Extreme close-up of the skeleton's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | the skeleton walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los vendedores buscando un canal / Y eligen al que de frente les dijo cómo ganar | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; the skeleton small in the aisle |
| 09 | MECANISMO | Me digo que los buenos ya están con los grandes (repite el dolor en imagen) | Miles de vendedores buscando canal | Two-shot at a fair stand: the skeleton handing a tablet with a sign-up form-shape to a blurred seller, a second seller signing on another ta |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of the skeleton seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking not |
| 11 | CTA | Y ya no me alcanza la mano, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | the skeleton facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands be |
| 12 | LOOP | Y ya no me alcanza la mano, se acabó | Ya no te alcanza la mano | The marketplace office again: the sellers bar now as tall as the buyers bar, the sign-up counter spinning, the skeleton leaning back. |

**Notas de producción.** Skeleton reggaetón. B2B marketplace. Dolor «con una mano los cuento» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_skeleton_p16-marketplace-vendedores-musical_20260904_aprobado.json
(antes: renombrar effix_skeleton_p16-marketplace-vendedores-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo skeleton: Skeleton reggaetón. Canción Reggaetón a 96 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 17 · Vender en otro país

**Público:** Internacionalización y expansión de negocios (🟡) · **Ángulo 17.1:** Vender en otro país  
**Estilo:** Crochet (mundo B&N) · **Música:** Cumbia pop, 100 BPM  
**Personaje:** PABLO, amigurumi del empresario que quiere vender en otro país. Único con color.  
**Dolor (3 veces en la letra):** «todavía no vendo allá»

**Micro-situación**  
*Momento.* Te preguntan si vendes en Ecuador o Guatemala, y dices que todavía no, sin saber por dónde empezar.  
*Síntoma.* Buscas cómo exportar y salen requisitos, no personas.  
*Explicación fallida.* Te dices que para entrar a otro país hay que ser grande.  
*Patrón.* Pero las empresas de tu tamaño que ya venden afuera lo hicieron con un aliado local.  
*Causa raíz.* No te falta tamaño. Te falta conocer a alguien del otro lado que ya venda allá.  
*Mecanismo.* En Feria Effix hay empresas de cinco países y ponentes de más de veinte, en el mismo recinto. El aliado del otro país está a un pasillo.  

**Letra**

```
[Verso 1]
Me preguntan por Ecuador, y todavía no vendo allá
Busco cómo exportar y salen requisitos, nada más
Un mapa con un solo país pintado de color
Todavía no vendo allá, y me da temor

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas de cinco países
Y el aliado del otro lado a un pasillo, sin disfraces

[Verso 2]
Me digo que para afuera hay que ser grande
Pero uno como yo ya vende allá, y no es gigante
Lo hizo con alguien local, no con un manual
Todavía no vendo allá, y eso va a cambiar

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas de cinco países
Y el aliado del otro lado a un pasillo, sin disfraces

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya vendo allá, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Me preguntan por Ecuador, y todavía no vendo allá / Busco cómo exportar y salen requisitos, nada más | Todavía no vendes allá | PABLO in a greyscale knitted office looking at a knitted map of Latin America on the wall where only one country is coloured; his mitten-han |
| 02 | CALLOUT | Un mapa con un solo país pintado de color / Todavía no vendo allá, y me da temor | ¿Quieres vender en otro país? | PABLO turns to face the camera in a small greyscale knitted office with a knitted map of Latin America on the wall, the knitted map with one |
| 03 | SINTOMA | Me digo que para afuera hay que ser grande | Requisitos, no personas | Close-up of a knitted laptop showing a long grey list of felt document shapes; PABLO's mitten scrolls and scrolls. |
| 04 | EXPL_FALLIDA | Pero uno como yo ya vende allá, y no es gigante | «Hay que ser grande» | PABLO from behind, small, looking up at a tall grey knitted skyscraper with a felt globe on top. |
| 05 | PATRON | Lo hizo con alguien local, no con un manual | Con un aliado local | Low-angle wide of the knitted street: a grey knitted business owner shakes hands with a figure holding a small felt flag of another country; |
| 06 | CAUSA_RAIZ | Todavía no vendo allá, y eso va a cambiar | Alguien del otro lado | Extreme close-up of PABLO's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | PABLO walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. The whole  |
| 08 | CORO_FERIA | Ahí están las empresas de cinco países / Y el aliado del otro lado a un pasillo, sin disfraces | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; PABLO small in the aisle lookin |
| 09 | MECANISMO | Me digo que para afuera hay que ser grande (repite el dolor en imagen) | Empresas de cinco países | At a knitted fair stand, PABLO exchanging knitted cards with two grey figures holding felt flags of different countries; a felt map on the c |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of PABLO seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. The |
| 11 | CTA | Y ya vendo allá, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | PABLO facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. T |
| 12 | LOOP | Y ya vendo allá, se acabó | Ya vendes allá | The knitted office again: the wall map now with two coloured countries, a knitted parcel with a felt flag on the desk, PABLO smiling with a  |

**Notas de producción.** Crochet cumbia. Mundo B&N, PABLO única con color; el mapa gana color país por país. Verbatim de crochet. Dolor «todavía no vendo allá» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_crochet_p17-otro-pais-musical_20260904_aprobado.json
(antes: renombrar effix_crochet_p17-otro-pais-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo crochet: Crochet cumbia. Canción Cumbia pop a 100 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 18 · Tengo local y no vendo online

**Público:** Comerciantes y negocios físicos que quieren vender online (🟡) · **Ángulo 18.1:** Tengo tienda física pero no vendo online  
**Estilo:** Claymation · **Música:** Merengue urbano, 130 BPM  
**Personaje:** ROSA, dueña de almacén de ropa en plastilina (continuidad del personaje de 'La acera').  
**Dolor (3 veces en la letra):** «no entró nadie»

**Micro-situación**  
*Momento.* Llovió todo el sábado, no entró nadie, y tu mes depende del clima y del andén.  
*Síntoma.* Mandas la foto por WhatsApp a las mismas clientas de siempre.  
*Explicación fallida.* Te dices que lo tuyo se vende es viéndolo.  
*Patrón.* Pero el local de al lado ya despacha para otra ciudad. Mismo producto, mismo precio.  
*Causa raíz.* No es que tu producto no sirva para internet. Es que nadie te ha mostrado cómo.  
*Mecanismo.* En Feria Effix están las plataformas para montar la tienda, las pasarelas, la logística y los que ya lo hicieron desde un local como el tuyo.  

**Letra**

```
[Verso 1]
Llovió el sábado y no entró nadie
Mi mes depende del clima y de la calle
Mando la foto a las de siempre, y contesta una
No entró nadie, y la vitrina no vende ninguna

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que te montan la tienda en la red
Y los que despachan desde un local como el de usted

[Verso 2]
Me digo que mi ropa se vende es viéndola
Pero la del lado ya despacha a otra ciudad, y es la misma tela
Nadie me ha mostrado cómo, y por eso no arranco
No entró nadie, y el andén sigue en blanco

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que te montan la tienda en la red
Y los que despachan desde un local como el de usted

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no depende del andén, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Llovió el sábado y no entró nadie / Mi mes depende del clima y de la calle | Llovió. No entró nadie | ROSA inside a clay clothing shop looking out through a window with clay raindrops at an empty clay sidewalk, clay dresses on racks behind he |
| 02 | CALLOUT | Mando la foto a las de siempre, y contesta una / No entró nadie, y la vitrina no vende ninguna | ¿Tienes local y no vendes online? | ROSA turns to face the camera in a small clay clothing shop with a window onto a rainy sidewalk, the clay shop window with rain and an empty |
| 03 | SINTOMA | Me digo que mi ropa se vende es viéndola | Las mismas clientas | Close-up of ROSA's clay phone: a photo of a dress sent to a chat with five avatar circles, one glows in reply. |
| 04 | EXPL_FALLIDA | Pero la del lado ya despacha a otra ciudad, y es la misma tela | «Se vende es viéndola» | ROSA from behind holding a dress up against a clay customer, turning it, gesturing 'you have to see it on'. |
| 05 | PATRON | Nadie me ha mostrado cómo, y por eso no arranco | La del lado ya despacha | Low-angle wide of the clay street: the shop next door loads clay parcels into a clay van; ROSA small in her doorway. |
| 06 | CAUSA_RAIZ | No entró nadie, y el andén sigue en blanco | Nadie te ha mostrado cómo | Extreme close-up of ROSA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | ROSA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que te montan la tienda en la red / Y los que despachan desde un local como el de usted | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; ROSA small in the aisle looking |
| 09 | MECANISMO | Me digo que mi ropa se vende es viéndola (repite el dolor en imagen) | Plataformas, pasarelas, logística | At a clay fair stand, ROSA between two clay figures: one holding a tablet with a storefront shape, the other a parcel; she touches the table |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of ROSA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no depende del andén, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | ROSA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no depende del andén, se acabó | Ya no depende del andén | The clay shop, sunny: ROSA taping a parcel at the counter with a small label, a clay courier at the door, the window clear. |

**Notas de producción.** Claymation merengue. Continuidad de ROSA (personaje 2D de 'La acera') en plastilina. Dolor «no entró nadie» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_claymation_p18-tienda-fisica-musical_20260904_aprobado.json
(antes: renombrar effix_claymation_p18-tienda-fisica-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo claymation: Claymation merengue. Canción Merengue urbano a 130 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 19 · Dos tiendas que no se hablan

**Público:** Retail (🟡) · **Ángulo 19.1:** Omnicanalidad  
**Estilo:** Anime · **Música:** Latin pop electrónico, 104 BPM  
**Personaje:** VALERIA, personaje anime: gerente de un retail cuya tienda física y tienda online no se hablan.  
**Dolor (3 veces en la letra):** «eso es de internet»

**Micro-situación**  
*Momento.* Un cliente compra en tu página, va a cambiarlo en la tienda, y le dicen que «eso es de internet».  
*Síntoma.* Tienes dos negocios que se llaman igual y no se hablan.  
*Explicación fallida.* Te dices que integrar eso es un proyecto de años.  
*Patrón.* Pero hay retailers de tu tamaño que ya lo integraron con proveedores del mercado.  
*Causa raíz.* No te falta presupuesto. Te falta conocer a los que ya conectaron tienda física y online.  
*Mecanismo.* En Feria Effix están las plataformas de omnicanalidad, la logística y más de doscientas ponencias de retailers que ya lo resolvieron.  

**Letra**

```
[Verso 1]
Compró en la página y en la tienda le dicen «eso es de internet»
Dos tiendas con mi nombre, y ninguna se entiende
El cliente se va, y no vuelve a ninguna
«Eso es de internet» me cuesta una fortuna

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que unieron la tienda y la red
Y te cuentan a quién llamaron, y a quién no, también

[Verso 2]
Me digo que integrar es un proyecto de años
Pero uno como yo ya lo hizo sin tantos daños
Con proveedores que existen, no desde cero
«Eso es de internet» lo escucho, y me desespero

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que unieron la tienda y la red
Y te cuentan a quién llamaron, y a quién no, también

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya nadie me lo dice, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Compró en la página y en la tienda le dicen «eso es de internet» / Dos tiendas con mi nombre, y ninguna se entiende | «Eso es de internet» | VALERIA in a retail head office between two screens: a physical store icon and an online store icon facing away from each other; on one scre |
| 02 | CALLOUT | El cliente se va, y no vuelve a ninguna / «Eso es de internet» me cuesta una fortuna | ¿Diriges un retail? | VALERIA turns to face the camera in a retail head office with two screens: physical store and online store, two identical logo-shapes facing |
| 03 | SINTOMA | Me digo que integrar es un proyecto de años | Dos negocios que no se hablan | Close-up of VALERIA's tablet with two separate dashboards side by side, a thin wall drawn between them. |
| 04 | EXPL_FALLIDA | Pero uno como yo ya lo hizo sin tantos daños | «Es un proyecto de años» | VALERIA from behind looking at a wall calendar with years marked, a giant clock shape above it. |
| 05 | PATRON | Con proveedores que existen, no desde cero | Ya lo hicieron con proveedores | Low-angle wide: a rival store-front where a customer returns an online parcel at the counter with a smile; VALERIA small on the sidewalk. |
| 06 | CAUSA_RAIZ | «Eso es de internet» lo escucho, y me desespero | A quién contrataron | Extreme close-up of VALERIA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | VALERIA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que unieron la tienda y la red / Y te cuentan a quién llamaron, y a quién no, también | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; VALERIA small in the aisle look |
| 09 | MECANISMO | Me digo que integrar es un proyecto de años (repite el dolor en imagen) | Plataformas de omnicanalidad | At a fair stand, VALERIA between two exhibitors: one holds a tablet where the two store icons now face each other joined by a line; the othe |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of VALERIA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya nadie me lo dice, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | VALERIA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya nadie me lo dice, se acabó | Ya nadie dice «eso es de internet» | The head office again: one screen with the two icons joined, a customer-shape returning a parcel with a check mark; VALERIA smiling at the t |

**Notas de producción.** Anime latin pop electrónico. Retail. Dolor «eso es de internet» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_anime_p19-omnicanal-musical_20260904_aprobado.json
(antes: renombrar effix_anime_p19-omnicanal-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo anime: Anime latin pop electrónico. Canción Latin pop electrónico a 104 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 20 · Demasiados chats

**Público:** Atención al cliente y Customer Experience (🟡) · **Ángulo 20.1:** Demasiados chats  
**Estilo:** Cyberpunk · **Música:** Reggaetón oscuro / trap latino, 92 BPM  
**Personaje:** NICO, encargado de atención al cliente en una ciudad cyberpunk, ahogado en chats.  
**Dolor (3 veces en la letra):** «demasiados chats»

**Micro-situación**  
*Momento.* Un cliente pregunta a las diez, le respondes a las dos, y ya compró en otro lado.  
*Síntoma.* Los mensajes se acumulan, respondes por orden de llegada, y los que más valen se enfrían.  
*Explicación fallida.* Te dices que necesitas contratar a otra persona.  
*Patrón.* Pero hay negocios con el triple de mensajes que responden en segundos con el mismo equipo.  
*Causa raíz.* No te falta gente. Te falta un sistema que responda lo repetido.  
*Mecanismo.* En Feria Effix están las plataformas de atención, los chatbots y los que ya atienden miles de chats al día, con demostración en stand.  

**Letra**

```
[Verso 1]
Demasiados chats y una sola persona
Preguntó a las diez, respondí a las dos, y ya no funciona
Compró en otro lado mientras yo contestaba
Demasiados chats, y ninguno se acababa

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los sistemas que responden primero
Y te dejan a ti lo que cierra el dinero

[Verso 2]
Me digo que necesito contratar a alguien más
Pero uno con el triple responde en segundos, no más
Con la misma gente, porque el sistema atiende
Demasiados chats, y el mío no se entiende

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los sistemas que responden primero
Y te dejan a ti lo que cierra el dinero

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no son demasiados, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Demasiados chats y una sola persona / Preguntó a las diez, respondí a las dos, y ya no funciona | Demasiados chats | NICO at a neon desk with dozens of floating holographic chat windows stacking up around him, one at the bottom timestamped hours ago with a  |
| 02 | CALLOUT | Compró en otro lado mientras yo contestaba / Demasiados chats, y ninguno se acababa | ¿Atiendes clientes por chat? | NICO turns to face the camera in a neon customer-service desk with floating chat holograms, a wall of holographic chat windows stacking up s |
| 03 | SINTOMA | Me digo que necesito contratar a alguien más | Ya compró en otro lado | Close-up of NICO's hands typing while a holographic queue counter climbs; a clock hologram spins. |
| 04 | EXPL_FALLIDA | Pero uno con el triple responde en segundos, no más | «Necesito otra persona» | NICO from behind, pointing at an empty neon chair beside him, a hologram of a job-post shape floating above it. |
| 05 | PATRON | Con la misma gente, porque el sistema atiende | El triple, en segundos | Low-angle wide: through a glass wall, a rival desk where one person sips coffee while holographic replies fire off by themselves; NICO small |
| 06 | CAUSA_RAIZ | Demasiados chats, y el mío no se entiende | Un sistema para lo repetido | Extreme close-up of NICO's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | NICO walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los sistemas que responden primero / Y te dejan a ti lo que cierra el dinero | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; NICO small in the aisle looking |
| 09 | MECANISMO | Me digo que necesito contratar a alguien más (repite el dolor en imagen) | Chatbots con demostración | At a fair stand under neon, NICO watching an exhibitor tap once on a tablet and a stream of holographic replies answer a queue; his mouth op |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of NICO seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no son demasiados, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | NICO facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no son demasiados, se acabó | Ya no son demasiados | The neon desk again: holographic windows answering themselves in order, only two flagged windows in front of NICO, who leans back with coffe |

**Notas de producción.** Cyberpunk reggaetón oscuro. Dolor «demasiados chats» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_cyberpunk_p20-chats-musical_20260904_aprobado.json
(antes: renombrar effix_cyberpunk_p20-chats-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo cyberpunk: Cyberpunk reggaetón oscuro. Canción Reggaetón oscuro / trap latino a 92 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 21 · Fotos que no venden

**Público:** Contenido para e-commerce (🟡) · **Ángulo 21.1:** Fotos que no venden  
**Estilo:** Animado 2D · **Música:** Salsa urbana / champeta, 98 BPM  
**Personaje:** CAMI, dueña de tienda que hace sus propias fotos, en animación 2D.  
**Dolor (3 veces en la letra):** «nadie pregunta el precio»

**Micro-situación**  
*Momento.* Subes la foto del producto, la ven trescientas personas, y nadie pregunta el precio.  
*Síntoma.* La foto es bonita, el producto es bueno, y nadie compra.  
*Explicación fallida.* Te dices que te falta una cámara mejor.  
*Patrón.* Pero las fotos que más venden hoy se hacen con celular: cambia quién sale y qué muestra.  
*Causa raíz.* No te falta cámara. Te falta saber qué tiene que mostrar una foto para que alguien compre.  
*Mecanismo.* En Feria Effix están las agencias de contenido, los creadores y más de doscientas ponencias sobre el contenido que sí vende.  

**Letra**

```
[Verso 1]
Subo la foto y nadie pregunta el precio
La ven trescientos y ninguno me da el gusto
Fondo blanco, buena luz, producto bonito
Y nadie pregunta el precio, ni un poquito

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que hacen las fotos que venden
Y te muestran qué mostrar pa' que la gente entienda

[Verso 2]
Me digo que me falta una cámara mejor
Pero la foto que vende se hizo con un celular
Cambia quién sale, y cambia lo que enseño
Nadie pregunta el precio, y yo con el mismo empeño

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que hacen las fotos que venden
Y te muestran qué mostrar pa' que la gente entienda

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ahora sí preguntan, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Subo la foto y nadie pregunta el precio / La ven trescientos y ninguno me da el gusto | Nadie pregunta el precio | CAMI in a home studio corner photographing a product on a white sheet with her phone; on the phone the photo gets small heart shapes but no  |
| 02 | CALLOUT | Fondo blanco, buena luz, producto bonito / Y nadie pregunta el precio, ni un poquito | ¿Tus fotos no venden? | CAMI turns to face the camera in a small home studio corner with a white sheet and a product, the product photo that nobody taps still visib |
| 03 | SINTOMA | Me digo que me falta una cámara mejor | Bonita, y nadie compra | Close-up of the phone gallery: a grid of clean product photos, each with a tiny grey counter. |
| 04 | EXPL_FALLIDA | Pero la foto que vende se hizo con un celular | «Me falta mejor cámara» | CAMI from behind looking at a camera-shop window with a big camera and a price tag shape. |
| 05 | PATRON | Cambia quién sale, y cambia lo que enseño | Las que venden son con celular | Low-angle wide: on a giant phone-shaped screen, a woman holding the same product in a kitchen, smiling, with message bubbles pouring in; CAM |
| 06 | CAUSA_RAIZ | Nadie pregunta el precio, y yo con el mismo empeño | Qué tiene que mostrar la foto | Extreme close-up of CAMI's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | CAMI walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que hacen las fotos que venden / Y te muestran qué mostrar pa' que la gente entienda | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; CAMI small in the aisle looking |
| 09 | MECANISMO | Me digo que me falta una cámara mejor (repite el dolor en imagen) | El contenido que sí vende | At a fair stand, CAMI watching a creator film a product with a phone while an agency person points at a screen with two photos side by side: |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of CAMI seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ahora sí preguntan, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | CAMI facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ahora sí preguntan, se acabó | Ahora sí preguntan | The home corner again, now with a friend holding the product in use, CAMI filming with the phone, message bubbles popping on the screen. |

**Notas de producción.** Animado 2D salsa urbana. Bible flat 2D verbatim. Dolor «nadie pregunta el precio» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_animado_2d_p21-fotos-musical_20260904_aprobado.json
(antes: renombrar effix_animado_2d_p21-fotos-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo animado_2d: Animado 2D salsa urbana. Canción Salsa urbana / champeta a 98 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 22 · Las plataformas que no se hablan

**Público:** Desarrollo, programación e integraciones (🟡) · **Ángulo 22.1:** APIs  
**Estilo:** Pixar 3D (objeto antropomórfico) · **Música:** Latin pop alegre, 108 BPM  
**Personaje:** ENCHUFE, un conector antropomórfico: el desarrollador que vive uniendo plataformas que no se hablan.  
**Dolor (3 veces en la letra):** «no se hablan»

**Micro-situación**  
*Momento.* Una tienda te llama porque su plataforma, su pasarela y su logística no se hablan, y alguien copia pedidos a mano.  
*Síntoma.* Cada integración es un proyecto nuevo, porque nunca sabes qué herramienta usa el próximo cliente.  
*Explicación fallida.* Te dices que en ecommerce cada tienda es un mundo.  
*Patrón.* Pero las plataformas del ecommerce latino se cuentan con los dedos, y todas tienen equipo técnico.  
*Causa raíz.* No te falta código. Te falta conocer de frente a los equipos de las herramientas que integras.  
*Mecanismo.* En Feria Effix están con stand las plataformas, las pasarelas y las logísticas con sus equipos técnicos, y las tiendas que necesitan que las conectes.  

**Letra**

```
[Verso 1]
La tienda, el pago y el envío no se hablan
Y alguien copia los pedidos a mano, y se traban
Me llaman a mí, y cada vez empiezo de cero
Porque no se hablan, y yo soy el mensajero

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las plataformas con su equipo técnico
Y las tiendas que te buscan pa' que las conectes rápido

[Verso 2]
Me digo que cada tienda es un mundo aparte
Pero las plataformas se cuentan con los dedos, en cualquier parte
Y todas tienen alguien con quien hablar de frente
No se hablan, y yo sin conocer a esa gente

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las plataformas con su equipo técnico
Y las tiendas que te buscan pa' que las conectes rápido

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ahora sí se hablan, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | La tienda, el pago y el envío no se hablan / Y alguien copia los pedidos a mano, y se traban | No se hablan | ENCHUFE on a developer desk between three glowing boxes (a store shape, a card shape, a truck shape) that do not connect; a hand-shaped spre |
| 02 | CALLOUT | Me llaman a mí, y cada vez empiezo de cero / Porque no se hablan, y yo soy el mensajero | ¿Desarrollas para tiendas online? | ENCHUFE turns to face the camera in a developer's desk with three screens and cables everywhere, three glowing boxes (store, payment, logist |
| 03 | SINTOMA | Me digo que cada tienda es un mundo aparte | Cada vez desde cero | Close-up of ENCHUFE's prongs plugging into a box, a spark, then unplugging to start again with a different-shaped socket. |
| 04 | EXPL_FALLIDA | Pero las plataformas se cuentan con los dedos, en cualquier parte | «Cada tienda es un mundo» | ENCHUFE from behind looking at a wall of dozens of different socket shapes, arms spread. |
| 05 | PATRON | Y todas tienen alguien con quien hablar de frente | Se cuentan con los dedos | Low-angle wide: a big glowing hall where a handful of large platform-shapes stand with friendly technician figures beside them; ENCHUFE smal |
| 06 | CAUSA_RAIZ | No se hablan, y yo sin conocer a esa gente | Conoce a los equipos de frente | Extreme close-up of ENCHUFE's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | ENCHUFE walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las plataformas con su equipo técnico / Y las tiendas que te buscan pa' que las conectes rápido | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; ENCHUFE small in the aisle look |
| 09 | MECANISMO | Me digo que cada tienda es un mundo aparte (repite el dolor en imagen) | Plataformas con equipo técnico | At a fair stand, ENCHUFE with a technician figure showing a diagram where the three boxes now link with glowing lines; a store owner watches |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of ENCHUFE seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ahora sí se hablan, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | ENCHUFE facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ahora sí se hablan, se acabó | Ahora sí se hablan | The developer desk again: the three boxes linked by steady glowing lines, orders flowing through, ENCHUFE resting with its spark on. |

**Notas de producción.** Pixar latin pop, objeto antropomórfico (conector). Dolor «no se hablan» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_pixar_p22-apis-musical_20260904_aprobado.json
(antes: renombrar effix_pixar_p22-apis-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo pixar: Pixar latin pop, objeto antropomórfico (conector). Canción Latin pop alegre a 108 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 23 · El pago que era fraude

**Público:** Ciberseguridad y prevención de fraude (🟡) · **Ángulo 23.1:** Fraude en pagos  
**Estilo:** Skeleton · **Música:** Reggaetón, 96 BPM  
**Personaje:** El esqueleto es la empresa de prevención de fraude que quiere que las tiendas la escuchen antes.  
**Dolor (3 veces en la letra):** «era fraude»

**Micro-situación**  
*Momento.* A una tienda le aprueban un pago, despachan, y a los quince días llega el contracargo: era fraude.  
*Síntoma.* Vendes protección, y las tiendas solo te buscan después de perder.  
*Explicación fallida.* Te dices que la seguridad se vende después del susto.  
*Patrón.* Pero las tiendas que ya crecieron contratan antes, porque alguien les mostró el riesgo con casos reales.  
*Causa raíz.* No te falta producto. Te falta estar delante de miles de tiendas antes del fraude.  
*Mecanismo.* En Feria Effix hay más de sesenta mil asistentes que cobran por internet, y un stand para mostrarles el riesgo con ejemplos reales.  

**Letra**

```
[Verso 1]
Aprobaron el pago, despacharon, y era fraude
Quince días después el contracargo, y nadie sabe
Yo vendo la protección que lo detiene antes
Pero era fraude, y me llaman después, no antes

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que cobran cada día
Y tú les muestras el riesgo antes de que sea un día

[Verso 2]
Me digo que la seguridad se vende con el susto
Pero la que creció contrató antes, y con gusto
Porque alguien de frente le mostró un caso real
Era fraude otra vez, y yo sin estar ahí pa' evitarlo

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las tiendas que cobran cada día
Y tú les muestras el riesgo antes de que sea un día

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no es fraude, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Aprobaron el pago, despacharon, y era fraude / Quince días después el contracargo, y nadie sabe | Era fraude | The skeleton in a dim security room watching a big screen: a card-shape transaction turns green, a parcel-shape leaves, then fifteen calenda |
| 02 | CALLOUT | Yo vendo la protección que lo detiene antes / Pero era fraude, y me llaman después, no antes | ¿Vendes prevención de fraude? | the skeleton turns to face the camera in a security operations room with screens of transactions, a transaction card-shape that turns red af |
| 03 | SINTOMA | Me digo que la seguridad se vende con el susto | Te buscan después de perder | Close-up of a bony hand on a phone: the only incoming call bubbles are timestamped after red card-shapes. |
| 04 | EXPL_FALLIDA | Pero la que creció contrató antes, y con gusto | «Se vende con el susto» | The skeleton from behind, shrugging at a wall poster-shape of a scared face, tapping it as if to say 'that sells'. |
| 05 | PATRON | Porque alguien de frente le mostró un caso real | Contratan antes, con un caso real | Low-angle wide: a tall glowing store building with a shield-shape on the door and green cards flowing in; the skeleton small on the street. |
| 06 | CAUSA_RAIZ | Era fraude otra vez, y yo sin estar ahí pa' evitarlo | Antes del fraude | Extreme close-up of the skeleton's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | the skeleton walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las tiendas que cobran cada día / Y tú les muestras el riesgo antes de que sea un día | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; the skeleton small in the aisle |
| 09 | MECANISMO | Me digo que la seguridad se vende con el susto (repite el dolor en imagen) | Sesenta mil que cobran por internet | Two-shot at a fair stand: the skeleton showing a tablet where a red card-shape is caught by a shield before a parcel leaves; a blurred store |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of the skeleton seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking not |
| 11 | CTA | Y ya no es fraude, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | the skeleton facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands be |
| 12 | LOOP | Y ya no es fraude, se acabó | Ya no es fraude | The security room again: the big screen full of green cards and shields, the phone lit with incoming call bubbles before any red card, the s |

**Notas de producción.** Skeleton reggaetón. B2B seguridad. Dolor «era fraude» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_skeleton_p23-fraude-pagos-musical_20260904_aprobado.json
(antes: renombrar effix_skeleton_p23-fraude-pagos-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo skeleton: Skeleton reggaetón. Canción Reggaetón a 96 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 24 · Vendo y no sé cuánto debo

**Público:** Servicios profesionales para e-commerce (🟡) · **Ángulo 24.1:** Impuestos  
**Estilo:** Crochet (mundo B&N) · **Música:** Cumbia pop, 100 BPM  
**Personaje:** DIEGO, amigurumi del dueño de tienda que no sabe cuánto debe de impuestos. Único con color.  
**Dolor (3 veces en la letra):** «no sé cuánto debo»

**Micro-situación**  
*Momento.* Llega la carta de impuestos y no sabes si debes mucho, poco, o nada. Vendes bien, y no tienes idea.  
*Síntoma.* Cada pago, cada pasarela, cada envío queda en un lugar distinto, y nadie lo junta.  
*Explicación fallida.* Te dices que eso lo miras cuando la tienda sea más grande.  
*Patrón.* Pero las tiendas grandes tienen contador de ecommerce desde que eran pequeñas.  
*Causa raíz.* No te falta plata para un contador. Te falta uno que entienda el modelo.  
*Mecanismo.* En Feria Effix están los contadores y abogados especializados en ecommerce, y más de doscientas ponencias para entender lo que debes y lo que no.  

**Letra**

```
[Verso 1]
Llegó la carta y no sé cuánto debo
Vendo bien, pero de impuestos no entiendo
Cada pago en un lado, y nadie lo junta
No sé cuánto debo, y me da miedo la pregunta

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los contadores que entienden la tienda
Y te dicen qué debes antes de que te sorprenda

[Verso 2]
Me digo que eso lo miro cuando sea más grande
Pero la grande tuvo contador desde temprano, y con calma
No me falta plata, me falta uno que entienda
No sé cuánto debo, y la carta me espera en la mesa

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los contadores que entienden la tienda
Y te dicen qué debes antes de que te sorprenda

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya sé cuánto debo, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Llegó la carta y no sé cuánto debo / Vendo bien, pero de impuestos no entiendo | No sabes cuánto debes | DIEGO at a greyscale knitted desk holding a knitted envelope with a felt exclamation mark, a pile of felt receipts and a knitted laptop with |
| 02 | CALLOUT | Cada pago en un lado, y nadie lo junta / No sé cuánto debo, y me da miedo la pregunta | ¿Vendes y no sabes de impuestos? | DIEGO turns to face the camera in a small greyscale knitted home office with a knitted laptop and a pile of felt receipts, a knitted envelop |
| 03 | SINTOMA | Me digo que eso lo miro cuando sea más grande | Nadie lo junta | Close-up of felt receipts of different shapes scattered across the knitted desk; DIEGO's mitten tries to stack them and they slide apart. |
| 04 | EXPL_FALLIDA | Pero la grande tuvo contador desde temprano, y con calma | «Cuando sea más grande» | DIEGO from behind sliding the envelope under the knitted laptop and turning to a knitted parcel to pack. |
| 05 | PATRON | No me falta plata, me falta uno que entienda | Contador desde temprano | Low-angle wide of the knitted street: a big grey knitted shop with a small grey accountant figure at its door holding a tidy folder; DIEGO s |
| 06 | CAUSA_RAIZ | No sé cuánto debo, y la carta me espera en la mesa | Uno que entienda el modelo | Extreme close-up of DIEGO's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | DIEGO walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. The whole  |
| 08 | CORO_FERIA | Ahí están los contadores que entienden la tienda / Y te dicen qué debes antes de que te sorprenda | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; DIEGO small in the aisle lookin |
| 09 | MECANISMO | Me digo que eso lo miro cuando sea más grande (repite el dolor en imagen) | Contadores especializados en ecommerce | At a knitted fair stand, DIEGO across from a grey knitted accountant figure with a felt chart of three clear bars; the envelope on the count |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of DIEGO seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. The |
| 11 | CTA | Y ya sé cuánto debo, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | DIEGO facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. T |
| 12 | LOOP | Y ya sé cuánto debo, se acabó | Ya sabes cuánto debes | The knitted office again: receipts in a tidy knitted folder, the laptop with a clean felt summary, DIEGO calm with coffee, the envelope with |

**Notas de producción.** Crochet cumbia. DIEGO única con color. Verbatim de crochet. Dolor «no sé cuánto debo» 3 veces. No se dan cifras ni consejos tributarios.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_crochet_p24-impuestos-musical_20260904_aprobado.json
(antes: renombrar effix_crochet_p24-impuestos-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo crochet: Crochet cumbia. Canción Cumbia pop a 100 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 25 · Quiero aprender ecommerce

**Público:** Educación y formación en e-commerce (🟡) · **Ángulo 25.1:** Aprender e-commerce  
**Estilo:** Claymation · **Música:** Merengue urbano, 130 BPM  
**Personaje:** LUCÍA, estudiante de plastilina que quiere aprender ecommerce y no sabe por dónde.  
**Dolor (3 veces en la letra):** «ningún primer paso»

**Micro-situación**  
*Momento.* Quieres aprender ecommerce, buscas por dónde, y hay mil cursos, mil videos y ningún primer paso.  
*Síntoma.* Aprendes teoría, y no has visto una tienda real funcionando por dentro.  
*Explicación fallida.* Te dices que primero terminas de estudiar.  
*Patrón.* Pero los que hoy trabajan en ecommerce aprendieron viendo a las empresas hacerlo, no esperando.  
*Causa raíz.* No te falta información. Te falta ver el negocio real y hablar con quien lo opera.  
*Mecanismo.* En Feria Effix están más de trescientas cincuenta empresas del ecommerce con sus dueños, y más de doscientas ponencias de los que ya tienen resultados.  

**Letra**

```
[Verso 1]
Quiero aprender ecommerce y no hay ningún primer paso
Mil cursos, mil videos, y yo dando vueltas al vaso
Sé la teoría, pero nunca vi una tienda por dentro
Ningún primer paso, y el tiempo corriendo

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas con sus dueños al frente
Y en tres días aprendes lo que no enseña la gente

[Verso 2]
Me digo que primero termino de estudiar
Pero el que ya trabaja aprendió viendo el lugar
Viendo a las empresas hacerlo, y preguntando
Ningún primer paso, y yo sigo esperando

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas con sus dueños al frente
Y en tres días aprendes lo que no enseña la gente

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya tengo el primer paso, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Quiero aprender ecommerce y no hay ningún primer paso / Mil cursos, mil videos, y yo dando vueltas al vaso | Ningún primer paso | LUCIA at a clay library table with a laptop showing a grid of dozens of tiny course-card shapes; her clay notebook full of arrows pointing e |
| 02 | CALLOUT | Sé la teoría, pero nunca vi una tienda por dentro / Ningún primer paso, y el tiempo corriendo | ¿Quieres aprender ecommerce? | LUCÍA turns to face the camera in a clay university library table with a laptop and notebooks, a clay notebook with too many arrows and no f |
| 03 | SINTOMA | Me digo que primero termino de estudiar | Nunca viste una tienda por dentro | Close-up of the clay notebook: neat theory diagrams, and beside it a phone with a blurred real store video she pauses. |
| 04 | EXPL_FALLIDA | Pero el que ya trabaja aprendió viendo el lugar | «Primero termino de estudiar» | LUCIA from behind looking at a clay wall calendar with a graduation-cap shape circled far away. |
| 05 | PATRON | Viendo a las empresas hacerlo, y preguntando | Aprendieron viendo a las empresas | Low-angle wide: through the library window, a clay warehouse where a young worker packs parcels beside an owner explaining; LUCIA small at t |
| 06 | CAUSA_RAIZ | Ningún primer paso, y yo sigo esperando | Ve el negocio real | Extreme close-up of LUCÍA's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | LUCÍA walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las empresas con sus dueños al frente / Y en tres días aprendes lo que no enseña la gente | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; LUCÍA small in the aisle lookin |
| 09 | MECANISMO | Me digo que primero termino de estudiar (repite el dolor en imagen) | Empresas con sus dueños al frente | At a clay fair stand, LUCIA with her notebook open asking a clay business owner who points at a product and a tablet; she writes fast. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of LUCÍA seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya tengo el primer paso, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | LUCÍA facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya tengo el primer paso, se acabó | Ya tienes el primer paso | The library table again: the notebook now with one clear arrow and a first box ticked, the laptop showing a single storefront shape, LUCIA s |

**Notas de producción.** Claymation merengue. Dolor «ningún primer paso» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_claymation_p25-aprender-musical_20260904_aprobado.json
(antes: renombrar effix_claymation_p25-aprender-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo claymation: Claymation merengue. Canción Merengue urbano a 130 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 26 · La transformación digital que no llega

**Público:** Ejecutivos y líderes de transformación empresarial (🟡) · **Ángulo 26.1:** Transformación digital  
**Estilo:** Anime · **Música:** Latin pop electrónico, 104 BPM  
**Personaje:** RICARDO, personaje anime: gerente al que le pidieron transformación digital y no sabe por dónde.  
**Dolor (3 veces en la letra):** «solo una presentación»

**Micro-situación**  
*Momento.* La junta aprobó la transformación digital hace un año, y lo único que hay es una presentación.  
*Síntoma.* Todo el mundo habla de digital en tu empresa y ningún proceso cambió.  
*Explicación fallida.* Te dices que primero hay que ordenar la casa.  
*Patrón.* Pero las empresas que ya se transformaron empezaron por un proceso pequeño que vieron funcionando en otra empresa.  
*Causa raíz.* No te falta estrategia. Te falta ver casos reales contados por quien los implementó.  
*Mecanismo.* En Feria Effix hay más de doscientas ponencias de empresas que ya vendieron, atendieron y operaron en digital, y los proveedores que lo implementan.  

**Letra**

```
[Verso 1]
Un año después, solo una presentación
La junta aprobó, y no cambió ni una operación
Todos hablan de digital en la reunión
Y lo único que hay es solo una presentación

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas que ya lo hicieron
Y te cuentan de frente por dónde lo movieron

[Verso 2]
Me digo que primero hay que ordenar la casa
Pero el que ya cambió empezó con algo que pasa
Un proceso pequeño que vio en otra empresa
Solo una presentación, y la junta que espera

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están las empresas que ya lo hicieron
Y te cuentan de frente por dónde lo movieron

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no es una presentación, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Un año después, solo una presentación / La junta aprobó, y no cambió ni una operación | Solo una presentación | RICARDO in a boardroom in front of a big screen with a slide-shape showing a rocket icon on a launch pad; a calendar on the wall with twelve |
| 02 | CALLOUT | Todos hablan de digital en la reunión / Y lo único que hay es solo una presentación | ¿Te pidieron transformación digital? | RICARDO turns to face the camera in a corporate boardroom with a big screen, a slide-shape with a rocket icon that never launches still visi |
| 03 | SINTOMA | Me digo que primero hay que ordenar la casa | Ningún proceso cambió | Close-up of the boardroom table: several folders with the same rocket icon, coffee cups, no laptop running anything. |
| 04 | EXPL_FALLIDA | Pero el que ya cambió empezó con algo que pasa | «Primero ordenar la casa» | RICARDO from behind at a whiteboard drawing a big house shape with many rooms and writing check-boxes in each room. |
| 05 | PATRON | Un proceso pequeño que vio en otra empresa | Empezaron con un proceso pequeño | Low-angle wide: across the street, a rival company's window where a small glowing process-diagram runs on a screen and two employees high-fi |
| 06 | CAUSA_RAIZ | Solo una presentación, y la junta que espera | Casos reales de quien lo hizo | Extreme close-up of RICARDO's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | RICARDO walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están las empresas que ya lo hicieron / Y te cuentan de frente por dónde lo movieron | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; RICARDO small in the aisle look |
| 09 | MECANISMO | Me digo que primero hay que ordenar la casa (repite el dolor en imagen) | Empresas que ya lo hicieron | At a fair auditorium, RICARDO in the front row as a speaker on stage points at a simple three-step diagram; RICARDO writes in his folder. |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of RICARDO seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no es una presentación, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | RICARDO facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ya no es una presentación, se acabó | Ya no es una presentación | The boardroom again: the big screen shows a small process-diagram running with green check marks, the rocket icon lifting off in the corner, |

**Notas de producción.** Anime latin pop electrónico. Dolor «solo una presentación» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_anime_p26-transformacion-musical_20260904_aprobado.json
(antes: renombrar effix_anime_p26-transformacion-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo anime: Anime latin pop electrónico. Canción Latin pop electrónico a 104 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 27 · Solo no lo puedo coger

**Público:** Empresarios que buscan networking y alianzas (🔵) · **Ángulo 27.1:** Encontrar socios  
**Estilo:** Cyberpunk · **Música:** Reggaetón oscuro / trap latino, 92 BPM  
**Personaje:** SANTIAGO, empresario en una ciudad cyberpunk que necesita un socio.  
**Dolor (3 veces en la letra):** «solo no lo puedo coger»

**Micro-situación**  
*Momento.* Te llega un negocio grande, lo miras, y sabes que solo no lo puedes coger.  
*Síntoma.* Piensas en quién podría entrar contigo y no se te ocurre nadie que no sea familia.  
*Explicación fallida.* Te dices que un socio se encuentra con el tiempo.  
*Patrón.* Pero los negocios que ves crecer casi siempre son de dos o tres que se conocieron en algún lado.  
*Causa raíz.* No es que no haya socios para ti. Es que los socios se conocen en lugares donde tú no estás.  
*Mecanismo.* En Feria Effix hay más de trescientas cincuenta empresas de cinco países en el mismo recinto, y muchas llegaron a lo mismo: buscar con quién crecer.  

**Letra**

```
[Verso 1]
Me llegó el negocio grande y solo no lo puedo coger
Pienso en un socio, y no se me ocurre a quién
Familia, amigos, y nadie que sepa de esto
Solo no lo puedo coger, y lo dejo puesto

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que buscan con quién crecer
Y el socio que no tienes te lo cruzas al volver

[Verso 2]
Me digo que un socio se encuentra con el tiempo
Pero el negocio que crece son dos que se conocieron, lo siento
En algún lugar donde yo nunca he estado
Solo no lo puedo coger, y el tiempo ha pasado

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que buscan con quién crecer
Y el socio que no tienes te lo cruzas al volver

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ya no estoy solo, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Me llegó el negocio grande y solo no lo puedo coger / Pienso en un socio, y no se me ocurre a quién | Solo no lo puedes coger | SANTIAGO on a rooftop office at night holding a glowing contract-shape too large for one hand, the other hand empty, the neon city below. |
| 02 | CALLOUT | Familia, amigos, y nadie que sepa de esto / Solo no lo puedo coger, y lo dejo puesto | ¿Necesitas un socio? | SANTIAGO turns to face the camera in a rooftop office at night over a neon city, a glowing contract-shape too big to hold with one hand stil |
| 03 | SINTOMA | Me digo que un socio se encuentra con el tiempo | Nadie que no sea familia | Close-up of his phone: a short contact list with family-shaped avatars only; his thumb scrolls and reaches the end. |
| 04 | EXPL_FALLIDA | Pero el negocio que crece son dos que se conocieron, lo siento | «Se encuentra con el tiempo» | SANTIAGO from behind leaning on the railing looking at the city, a clock hologram drifting past. |
| 05 | PATRON | En algún lugar donde yo nunca he estado | Dos que se conocieron en algún lado | Low-angle wide: on a giant hologram above the city, two figures shaking hands over a glowing company-shape that grows; SANTIAGO small on the |
| 06 | CAUSA_RAIZ | Solo no lo puedo coger, y el tiempo ha pasado | Donde tú no estás | Extreme close-up of SANTIAGO's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | SANTIAGO walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que buscan con quién crecer / Y el socio que no tienes te lo cruzas al volver | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; SANTIAGO small in the aisle loo |
| 09 | MECANISMO | Me digo que un socio se encuentra con el tiempo (repite el dolor en imagen) | Empresas buscando con quién crecer | At a fair stand under neon, SANTIAGO across from a woman entrepreneur holding the other half of a glowing contract-shape; the two halves dri |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of SANTIAGO seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ya no estoy solo, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | SANTIAGO facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind |
| 12 | LOOP | Y ya no estoy solo, se acabó | Ya no estás solo | The rooftop again: SANTIAGO and the partner each holding one side of the big contract-shape, steady, the city lights behind. |

**Notas de producción.** Cyberpunk reggaetón oscuro. Dolor «solo no lo puedo coger» 3 veces.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_cyberpunk_p27-socios-musical_20260904_aprobado.json
(antes: renombrar effix_cyberpunk_p27-socios-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo cyberpunk: Cyberpunk reggaetón oscuro. Canción Reggaetón oscuro / trap latino a 92 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```


---

## 28 · Nadie sabe lo que sé

**Público:** Personas que quieren convertirse en referentes del e-commerce (🔵) · **Ángulo 28.1:** Construir marca personal  
**Estilo:** Animado 2D · **Música:** Salsa urbana / champeta, 98 BPM  
**Personaje:** JULIÁN, profesional del ecommerce que sabe mucho y nadie lo asocia con eso, en animación 2D.  
**Dolor (3 veces en la letra):** «nadie sabe lo que sé»

**Micro-situación**  
*Momento.* Alguien te pregunta a qué te dedicas, se lo explicas bien, y te dice que nunca te había visto hablar de eso.  
*Síntoma.* Tu perfil son fotos de la vida y uno que otro repost.  
*Explicación fallida.* Te dices que la marca personal es para los que venden cursos.  
*Patrón.* Pero las personas que hoy reciben las oportunidades de tu sector son las que sí se mostraron.  
*Causa raíz.* No es que la marca personal no sea para ti. Es que nunca has estado rodeado de gente que la construye.  
*Mecanismo.* En Feria Effix hay doscientos ponentes que viven de que los conozcan, y tres días para grabar contenido con ellos y ver cómo lo hacen.  

**Letra**

```
[Verso 1]
Explico lo que hago y me dicen «no sabía»
Nadie sabe lo que sé, y lo sé desde hace días
Mi perfil son fotos de la vida y un repost
Nadie sabe lo que sé, y el que sabe menos, cobró

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que viven de que los conozcan
Y en tres días grabas con ellos, y te reconozcan

[Verso 2]
Me digo que la marca personal es pa' vender cursos
Pero el que recibe las oportunidades hoy se mostró, seguro
Nunca he estado con gente que la construya
Nadie sabe lo que sé, y la oportunidad es suya

[Coro]
Feria Effix, del quince al diecinueve
En Plaza Mayor, Medellín, todo se mueve
Ahí están los que viven de que los conozcan
Y en tres días grabas con ellos, y te reconozcan

[Puente]
Más de trescientas cincuenta empresas, sesenta mil personas
Doscientas ponencias pa' aprender de las que ya funcionan

[Outro]
Y ahora sí saben lo que sé, se acabó
Compra tu ingreso dando clic en el botón
```

**Las 12 escenas**

| # | Beat | Se canta | En pantalla | Escena |
|---|---|---|---|---|
| 01 | MOMENTO | Explico lo que hago y me dicen «no sabía» / Nadie sabe lo que sé, y lo sé desde hace días | Nadie sabe lo que sé | JULIAN at a co-working desk mid-conversation with a colleague whose speech bubble is a surprised face; JULIAN's phone on the desk shows a pr |
| 02 | CALLOUT | Mi perfil son fotos de la vida y un repost / Nadie sabe lo que sé, y el que sabe menos, cobró | ¿Sabes de ecommerce y nadie lo sabe? | JULIÁN turns to face the camera in a co-working desk and, later, a street with the city behind, a social profile grid full of casual photos  |
| 03 | SINTOMA | Me digo que la marca personal es pa' vender cursos | Fotos de la vida y un repost | Close-up of the phone grid: beach photos, food photos, one repost card; a thumb scrolls and finds nothing about work. |
| 04 | EXPL_FALLIDA | Pero el que recibe las oportunidades hoy se mostró, seguro | «Es para vender cursos» | JULIAN from behind waving off a floating course-box shape with a price tag, shaking his head. |
| 05 | PATRON | Nunca he estado con gente que la construya | Los que se mostraron reciben | Low-angle wide: on a giant screen a person JULIAN's age speaks on a small stage and receives a floating opportunity-envelope; JULIAN small b |
| 06 | CAUSA_RAIZ | Nadie sabe lo que sé, y la oportunidad es suya | Rodéate de quien la construye | Extreme close-up of JULIÁN's eyes; in the reflection a bright crowded trade-fair pavilion appears. |
| 07 | CORO_LLEGADA | Feria Effix, del quince al diecinueve / En Plaza Mayor, Medellín, todo se mueve | Feria Effix · 15–19 oct · Medellín | JULIÁN walking toward the glass entrance of a large modern convention centre in Medellin, morning light, a big crowd streaming in. |
| 08 | CORO_FERIA | Ahí están los que viven de que los conozcan / Y en tres días grabas con ellos, y te reconozcan | +350 empresas · +60.000 asistentes | High-angle wide over an enormous trade-fair pavilion: hundreds of colourful stands and a crowd of thousands; JULIÁN small in the aisle looki |
| 09 | MECANISMO | Me digo que la marca personal es pa' vender cursos (repite el dolor en imagen) | Doscientos ponentes con quienes grabar | At a fair corridor, JULIAN filming a short video on his phone beside two speakers with lanyards who lean in and laugh; other attendees gathe |
| 10 | PUENTE_CIFRAS | Más de trescientas cincuenta empresas, sesenta mil personas / Doscientas ponencias pa' aprender de las que ya funcionan | +200 ponencias educativas | Side view of JULIÁN seated in a packed auditorium, a speaker on a lit stage pointing at a floating abstract chart, audience taking notes. |
| 11 | CTA | Y ahora sí saben lo que sé, se acabó / Compra tu ingreso dando clic en el botón | Compra tu ingreso: clic en el botón | JULIÁN facing camera in the pavilion aisle pressing a large glowing rounded button shape floating in front, confident, bokeh stands behind. |
| 12 | LOOP | Y ahora sí saben lo que sé, se acabó | Ahora sí saben | The co-working desk again: the phone grid now with videos of JULIAN talking beside recognisable-lanyard figures, a floating opportunity-enve |

**Notas de producción.** Animado 2D salsa urbana. Bible flat 2D verbatim. Dolor «nadie sabe lo que sé» 3 veces. Nunca en tarima: graba en pasillos.

**Prompt para Claude Code (este video solo)**

```
produce scripts/guiones/effix_animado_2d_p28-marca-personal-musical_20260904_aprobado.json
(antes: renombrar effix_animado_2d_p28-marca-personal-musical_20260904_por-aprobar.json a _aprobado.json y poner estado: aprobado).
Estilo animado_2d: Animado 2D salsa urbana. Canción Salsa urbana / champeta a 98 BPM con la letra del JSON tal cual;
si no rima al oído o canta mal la marca, regenerar (0.15 USD). Parar después de canción y de héroe para revisión.
```
