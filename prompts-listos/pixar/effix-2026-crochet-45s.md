# Feria Effix 2026 — Ad Crochet · "LANA" · Reel 45s vertical

**Versión 2 del ad.** Personaje nuevo, estética amigurumi, keyframes encadenados.
**Modelo:** Seedance 1.5 Pro (`bytedance-seedance-pro-1.5`) vía Magnific
**Formato:** 9:16 · 1080p · 45s · 6 clips
**Estado:** concepto cerrado, esperando el branding de Effix para la paleta

---

## LA IDEA CENTRAL — el material es la metáfora

Esto es lo que le faltaba a la versión de cartón.

**LANA está tejida a crochet. Y el tejido se puede deshacer o se puede tejer.**

- **Al inicio** está deshilachada: un hilo suelto se le va soltando del puño, una
  manga a medio destejer, colores apagados. Se está deshaciendo, literalmente.
- **En la feria** los hilos sueltos empiezan a re-tejerse solos. Gana puntadas,
  gana color, se le cierra la manga.
- **Al final** está completa y firme, con detalles nuevos tejidos que antes no tenía.

El espectador entiende la transformación **sin que la voz se la explique**. Eso es
storytelling visual: el estado del personaje ES el mensaje.

Y encaja perfecto con el pedido de keyframes: cada clip **empieza y termina en un
estado de tejido definido**, así que el progreso es medible cuadro a cuadro.

---

## POR QUÉ KEYFRAMES ENCADENADOS

Seedance 1.5 Pro acepta `start` **y** `end` keyframe. La técnica:

```
KF1 ──clip 1──> KF2 ──clip 2──> KF3 ──clip 3──> KF4 ──clip 4──> KF5 ──clip 5──> KF6 ──clip 6──> KF7
```

**El end frame de cada clip es el start frame del siguiente.** Resultado:
- Cero saltos de continuidad entre clips
- El personaje no deriva: cada clip está anclado por ambos extremos
- El progreso del tejido queda controlado por diseño, no por suerte
- Los cortes se sienten como un solo plano continuo, no como 6 clips pegados

7 keyframes para 6 clips. Es el paso que más trabajo da y el que más se nota.

---

## PERSONAJE — "LANA"

Emprendedora amigurumi. Muñeca de crochet tejida a mano, tamaño de peluche pero
tratada con peso y físicas reales.

**Regla age-blind (obligatoria en Seedance):** nunca describir por edad. Se describe
por rol, ropa y acción. Nada de "joven", "chica", "señora".

### Identity Block — copiar VERBATIM en los 7 keyframes

```
LANA: a handmade crochet amigurumi woman, body built from visible tight single-crochet
stitches with the spiral rounds readable across every surface, soft yarn-fibre halo
catching the light along her silhouette, two small black safety-eye beads with a tiny
embroidered smile, dark brown yarn hair gathered in a bun held with a wooden crochet
hook pushed through it, wearing a knitted apron over a plain long-sleeve top, a small
stitched pocket on the apron front, felted rounded hands with no separate fingers.
```

### Estado del tejido por acto — el arco visual

| Acto | Estado de LANA |
|---|---|
| Inicio | Un hilo suelto colgando del puño derecho, la manga izquierda a medio destejer mostrando la espiral abierta, colores lavados y apagados, fibras despeinadas |
| Medio | Los hilos sueltos empiezan a moverse solos y a re-tejerse, la manga se cierra punto a punto, el color sube y se satura |
| Final | Tejido completo y firme, puntadas apretadas y parejas, colores plenos, un detalle nuevo tejido en el apron que antes no estaba |

⚠️ El estado del tejido va **en cada keyframe**, no en el prompt de video. El
keyframe define el estado; el prompt define solo el movimiento.

---

## ⏳ PALETA — PENDIENTE DEL BRANDING

Alexander va a pasar los colores oficiales de Effix. Hasta entonces **no invento
hex**: esta vez la paleta sale del manual de marca, no de mi criterio.

Cuando llegue, se define aquí:

```
Primario:    #______
Secundario:  #______
Acento:      #______
Neutro claro:#______
Neutro oscuro:#______
Tipografía:  ______
```

**Cómo se aplica al personaje:**
- El **hilo de LANA** en el estado inicial: versión desaturada del primario
- El **hilo re-tejido**: el primario a plena saturación
- El **apron**: secundario
- Los **stands y banners de la feria**: primario + acento
- El **detalle nuevo tejido** del final: el acento, para que remate en la marca

**Forbidden list (independiente del branding):**
> NO plástico ni superficies lisas — todo debe leerse como fibra.
> NO ojos humanos realistas — son cuentas de seguridad.
> NO dedos separados — manos afieltradas redondeadas.
> NO puntadas perfectas de máquina — es hecho a mano, con irregularidad honesta.
> NO texto renderizado dentro del video.

