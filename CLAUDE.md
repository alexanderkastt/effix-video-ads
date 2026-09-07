# CLAUDE.md — skills-video-ads (Video Factory de ads con IA)

Este archivo lo lee Claude al abrir el proyecto. Es la constitución: reglas que no se
negocian, el orden de trabajo y dónde vive cada cosa. El detalle técnico y el historial
están en `MASTER_CONTEXT.md` (reglas y costos) y `ESTADO.md` (bitácora de decisiones).
**Si este archivo y el código se contradicen, el código gana y este archivo se corrige.**

---

## 1. Qué es este proyecto

Fábrica semi-automática de ads de video en 9:16 (30–60s) para Reels/TikTok, producidos
con modelos de IA (Seedance 1.5 Pro vía fal.ai para video, MiniMax Music 3 para
la canción cantada, ElevenLabs para voz, stable-audio para música de librería,
ffmpeg para montaje). Cliente actual: **Feria Effix 2026** (Medellín, Plaza Mayor,
15–19 oct). El objetivo comercial de cada ad es **vender boletería**, no "dar a conocer
el evento". Marcas propias que también se producen aquí: @alexemprendee, @militougc,
@kreoon.latam.

Todo vive en `skills-video-ads/`. **No crear subproyectos ni repos aparte.**

---

## 2. Entorno (Windows 11) — leer antes de correr nada

| Cosa | Regla |
|---|---|
| Python | `python`, **nunca `python3`** (no existe en Windows). Versión 3.13.5. |
| Entorno | `venv\Scripts\activate` antes de cualquier script. Dependencias: `pip install -r requirements.txt`. |
| pip | Dentro del venv **no** va `--break-system-packages`. **Nunca** instalar el paquete `asyncio` de PyPI (rompe los imports; es stdlib). |
| venv | No se mueve de carpeta ni se versiona. Si el proyecto cambia de ruta, se recrea. |
| ffmpeg / ffprobe | Instalados (7.1 / 8.0.1). Todo montaje pasa por ffmpeg, no por librerías de video en Python. |
| Node | 22.17 disponible, uso marginal. |
| Consola | Los scripts llaman `usar_utf8()` de `src/consola.py` para que los acentos no rompan la salida. Mantenerlo en scripts nuevos. |
| Submódulos | `skills/higgsfield` y `skills/shortfilm` son repos ajenos. `git submodule update --init --recursive` si llegan vacíos. Nunca editarlos dentro. |
| Secretos | `.env` nunca se sube ni se pega en chat. `.env.example` es la plantilla y **debe mantenerse en sincronía** cuando se agrega una variable nueva. |

Comprobación de salud (sin gastar un peso):
```
python scripts/test_dry_run.py
python scripts/test_integracion_creativa.py
```
Los dos en verde antes y después de tocar `src/`.

---

## 3. Reglas de dinero — las más importantes

1. **Presupuesto: 5 USD promedio por ad, tope 6 USD**, todo incluido (video + imágenes +
   voz + música). Definido en `config/costos.json → presupuesto`. Si la estimación pasa
   el tope, **se avisa y se propone el recorte ANTES de gastar**, nunca después. Quien
   decide si un ad vale 6 USD es Alexander.
2. **Estimar antes de producir, con los parámetros reales** (duración final, resolución
   final, con keyframes, con `n_imagenes`). Un preflight a 6s sin keyframes subestimó el
   costo real en más del doble. Usar `src/cost_estimator.py` (`estimar()` / `formatear()`)
   o `simulate_cost` en Magnific.
3. **Nunca gastar sin aprobación humana.** `scripts/crear_video.py` genera guion,
   escenografía, brief de música y storyboard y **para**. La producción real solo arranca
   con `--producir` sobre un guion aprobado, o con los scripts `_producir_*.py` fase por
   fase (`hero · escenas · clips · montaje`), nunca `todo` sin que Alexander lo pida.
