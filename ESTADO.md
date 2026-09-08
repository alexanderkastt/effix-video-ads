# Estado del proyecto — 2026-08-29

Sesión de setup + producción de dos ads para **Feria Effix 2026**.

---

## 🎬 ENTREGABLES

| Archivo | Estilo | Dur | Estado |
|---|---|---|---|
| `outputs/claymation/EFFIX-LANA-v2-FINAL.mp4` | Crochet amigurumi | 37s | ⭐ **El bueno** |
| `outputs/claymation/EFFIX-LANA-45s-FINAL.mp4` | Crochet | 45s | v1 descartada (cámara lenta, voz española) |
| `outputs/pixar-disney/EFFIX-2026-pixar-36s-FINAL.mp4` | Pixar 3D | 36s | Primera versión, nicho distinto |

**El ad final:** LANA, emprendedora amigurumi a medio tejer, camina desde un cuarto
cerrado hasta la feria. Se completa y gana color mientras el mundo permanece en blanco
y negro de marca. Cierra con material real de la 5ª edición.

**Nicho:** el emprendedor que NO ha logrado arrancar a vender por internet.

---

## 📁 DÓNDE ESTÁ CADA COSA

| Ruta | Contenido |
|---|---|
| `MASTER_CONTEXT.md` | Reglas de audio, guiones, y **la tabla de costos por modelo** |
| `.env` | Claves de API + parametros de produccion (44s / 11 clips de 4s) |
| `requirements.txt` | Dependencias Python congeladas |
| `src/` | Codigo del pipeline de ensamblaje (vacio, pendiente de escribir) |
| `config/` | Perfiles por estilo visual y presets ffmpeg (vacio) |
| `assets/clips` · `assets/audio` · `assets/renders` | Material intermedio del pipeline |
| `outputs/GUIONES.md` | Todos los guiones producidos, acumulativo |
| `prompts-listos/pixar/effix-2026-crochet-45s.md` | Pack del ad de LANA + aprendizajes |
| `prompts-listos/pixar/effix-2026-guiones-alternativos.md` | 3 conceptos: pasillo, dos octubres, seis "no sé" |
| `prompts-listos/pixar/effix-2026-ia-45s.md` | Pack del ad Pixar (EFFI, caja de cartón) |
| `referencias/esteticas/BRANDING-EFFIX.md` | Paleta y tipografía reales del sitio |
| `referencias/esteticas/fuentes/Montserrat.ttf` | Tipografía oficial de la marca |
| `referencias/esteticas/feria-real/` | 13 fotos de la 5ª edición + 3 logos |
| `referencias/personajes/kf/` | Los 7 keyframes encadenados |
| `skills/higgsfield/` | 33 sub-skills de prompting |
| `skills/shortfilm/` | 28 plantillas de género |

---

## 💰 CRÉDITOS

| Plataforma | Disponible | Nota |
|---|---|---|
| **Magnific** | **21.599** de 45.000 | Todo se produce aquí |
| Higgsfield | 4 | Agotado, plan cayó a free |

**Modelo más económico medido: Kling 2.5** — 650 créditos por 10s a 1080p con
keyframes start+end. Seedance 1.5 Pro cuesta 1.760 por 8s. Ver `MASTER_CONTEXT.md`.

---

## ⏭️ PENDIENTE

1. **Derechos de imagen** — confirmar con Effix que se pueden usar en pauta las fotos
   de 2025 (hay personas identificables).
2. **Color de subtítulos** — el amarillo no es de marca (Effix es B&N estricto).
   Decidir si se mantiene por rendimiento en redes o se pasa a blanco.
3. **Si la aceleración 1.4x no convence** — regenerar con Kling 2.5 (~2.750 créditos
   en vez de los 9.900 que costó Seedance).
4. **Voz Cristian Sanchez** — la voz paisa de Alexander vive en su cuenta de
   ElevenLabs y no es accesible desde acá. Los 6 mp3 sueltos están listos para
   reemplazar uno a uno si la quiere usar.
5. Los conceptos A y C de `effix-2026-guiones-alternativos.md` quedan sin producir —
   sirven para retargeting y cierre de campaña.

---

## 🏭 SETUP DE LA VIDEO FACTORY — 2026-08-29

Montado el entorno automatizable sobre el proyecto que ya existia (no se creo
proyecto aparte: todo vive en `skills-video-ads/`).

**Verificado en este equipo (Windows 11):**

| Binario | Version |
|---|---|
| python | 3.13.5 (⚠️ `python3` NO existe en Windows, usar `python`) |
| node | 22.17.0 |
| ffmpeg | 7.1 |
| ffprobe | 8.0.1 |

**Instalado** en `venv/`: fal-client, elevenlabs, librosa, soundfile, httpx,
aiofiles, pillow, requests, python-dotenv. Congelado en `requirements.txt`.

**Estilos de salida ampliados** de 4 a 7: a `ugc`, `pixar-disney`, `claymation`
y `cinematic` se sumaron `cyberpunk`, `anime` y `musical` (en `outputs/` y en
`prompts-listos/`).

**Configuracion cargada (PASO 4-6):** `.env` definitivo + `config/brand.json`.
Verificado que `python-dotenv` los lee y que 11 x 4s = 44s. Pendientes de llenar:
`FAL_API_KEY`, `ELEVENLABS_API_KEY`, `SUNO_API_KEY`, `ELEVENLABS_VOICE_ID`.

🔴 **CONFLICTO DE PALETA — decidir antes de producir con `brand.json`:**
`config/brand.json` declara rojo `#E31B23`, azul `#1A1A2E` y dorado `#FFD700`.
`referencias/esteticas/BRANDING-EFFIX.md` — extraido del DOM real de feriaeffix.com —
dice que **la marca es blanco y negro estricto, sin color de acento**, y ese mismo
archivo advierte de una extraccion previa que invento colores. Los prompts 2-4 tratan
a `brand.json` como "fuente de verdad visual", asi que si no se corrige, los ads
saldran con una paleta que la marca no tiene. Ademas `brand.json` pide fuente `Inter`
para cuerpo, pero la unica fuente descargada es `Montserrat.ttf` (y el sitio usa
Montserrat 300 para cuerpo, no Inter).

✅ **Conflicto de formato RESUELTO (2026-09-02).** Era: el brief pedia 11 clips
de 4s (44s) y `MASTER_CONTEXT.md` empujaba a clips de 10s, mas baratos pero con
menos cortes. Se resolvio separando las dos cosas que estaban peleando:

- **Clip** = lo que se le paga al modelo. Conviene largo, porque sale mas barato.
- **Plano** = la unidad de corte. Conviene corto, porque es lo que da ritmo.

No hay que elegir: un clip largo se parte en varios planos por reencuadre, en
`src/ritmo.py`, sin pagar video extra. Se gana el precio del clip de 10s y el
ritmo del corte de 2s a la vez.

---

## 🧠 CAPA CREATIVA — 2026-08-29

Construida la capa que genera guiones, escenografía, música y storyboard.
No hace ni una llamada a API de pago.

| Archivo | Qué hace |
|---|---|
| `config/brand_dna.json` | ADN creativo: avatar, dolores, objeciones, angulos, palabras prohibidas |
| `config/costos.json` | Tarifas para estimar antes de producir (⚠️ en cero, sin verificar) |
| `src/paths.py` | Rutas y carga de .env / JSON de marca |
| `src/script_engine.py` | Guion de 11 beats, 3 hooks por angulo, validador de calidad |
| `src/scene_builder.py` | 9 estilos visuales -> prompt de video de 120-200 palabras |
| `src/music_engine.py` | Brief Suno (fondo y sincronizado) + deteccion de beats con librosa |
| `src/storyboard_builder.py` | Storyboard HTML autonomo + JSON para el pipeline |
| `src/cost_estimator.py` | Estimacion de costo; avisa cuando las tarifas no estan verificadas |
| `scripts/crear_video.py` | CLI del dia a dia |
| `scripts/test_dry_run.py` | Prueba de extremo a extremo sin gastar |

**Comando del dia a dia:**

```
venv\Scripts\activate
python scripts/crear_video.py --concepto "..." --estilo ugc_realista --marca effix --angulo comunidad_que_no_tienes
```

**Probado:** 216 combinaciones (8 angulos x 3 hooks x 9 estilos) sin un solo fallo
de validacion. Dry run: 8/8 checks en verde.

**Motor determinista, no LLM.** Los guiones se componen desde plantillas escritas a
mano + los datos de `brand_dna.json`. No hay ninguna API de LLM configurada en el
`.env`, y el dry run tiene que correr sin gastar. Si se quiere variacion generativa,
el enganche natural es Kreoon MCP (`generate_script`), como ya dice MASTER_CONTEXT.

**Datos que NO se inventaron:** el guion solo usa cifras verificables del brand_dna
(cinco paises, 15-19 de octubre, Plaza Mayor, rango de facturacion del avatar,
codigo EFFIX20). No hay metricas de asistencia ni testimonios fabricados: si hacen
falta para el beat 06, hay que traer datos reales de Effix.

---

## 🎭 CAPA CREATIVA AVANZADA — 2026-08-29

Micro-situaciones + cinco estilos con pipeline propio, construidos desde los
skills originales (`crochet.md`, `skeleton.md`, `Zack-d-films`, `object-talk`,
`guía-microsituaciones.pdf`).

| Archivo | Qué hace |
|---|---|
| `src/microsituaciones.py` | Framework de 7 pasos + 8 micro-situaciones de Effix + plan de duracion + auditoria de cifras |
| `src/estilos_especiales.py` | crochet · skeleton · zack_films · micro_doc_ugc · object_talk |
| `src/storyboard_director.py` | Ficha de rodaje por beat: prompt imagen, prompt I2V, tipo A/B/C, notas, modelos |
| `.claude/skills/` | 7 skills: los 4 originales + 3 propios (ver abajo) |
| `scripts/test_integracion_creativa.py` | 11 checks, sin gastar un peso |

**Textos universales VERBATIM.** El positivo/negativo/cierre I2V de crochet y los
Character Bibles de skeleton se copian palabra por palabra. Cambiar una sola
convierte un clip bueno en uno inservible.

**Reglas anti-fallo respetadas:** crochet enmarca el MUNDO como diorama (nunca
"personaje tejido") y evita poses de dedos; skeleton referencia siempre la imagen
heroe, nunca la anterior; zack_films no lipsyncea y sus anotaciones son formas, no
palabras; micro_doc_ugc actua la micro-situacion en vez de describirla.

