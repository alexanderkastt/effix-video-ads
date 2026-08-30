# Stack de Video IA para Ads

Este proyecto es tu **caja de herramientas para escribir prompts de video con IA**.
No genera videos por sí solo: te da los prompts perfectos que luego pegas en
Higgsfield, Hailuo, Pollo.ai o donde vayas a generar el video.

Cuatro estilos listos: **UGC auténtico**, **Pixar/Disney**, **Claymation** y
**Cinematic product hero**.

---

## Cómo levantarlo en otro computador

Estos pasos son para cuando quieras trabajar desde otro equipo. Se hacen una sola vez.

1. **Descarga el proyecto.** El `--recurse-submodules` es importante: sin él las
   carpetas `skills/higgsfield` y `skills/shortfilm` llegan vacías, porque son dos
   proyectos de otras personas que viven en sus propios repositorios.

   ```
   git clone --recurse-submodules <URL-del-repo>
   cd skills-video-ads
   ```

   Si ya lo clonaste sin esa opción y las carpetas están vacías:

   ```
   git submodule update --init --recursive
   ```

2. **Instala Python 3.10 o superior**, si no lo tienes. En Windows el comando es
   `python`, no `python3`.

3. **Crea la cajita de Python** (el entorno). No se descarga con el repo a propósito:
   lleva rutas del computador donde se creó, así que hay que hacerla nueva en cada equipo.

   ```
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Instala ffmpeg.** Es el programa que une los videos. Descárgalo de
   [gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds/) y agrégalo al PATH.
   Para comprobar que quedó: escribe `ffmpeg -version` y debe responder algo.

5. **Crea tu archivo de claves.** Copia `.env.example` y renómbralo a `.env`, después
   ábrelo y pega tus claves. **El `.env` nunca se sube al repositorio** — cada equipo
   tiene el suyo.

   ```
   copy .env.example .env
   ```

6. **Comprueba que todo quedó bien:**

   ```
   python scripts/test_dry_run.py
   python scripts/test_integracion_creativa.py
   ```

   Los dos deben terminar en verde. Si alguno falla, el mensaje dice qué falta.

### Qué NO viaja en el repositorio

| Qué | Por qué | Cómo lo recuperas |
|---|---|---|
| `.env` | Tiene tus claves privadas | Copias `.env.example` y pegas las tuyas |
| `venv/` | Lleva rutas del equipo donde se creó | Lo recreas con el paso 3 |
| Videos `.mp4` | Son 554 MB; GitHub no es para eso | Drive o Bunny CDN |
| `assets/clips`, `renders`, `audio` | Material intermedio, se regenera | Se vuelve a generar al producir |

---

## Cómo usarlo (paso a paso)

### Paso 0 — Instalar (SOLO la primera vez)

Esto se hace una sola vez en la vida del proyecto. Si ya lo hiciste, salta al Paso 1.

1. Abre PowerShell y entra a la carpeta del proyecto:

   ```
   cd "F:/Users/SICOMMER SAS/Documents/Proyectos/skills-video-ads"
   ```

2. Crea el "entorno" de Python. Un entorno es una cajita aparte donde se
   instalan los programas que este proyecto necesita, para que no se mezclen
   con el resto del computador:

   ```
   python -m venv venv
   ```

3. Enciende esa cajita (esto se llama "activar el entorno"):

   ```
   venv\Scripts\activate
   ```

   Sabrás que funcionó porque al inicio de la línea aparece `(venv)`.

4. Instala los programas que el proyecto necesita:

   ```
   pip install -r requirements.txt
   ```

5. Abre el archivo `.env` (con el Bloc de notas sirve) y pega tus claves.
   Una clave (o *API key*) es la contraseña que le das a este proyecto para
   que pueda usar tu cuenta de ElevenLabs, Magnific, etc. Cada línea que
   termina en `=` está esperando la suya.

   **Nunca compartas ese archivo ni lo subas a internet.**

---

### Paso 1 — Abre este proyecto en Claude Code

En la terminal, escribe:

```
cd "F:/Users/SICOMMER SAS/Documents/Proyectos/skills-video-ads"
claude
```

Si vas a correr scripts de Python a mano, primero enciende la cajita:
`venv\Scripts\activate`

### Paso 2 — Pídele un prompt

Escríbele en lenguaje normal. Ejemplos que funcionan:

- `Hazme un prompt UGC para un serum anti-edad, mujer de 35 años en su baño`
- `Necesito un ad estilo Pixar de 8 beats para Kreoon`
- `Prompt cinematic product hero para una crema, fondo oscuro, dark luxury`
- `Ad de claymation para @alexemprendee, 15 segundos`

Claude lee las plantillas de este proyecto y te devuelve el prompt listo para copiar.

### Paso 3 — Copia el prompt y pégalo en la herramienta de video

| Si el prompt dice… | Pégalo en… |
|---|---|
| Seedance / Kling / Veo / Sora | higgsfield.ai |
| Hailuo | hailuoai.com |
| Pollo | pollo.ai |
| Runway | runwayml.com |

### Paso 4 — Guarda lo que funcionó

Cuando un prompt te dé buen resultado, guárdalo en la carpeta `prompts-listos/`
del estilo que corresponda. Así no lo vuelves a escribir desde cero.

Y si aprendiste algo nuevo (por ejemplo: "Hailuo no entiende bien las manos"),
anótalo al final de `MASTER_CONTEXT.md`, en la sección
**Notas de aprendizaje**. Claude lee ese archivo siempre.

### Paso 5 — Une los clips (cuando ya tengas los videos)

Si generaste varios clips sueltos y los quieres pegar en uno solo, pon todos los
`.mp4` en una carpeta y pídele a Claude: `une estos clips con ffmpeg`.
ffmpeg ya está instalado en este equipo.

---

## Qué hay en cada carpeta

| Carpeta | Para qué sirve |
|---|---|
| `MASTER_CONTEXT.md` | El cerebro. Tus marcas, tus reglas de prompting, tus pipelines. Claude lo lee siempre. |
| `generar-prompt.md` | Las 4 plantillas base (UGC, Pixar, cinematic, claymation). |
| `skills/higgsfield/` | 33 sub-skills de prompting profesional para Higgsfield. |
| `skills/shortfilm/` | 27 plantillas de género cinematográfico (claymation, product-commercial, etc.). |
| `referencias/` | Aquí subes fotos: productos, personajes, estéticas que te gustan. |
| `prompts-listos/` | Los prompts que ya te funcionaron, para reutilizarlos. |
| `outputs/` | Los videos y entregables finales por estilo. |
| `assets/clips/` | Los clips sueltos de 4s recién generados, antes de unirlos. |
| `assets/audio/` | Voz de ElevenLabs y música, antes de mezclar. |
| `assets/renders/` | Ensamblados a medio hacer (ffmpeg trabaja aquí). |
| `src/` | El código Python que arma los videos automáticamente. |
| `config/` | Ajustes de cada estilo visual y presets de ffmpeg. |
| `logs/` | Registro de qué generaste y cuánto costó. |
| `.env` | Tus claves privadas. No se comparte nunca. |
| `venv/` | La cajita de Python. No la toques ni la borres. |

---

## Referencia técnica

### Plantillas de género útiles (en `skills/shortfilm/templates/`)

| Estilo que quieres | Archivo que sirve |
|---|---|
| Claymation | `claymation.md` |
| Cinematic product hero | `product-commercial.md`, `car-commercial.md` |
| Antes/después de 15s | `15s-transformation.md` |
| Ad narrativo multi-shot | `multi-shot-narrative.md`, `micro-drama.md` |
| Food / bebida | `food-asmr.md` |
| Moda / belleza | `fashion-film.md` |
| Movimientos de cámara | `camera-move-library.md` |
| Qué prohibir en el prompt | `negative-prompts.md` |

### Sub-skills de Higgsfield más relevantes (en `skills/higgsfield/skills/`)

- `higgsfield-prompt` — el núcleo, fórmula MCSLA
- `higgsfield-seedance` / `higgsfield-seedance-2-5` — UGC realista
- `higgsfield-camera` / `higgsfield-motion` — control de cámara y movimiento
- `higgsfield-soul` — consistencia de personaje (Soul ID)
- `higgsfield-marketing-studio` — ads y contenido comercial
- `higgsfield-character-design` — diseño de mascotas/personajes Pixar
- `higgsfield-troubleshoot` — cuando una generación sale mal

### Actualizar los repos de skills

```
git -C ./skills/higgsfield pull
git -C ./skills/shortfilm pull
```

### Reglas de oro del prompting UGC

- **Nunca** uses: `cinematic`, `professional`, `stunning`, `8k`, `studio`, `perfect`
- **Siempre** usa: `handheld`, `authentic`, `natural light`, `candid`, `iPhone-shot`
- Mínimo 3 señales de movimiento humano por prompt
- Entre 100 y 260 palabras