4. **Cada modelo cobra distinto y hay que saber cómo.** Seedance cobra por
   tokens — `(alto × ancho × fps × segundos) / 1024`, a 1.2 USD el millón: un
   clip de 4s a 1080p son 0.2333. MiniMax Music 3 cobra por segundo de canción
   (0.002). Kling cobraba tramos cerrados de 5 o 10s, y por eso se abandonó:
   un clip de 6s se facturaba como 10.
5. **Los planos extra no cuestan video.** Para dar ritmo se reencuadra el mismo clip
   (`src/ritmo.py`), no se generan clips nuevos.
6. **La música es de librería** (`assets/audio/soundtracks/<mood>.mp3`, indexada en
   `config/soundtracks.json`). Ya está pagada. Solo se genera una pista nueva si el guion
   pide un mood que no existe, y se guarda para la siguiente.
7. Créditos externos: Magnific tiene saldo; Higgsfield está en plan free (4 créditos) —
   `zack-d-films` corre pero no genera hasta recargar.
8. Registrar en `logs/` qué se generó y cuánto costó.

---

## 4. Orden de producción — no es negociable

```
micro-situación (7 pasos) → nivel de conciencia → gancho → guion (beats)
→ auditoría del guion → aprobación de Alexander
→ VOZ (ElevenLabs) → medir el mp3 con ffprobe → plan de clips desde el audio
→ imágenes/keyframes → clips de video → ritmo (planos) → mezcla → render → QA
```

**El audio manda.** Primero se genera la voz, se mide, y con la duración real se decide
cuántos clips hacen falta (`plan_clips.planificar_desde_audio()`). Al revés se generan
clips que no cuadran y se pagan dos veces. `planificar()` (estimado) sirve solo para
presupuestar.

Módulos por etapa: `microsituaciones.py` → `ganchos.py` → `script_engine.py` /
`narracion_hablada.py` → `voice_generator.py` → `plan_clips.py` → `video_generator.py`
→ `ritmo.py` → `mezcla.py` → `video_assembler.py` / `postproduccion.py`. Orquesta
`pipeline_orchestrator.py`.

---

## 4b. Producir desde un guion aprobado — el comando único

La parte creativa (micro-situación, gancho, guion, storyboard, auditoría) llega a
este repo como **un JSON aprobado** en `scripts/guiones/*_aprobado.json`, con el
esquema de `docs/FORMATO-GUION.md`. Se escribe en Cowork o a mano; **aquí no se
reescribe el contenido**, se produce.

Cuando Alexander diga `produce scripts/guiones/<archivo>_aprobado.json`:

1. Validar el JSON con las 6 reglas de `docs/FORMATO-GUION.md` (estado, registros,
   palabras prohibidas, prompts sin `slow`, overlays ≤ 7 palabras, duración 30–60).
   Si falla algo, decir qué y **parar**: no se arregla el guion aquí sin avisar.
2. Estimar costo con parámetros reales (tramos de 5/10s por línea, keyframes,
   `n_imagenes`) y mostrar el veredicto ✅/⚠️/🛑 de `cost_estimator.formatear()`.
3. **Esperar el OK explícito de Alexander.** Sin OK no se llama a ninguna API.
4. Voz por línea (`beat_NN.mp3`) → medir con ffprobe → repartir clips desde el audio.
5. Imágenes (`@Image1`, `@Image2` si hay `prompt_keyframe_final`) → clips → `ritmo.py`
   → `mezcla.py` → `assets/renders/<job_id>.mp4`.
6. QA: duración, −14 LUFS, número de planos, ningún plano < 1.25s. Anotar costo real
   en `logs/` y la entrega en `ESTADO.md`.

✅ **`scripts/producir.py` ya existe** (2026-09-06). Corre por fases, cada una con
su comando, y ninguna que cueste dinero arranca si las 6 reglas no pasan:

```
python scripts/producir.py <guion_aprobado.json> validar|costo|cancion|hero|escenas|clips|montaje|qa|todo
```