### Skills instaladas en el proyecto

Convencion: `.claude/skills/<nombre>/SKILL.md` — los `.md` sueltos NO se cargan.

| Skill | Origen | Que aporta |
|---|---|---|
| `crochet-ad-visuals` | archivo original | Flujo de 3 pasos: pregunta de personaje, 5 ideas visuales por frase, storyboard |
| `skeleton-ads` | archivo original | 4 etapas con hand-offs: guion, concept board, prompts de imagen, prompts de video |
| `zack-d-films` | archivo original | 8 fases con gates, pipeline Higgsfield MCP |
| `object-talk` | archivo original | Diseno de personaje antropomorfo + prompts (incluye `references/examples.md`) |
| `microsituaciones` | propio | Obliga a construir los 7 pasos antes de escribir copy |
| `director-estilos` | propio | Enruta al template correcto segun el estilo |
| `storyboard-director` | propio | Ficha de rodaje por clip |

**Los dos enfoques se complementan.** El codigo Python (`estilos_especiales.py`)
tiene las REGLAS y genera 11 clips validados de forma reproducible. Los skills
originales tienen los FLUJOS conversacionales: crochet ofrece cinco ideas
visuales por frase para que Alexander elija, cosa que el codigo no hace.

⚠️ `zack-d-films` depende de Higgsfield MCP y su plan cayo a free con 4 creditos.
El skill corre, pero la generacion real esta bloqueada hasta recargar.

✅ **FORMATO CERRADO — corte cada 1.5-2.5s, video de 30 a 60s.**
*(2026-09-02: era "corte cada 4s". Ver "Ritmo, dinamica y soundtrack" al final.)*

Se separaron tres unidades que estaban confundidas:

- **Beat narrativo** — uno de los once pasos de la micro-situacion.
- **Clip** — lo que se le paga al modelo de video. Su duracion la decide el
  audio real, no una ventana fija.
- **Plano** — 1.5 a 2.5 segundos. Es la unidad de corte, y no le pide permiso
  ni al beat ni al clip.

Un beat que habla mas de 2.5s no se vuelve un plano largo: se vuelve DOS o TRES
planos con encuadre alterno. Y esos planos salen del MISMO clip, reencuadrados
— no se generan clips nuevos para tener mas cortes, porque eso multiplica el
costo. Lo hace `src/ritmo.py`.

La micro-situacion completa (76-88s) se quedo como INVESTIGACION dentro del
beat, en el campo `investigacion`. Lo que se locuta es la version hablada de
`src/narracion_hablada.py`, escrita al presupuesto real.

**El techo son 8 palabras por linea.** A 2.2 palabras/segundo, 8 palabras son
3.64s y caben en el clip. A 9 ya piden 4.09s y se llevan un clip entero de mas:
el video salta de 44s a 48s por una sola palabra. `validar_presupuesto()` lo
verifica en las 88 lineas.

*(2026-09-02: ese techo quedo holgado. La voz real corre a 3.69 palabras/segundo
—medido con `scripts/calibrar_voz.py`—, no a 2.2, y el plano ya no es una ventana
fija que una palabra de mas desborde. El presupuesto sale ahora de
`PALABRAS_POR_SEGUNDO` en el `.env`.)*

Resultado medido en los 8 angulos: **11 clips x 4s = 44s**, locucion 35-39s,
holgura 5-9s de respiracion entre frases. Los 8 dentro del rango 30-60s.

| Modulo | Que hace |
|---|---|
| `src/narracion_hablada.py` | Las 88 lineas habladas, con validador de presupuesto |
| `src/plan_clips.py` | Reparte beats en clips de 4s y valida el rango 30-60s |

⚠️ **CIFRAS SIN VERIFICAR** — la guia lo llama Error 3: "la especificidad solo
funciona cuando la situacion es real". Cinco cifras heredadas del brief siguen sin
fuente y estan declaradas en `datos_sin_verificar`, no escondidas:

- "las 500 personas que mueven el ecommerce LATAM" (comunidad)
- "facturando 3 veces lo tuyo" (comunidad, ilustrativo)
- "400 personas de tu competencia ya compraron" (competencia)
- "18 meses" y "el tercero este año" (cursos, ilustrativos)

Ya se quitaron dos afirmaciones factuales sin fuente: "+40% de conversiones" del
arco skeleton y "los top sellers gastan menos en ads" del angulo de Zack.

---

## 🪝 GANCHOS Y ORDEN DE PRODUCCION — 2026-08-29

### El metodo de ganchos entro al codigo

`.claude/skills/ganchos-y-retencion/` (skill + banco de 320) · `src/ganchos.py`
(selección y validadores) · `config/banco_ganchos.json` (derivado) ·
`scripts/parsear_banco.py` (regenera el JSON cuando se edita el markdown).

El banco vive en el proyecto: 320 ganchos, 108 de @alexemprendee, 108 de
@militougc y 104 plantillas genéricas. Para Effix aplican los de Alexander y
los genéricos — el avatar del evento es el mismo. `candidatos(nivel, objetivo)`
cruza el banco con el método y devuelve solo lo que sirve: 37 para
(problem, conversión), 25 para (unaware, alcance), cero para (most_aware, alcance)
porque esa combinación no existe en el marco.

**Regla cero:** no se elige el gancho, se elige el nivel de conciencia y el nivel
decide el gancho (Schwartz 1966). Segunda pregunta obligatoria: alcanzar o cerrar.
Un creativo de conversion **nunca** lleva curiosidad.

`auditar_guion()` corre seis reglas con evidencia sobre cualquier guion:

| Regla | Evidencia |
|---|---|
| Marca y mensaje en los primeros 5s | 1,7x mas intencion de compra (Meta + Toluna) |
| Complicacion (un "pero") antes del segundo 12 | trama imaginable, ρ = .29 |
| Defecto admitido al final y debil | blemishing, Ein-Gar 2012 |
| Describir la situacion, nunca a la persona | politica de Meta |
| Cifras no redondeadas | la precision implausible es el mecanismo |
| Video entre 30 y 60s | pico de alcance en Reels |

**Tres cosas que la auditoria encontro en nuestro propio guion:**

1. 🔴 **`no_esta_en_cursos` beat 03 decia "empiezas a pensar que eres tu"** — afirma
   una caracteristica personal del espectador. Meta rechaza eso. Reescrito.
2. **La marca entraba en el segundo 36.** Ahora el logo es identidad visual desde el
   clip 01 (`marca_en_pantalla`), sin gastar palabras de locucion.
3. **Faltaba el defecto admitido.** Se agrego el beat 11 (DEFECTO) entre el CTA y el
   loop, con su linea en los 8 angulos. Ej: *"No es barato. Y no es para principiantes."*
   El guion pasa de 11 a 12 beats — 12 clips x 4s = 48s, dentro del rango.

Cuatro angulos tampoco tenian complicacion antes del segundo 12: se les puso el
"pero" explicito.

### El audio manda: nuevo orden de produccion

Antes se estimaba la locucion a 2.2 palabras/segundo y se generaban los clips sobre
esa estimacion. **Con `ELEVENLABS_SPEED=0.83` el desvio medido es de +7 segundos** —
suficiente para que los clips no cuadren y haya que regenerarlos pagando de nuevo.

Orden correcto, en `src/plan_clips.py`:

1. `planificar()` — estima a 2.2 pal/s. Sirve para **presupuestar antes de gastar**.
2. Se genera la voz en ElevenLabs.
3. `planificar_desde_audio()` — mide el mp3 con **ffprobe** y recalcula.
4. Recien ahi se generan los videos.

**Linea de tiempo continua, no `ceil` por beat.** Redondear cada beat por separado
pagaba video que nadie ve: un beat de 4,3s se llevaba dos clips enteros (8s) para
cubrir 4,3s de voz. Sobre la linea continua ese sobrante lo aprovecha el beat
siguiente.

Medido en el angulo comunidad: **17 clips (68s) con el metodo viejo contra 12 clips
(48s) con el nuevo**, para el mismo audio de 47,7s. Veinte segundos de video que ya
no se pagan, y el corte final queda a 0,3s de la ultima silaba.

---

## 🎟️ EL OBJETIVO ES VENDER BOLETERIA — 2026-08-29

Todo lo que produce este proyecto existe para **vender boleteria de Feria Effix**.
Cada guion cierra en la compra de un pase, no en "conocer el evento".

**Dos productos, datos confirmados por Effix:**

| | Pasaporte 3 dias (principal) | Entrada VIP |
|---|---|---|
| Fechas | viernes 16, sabado 17, domingo 18 oct | jueves 15 al lunes 19 oct |
| Precio | **$201.300** COP · IVA incl. | **$1.155.000** COP · IVA incl. |
| Con EFFIX20 | $161.040 | $924.000 |
| Acceso | 3 dias generales | 5 dias completos |
| Extras | +350 empresas · +200 conferencias · +200 ponentes · networking | escarapela VIP · entrada/salida ilimitada · sin filas · inauguracion privada 15 · clausura 19 · zona VIP con hidratacion · areas reservadas · zonas de creacion de contenido |

Ratio VIP/basico: **5,7x**. Estrategia acordada: **todos los creativos al pase de 3**;
el VIP es upsell para quien ya compro o retargeting, nunca pauta fria.

### ⏰ La urgencia real: el taller de IA es el 3 de SEPTIEMBRE

El taller de inteligencia artificial en vivo (4 horas) esta incluido en **ambos**
pases y ocurre el **3 de septiembre**, no en octubre. Quien compre despues pierde un
beneficio que ya venia pagado.

Es escasez con fecha verificable, no fabricada — y es la mas fuerte del embudo:
**faltan cinco dias**, contra los 47 que faltan para el evento.

Por eso existe el CTA `pase_3_dias_taller`: *"Compra antes del tres y entras al
taller."* Despues del 3 de septiembre hay que volver a `pase_3_dias`.

⚠️ Confirmar con Effix: ¿el taller se graba y queda disponible, o se pierde? La
respuesta cambia si la urgencia es "lo perdes" o "lo ves en vivo".

### Las fechas son fin de semana — y eso es argumento de venta

El pase principal cae **viernes a domingo**. El avatar que todavia tiene empleo no
necesita pedir permiso. Es respuesta directa a una de las objeciones del brand_dna
("no se si vale la pena ir presencialmente"), y por eso el CTA quedo en
*"Viernes a domingo. Ni pedis permiso."*