---

## STORYTELLING — 6 actos, 45s

Ahora sí llegamos a 45s: Seedance 1.5 Pro acepta 4–12s por clip.

| # | Acto | Dur | Qué pasa | Cámara |
|---|---|---|---|---|
| 1 | **El deshilache** | 8s | LANA en su taller, rodeada de pedidos. Un hilo se le suelta del puño y cae al piso. Mira el hilo caer. | `static` → `pushIn` lento |
| 2 | **La grieta de luz** | 7s | El celular se ilumina en la mesa. El hilo suelto, en el piso, se tensa y apunta hacia la luz. Ella lo sigue con la mirada. | `handheld` sutil |
| 3 | **El umbral** | 8s | Puertas de Plaza Mayor. LANA entra. El hilo suelto entra con ella y empieza a subir, enredándose de vuelta en su muñeca. | `leftWalking` + `craneUp` |
| 4 | **El re-tejido** | 7s | Close-up: la manga deshecha se cierra sola, punto a punto. El color sube por la fibra. Los ojos se le agrandan. | `static` + `focusChange` |
| 5 | **La escala** | 8s | Aéreo sobre la feria. Desde arriba se ve que los pasillos forman un patrón de tejido. LANA es un punto de color que avanza. | `craneUp` + `pullOut` |
| 6 | **Completa** | 7s | LANA camina hacia cámara, tejido firme, colores plenos. Se toca el apron: ahí hay un detalle nuevo tejido. Sonríe. | `pushIn` + `pedestalUp` |

**Total: 45s exactos.**

### Doble contraste verificado

| Clip | Tamaño | Carácter de cámara |
|---|---|---|
| 1 | Wide | Static → push lento |
| 2 | MCU | Handheld |
| 3 | Medium | Tracking lateral + crane |
| 4 | ECU | Static con focus pull |
| 5 | Extreme wide | Aerial |
| 6 | MCU | Push + pedestal |

Ningún corte repite tamaño ni carácter de cámara.

### El remate del acto 5

El detalle que amarra todo: **desde el aire, los pasillos de stands forman un patrón
de tejido**. La feria entera se revela como un tejido gigante — la misma textura del
personaje. Ahí el concepto cierra: ella no llegó a un evento, llegó al tejido que le
faltaba.

---

## LOS 7 KEYFRAMES

Se generan con Nano Banana Pro o Seedream, 9:16, encadenados.
**Cada uno lleva el Identity Block completo + el estado de tejido que corresponde.**

| KF | Momento | Estado tejido | Encuadre |
|---|---|---|---|
| 1 | Taller, hilo intacto en el puño | Deshilachado | Wide |
| 2 | Hilo ya caído en el piso | Deshilachado | Wide (mismo espacio, hilo caído) |
| 3 | Frente al celular iluminado | Deshilachado, hilo tenso | MCU |
| 4 | En el umbral de la feria | Hilo subiendo por la muñeca | Medium |
| 5 | Manga a medio cerrar, color subiendo | En re-tejido | ECU |
| 6 | Vista aérea, ella diminuta abajo | Casi completa | Extreme wide |
| 7 | Frente a cámara, tejido completo | Completa + detalle nuevo | MCU |

**Regla de encadenado:** KF2 es el end del clip 1 **y** el start del clip 2. Por eso
KF2 y KF3 tienen que ser coherentes entre sí en luz, posición y encuadre — si no, el
corte se nota.

---

## PROMPTS DE VIDEO — solo movimiento

Con start y end keyframe puestos, el prompt **no describe la escena** — la escena ya
está en los dos frames. El prompt describe **cómo se va de uno al otro**.

Este es el error más común: re-describir lo que ya está en los keyframes. No hacerlo.

Plantilla:

```
[Movimiento de cámara nombrado, de los 52 valores de cameraMotion].
[Qué se mueve y en qué dirección, un movimiento primario].
[Cómo evoluciona el tejido durante el clip].
[Ritmo: lento y sostenido / acelera al final / se detiene].
Audio: [textura, sin habla — no discernible speech].
```

Los 6 prompts se escriben cuando entre el branding, porque el color forma parte de la
evolución visible del tejido.

---

## COSTOS

| Concepto | Unitario | Total |
|---|---|---|
| 7 keyframes (Nano Banana Pro) | 100 cr | 700 |
| 6 clips Seedance 1.5 Pro 1080p | 660 cr | ~3.960 |
| Voz en off (7 segmentos) | ~15 cr | ~105 |
| Música | 740 cr | 740 |
| **Total estimado** | | **~5.500 cr** |