`todo` sólo si Alexander lo pide. El modo `musical_sync` está probado de punta a
punta con `effix_pixar_abogados-musical_20260904_aprobado.json`; **la fase de voz
del modo `locucion` falta por portar** desde `_producir_animado2d_la_acera.py`,
que hasta entonces no se borra.

Piezas de apoyo: `src/guion_aprobado.py` (las 6 reglas + estimación con
parámetros reales) y `src/transcripcion.py` (whisper por fal y alineación de la
letra con la canción, para que los tiempos del montaje musical no se escriban a
mano nunca más).

**Nichos nuevos (2026-09-04):** `networking` (27) y `referentes` (28), públicos
fríos, ya integrados en `src/nichos_effix.py` y `src/narracion_effix.py`. Sus
bancos de 10 ángulos cada uno están en `config/nichos/`. Los tests se corrieron
el 2026-09-06 y quedaron los dos en verde.

---

## 5. Reglas de guion

- **Sin micro-situación no hay guion.** Los 7 pasos (momento → síntoma → reacción →
  explicación fallida → patrón → causa raíz → mecanismo) van antes de la primera línea de
  copy. Fuente: `config/brand_dna.json`. Skill: `microsituaciones`.
- **No se elige el gancho; se elige el nivel de conciencia (Schwartz) y el objetivo
  (alcance o conversión), y eso decide el gancho.** Un creativo de conversión nunca lleva
  curiosidad. Banco: `config/banco_ganchos.json` (derivado del markdown de la skill
  `ganchos-y-retencion`; regenerar con `scripts/parsear_banco.py`, nunca editar el JSON a mano).
- `ganchos.auditar_guion()` corre seis reglas con evidencia: marca y mensaje en los
  primeros 5s; complicación ("pero") antes del segundo 12; defecto admitido al final y
  débil; describir la **situación, nunca a la persona** (política de Meta); cifras no
  redondeadas; 30–60s.
- **Solo cifras verificables.** Nada de métricas, testimonios o "+40%" inventados. Lo que
  no tiene fuente va declarado en `datos_sin_verificar`, no escondido. Cifras oficiales
  de Effix: +350 empresas, +200 conferencias, +200 ponentes, cinco ediciones.
- **Nunca prometer más días de los que da el pase.** El evento dura 5 días; el Pasaporte
  da 3 (16–18 oct, fin de semana, "sin pedir permiso"). Describir el evento es factual;
  prometerle al comprador esos días es un problema legal (Ley 1480 de 2011).
  `validar_coherencia_de_pase()` lo verifica.
- Sin descuentos ni códigos en los guiones actuales; sin mencionar el taller de IA
  (decisión de comunicación). El CTA cierra en compra: "Compra tu boleta/pasaporte…".
- Texto en pantalla: máximo 7 palabras. El video tiene que funcionar sin sonido.
- Español **neutro colombiano o paisa**, nunca voseo rioplatense. Kreoon MCP
  (`generate_script`) devuelve "sentís/convertite": revisar y adaptar siempre.
- Números escritos en letras para la locución.
- Longitud: la voz corre a **`PALABRAS_POR_SEGUNDO` del `.env`** (3.69 medido a speed
  1.15). Ese número **se mide, no se calcula**: remedir con `scripts/calibrar_voz.py`
  cada vez que cambie la voz o el speed. No dejar constantes duplicadas en el código.

---

## 5b. Modelos en producción (2026-09-07)

| Para | Modelo | Cuánto cuesta | Por qué ése |
|---|---|---|---|
| Video | `fal-ai/bytedance/seedance/v1.5/pro/image-to-video` | 0.2333 el clip de 4s a 1080p | Acepta frame final, duraciones de 4 a 12s y 1080p nativo en 9:16. Kling sólo vendía tramos de 5/10s y no aceptaba `end_image_url`. |
| Canción cantada | `minimax/music-3` | 0.002 el segundo | Canta la letra verbatim y acepta `duration`, que es lo único que permite encargar un ad de una duración concreta. |
| Imágenes | `fal-ai/nano-banana-2` y `/edit` | 0.08 c/u | La héroe se genera con el primero; las escenas se editan desde ella con el segundo. |
| Transcripción | `fal-ai/whisper` | centavos | Alinea la letra con la canción. **No sirve para juzgar pronunciación** sobre música: eso lo decide el oído de Alexander. |