### Cifras oficiales que reemplazaron estimaciones

`+350 empresas y marcas`, `+200 conferencias, paneles y talleres`, `+200 ponentes`
son datos de Effix. Reemplazaron a *"las 500 personas que mueven el ecommerce
LATAM"*, que arrastrabamos sin verificar desde el brief. Un dato sin fuente menos.

Todo registrado en `config/brand_dna.json` → `objetivo_comercial`.

### 🔴 El hallazgo: 17 lineas prometian cinco dias

El **evento** dura cinco dias (15 al 19 de octubre). El **pase principal** da acceso
a **tres**. Diecisiete lineas de los ocho angulos prometian "cinco dias" al
espectador — quien comprara el pase de 3 iba a recibir menos de lo que el anuncio
prometio.

No es un detalle de copy: es un problema comercial, de confianza y **legal** (Ley
1480 de 2011, la publicidad obliga al anunciante).

**Diez lineas corregidas.** La distincion que ahora respeta el sistema:

- ✅ Describir el evento: *"Cinco paises en el mismo salon"*, *"del quince al
  diecinueve de octubre"* — es factual.
- ❌ Prometerle al comprador esos dias: *"Cinco dias con quienes ya lo resolvieron"*
  — el pase de 3 no lo entrega.

### El CTA cambia por producto

El beat 10 es el unico que depende del pase. Todo lo demas describe el evento y
sirve para los dos.

| Pase | CTA hablado | Overlay |
|---|---|---|
| `pase_3_dias` | "Pase de tres dias. Codigo EFFIX veinte." | Pase 3 días · EFFIX20 |
| `vip_5_dias` | "Pase VIP, los cinco dias. Codigo EFFIX veinte." | VIP 5 días · EFFIX20 |
| `generico` | "Quince al diecinueve de octubre. Codigo EFFIX veinte." | 15–19 oct · EFFIX20 |

`beat_a_beats_con_microsituacion(pase=...)` lo selecciona.
`validar_coherencia_de_pase()` impide que vuelva a colarse una promesa de mas dias
de los que da el producto. Corre en el test sobre las 16 combinaciones
(8 angulos x 2 pases), todas en 48s.

---

## ⚠️ REGLAS APRENDIDAS (ya aplicadas en MASTER_CONTEXT)

- La voz **siempre latina**. El catálogo de Magnific miente sobre el origen: probar
  con una frase corta antes de comprometer un ad.
- `eleven_turbo_v2_5` cuesta la mitad que `eleven_v3`.
- Nunca pedir "slow" / "deliberate" en prompts de video: sale cámara lenta real.
- Preflight de costo con los **parámetros finales** (duración, resolución, keyframes).
  Un preflight a 6s sin keyframes subestimó el costo real en más del doble.

---

## Ritmo, dinamica y soundtrack (2026-09-02)

Alexander vio los ads de `tienda_ropa` y dijo tres cosas: la voz suena lenta, al
video le falta dinamica, y hay que ponerle soundtrack a todos. Las tres eran el
mismo problema de fondo — el montaje seguia el ritmo del habla en vez de imponer
el suyo — y ninguna era del guion.

**Lo que cambio:**

| Antes | Ahora |
|---|---|
| 1 plano = 1 linea (hasta 7s de la misma camara) | Corte cada 1.5–2.5s, planos del mismo clip reencuadrados |
| `ELEVENLABS_SPEED=1.0` | `1.15` |
| Respiro de 0.25 / 0.35 / 0.12 segun el script | `RESPIRO_S=0.12` para todos |
| `PALABRAS_POR_SEGUNDO` = 2.96 / 2.75 / 2.2 segun el archivo | 3.69, medido, en el `.env` |
| Musica opcional, en 2 de 5 pipelines | Obligatoria, de libreria, en todos |
| 3 mezclas distintas, volumen 0.13 / 0.25 | Una sola, con ducking real y −14 LUFS |

**Modulos nuevos:** `src/ritmo.py` (reparto de planos y encuadres) y
`src/mezcla.py` (ducking con sidechain, fade derivado, loudnorm).
**Scripts nuevos:** `scripts/generar_soundtracks.py` (libreria, 1.20 USD una vez)
y `scripts/calibrar_voz.py` (remide las palabras/segundo).
**Skill nueva:** `.claude/skills/ritmo-y-montaje/SKILL.md`, transversal, citada
desde las cinco skills de formato.

**Medido en los dos ads existentes, re-montando sin generar video nuevo:**

| Ad | Planos antes | Planos ahora | Duracion | Loudness |
|---|---|---|---|---|
| `tienda-ropa-2d-la-acera` | 12 | 19 (0.86–2.40s) | 35.96s → 34.4s | −15.5 LUFS |
| `tienda-ropa-skeleton-vitrina` | 9 | 23 (1.48–2.39s) | 47.44s → 45.5s | −14.3 LUFS |

Costo extra por ad: **cero**. Los planos salen del clip ya pagado y la musica de
la libreria.

⚠️ **Los ads ya entregados NO se re-produjeron** — por decision de Alexander esto
aplica de aqui en adelante. Los numeros de arriba salen de renders de prueba que
se borraron.

⚠️ **Efecto secundario en los guiones:** a 3.69 palabras/segundo el mismo guion
dura menos. Un guion de 110 palabras pasa de ~37s a ~30s. Los guiones nuevos
pueden llevar mas texto, o el ad queda mas corto que antes.

---

## 🧭 NICHOS 27 Y 28 + FORMATO ÚNICO DE GUION — 2026-09-04

Sesión en Cowork (sin gastar). Se definió cómo se separa lo creativo de la
producción y se abrieron dos nichos de público frío.

**Formato único de guion aprobado** — `docs/FORMATO-GUION.md`. El repo tenía dos
formatos (`beats` del motor y `lineas` de los `_producir_*.py`); los cuatro ads
reales salieron del segundo, así que ese se formalizó. La frontera es
`scripts/guiones/*_aprobado.json` (ahora SÍ versionado, ver `.gitignore`). En
Claude Code se produce con una frase: `produce <archivo>`. Protocolo en
`CLAUDE.md` §4b.

**Nichos nuevos** en `src/nichos_effix.py` y `src/narracion_effix.py`:

| Nicho | Ancla | Gatillo | Ángulo principal | Guion listo |
|---|---|---|---|---|
| `networking` (27) | la agenda de WhatsApp | dejar_de_ganar | 27.2 proveedores | `effix_microdoc_networking-la-agenda_20260904_aprobado.json` · micro_doc_ugc · 180 palabras ≈ 50s |
| `referentes` (28) | la tarima vs. la silla | ego | 28.10 convertirse en referente | `effix_cinematic_referentes-la-tarima_20260904_aprobado.json` · cinematic · 175 palabras ≈ 49s |

Bancos de 10 ángulos cada uno en `config/nichos/27-networking-angulos.json` y
`28-referentes-angulos.json`; versión legible en `outputs/MICROSITUACIONES-27-28.md`.

**Decisiones de copy:** en `referentes` nunca se muestra al personaje EN tarima ni
se promete cupo de ponente (el pase es de asistente); las "zonas de creación de
contenido" son del VIP y no se prometen en creativos del pase de 3. Ambos guiones
cierran con el CTA `pase_3_dias` de `CTA_POR_PASE`, sin descuento ni taller.

**⚠️ Pendiente inmediato en Claude Code:**
1. Correr `test_dry_run.py` y `test_integracion_creativa.py` — la integración se
   hizo fuera del venv (solo se validó sintaxis y estructura de claves). La
   parrilla pasa de 11 a 13 nichos, así que `generar_guiones_md.py` va a
   reportar "se esperan 10" — es el validador viejo, no un error nuevo.
2. Construir `scripts/producir.py` genérico desde
   `_producir_animado2d_la_acera.py` y probarlo con el guion de networking.
3. Los archivos del repo en disco están en CRLF; los nuevos de esta sesión en LF.
   Git en Windows lo normaliza al commit; si `git status` muestra medio `src/`
   modificado, es eso y no cambios reales (`git diff --stat --ignore-cr-at-eol`).

---

## 🎵 14 GUIONES MUSICALES (guion 1 por nicho) — 2026-09-04

Un guion por nicho en modo **musical sync** (canción MiniMax, sin locución),
rotando tres formatos: **Pixar** (abogados, contadores, ia, logistica, referentes),
**Skeleton** (agencias_contenido, dropshipping, importadores, networking) y
**Crochet** (agencias_pauta, ecommerce, laboratorios, sin_arrancar, tienda_ropa).

- Documento para aprobar: `outputs/GUIONES-MUSICALES-20260904.md` (letra, 12 escenas,
  personaje, notas y el comando de producción de cada uno).
- JSON listos: `scripts/guiones/effix_<estilo>_<nicho>-musical_20260904_por-aprobar.json`
  (14). Se producen renombrando a `_aprobado.json` con `estado: aprobado` y diciendo
  `produce <archivo>` en Claude Code.
- Costo estimado por ad: **4,55 USD** (canción 0,15 + héroe 0,08 + 12 imágenes + 12
  clips de 5s en Kling v2.1 std). Cada reintento de canción suma 0,15.
- Continuidad de personajes: EFFI+BIT (ia), LANA (sin_arrancar), ROSA en amigurumi
  (tienda_ropa). Personajes nuevos: CÓDIGO, CALCU, RUTA, TRIPI, TEO, SARA, DON RUBÉN.
- Estructura fija: 12 escenas = MOMENTO · CALLOUT · SÍNTOMA · EXPL. FALLIDA · PATRÓN ·
  CAUSA RAÍZ · CORO (llegada) · CORO (350 empresas) · MECANISMO · PRUEBA · CTA · LOOP.
  Sin beat DEFECTO (decisión heredada del skeleton musical de sin_arrancar).
- Validado: sin palabras prohibidas, sin descuento/taller, sin `slow` en video,
  `no discernible speech` en todos, verbatim de crochet/skeleton en todos los prompts,
  overlays ≤ 7 palabras, coro con la marca escrita completa.

⚠️ El builder que generó los 14 JSON fue un script de un solo uso fuera del repo. Si
hay que cambiar una letra o un plano, se edita el JSON directamente (o se pide en
Cowork, que tiene el contexto).

### v2 de los musicales — ajustes de Alexander (2026-09-04, misma sesión)