Magnific tiene ~33.700. Alcanza para esta versión y dos iteraciones más.

⚠️ Higgsfield está en 4 créditos — todo se produce en Magnific.

---

## QUÉ FALTA PARA ARRANCAR

1. **El branding de Effix** — colores, tipografía, logo. Es lo único que bloquea.
2. Confirmar el nombre "LANA" o cambiarlo.
3. Decidir si LANA reemplaza a EFFI o si conviven en algún momento.

---

# ✅ PRODUCIDO — 2026-08-28

## Entregable final

`outputs/claymation/EFFIX-LANA-v2-FINAL.mp4` — **37s · 1080×1920 · 38 MB · −14 LUFS**

| Archivo | Qué es |
|---|---|
| `EFFIX-LANA-v2-FINAL.mp4` | **El ad.** Ritmo real, voz latina, subs animados, cierre real |
| `EFFIX-LANA-45s-FINAL.mp4` | v1 — 45s, cámara lenta, voz con acento español. Descartada |
| `con-subs.mp4` | Video con subtítulos, sin audio |
| `base-37s.mp4` | Video acelerado + cierre, sin subs ni audio |
| `cierre-real.mp4` | Los 4.7s de material real de la feria |
| `c1..c6.mp4` | Los 6 clips originales de Seedance, sin acelerar |
| `subs.ass` | Los subtítulos animados, editables |
| `voz/norah/n1..n6.mp3` | Las 6 líneas de voz |
| `voz/musica.mp3` | La música |
| `voz/pruebas/` | Las 3 muestras de voz comparadas |

## Assets de marca guardados

- `referencias/esteticas/BRANDING-EFFIX.md` — paleta y tipografía reales del sitio
- `referencias/esteticas/fuentes/Montserrat.ttf` — la tipografía oficial
- `referencias/esteticas/feria-real/` — 13 fotos de la 5ª edición + 3 logos de patrocinadores
- `referencias/personajes/lana-sheet-v2.jpg` — hoja de personaje de LANA (la elegida)
- `referencias/personajes/kf/kf1..kf7.jpg` — los 7 keyframes encadenados

## Costo total de la producción

| Etapa | Créditos |
|---|---|
| 2 hojas de personaje | 150 |
| 7 keyframes + 4 regeneraciones | 825 |
| 6 clips Seedance 1.5 Pro | 9.900 |
| Voz v1 (descartada) | 92 |
| Música | 920 |
| Voz v2 Norah + 2 pruebas | 49 |
| **Total** | **~11.936** |

Magnific quedó en **21.599** de 45.000.

⚠️ **Los 6 clips fueron el 83% del gasto.** Con Kling 2.5 habrían costado ~2.750
en vez de 9.900. Ver la tabla comparativa en `MASTER_CONTEXT.md`.

## Aprendizajes de esta producción

1. **Color selectivo:** "warm colour" no funciona. Nombrar colores concretos
   (mostaza, terracota, teal) Y declarar el fondo como *"strict pure greyscale with
   zero colour information"*.
2. **Banners sin texto:** "no legible text" devuelve texto inventado igual. Funciona:
   *"plain solid black panels with bold white abstract geometric shapes only,
   absolutely no letters, no words, no writing anywhere"*.
3. **Keyframes encadenados sí funcionan:** verificado frame a frame, los pares
   fin/inicio son idénticos. Se lee como una sola toma.
4. **No pedir movimiento lento:** "slow", "slowest possible", "deliberate" producen
   cámara lenta real. Pedir "natural real-time pace, fluid continuous motion".
5. **`sidechaincompress` corta la salida** cuando termina la señal de sidechain.
   Arreglo: `apad=whole_dur=<total>` antes del `asplit`.
6. **ElevenLabs Music mete silencios reales.** Pedir explícitamente "no silence, no
   empty bars, every second has audible instrumentation, even dynamics".
7. **El catálogo de voces miente sobre el origen.** Probar siempre con una frase
   corta antes de comprometer un ad.
8. **Rutas con espacios rompen el filtro `subtitles` de ffmpeg.** Copiar la fuente
   al directorio de trabajo y usar `fontsdir=.`.
9. **`zoompan` multiplica frames** si `d` > 1 sobre un input en loop. Usar `d=1` y
   animar el zoom con la variable `on`.

## Pendiente

- Confirmar con Effix los **derechos de imagen** de las fotos de 2025 antes de
  pautar — hay personas identificables.
- Decidir si el amarillo de los subtítulos se mantiene o se pasa a blanco puro
  (la marca es B&N estricto; el amarillo es decisión de plataforma, no de marca).
- Si la aceleración 1.4x no convence: regenerar con Kling 2.5 (~2.750 créditos).