Descartados con motivo: **ElevenLabs Music** (0.60/min) canta mejor pero
devuelve la voz **sin acompañamiento**; **Seedance 2.0/2.5** cuesta 1.21 por
clip porque incluye audio nativo que aquí no se usa; **Suno** no está en fal y
su clave está vacía — los campos `suno_*` del formato son herencia de cuando el
brief se pegaba a mano en la web.

## 6. Reglas de audio

Tres capas siempre: **textura** (SFX/ambiente dentro del prompt de video), **voz en off**
(ElevenLabs) y **música** (librería). El video generado nunca aporta voz.

- Todo prompt de video cierra el bloque de audio con `no discernible speech`.
- **La canción va ENTERA.** Ni se recorta la intro, ni se corta el final, ni se
  apaga mientras todavía se canta: si falta imagen, se estira el video. El fade
  de salida recibe `fin_voz_s` y no puede empezar antes de la última palabra —
  estaba clavado a 3s del final y en dos ads apagó el CTA. Y `duration` se le
  pide al modelo con margen, porque es un tope: con aire, la canción cierra
  sola en vez de cortarse.
- **Hay palabras que el modelo no sabe cantar** (`resultados`, `trafficker`,
  `ecommerce`, `dropshipping`): viven en `audio_extra.PALABRAS_QUE_NO_CANTA` y
  la regla 7 del productor las avisa gratis, antes de pagar. Cuando el modelo
  no sabe decir una palabra, se cambia la palabra. Cuando sí sabe pero une mal
  (la sinalefa de "Feria Effix"), se corrige la grafía: "Feria Éffix".
- Voz **siempre latina**. Los catálogos mienten sobre el origen: probar con una frase
  corta antes de comprometer un ad. Voz paisa de Alexander ("Cristian Sanchez") vive en su
  cuenta de ElevenLabs. `eleven_turbo_v2_5` cuesta la mitad que `eleven_v3`.
- Settings validados en `.env`: stability 0.45, similarity 0.83, style 0.12, speed 1.15,
  `RESPIRO_S=0.12`.
- **Una sola mezcla**: `src/mezcla.py` — ducking con `sidechaincompress`, fade derivado de
  la duración real, `loudnorm` a **−14 LUFS**. No reimplementar mezclas en scripts.
  `MUSICA_VOLUMEN=0.18`.
- `video_assembler.ensamblar()` pone música por defecto; `musica=False` solo para
  `musical_sync`, donde la canción es la pista principal.
- Lipsync solo en clips puntuales y **después** de generar el clip. Nunca pedir boca en
  el prompt y lipsync encima (boca doble). En personajes no humanos suele fallar: plan B,
  reacción con los ojos y la línea en off. Un solo rostro hablando por clip.

---

## 7. Reglas de ritmo y montaje

- **Corte visual cada 1.5–2.5s**, no cada 4s ni "cuando termine la frase". Piso duro
  1.25s por plano.
- Tres unidades distintas: **beat** (paso narrativo), **clip** (lo que se paga al
  modelo; conviene largo), **plano** (unidad de corte; conviene corto). Un clip largo se
  parte en planos por reencuadre en `src/ritmo.py`.
- Encuadres que alternan sin repetirse: `full`, `punch` (crop 0.80 al tercio superior),
  `lateral`, `contra`. Zoom máximo 1.25x.
- La frase **debe** cruzar el corte (`FACTOR_DESBORDE = 1.15` en `plan_clips.py`).
- **Prohibido "slow" / "deliberate" / "slowest push"** en prompts: sale cámara lenta real
  y arreglarlo en post cuesta calidad. El ritmo se construye en el montaje.