- **Coro:** «Más de trescientas cincuenta empresas / Más de sesenta mil asistentes».
  La cifra de asistentes la dio Alexander; se registró en `brand_dna.json`
  (`asistentes_estimados`) con nota de "sin fuente verificada" y en
  `datos_sin_verificar` de los 14 JSON. **Confirmar con Effix antes de pautar.**
- **CTA:** «Compra tu ingreso dando clic en el botón», sin URL, porque el mismo ad
  va a landing y a WhatsApp. Nueva clave `pase_3_dias_boton` en `CTA_POR_PASE`
  (`src/narracion_effix.py`) para que el motor narrado también la tenga.
- **#01 abogados reescrito** con estructura dolor (1–5) → giro (6) → solución en
  Effix (7–12): la MISMA tienda-cliente (TIENDA, carrito antropomórfico) pregunta en
  la oficina y Código no sabe; en la feria vuelve a preguntar y Código responde.
  Es el primero que se produce; los otros 13 se afinan con lo que se aprenda.

### v3 de los musicales (2026-09-04, misma sesión)

- Fechas en el coro: **del quince al diecinueve de octubre** (las del evento; es
  factual y la letra no menciona el pase, así no promete duración).
- Línea fija en los 14: «Más de doscientas ponencias para aprender de los que ya
  tienen resultados» (pedido de Alexander: que se sepa que hay formación).
- **Callout de oficio directo:** «Eres abogado», «Eres contador». Decisión:
  nombrar la profesión está permitido por Meta; la regla de "describir la
  situación, no a la persona" aplica a atributos sensibles (salud, dinero,
  estado emocional), no al oficio. Se había sobre-aplicado y quitaba claridad.
- #01 abogados reescrito en lenguaje llano ("Tus próximos clientes están en
  Feria Effix"): Alexander no entendía la versión anterior. Regla que queda:
  **si el guion necesita explicación, no está listo.** Cada letra debe poder
  resumirse en una frase y cada escena debe leerse sola.

### Tanda 2 — #02 agencias_contenido, #03 agencias_pauta, #04 contadores (2026-09-04)

Reescritos con el criterio del #01 (historia en una frase, problema 1-5 → giro 6 →
solución 7-12, callout de oficio directo, lenguaje llano, hilo visual recurrente):
- `agencias_contenido` (skeleton): "Tus próximos clientes no llegan por referido".
- `agencias_pauta` (crochet, TEO): "Sabes pautar, pero nadie lo sabe"; los tres
  "de traje" son el hilo (4, 5, 9, 12).
- `contadores` (pixar, CALCU + TIENDA): "Los clientes de ecommerce necesitan
  contador"; misma estructura que abogados a propósito (mismo avatar de oficio).
Pendientes de reescribir con este criterio: los 10 restantes (llevan coro, fechas,
ponencias y CTA nuevos, pero la letra todavía es la v1).


---

## Ad musical de abogados y el productor generico (2026-09-06)

Primer ad producido con **`scripts/producir.py`**, el productor generico que
`docs/FORMATO-GUION.md` pedia desde el 04-sep. Los `_producir_*.py` desechables
ya no hacen falta para el modo `musical_sync`.

**Entregable:** `assets/renders/abogados-musical-pixar.mp4` — 77.91s, 38 planos,
-14.4 LUFS. Nicho abogados, estilo Pixar, dos personajes: CODIGO (un libro de
leyes con gafas) y TIENDA (un carrito con globo de papel).

### Lo que se construyo

| Pieza | Que hace |
|---|---|
| `scripts/producir.py` | Lee el formato unico y corre por fases: `validar · costo · cancion · hero · escenas · clips · montaje · qa · todo` |
| `src/guion_aprobado.py` | Las 6 reglas del formato, con dos varas segun el modo (locucion mide palabras, musical mide video generado) |
| `src/transcripcion.py` | Whisper por fal + alineacion de la letra con `difflib`. Los tiempos del montaje musical ya no se escriben a mano |
| `ritmo.planos_en_fuente()` | Llena un tramo de 8s con planos de un clip de 5s, sin congelar frame ni camara lenta |
| `ritmo.imantar()` | Lleva los cortes al golpe de la cancion, con guardas de tolerancia y piso |
| `mezcla.cadena_master()` | Master a -14 LUFS sin ducking, para cuando la cancion ES la pista |
| `postproduccion.ajustar()` | Overlays en dos renglones: 9 de 12 no cabian y se dibujaban al piso de 40px |
| `producir.py` → `ventana_util_s` | Usa solo la parte buena de un clip que se estropea a mitad. Gratis |

### Costo: estimado 4.65, real 6.89 USD

| Concepto | USD |
|---|---|
| Cancion (MiniMax) + whisper | 0.246 |
| Heroe | 0.08 |
| Escenas (26 llamadas, 12 utiles) | 2.08 |
| Clips (15 llamadas, 12 utiles) | 4.20 |
| **Total** | **6.886** |

Detalle en `logs/abogados-musical-pixar_costo.json` y `_gasto.jsonl`.
**Se paso el tope de 6 con aprobacion explicita de Alexander**, dos veces.

### Los tres errores que costaron los 2.24 de desvio

1. **La heroe salio duplicada en dos filas** (pedi "character sheet" y
   nano-banana devolvio una hoja de contactos). Como cada escena se edita DESDE
   la heroe, las 12 heredaron el diptico: 0.96 USD tirados. Corregido en el
   codigo con `UN_SOLO_CUADRO` en el prompt y `SISTEMA_UN_CUADRO` en el
   `system_prompt`. **No le vuelve a pasar a los otros 13 guiones musicales.**
2. **Escenas 8 y 9 con aire de plaza de mercado.** `hundreds of colourful stands`
   y `at a stand` se leen como puesto de mercado; el ad vende una feria de
   ecommerce. Reescritas a `modern convention hall, corporate exhibition booths,
   backlit display walls, carpeted aisles, lanyards` + veto de mercado: 0.36 USD.
3. **Kling metia humanos en los clips 4 y 12.** La causa no era el modelo sino el
   prompt: pedia acciones que los personajes no pueden hacer — `CODIGO types and
   hits a key` y `TIENDA lifts the three papers`. Un libro no teclea y un carrito
   no tiene manos, asi que el modelo dibuja a alguien que si. Reescritos a
   acciones ejecutables + veto explicito de humanos: 0.56 USD.

### Aprendizajes

- **Nunca pedirle a un personaje-objeto una accion que necesita manos humanas.**
  Es el error que mas caro sale en estilos con objetos animados: el modelo no
  falla, resuelve la accion imposible metiendo una persona. Vale para
  `object_talk`, `crochet` y `skeleton` igual que para este.
- **"Character sheet" es una palabra peligrosa** con nano-banana: devuelve grilla.
  Pedir "single row", "single full-frame image" y repetirlo en el `system_prompt`.
- La heroe es el punto de control mas barato del pipeline: **mirarla antes de
  generar las escenas** cuesta cero y se habria ahorrado 0.96 USD.
- MiniMax no acepta duracion objetivo: **la letra decide cuanto dura**. 120
  palabras cantadas dieron 75.41s. Para caber en 60 hay que escribir ~90.
- Whisper transcribe "Feria Effix" como "Feria Fix" y "resultados" como
  "bra rosados": **la transcripcion sirve para alinear, no para juzgar la
  pronunciacion.** Eso se hace con el oido.

### Pendiente de este ad

- **Duracion 77.91s, fuera del rango 30-60** del formato. Alexander lo acepto
  sabiendolo. Los otros 13 guiones musicales tienen el mismo problema de origen:
  la letra es demasiado larga.
- **"Mas de sesenta mil asistentes"** sigue en `datos_sin_verificar`: cifra de
  Alexander, no esta en el sitio de Effix. Se canta y va en overlay. Confirmar
  con Effix antes de pautar.
- Carteles de fondo con garabatos tipo letras en los clips 3 y 5, en desenfoque.
  No se corrigio: 0.56 USD por un defecto que a tamano de movil no se lee.

### Overlays reescritos (2026-09-06, tarde)

Alexander pidio tres cosas sobre los overlays y las tres estaban en
`src/postproduccion.py`:

1. **Centrados siempre.** `drawtext` con texto de varias lineas centra el BLOQUE
   y deja cada linea alineada a la izquierda dentro de el: el segundo renglon
   empezaba donde empezaba el primero. Ahora se dibuja **un drawtext por
   renglon**, cada uno con su `x=(w-text_w)/2`. Las dos lineas comparten
   animacion, asi que el overlay se sigue leyendo como una pieza.
2. **Animados, no estaticos.** Entrada con ease-out cubico desde 34px abajo,
   flotacion continua de 3px con periodo de 2.4s mientras esta en pantalla, y
   salida que baja y se desvanece. El alpha tambien lleva easing (`pow(p,0.6)`):
   un fade lineal se ve como cross-dissolve de editor, no como sticker.
   Entrada y salida se acortan solas si el overlay dura poco.
3. **Menos espacio entre renglones.** `INTERLINEA = 1.0` del cuerpo. En caja
   alta no hay descendentes que llenar, asi que el interlineado propio de
   `drawtext` dejaba las dos lineas flotando separadas.

De paso: un separador (`·`, `|`, `–`) que caia en la frontera del corte quedaba
colgando al final del primer renglon (`+350 EMPRESAS ·`). Ahora se descarta — el
salto de linea ya separa. Vive en `_SEPARADORES`.

⚠️ Los ads entregados antes de hoy **no se re-montaron**: la regla del repo es
que las mejoras aplican de aqui en adelante.

---

## Tanda 2 · Ad #1: agencias de contenido, estilo skeleton (2026-09-06)

**Entregable:** `assets/renders/agencias-contenido-musical-skeleton.mp4` — 54.08s,
25 planos, -14.1 LUFS, -1.9 dBTP. **El primer ad del proyecto que pasa las cinco
comprobaciones del QA**, duracion incluida.

Costo real **6.352** contra 4.646 estimado. El desvio (+1.71) es casi todo el
precio de encontrar el modelo de cancion correcto, y no se repite: los ads que
siguen arrancan con esa decision tomada.

### La cancion: seis intentos, tres modelos

| # | Modelo | Resultado |
|---|---|---|
| 1-2 | MiniMax 2.6 | marca deformada ("Veria fix", "Feia FX") |
| 3 | MiniMax 2.6 | marca OK con la tilde, pero "resultados" -> "resurodios" |
| 4 | MiniMax 2.6 | **pista degenerada**: "eh eh eh" 58s, sin letra |
| 5 | ElevenLabs Music | diccion excelente pero **sin acompanamiento**: es voz cantada, no musica. Lo detecto Alexander de oido |
| 6 | **MiniMax Music 3** | ✅ letra verbatim, con arreglos, 54s, 0.116 USD |

