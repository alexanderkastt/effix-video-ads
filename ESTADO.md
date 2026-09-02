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