- Texto en pantalla siempre en post (Montserrat, `referencias/esteticas/fuentes/`), nunca
  pidiéndoselo al modelo.
- "Le falta dinámica" casi nunca es el guion: revisar primero planos por línea, speed de
  voz y música. Skill: `ritmo-y-montaje`.

---

## 8. Reglas de prompting de video

- Fórmula MCSLA: Model · Camera · Subject · Look · Action. 100–260 palabras.
- UGC: **nunca** `cinematic, professional, stunning, 8k, studio, perfect`; **sí**
  `handheld, authentic, natural light, candid, iPhone-shot`; 3–4 human motion cues;
  bloque de imperfección.
- **Cada estilo tiene su template** en `src/estilos_especiales.py` (`obtener(estilo)`).
  Nunca usar el template de `ugc_realista` para crochet, skeleton, object talk, etc.
  Skill: `director-estilos`.
- **Textos universales VERBATIM**: el positivo/negativo/cierre I2V de crochet y los
  Character Bibles de skeleton se copian palabra por palabra.
- Anti-fallo por estilo: crochet enmarca el MUNDO como diorama (nunca "personaje tejido")
  y evita poses de dedos; skeleton referencia siempre la imagen héroe, nunca el clip
  anterior; zack_films no lipsyncea y sus anotaciones son formas, no palabras;
  micro_doc_ugc actúa la micro-situación en vez de describirla.
- Color selectivo: nombrar colores concretos (mostaza, terracota, teal) **y** declarar el
  fondo `strict pure greyscale with zero colour information`. "Warm colour" no funciona.
- Sin texto en imagen: `plain solid black panels with bold white abstract geometric
  shapes only, absolutely no letters, no words, no writing anywhere`. "No legible text"
  produce texto inventado igual.
- Keyframes encadenados (end del clip N = start del N+1) dan continuidad total.
  Seedance 1.5 Pro los acepta con `end_image_url`, y `src/plan_musical.py` los
  reparte solo: el clip que CIERRA una línea encadena con la escena de la
  siguiente; los intermedios van sueltos, que es donde se quiere movimiento.
- Character sheet obligatoria antes de los clips.

---

## 9. Marca Effix — la fuente de verdad

- **Effix es blanco y negro estricto, sin color de acento.** Fuente:
  `referencias/esteticas/BRANDING-EFFIX.md` (extraído del DOM real). Tipografía
  Montserrat (300 cuerpo).
- 🔴 `config/brand.json` declara rojo/azul/dorado e Inter: **está mal y no se ha
  corregido**. Hasta que se corrija, ante conflicto manda `BRANDING-EFFIX.md`. No tratar
  `brand.json` como fuente de verdad visual.
- Subtítulos amarillos: decisión abierta (rendimiento en redes vs. marca B&N). No cambiar
  sin preguntar.
- Fotos de la 5ª edición (`referencias/esteticas/feria-real/`): hay personas
  identificables; derechos de uso en pauta pendientes de confirmar con Effix.

---

## 10. Skills del proyecto (`.claude/skills/`)

Convención: `.claude/skills/<nombre>/SKILL.md`. Los `.md` sueltos no se cargan.
**Descripciones largas siempre en bloque YAML `>-`**: un `": "` dentro de un escalar
plano rompe el frontmatter y la skill deja de dispararse (ya pasó dos veces).

| Skill | Cuándo |
|---|---|
| `microsituaciones` | Antes de cualquier guion. Obligatoria. |
| `ganchos-y-retencion` | Elegir/auditar ganchos; alcance vs conversión. Capa de método. |
| `ritmo-y-montaje` | Montar, decidir planos, voz lenta, "ponle música". Capa de método. |
| `director-estilos` | El usuario nombra un estilo visual → carga su template. |
| `storyboard-director` | Guion aprobado → ficha de rodaje por beat (HTML + JSON). |
| `crochet-ad-visuals` · `skeleton-ads` · `object-talk` · `zack-d-films` | Flujos conversacionales por formato. |