**MiniMax Music 3 es el modelo de aqui en adelante.** Es la version nueva de la
2.6 con la que empezo el proyecto y trae las dos cosas que faltaban: campo
`duration` —encargar los segundos que caben en el formato en vez de aceptar lo
que salga— y `guidance_scale`. Cuesta 0.002 por segundo: 0.116 el ad, contra
0.15 de la 2.6 y 0.58 de ElevenLabs.

Suno no esta disponible y no lo va a estar: `SUNO_API_KEY` vacia, y **fal no lo
tiene en catalogo**. Los campos `suno_*` del formato son herencia de cuando el
brief se pegaba a mano en suno.com.

### Tres arreglos que valen para los diez guiones restantes

1. **`guidance_scale` 2.2 -> 1.8.** Lo habia subido para apretar la diccion y fue
   lo que degenero una cancion en "de-de-de-de" durante 58s. Guidance alto atasca
   al modelo en una silaba: es el modo de fallo clasico de la difusion sobreguiada.
2. **Palabras que el modelo no sabe cantar**, en
   `audio_extra.PALABRAS_QUE_NO_CANTA` y validadas por la regla 7 del productor:
   `resultados` (salio "resurodios", "bra rosados", "jesuitos" — cinco fallos en
   cuatro pistas), `trafficker` ("trafico, me encas"), `ecommerce` ("Kecoxie",
   "Conte Day"), `dropshipping`. **Aparecen en 13 de los 14 guiones musicales.**
   La comprobacion es gratis y corre antes de pagar la cancion. La salida no es
   pelear con la grafia sino cambiar la palabra: son letras publicitarias.
3. **Limitador con margen de codec** en `mezcla.py`. El QA marcaba clipping y
   hubo dos pistas falsas antes de aislarlo:
   - `alimiter` recibe amplitud **lineal** (0.0625 a 1), no dB. Escribirle
     "-1.5dB" no da error: ffmpeg lo descarta en silencio y no limita nada.
   - Corregido eso, el WAV salia a -1.4997 pero el **AAC a 192k subia a -0.38**:
     1.1 dB de overshoot intersample que el codec inventa al reconstruir. Ahora
     se limita `MARGEN_CODEC` (1.5 dB) por debajo, para que cumpla el archivo
     entregado y no solo la senal antes de codificar.

### Lo que si funciono a la primera

- La **tilde de "Feria Éffix"** rompe la sinalefa que fundia la "a" de Feria con
  la "E" de Effix. Alexander confirmo de oido que asi suena bien. La grafia solo
  se aplica a lo que se canta; el JSON conserva "Feria Effix", que es lo que se
  lee y con lo que whisper alinea.
- La **heroe de un personaje solo** (fondo neutro, veto explicito de gente y
  escenario). El primer intento salio con seis humanos alrededor del esqueleto
  porque el prompt generico decia "all the characters side by side".
- Las 12 escenas y los 12 clips salieron **sin un solo fallo**: el esqueleto se
  mantiene identico en los doce y ninguno invento un humano, que fue el problema
  del ad de abogados.

⚠️ **Whisper no es juez de pronunciacion sobre musica.** Transcribio mal frases
que estaban bien cantadas ("proxy play antes" por "el proximo cliente") y bien
frases que estaban mal. Sirve para alinear tiempos, no para decidir si algo suena
bien: eso lo decide el oido de Alexander.

---

## 🗺️ MAPA COMPLETO DE 28 PÚBLICOS + 28 GUIONES PARA EQUIPO AV — 2026-09-04

Alexander entregó el mapa completo: **28 públicos** (16 calientes, 10 tibios, 2 fríos)
con **282 ángulos**. Está en `config/nichos/mapa-28-publicos.json` y es la fuente de
verdad de nichos. Los 14 de `src/nichos_effix.py` son un subconjunto (varios mapean a
públicos del mapa: tienda_ropa→18, abogados/contadores→24, networking→27, referentes→28).

**Entregable:** el ángulo .2 de cada público como guion narrado para producción humana:
- `outputs/GUIONES-EQUIPO-AV-28-publicos.md` (repo) y `.docx` (para el equipo).
- `config/nichos/guiones-av-28.json` (estructurado, por si se quiere producir con IA
  o alimentar el motor).

**Formato:** 12 beats fijos — PROBLEMA (1-5: momento, callout, síntoma, explicación
fallida, patrón) → GIRO (6: causa raíz) → SOLUCIÓN (7-10: fechas 15-19 oct, +350
empresas / +60.000 asistentes, mecanismo del nicho, +200 ponencias) → CTA (11: botón)
→ CIERRE (12). Locución corrida + guion técnico con overlay ≤ 7 palabras y plano por
beat. 153-193 palabras, 43-54 s a 3,69 pal/s. Validado sin palabras prohibidas, sin
descuento/taller, sin cifras en dígitos, callout de oficio directo.

**Decisiones:** los públicos B2B (11-16, 22, 23) no son asistentes que buscan
aprender sino empresas que buscan clientes: su "solución" es exponerse/venderle a los
60.000 asistentes, y el guion lo dice así. 18.2, 24.2, 27.2 y 28.2 reutilizan las
micro-situaciones ya construidas (tienda_ropa, contadores, networking, referentes).

**Pendiente:** los otros 254 ángulos (.1, .3-.10) se escriben con el mismo molde
cuando Alexander apruebe este primer lote. Los 14 musicales de IA siguen su curso
aparte (ver arriba).


---

## 🎬 28 GUIONES PIXAR DEL ÁNGULO .2 — SIETE ESTRUCTURAS — 2026-09-07

Sesión en Cowork, sin gastar. Alexander pidió los guiones del **ángulo .2** de los 28
públicos para que el equipo audiovisual los produzca **en Pixar con IA**, con
**estructuras distintas para que no se sienta el mismo patrón** (crítica al lote .2
anterior, que tenía los 28 con los mismos doce beats).

**Entregable:** `outputs/GUIONES-PIXAR-28-angulo2.md` y `.docx` (para el equipo).

**Decisiones de Alexander en esta sesión:**
- **Locución narrada**, no musical: el carril cantado ya lo ocupa el ángulo .1, y el
  narrado explica el mecanismo con más claridad y sin reintentos de canción.
- **Los personajes los define el equipo.** El documento da el *rol* del objeto en la
  historia y lo que tiene que poder hacer en cámara; el diseño, el nombre y la
  personalidad son del equipo. No se nombró ningún personaje.
- Detalle de producción: guion + dirección por escena, sin prompts listos para pegar.

**Las siete estructuras** (cuatro guiones cada una, agrupadas así en el documento):

| Estructura | Guiones | Dónde cae la campaña |
|---|---|---|
| E1 Monólogo del objeto | 01, 08, 15, 24 | El objeto anuncia su propia fecha de salida |
| E2 Dos objetos conversan | 02, 09, 16, 22 | El que ya cambió cuenta dónde lo aprendió |
| E3 La escalada | 03, 10, 19, 25 | La feria rompe la serie que escalaba |
| E4 Mundo espejo | 04, 11, 18, 26 | El mundo B es el de quien ya fue |
| E5 Preguntas al espectador | 05, 12, 20, 27 | La última pregunta la contesta la feria |
| E6 Reloj | 07, 13, 21, 23 | La última marca de tiempo es el 15 de octubre |
| E7 El viaje | 06, 14, 17, 28 | El destino ES la feria |

**Métrica:** 132–167 palabras por guion, 36–45 s de locución a 3,69 pal/s (con aire y
cierre, 40–50 s por video). Validado con script: 28/28 sin palabras prohibidas, sin
dígitos en locución, sin descuento/taller/URL, todos con fechas, lugar y CTA
`«compra tu ingreso dando clic en el botón»`. Cabeceras e índice con las palabras y
segundos reales, no estimados.

**Reglas Pixar que quedaron escritas en el documento** (todas salen de plata perdida en
`abogados-musical-pixar` y `agencias-contenido-musical-skeleton`): nunca pedirle a un
objeto una acción que necesita manos humanas; hoja de personaje en un solo cuadro
(`single full-frame image`, repetido en el system prompt); el recinto es
`modern convention hall`, nunca `hundreds of colourful stands`; prohibido `slow`; nada
de texto dentro de la imagen.

**Marca:** el mundo del problema puede tener color; **el recinto va en blanco, negro y
gris**, y ese corte de color a B&N es el argumento visual de los 28. Fuente
`BRANDING-EFFIX.md`, no `brand.json`.

**⚠️ Pendiente antes de pautar:** confirmar con Effix «más de sesenta mil asistentes».
Está en la locución de varios guiones (10, 11, 12, 23), así que si no se confirma hay
que **regrabar voz**, no solo cambiar overlays. Es más barato preguntar ahora.

**Pendientes de este lote:**
1. Los personajes, cuando el equipo los defina, valen un documento aparte: si un objeto
   se repite entre nichos, la hoja de personaje se reutiliza.
2. Pasar los 28 al formato JSON de `docs/FORMATO-GUION.md` si se quieren producir con
   `scripts/producir.py` en vez de a mano. El contenido ya está; es trabajo de estructura.
3. Los ángulos .4 a .10 (224 guiones) salen con el mismo molde cuando se apruebe este lote.

---

## Tanda 2 y el primer ad con Seedance (2026-09-07)

Cuatro ads entregados, todos con el logo de Feria Effix y la canción sin cortar.

| Ad | Estilo | Duración | Costo | Video |
|---|---|---|---|---|
| agencias-contenido | skeleton | 54.08s | 6.35 | Kling |
| agencias-pauta | crochet | 68.08s | 6.89 | Kling |
| contadores | pixar | 68.08s | 5.33 | Kling |
| **p01 "Quiero vender y no sé por dónde"** | pixar (NUBE) | 68.08s | **5.47** | **Seedance** |

QA en verde en los cuatro salvo la duración, que es consecuencia directa de no
cortar la canción — decisión de Alexander, no un descuido.

### Lo que cambió en el pipeline

- **Seedance 1.5 Pro** sustituye a Kling 2.1 standard. Frame final, duraciones
  de 4 a 12s y 1080p nativo por 0.01 USD más el clip.
