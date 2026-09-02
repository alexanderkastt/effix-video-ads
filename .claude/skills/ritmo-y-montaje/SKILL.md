---
name: ritmo-y-montaje
description: >-
  Reglas transversales de ritmo, corte y sonido para TODOS los ads de video, sin importar el
  estilo. Define cada cuántos segundos cae el corte visual, cómo se sacan planos extra de un
  clip ya pagado sin generar video nuevo, cuánto aire va entre réplicas, a qué velocidad
  locuta la voz y cómo se mezcla la música de fondo con ducking y loudness de plataforma.
  Usa esta skill SIEMPRE que haya que montar un ad, decidir cuántos planos tiene una línea,
  ajustar la velocidad de la locución, poner música, o cuando alguien diga "le falta
  dinámica", "la voz suena lenta", "está muy plano", "se siente largo" o "ponle música". Es
  la capa de método: las skills de formato (crochet-ad-visuals, skeleton-ads, object-talk,
  zack-d-films, storyboard-director) la consultan antes de montar.
---

# Ritmo y montaje — el método

Las skills de formato deciden **qué se ve**. Esta decide **cada cuánto cambia** y
**cómo suena**. Son decisiones independientes: un estilo puede pedir cámara
quieta dentro del plano y aun así cortar rápido entre planos.

Implementación ejecutable: `src/ritmo.py` y `src/mezcla.py`. Ningún montaje
reimplementa esto.

---

## REGLA CERO — el corte no espera a la frase

**El corte visual cae cada 1.5–2.5 segundos.**

El error que esto corrige: durante meses un plano era una línea de guión. Una
línea de seis segundos era un plano de seis segundos, y el ad se leía como lento
aunque el guión estuviera bien. El problema nunca fue la redacción; era que la
unidad de corte estaba atada a la unidad de habla.

Se separan:

- **Beat / línea** — la unidad del guión. Lo que se dice.
- **Plano** — la unidad de corte. Dura 1.5–2.5s y no le pide permiso a la frase.

Una línea de 5s no es un plano largo: son dos o tres planos con encuadres
distintos, y la voz corre por debajo cruzando los cortes.

---

## De dónde salen los planos extra (sin gastar un centavo)

**El segundo plano sale del MISMO clip generado, reencuadrado.** `trim` del tramo
que toca y un `crop` distinto. Es el punch-in clásico de edición: la misma toma
vista más cerca se lee como otra cámara.

Generar dos clips por línea larga duplicaría el gasto de video y rompería el tope
de 5–6 USD por ad. Esto no cuesta nada.

| Duración de la línea | Planos |
|---|---|
| hasta 2.5s | 1 |
| 2.5 – 5.0s | 2 |
| 5.0 – 7.5s | 3 |
| más | 4+ |

Se redondea **hacia arriba**: 3.6s son dos planos de 1.8s, nunca un plano de 3.6s.

**Piso duro de 1.25s.** Debajo de eso el ojo no alcanza a leer el encuadre y el
corte se siente como un error, no como intención. Si partir dejaría planos por
debajo del piso, se parte en menos: es preferible un plano de 2.8s a dos de 1.4s
cortados a mitad de palabra.

### Los cuatro encuadres

Alternan por posición y nunca se repiten seguidos — dos planos consecutivos con
el mismo encuadre se ven como un salto de montaje, no como un corte.

| Encuadre | Zoom | Qué hace |
|---|---|---|
| `full` | 1.00 | El cuadro completo |
| `punch` | 1.25 | Cerrado, subido al tercio superior donde vive la cara |
| `lateral` | 1.14 | Medio, desplazado a un lado |
| `contra` | 1.14 | Medio, desplazado al otro |

El ciclo se arrastra entre líneas: si una línea termina en `punch`, la siguiente
arranca en `lateral`, para que el corte también se note al pasar de una a otra.

**Zoom máximo 1.25x.** Recortar al 80% de 1080x1920 y volver a escalar todavía
aguanta; más que eso se empieza a ver el pixel.

### El caso del lip-sync

Reencuadrar un clip con lip-sync es válido: es la misma toma vista más cerca, la
boca sigue sincronizada. Y como el lip-sync devuelve el clip cortado a la voz
(`sync_mode=cut_off`), el último plano de la línea pide más de lo que dura el
clip — `tpad` clona el último frame. En una conversación real el aire entre
réplicas es justamente la cara sosteniendo el gesto.

---

## La voz

**`ELEVENLABS_SPEED=1.15`.** A 1.0 la locución se oía lenta contra el corte.
Aguanta porque `stability` está en 0.45; el atropello de la frase venía de tenerla
en 0.28.