Las de método (`ganchos`, `ritmo`) se consultan antes que las de formato. El código
Python tiene las REGLAS (reproducible); las skills tienen los FLUJOS (ofrecen opciones
para que Alexander elija). Se complementan, no se reemplazan.

---

## 11. Estructura de archivos

| Ruta | Qué es |
|---|---|
| `MASTER_CONTEXT.md` | Reglas técnicas, tabla de costos por modelo, notas de aprendizaje. |
| `ESTADO.md` | Bitácora: decisiones, entregables, pendientes. Se actualiza al cerrar sesión. |
| `config/brand_dna.json` | ADN creativo Effix: avatar, dolores, ángulos, objetivo comercial, pases. |
| `config/costos.json` | Tarifas verificadas + presupuesto. |
| `config/soundtracks.json` · `banco_ganchos.json` · `parrilla*.json` | Librería musical, ganchos (derivado), parrilla de nichos. |
| `src/` | Pipeline. Ver §4. |
| `scripts/crear_video.py` | CLI del día a día. `scripts/_producir_*.py` son corridas concretas (se borran al terminar). |
| `prompts-listos/<estilo>/` | Packs de prompts que ya funcionaron + aprendizajes. |
| `outputs/` | Entregables por estilo; `GUIONES.md` (acumulativo), `GUIONES-EFFIX.md`, HTML de parrilla. |
| `assets/clips` · `audio` · `renders` | Intermedios, se regeneran. No se versionan (salvo `soundtracks/`). |
| `referencias/` | Branding real, fotos de la feria, character sheets, keyframes. |
| `skills/higgsfield` · `skills/shortfilm` | Submódulos ajenos, solo lectura. |
| `logs/` | Qué se generó y cuánto costó. |

---

## 12. Cómo trabajar en este repo

- **Lee `ESTADO.md` al empezar** para saber qué quedó pendiente; **actualízalo al
  terminar** con decisiones, entregables y aprendizajes fechados.
- Una regla que solo está escrita no existe: si es fija, el **default del código** tiene
  que serlo también (pasó con la música). Cuando cambies una regla, cambia código, skill
  y este archivo en el mismo commit.
- Toda constante que salga de una medición va al `.env` con el script que la remide al
  lado. Nada de números mágicos duplicados en `src/`.
- Antes de proponer un pipeline, calcula su costo. Antes de declarar algo terminado,
  míralo/óyelo (ffprobe de duración y loudness, revisar planos).
- Los ads ya entregados **no se re-producen** con reglas nuevas salvo que Alexander lo
  pida. Las reglas aplican de aquí en adelante.
- Scripts de corrida (`_producir_*.py`) son desechables; la lógica reutilizable va a `src/`.
- Cuando algo nuevo funcione (o falle), anótalo en **Notas de aprendizaje** de
  `MASTER_CONTEXT.md` y, si es un prompt, en `prompts-listos/`.
- Commits en español, en imperativo o pasado corto, como los existentes
  ("Ritmo rapido, voz mas agil y soundtrack en todos los ads").
- Comunicación con Alexander: directa, sin adornos, con números. Si algo no se sabe o no
  está verificado, decirlo plano.

---

## 13. Pendientes abiertos (ver `ESTADO.md` para el detalle)

1. Corregir `config/brand.json` a la paleta B&N real y Montserrat.
2. Confirmar con Effix derechos de imagen de las fotos 2025 para pauta.
3. Decidir color de subtítulos (amarillo vs blanco).
4. Voz paisa "Cristian Sanchez" solo accesible desde la cuenta de Alexander.
5. Conceptos A y C de `effix-2026-guiones-alternativos.md` sin producir (retargeting).
6. Correr los dos tests tras integrar los nichos 27 y 28; construir `scripts/producir.py`.
7. Guiones de `GUIONES-EFFIX.md` generados a 75s: fuera del rango 30–60s; la
   validación lo marca. Regenerar con `PALABRAS_POR_SEGUNDO` actual.