- **`src/plan_musical.py`**: el clip deja de ser "una línea" y pasa a ser un
  hueco de una rejilla de 4s sobre la canción. El clip que cierra una línea
  encadena con la escena de la siguiente; los intermedios van sueltos.
- **La canción va entera**, y el fade recibe `fin_voz_s` para no apagar el
  último verso. Dos ads lo tenían y no se veía en ninguna métrica.
- **Logo de marca** en tres momentos deducidos del guion, uno de ellos
  sincronizado con la palabra cantada.
- **`src/descargas.py`**: reintentos y URL anotada antes de bajar. Nació de una
  caída de internet que tiró cinco clips ya pagados.
- La validación acepta la serie de parrilla numerada (`nicho_mapa` + `publico`).

### Pendientes

1. **La familia de personajes no se está usando.** `referencias/personajes/familia/`
   tiene diez character sheets (LEX abogados, CIFRA contadores, CARRI ecommerce,
   CLAP contenido, MATRA laboratorios, VANI logística, BIT ia, EFFI marca,
   CONTE, PANEL) y los guiones Pixar inventan protagonistas nuevos porque sus
   fichas los describen así. Falta decidir qué personaje va con cada público y
   apuntar los guiones a la hoja: ahorra 0.08 USD por ad y da consistencia
   entre creativos del mismo nicho.
2. **Las letras de los 14 guiones musicales de la primera serie no son
   cantables**: métrica de 7 a 23 sílabas, sin rima, estribillo una sola vez.
   Los P01–P28 sí lo son (rima consonante, métrica pareja, estribillo x2) y se
   nota al oírlos. Reescribir las primeras está propuesto y sin aprobar.
3. Los 28 guiones de la parrilla numerada quedaron versionados hoy, en siete
   estilos. Ninguno producido salvo P01 y P02.
4. La fase de voz del modo `locucion` sigue sin portar.

## 2026-09-07 · Ad p04 claymation "Mil mensajes en WhatsApp"

**Entregado:** `assets/renders/effix_claymation_vendedores-de-redes-sociales_mil-mensajes-en-whatsapp_20260907.mp4`
62.08s · 31 planos de 2.00s · -14.8 LUFS · true peak -2.1 dBTP · **5.88 USD reales**.

Guion `effix_claymation_p04-whatsapp-musical_20260904_aprobado.json` (renombrado
desde `_por-aprobar` y marcado `estado: aprobado`).

**Lo que se decidió y por qué:**
- La letra original (170 palabras) no cabía en la canción: cuatro intentos y
  ninguno cantó el CTA. Se bajó a 108 y entonces sí llegó.
- Salió de la letra la cifra "sesenta mil personas": era el único dato sin
  verificar con Effix, y el recorte lo quitó de encima. `datos_sin_verificar`
  queda limpio.
- Las líneas se reordenaron al orden real de la canción. El guion original
  ponía el verso 2 antes del coro, y `alinear` empareja en secuencia: cada
  plano caía desplazado.
- 13 planos bajaron a 12 (se cayó el de los ojos con el reflejo de la feria).

**Regla nueva en el código** (Alexander): la canción arranca cantada.
`ARRANQUE_CANTADO` en `src/audio_extra.py` va en el Structured Caption y aplica
a todos los ads; `producir.py` avisa si la intro pasa de `INTRO_MAXIMA_S` (2.0s).
Motivo: `duration` es un tope y cada segundo de intro se lo quita a la letra —
un intento gastó 13.6s en intro y salió sin puente ni CTA.

**Abierto, decide Alexander:**
1. Los primeros 24s del render son el mismo plano (fallo de alineación, ver
   MASTER_CONTEXT). Rehacer esos clips apuntándolos a las 3 líneas que se
   quedaron sin material cuesta ~1.17 USD y llevaría el ad a ~7.05, por encima
   del tope de 6.
2. La marca suena "de fix" en las cinco canciones. Ninguna grafía lo arregla
   con MiniMax Music 3.
3. Duración 62.08s: dos segundos por encima del rango 30-60.

**Pendiente de código:** techo de clips por línea en
`plan_musical.repartir_clips()` para que una línea no absorba el tiempo de las
que no anclaron. Sale gratis y evita repetir este gasto.

---

## 2026-09-07 · Ad P01 v2 pixar "Quiero vender y no sé por dónde"

**Entregado:** `assets/renders/P01_effix_pixar_emprendedores-que-empiezan_quiero-vender-y-no-se-por-donde_20260907.mp4`
51.83s · 26 planos de 1.91–2.00s · −14.3 LUFS · true peak −4.5 dBTP · **4.4569 USD reales**
(estimado 4.0634; la diferencia son dos escenas regeneradas y el whisper).

Guion `effix_pixar_p01-empezar-musical_v2_aprobado.json`, formato F6 dos voces.
**Primer ad del lote que cae dentro del rango 30–60s** sin cortar la canción:
la letra corta (108 palabras) y `duracion_ms` con margen hicieron el trabajo.

### Cuatro prompts corregidos ANTES de gastar

La validación automática pasaba limpia; los cuatro fallos los cazó la lectura
contra las reglas escritas, y ninguno costó dinero:

1. L9 traía `hundreds of colourful stands` — la frase que ya costó 0.36 USD en
   `contadores-musical`. Reescrita a la redacción canónica de `modern convention
   hall` con veto de mercado. **La escena 9 salió a la primera y es la mejor del ad.**
2. L10 traía `at a fair stand`, vetado por la misma entrada.
3. L7 hacía *volver* el color al aparecer la feria, justo al revés del corte
   declarado para los 28.
4. L12 seguía con el botón flotante en `prompt_video` pese a la corrección del
   2026-09-07 que lo quitó del `prompt_imagen`: el clip lo habría dibujado igual.

**Aprendizaje:** una corrección aplicada sólo al `prompt_imagen` no está
aplicada. El clip nace de la imagen pero el movimiento lo dicta el
`prompt_video`, y ahí seguía el botón. Revisar los dos campos siempre.

### Dos escenas regeneradas en producción (0.16 USD)

- **Escena 6:** nano-banana puso el logotipo de una marca real en la tapa del
  portátil, y encima los "abstract geometric shapes" se leían como glifos. El
  `negative_prompt` ya decía `logo` y no bastó: hizo falta pedir la tapa lisa
  explícitamente (`plain unbranded matte laptop, completely blank smooth lid`).