**El aire entre réplicas son 0.12s** (`RESPIRO_S`). Cada centésima de más es un
hueco que en el video se oye como duda. Eran 0.25, 0.35 y 0.12 hardcodeados en
tres scripts distintos: el mismo guión respiraba distinto según por dónde se
montara.

**3.69 palabras por segundo.** Medido, no calculado — no escala lineal con el
`speed`. Se remide con `python scripts/calibrar_voz.py` cada vez que cambia la voz
o la velocidad, y el resultado va a `PALABRAS_POR_SEGUNDO` en el `.env`. Un ad de
45s de locución son ~166 palabras.

**La frase cruza el corte, y debe.** `FACTOR_DESBORDE = 1.15`. Ahora que la imagen
corta cada 1.5–2.5s, el desborde es más necesario, no menos: una locución que
respeta el corte al milímetro suena a lista de viñetas leída en voz alta.

---

## La música

**No es opcional.** Todo ad lleva fondo. `video_assembler.ensamblar()` toma por
defecto la pista del estilo y solo se apaga con `musica=False`, que es para el
modo `musical_sync` — ahí la canción ya es la pista principal.

**Sale de la librería, no se compone por ad.** `assets/audio/soundtracks/`, seis
moods indexados en `config/soundtracks.json`. Se generaron una vez por 1.20 USD.
Componer una pista nueva por video sería 0.20 recurrentes por un fondo que nadie
va a distinguir del anterior. Solo se genera nueva cuando el ad pide un mood que
no está en el catálogo, y esa pista se guarda para que la próxima tampoco cueste.

| mood | BPM | para |
|---|---|---|
| `energetico` | 95 | ugc_realista, testimonial |
| `emotivo` | 72 | el cierre que aterriza, la historia personal |
| `aspiracional` | 85 | cinematic, zack_films |
| `alegre` | 110 | todo lo animado: pixar, claymation, 2D, object-talk, crochet |
| `tenso` | 100 | skeleton, suspenso, cyberpunk |
| `epico` | 130 | anime, avengers |

**La mezcla la hace `src/mezcla.py`, y solo ella.** Tres cosas que no son
negociables:

1. **Ducking real** con `sidechaincompress`. La música se hunde sola cuando
   alguien habla y vuelve a subir en los silencios. Bajarla a un volumen fijo
   obliga a elegir entre que se oiga y que no tape la voz.
2. **Fade-out derivado de la duración real**, nunca un segundo escrito a mano.
3. **`loudnorm` a −14 LUFS** en el master. Es lo que piden Instagram, TikTok y
   YouTube; sin esto cada ad sale a un volumen distinto y el de la competencia
   suena más fuerte en el mismo feed.

Volumen base `MUSICA_VOLUMEN=0.18`.

---

## Lo que NO se hace

- **No pedir "slow", "deliberate" ni "slow motion"** en los prompts de video: sale
  cámara lenta real. El ritmo se construye en el montaje, no pidiéndoselo al
  modelo.
- **No usar `xfade` ni disolvencias** entre planos. El corte es seco. Una
  disolvencia en un ad de 30s se come medio segundo y baja la energía.
- **No confundir cámara quieta con montaje lento.** Un estilo puede exigir plano
  fijo —`object-talk` lo hace, y con razón— y aun así cortar cada dos segundos.
  Son dos decisiones distintas.
- **No generar clips extra para tener más cortes.** Si hace falta más ritmo, sale
  del reencuadre. El presupuesto es 5–6 USD por ad.

---

## Diagnóstico rápido

| Síntoma | Causa probable | Dónde mirar |
|---|---|---|
| "Le falta dinámica" | Planos largos: el montaje no partió las líneas | `ritmo.resumen()` en la consola del montaje |
| "La voz suena lenta" | `ELEVENLABS_SPEED` bajo, o respiro largo | `.env`: `ELEVENLABS_SPEED`, `RESPIRO_S` |
| "Se oye a pedazos" | Falta `previous_text`/`next_text` en el TTS | `src/voice_generator.py` |
| "La música tapa la voz" | Mezcla sin sidechain | Que el montaje use `src/mezcla.py` |
| "Suena más bajo que otros ads" | Sin `loudnorm` en el master | `src/mezcla.py`, verificar con `medir_loudness()` |
| "Se ve pixelado en los cierres" | Zoom por encima de 1.25x | `ZOOM_MAX` en `src/ritmo.py` |
| El corte cae a mitad de palabra | Planos por debajo del piso | `PLANO_PISO_S` en `src/ritmo.py` |