- **Escena 12:** NUBE no hizo el gesto de señalar al borde inferior. "Pointing
  down with one hand" no basta; con `one stubby arm fully extended straight
  downward, the whole arm visible against the body` sí salió.

### La alineación salió perfecta, y por qué importa

Las 12 líneas ancladas, tramos contiguos de 2.5 a 7.5s, ninguna absorbiendo a
otra. Es lo contrario del p04, donde tres líneas se quedaron sin material y los
primeros 24s eran el mismo plano. **El pendiente del techo de clips por línea en
`plan_musical.repartir_clips()` sigue abierto**, pero aquí no se activó.

### Abierto, decide Alexander

1. **La aparición AGRAVADA de la micro-situación no está en imagen.** El guion
   la pedía en la línea 6 (la misma tapa, otro día, la libreta el doble de
   llena) y el reparto no le dio clip propio: su tramo dura 3.26s, por debajo
   del clip de 4s, así que el hueco lo cubre el clip encadenado 5→7 y en el
   segundo 19.5 se ve el pabellón con el overlay "Otro día igual". Las otras dos
   apariciones (cruda L2, resuelta L11) sí se reconocen. Un clip propio desde la
   escena 6 —ya pagada— cuesta 0.2333 y dejaría el ad en 4.69.
2. **La marca suena "de fix"** otra vez (whisper oye "Feria FX"). Sexta canción
   consecutiva; ninguna grafía lo ha arreglado con MiniMax Music 3.
3. **L7 se canta cambiada:** "el que vende **en pesos** sin saber jamás" en vez
   de "empezó". Es la línea de causa raíz. Regenerar la canción son 0.128 y
   obliga a rehacer el reparto de clips.
4. Los banners de fondo de la escena 12 tienen formas blancas que insinúan
   letras. Están desenfocados, pero la regla dice `absolutely no letters`.

### Código y documentación

`guion_aprobado.nombre_de_entrega()` ahora respeta el campo `nombre_entrega` del
guion y, si no está, antepone `P<NN>_` cuando el guion trae `nicho_mapa`. Los 28
ads de la parrilla se revisan por público, no por estilo. Actualizados
`CLAUDE.md` y `docs/FORMATO-GUION.md` en el mismo commit. Los dos tests de salud
en verde después del cambio.

---

## 2026-09-07 · Tanda v2: P02 skeleton y P04 claymation

| Ad | Duración | LUFS | Costo real | Render |
|---|---|---|---|---|
| P02 «La tienda que vende poquito» | 79.58s | −14.8 | 5.6228 | `P02_effix_skeleton_duenos-de-tiendas-online_...mp4` |
| P04 «Mil mensajes en WhatsApp» | 63.29s | −15.3 | 5.1528 | `P04_effix_claymation_vendedores-de-redes-sociales_...mp4` |

Los dos traían calcadas las cuatro correcciones ya aprobadas en el P01
(`at a fair stand`, botón falso en el `prompt_video`, gesto de señalar corto,
veto de logo). En el P04 la corrección del botón no se había aplicado ni a la
imagen. Todas salieron a la primera: la escena 9 del P02 y la 9 del P04 son
booths corporativos, no plaza de mercado.

### Por qué se cortaban las canciones, y las dos guardas nuevas

`musica.duracion_ms` **es un tope, no una duración pedida**: MiniMax compone
hasta ahí y, si la letra no cabe, deja de cantar a mitad de frase. Como el CTA
va al final, es lo primero que se pierde — y sólo se descubría después de pagar.
Cinco canciones desperdiciadas en esta tanda antes de entenderlo.

- `audio_extra.cabe_la_letra()` avisa **antes de pagar**, con la densidad medida
  (una palabra por pulso, `bpm/60`: 1.79–1.93 pal/s a 108 BPM, 1.18 a 96), y
  sugiere el BPM que haría caber la letra sin tocar el contenido.
- `transcripcion.cobertura_de_lineas()` compara la letra con lo cantado línea a
  línea **después de whisper**; si el beat `CTA` baja del 60% imprime 🛑 antes de
  gastar en imágenes. Cazó sola el P04 (CTA al 0%) y el P06.
- `_tope_de_cancion()` pide siempre con holgura (`OCUPACION_AL_PEDIR = 0.65`).
  Regla de Alexander: «no limites las canciones para que no se corten nunca».
  Pedir de más no alarga el ad porque `duration` es un tope: si la canción
  termina antes, se cierra sola.

El precio de esa regla es la duración: el P02 pasó de 64.08s (cortado en seco,
`cola_s` negativa) a 79.58s con la canción entera y 7.3s de cola.

### Aprendizajes que costaron dinero o tiempo

1. **Una corrección aplicada sólo al `prompt_imagen` no está aplicada.** El
   movimiento lo dicta el `prompt_video` y ahí seguía el botón falso.
2. **No paralelizar montajes.** El render del P04 murió con `Cannot allocate
   memory`: 16 clips 1080×1920 en un solo `filter_complex` no caben si hay otra
   fase corriendo. En serie funcionó a la primera.
3. **Los clips pagados se pueden reasignar.** Al rehacer la canción del P02 el
   plan pasó de 16 a 20 huecos; reasignar los clips existentes por línea cubrió
   los 20 por 0 USD, en vez de 3.03 en clips nuevos. `_clip()` los nombra por
   índice de tarea, así que sin reasignar habrían quedado desalineados.

### Abierto

1. **P04: la aparición agravada (L4) no se ve** — su tramo dura 0.76s. Y en ese
   punto aparece un cartel de plastilina que dice «TOY SHOP»: texto legible,
   prohibido.
2. **Loudness a −15.3 (P04) y −14.8 (P02)** contra el objetivo de −14. El P01
   salió a −14.3. Mirar el limitador de `mezcla.py` en los musicales.
3. **P06 cyberpunk congelado** con dos canciones pagadas (0.36) y ninguna
   servible: a 92 BPM repitió el coro y se saltó el CTA; a 112 metió 21.5s de
   intro y deshizo el final.
4. La marca sigue sonando «FX» en todas las canciones.

---

## 2026-09-07 · Ad P03 v2 crochet «De diez a cien»

**Entregado:** `assets/renders/P03_effix_crochet_ecommerce-en-crecimiento_de-diez-a-cien_20260907.mp4`
84.12s · 42 planos de 2.00s · −14.9 LUFS · true peak −4.1 dBTP · **6.5593 USD**
(estimado 4.0634; **Alexander aceptó pasar el tope de 6** cuando se vio el desvío,
antes de gastar en clips).

### Por qué costó 2.5 más de lo estimado

La estimación asumía la canción de 52s del guion → 12 clips. La canción salió de
**84.1s** y el reparto pidió **21**: 4.90 USD de video en vez de 2.80. La cadena
fue: a 100 BPM la letra ocupaba el 96% del tope, salió una pista de 90s que cantó
sólo hasta el 66 y se saltó el coro, el puente y el CTA; a 112 BPM cantó todo,
pero en 84s. **Estimar con la duración del guion es estimar con un número que la
canción todavía no ha confirmado** — el costo real de un musical no se sabe hasta
después de la canción.

### Cuatro correcciones antes de gastar

1. **El cierre I2V de crochet no estaba en ninguno de los 12 `prompt_video`** —
   iban con el cierre genérico del lote. CLAUDE.md §8 lo exige verbatim, y sin él
   Seedance suaviza la lana hacia CGI a mitad de clip. El positivo y el negativo
   sí estaban verbatim.
2. **L1, L10 y L12 pedían dedos y manos**, que `reglas_criticas` del template
   prohíbe: el modelo no los renderiza en lana.
3. **L9 y L10 volvían al mercado** (`hundreds of stands`, `at a fair stand`).
4. **L12 dibujaba el botón falso** en imagen y en video. Era el único v2 del lote
   sin esa corrección aplicada.

### Escena 4 regenerada (0.08)

Salió en plano general en vez del primer plano de la pila —rompía el mismo
encuadre que exige la aparición agravada— y con glifos legibles en los paneles
tejidos. Con el encuadre fijado a altura de mesa y el veto de letras reforzado
salió bien. **Las tres apariciones se reconocen como el mismo sitio**: diez cajas
ordenadas → las mismas diez con una reventada y el reloj en otra hora → la mesa
desbordada.

### Lo que no se corrigió, y por qué

**La escena 12 no hace el gesto de señalar**: LEO sale de frente con los brazos
caídos. No se regeneró a propósito — el template de crochet desaconseja las poses
de brazo, así que insistir era tirar 0.08 con poca probabilidad. Lo que importaba
de la corrección sí está (no hay botón falso) y el montaje pone las flechas
animadas hacia abajo durante los 6s del CTA.

### Abierto

1. **84.12s**, muy por encima del rango 30–60. Es el precio de no cortar la
   canción, y ya van tres ads seguidos (P02 79.6, P03 84.1).
2. **L11 dura 1.20s** en la alineación: la línea del remate («ya perdí la cuenta»)
   casi no tiene tiempo propio, mientras L1 se lleva 17.3s y L10 15.5s. El techo
   de clips por línea en `plan_musical.repartir_clips()` sigue pendiente.
3. El v1 (`effix_crochet_p03-diez-a-cien-musical_20260904_*`) volvió a
   `por-aprobar`: se había quedado marcado `aprobado` por error y nunca se produjo.

---

## 2026-09-07 · Dos reglas nuevas: tres micro-situaciones y cierre irrepetible

Alexander, al ver el lote: «todos los guiones o lyrics están quedando con el mismo
patrón». Medido sobre los ocho v2, tenía razón y era literal:

- **8 de 8** cantaban los mismos dos versos: «Feria Effix, del quince al
  diecinueve / Plaza Mayor, Medellín, la cosa se mueve» — y el pareado está
  además en 35 guiones del repo contando el lote v1.
- **8 de 8** cerraban con «Compra tu ingreso, dale clic…», cambiando sólo el
  verbo final.

Lo que sí cambió el v2 fue la arquitectura de secciones (cuña de radio, conteo,
carta, dos voces, pregón, relato en tercera persona), y se nota: los dos que
suenan distintos —P10 y P06— son los que además abren fuera del «yo me quejo».

**Reglas 8 y 9 en `guion_aprobado.validar()`**, con su documentación en
`CLAUDE.md` y `docs/FORMATO-GUION.md` en el mismo commit:

- **8 · Tres micro-situaciones.** `microsituacion_apariciones` con cruda,
  agravada y resuelta, `en_imagen >= 3`, y cada una anclada a una línea que
  exista. Error si falta.
- **9 · El cierre no se repite.** Los versos en beats de cierre (`FECHAS`,
  `CORO_FERIA`, `CORO_LLEGADA`, `PRUEBA`, `PUENTE_CIFRAS`, `CTA`) se comparan con
  los de todos los demás guiones. Si ya están cantados en otro, error. Fuera del
  cierre, sólo aviso.

Un ad ya entregado (con `render` o `costo_real_usd`) queda exento: avisa pero no
bloquea, porque las reglas nuevas no se aplican hacia atrás (CLAUDE.md §12).

**Efecto inmediato:** P01, P02, P03 y P04 siguen validando. **P06, P09, P10 y P12
quedan bloqueados** con 3 errores cada uno hasta que se reescriba su bloque de
cierre en Cowork. Es el efecto buscado.

### Cierre elegido para el P05 (2026-09-07)

Alexander eligió la opción C, el remate de la micro-situación. Va al guion v2
cuando salga de Cowork:

```
No estaba en la pantalla: el ganador estaba allá
Feria Effix, Plaza Mayor, en el centro de Medellín
Del quince al diecinueve, trescientas cincuenta marcas
Tu boleta está abajo: un clic y vas a comprar
```

Por qué pasa la regla 9: ninguno de los cuatro versos existe en los demás
guiones, y rompe los dos moldes quemados — el pareado «del quince al diecinueve
/ la cosa se mueve» (63 apariciones en el repo) y «compra tu ingreso dando clic
en el botón» (42). Dice «tu boleta», no «compra tu ingreso».

Dos restricciones que condicionaron la redacción: **«dropshipping» no se puede
cantar** (sale «Kecoxie», está en `PALABRAS_QUE_NO_CANTA`), así que al público
se le nombra por proveedor, catálogo y marcas; y el primer verso cierra la
micro-situación en vez de abrir bloque nuevo, con lo que la tercera aparición
y el cierre son lo mismo.

---

## 2026-09-07 · Ad P05 v2 anime «El producto ganador» — y el ad más caro hasta ahora

**Entregado:** `assets/renders/P05_effix_anime_dropshippers_el-producto-ganador_20260907.mp4`
76.38s · 37 planos de 2.00s · −14.9 LUFS · **8.0046 USD** (estimado 4.0634).

**El v2 lo escribí yo**, a petición de Alexander, desde el v1: se conservan
micro-situación, ángulo, KAI y bible; cambia la letra (de 158 a 90 palabras),
el formato de canción (F8 latiguillo de cola), las tres apariciones en el mismo
encuadre y el cierre (opción C, elegida el mismo día).

### Por qué costó el doble: seis canciones

De seis intentos, **sólo dos cantaron el CTA**. Una de cada tres. Lo que se
aprendió, por orden de descubrimiento:

1. **Las etiquetas de sección inventadas se cantan.** El primer intento cantó
   literalmente «Latiguillo» y «Latiguillo Roto». MiniMax reconoce [Verso],
   [Coro], [Puente], [Outro]; lo que no reconoce lo trata como letra. Ya hay
   guarda: `audio_extra.etiquetas_raras()`, avisando antes de pagar. **Casi
   todos los v2 usan etiquetas inventadas** ([Cuña], [Conteo], [Carta],
   [Pregón]) y hasta ahora habían tenido suerte.
2. **«herramienta» no se puede cantar.** Salió «hermanienta», «rejanienta», «la
   hermano» en cuatro canciones seguidas. Anotada en `PALABRAS_QUE_NO_CANTA`
   junto a «resultados». La línea pasó a «me falta ver el dato».
3. **Bajar el BPM no arregla la dicción.** 112 → 104 dio una canción peor, que
   se saltó medio texto. El problema era la palabra, no el tempo.
4. **Cambiar el verbo del CTA tampoco.** «comprar» salía «cumplir», se probó
   «nos vemos» y el sexto intento se saltó el cierre entero. Se recuperó la
   quinta pista de `cancion_intento_05.mp3` por el precio de una transcripción
   (0.096) en vez de otra canción.

**Los intentos guardados valen dinero:** `cancion_intento_NN.mp3` permitió
volver a la mejor pista sin pagarla otra vez. Al recuperarla hubo que devolver
la letra del guion a lo que esa pista canta.

### Escenas regeneradas

- **Escena 5** (aparición agravada): salió con «DELETED» y «FAILED» estampados
  en las capturas y partida en dos viñetas. Con el encuadre fijado y el veto de
  letras reforzado, correcta.
- **Escena 12** (CTA): «la mano parece de goma», dijo Alexander, y era cierto.
  Tres intentos: el segundo dio la mano bien en plano general, el tercero —al
  forzar el encuadre cerrado— sacó una mano gigante flotando desconectada del
  cuerpo. Se conservó el segundo. **Forzar el encuadre para agrandar una mano
  es cómo se consigue una mano peor.**

### Reasignación de clips, otra vez gratis

Al recuperar la quinta canción el reparto volvió a 19 huecos: 16 se cubrieron
con clips ya pagados y sólo hubo que generar 3 (0.70) — los dos de la línea 12,
porque su escena había cambiado, y uno de la 7.

### Abierto

1. **La línea 7 no se canta** en la pista final: el ad pierde la excusa del
   personaje, aunque el arco se entiende.
2. **El CTA canta «vas a cumplir»** en vez de «comprar». El overlay «Tu boleta
   está abajo» y las flechas al botón sostienen el mensaje.
3. **76.38s**, cuarto ad seguido fuera del rango 30–60.
4. La marca sigue sonando «FX».


---

## 2026-09-07 · P07 mayoristas, en crochet

**Entregado:** `assets/renders/P07_effix_crochet_mayoristas-y-distribuidores_pedidos-por-telefono_20260907.mp4`
81.18s · 41 planos de 1.98s · −14.8 LUFS · **6.2743 USD** (estimado 4.3766).

Guion: `scripts/guiones/effix_crochet_p07-mayorista-digital-musical_v2_aprobado.json`.
El `job_id` se dejó en `...animado2d-v2` a propósito: ahí vive la canción ya
pagada, y cambiarlo la habría tirado.

### La letra se escribió en tres pasadas, con Alexander

1. La del archivo (123 palabras) **no se produjo**: traía etiquetas `[Gloria]` y
   `[Don Fabio]` que MiniMax canta en voz alta, no cabía en el tope (75s de
   letra para 64s) y se habría quedado sin CTA. Se detectó gratis.
2. Alexander cambió el dolor: **"los archivos de Excel se borran, los cuadernos
   se pierden y después no encuentro los pedidos ni los datos de los clientes"**.
3. Y luego el ángulo: **digitalizar el pedido telefónico y automatizar el
   despacho** — el Excel borrado es el síntoma, no la promesa. La letra final
   cobra el dolor en cuatro golpes concretos (entendí diez y eran cien ·
   despaché lo que no era y me lo devolvieron · tuve que preguntarle qué pidió ·
   llamó a las once y nadie contestó) y el outro los desmonta uno por uno:
   *"Él pide solo, con precio y cantidad, y sale despachado"*.

99 palabras a 104 BPM = 89% del tope. **La canción salió al primer intento y
cantó el CTA.** Alexander la aprobó de oído pese a que la transcripción
marcaba "Feria FX", "350 en prensas" y "venga a xepa la feria": whisper sobre
música exagera, y el oído manda.

### El estilo se cambió después de la canción

Alexander pidió crochet con la canción ya hecha. Sólo se rehízo la capa visual
—bible, prompts de imagen y de video— con los textos universales **verbatim**
desde `src/estilos_especiales.py`; la canción no se tocó y no se volvió a pagar.

### El sobrecosto

**6.27 contra 4.38 estimados.** El estimador cuenta un clip por línea (13) y la
producción reparte por segundos de canción (20 clips). Detalle y la cuenta
correcta en **Notas de aprendizaje** de `MASTER_CONTEXT.md`.

### Abierto

1. **81.18s**, quinto ad seguido fuera del rango 30–60. Aquí es consecuencia
   directa de la canción de 84s.
2. `cost_estimator` sigue estimando por líneas: **hay que arreglarlo antes del P08**.
3. El QA sigue sin comparar el render contra `cancion_util.mp3` en `musical_sync`.
4. La marca sigue sonando «FX» pese a escribirla «Éffix». Tres ads seguidos.

---

## 2026-09-07 · Tres ads: P06 pixar, P08 skeleton, P10 crochet

| Entrega | Dur | Planos | LUFS | Costo real |
|---|---|---|---|---|
| `P06_effix_pixar_marcas-fabricantes-e-importadores_mi-marca-no-existe-en-internet` | 80.02s | 40 | −14.9 | **10.6578** |
| `P08_effix_skeleton_marketing-y-adquisicion_la-campana-que-dejo-de-funcionar` | 61.67s | 31 | −14.6 | 5.0508 |
| `P10_effix_crochet_expertos-en-tiendas-shopify_se-mucho-y-nadie-me-contrata` | 65.21s | 33 | −14.6 | 5.2931 |

### Por qué el P06 costó 10.66, el doble del tope

Se produjo entero en **cyberpunk** (héroe, 12 escenas, 6 clips = 3.40 USD) y
después Alexander lo pidió en **pixar**. El estilo va pegado a cada imagen: no
se recicla nada. Se avisó el número antes de gastar y él decidió seguir.

Lo que **sí** se reutilizó gratis fue la canción: copiar `cancion.mp3`,
`cancion_util.mp3`, `tramo.json` y `transcripcion.json` a la carpeta del job
nuevo evita repagarla. **Al cambiar de estilo se cambia el `job_id` y se copian
los cuatro archivos de audio.**

Un error caro y evitable: se corrió `todo` y el productor **reutilizó un
`cancion.mp3` viejo** —de la letra anterior— sin avisar de que la letra había
cambiado. Sólo se descubrió al leer la transcripción. `--forzar` es obligatorio
después de tocar la letra.

### La letra se lee y se aprueba antes de la canción

Alexander detuvo el P06 con cinco canciones ya generadas (0.892) porque la letra
no le gustaba. **Que el guion esté aprobado no es aprobación de la letra.**
Ahora se pega la letra en el chat y se espera respuesta antes de la fase
`cancion`.

Y la letra tiene que ser **explícita**. La del P06 era una carta en segunda
persona a la propia marca: no decía quién hablaba, ni qué tenía el competidor,
ni qué hay en la feria, y el CTA se lo cantaba a la marca en vez de al que
compra. Reescrita en primera persona —«soy fabricante y tengo marca propia»,
«con fotos, con precios, con el botón de comprar», «agencias, plataformas y
quien te vende en línea»— se entiende sola.

### `duracion_excepcion`: salirse del rango, pero por escrito

En `musical_sync` manda la canción, y si sale de 79s el ad dura 79s. La regla 6
bloqueaba. Ahora `duracion_excepcion: {motivo, aprobado_por}` la convierte en
aviso; sin esos dos campos sigue siendo error. Cambiado en
`src/guion_aprobado.py`, `docs/FORMATO-GUION.md` y `CLAUDE.md` a la vez.

### El montaje ahora va por capas — antes reventaba

El render del P06 murió **tres veces**, y ninguna era culpa de los clips:

1. **`0xC00000FD` (STACK_OVERFLOW).** 40 planos con sus drawtext y overlays en
   un solo `filter_complex` desbordan la pila de ffmpeg. El P05, con 37, había
   pasado raspando.
2. **`Cannot allocate memory` en el demuxer de png_pipe.** Cada `-loop 1 -i
   logo.png` encola frames que el overlay no consume hasta que llega su
   `enable`; cuatro colas de ~1900 frames no caben. Agrupar con `split` tampoco
   sirve: la rama que espera bloquea a las demás.
3. La primera vez **el fallo fue silencioso**: ffmpeg escribió el mp4 igual y el
   ad salió **sin el logo del plano final**. Se detectó mirando fotogramas, no
   por el código de salida.

`fase_montaje` se partió en: concat de planos → texto y música → **una pasada
por cada capa de PNG**, con los intermedios a crf 14. Memoria constante y ningún
error. El P08 y el P10 se montaron a la primera.

### Canciones: tres lecciones nuevas

- **`cabe_la_letra` no es decorativo.** La primera del P10 —106 palabras a 100
  BPM, 99% de ocupación— se comió «Shopify», saltó entera la línea 9 y dejó la 8
  en el 27%, sin fechas. A 112 BPM y 104 palabras (87%) cantó las once. 0.18
  tirados por no mirar el aviso antes de pagar.
- **«Shopify» no se canta**: salió «yo puedo». Se sacó de la letra y se puso en
  el overlay de la línea 1, que además se lee sin sonido. Mismo tratamiento que
  «ecommerce» y «dropshipping».
- **El modelo rellena el tiempo que le sobra con desvarío.** El P08 cerró el CTA
  en 59.38s y siguió con «no hay rinocerontes en las mesas de Ibai» hasta 67.68.
  Se cortó en 59.55 y se le pegó la cola instrumental real del final
  (67.70–69.80): cierre limpio, gratis, y siete clips menos.

### El P08 salió flaco

Alexander lo pidió «skeleton pero con músculos» y eligió el esqueleto fornido de
gimnasio. El bible pedía hombros anchos, caja torácica gruesa y huesos pesados,
y el modelo devolvió un esqueleto corriente. **Pedir volumen sin nombrar músculo
no funciona**: sin carne el modelo no tiene de dónde sacar el ancho. Rehacerlo
son 4.54 USD porque el personaje sale en los 15 clips. Pendiente de decisión.

### Abierto

1. La marca sigue sin sonar bien: «EFIX» en el P06 y el P08, y **«feria FX / De
   Vix»** en el P10, que es la peor versión. Siete ads, ninguna toma correcta.
   La tilde automática de `audio_extra` no basta.
2. Tres ads seguidos fuera del rango 30–60 (80.0, 61.7, 65.2). El P06 con
   excepción declarada; los otros dos no.
3. **El markdown `GUIONES-MUSICALES-28-angulo1-v2.md` está desfasado**: trae el
   P06 con etiquetas `[Carta]`, 92 BPM, el pareado quemado y un botón dentro del
   cuadro, y apunta a un JSON que no existe. Los JSON van por delante; hay que
   regenerarlo desde ellos.
4. El P08 con el personaje flaco, a la espera de si se rehace.
