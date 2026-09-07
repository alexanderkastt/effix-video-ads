# Formato único de guion aprobado

Un solo archivo JSON es la frontera entre la parte creativa y la producción.
Todo lo que está **antes** del archivo (micro-situación, gancho, guion, storyboard,
auditoría) se trabaja en Cowork o a mano, sin gastar. Todo lo que está **después**
(voz, imágenes, clips, montaje, mezcla, render) lo hace Claude Code con un solo
comando y sin volver a preguntar por el contenido.

```
scripts/guiones/<marca>_<estilo>_<nicho>-<slug>_<AAAAMMDD>_aprobado.json
```

Ejemplo: `scripts/guiones/effix_microdoc_networking-la-agenda_20260904_aprobado.json`

## Por qué este formato y no el de `crear_video.py`

El repo tenía dos formatos: el de `beats` que genera el motor determinista
(`crear_video.py`) y el de `lineas` que escribieron a mano los scripts
`_producir_*.py`. **Los cuatro ads reales salieron del segundo.** Este documento
lo formaliza y le agrega lo que quedaba implícito (micro-situación, nivel de
conciencia, auditoría), para que un solo `scripts/producir.py` genérico lo
consuma y los `_producir_*.py` desechables dejen de hacer falta.

## Esquema

```jsonc
{
  "formato": "guion-aprobado/1",          // versión del esquema
  "estado": "aprobado",                    // el productor se niega si no dice "aprobado"
  "job_id": "networking-la-agenda",        // carpeta en assets/clips|audio|renders
  "titulo": "La agenda",
  "marca": "effix",
  "nicho": "networking",                   // clave en src/nichos_effix.py
  "angulo": "27.2",                        // clave en config/nichos/*-angulos.json
  "estilo": "micro_doc_ugc",               // clave en src/estilos_especiales.py
  "modo": "locucion",                      // locucion (voz ElevenLabs) | musical_sync (canción, sin voz)
  "pase": "pase_3_dias",                   // clave en CTA_POR_PASE (narracion_effix.py)
  "objetivo": "conversion",                // alcance | conversion | urgencia
  "nivel_conciencia": "problem",           // unaware | problem | solution | product | most_aware
  "gancho": { "banco": "dolor_nombrado#33", "gatillos": ["dolor_nombrado","auto_relevancia"] },
  "aspect_ratio": "9:16",
  "duracion_objetivo_s": 45,               // 30–60. Se recalcula con el audio real.

  "microsituacion": {                      // los 7 pasos. Sin esto no hay guion.
    "momento": "...", "sintoma": "...", "reaccion_interna": "...",
    "explicacion_fallida": "...", "patron": "...", "causa_raiz": "...", "mecanismo": "..."
  },

  "bible": "...",                          // estilo visual VERBATIM del template. Va en TODOS los prompts.
  "negative_prompt": "...",
  "personajes": {                          // vacío si el estilo no tiene personaje fijo
    "clave": { "ficha": "descripción física en inglés", "voz": "perfil ElevenLabs", "quien_es": "rol", "lipsync": false }
  },

  "lineas": [                              // una por réplica. El montaje las parte en planos.
    {
      "n": 1,
      "beat": "MOMENTO",                   // MOMENTO SINTOMA REACCION EXPL_FALLIDA PATRON CAUSA_RAIZ MECANISMO PRUEBA VISUALIZACION FECHAS CTA DEFECTO LOOP CALLOUT
      "quien": "NARRADOR",                 // o clave de personajes
      "texto": "...",                      // lo que se lee (sin tildes raras para logs)
      "texto_tts": "...",                  // lo que se locuta: números en letras, tildes correctas
      "texto_pantalla": "...",             // ≤ 7 palabras. Vacío = sin overlay
      "plano": "...",                      // descripción del plano en español, para el humano
      "prompt_imagen": "...",              // en inglés. Sin texto, sin letras. Cierra con bible.
      "prompt_video": "...",               // en inglés. @Image1 = start. Sin slow/deliberate. Cierra con "no discernible speech".
      "prompt_keyframe_final": "...",      // opcional. Si existe, se genera @Image2 y el clip se factura a medida.
      "lipsync": false
    }
  ],

  "musica_mood": "energetico",             // clave en config/soundtracks.json (modo locucion)
  "musica": { ... },                       // solo modo musical_sync: suno_custom_lyrics, suno_style_tags, bpm_recomendado, modelo.
                                           // En ese modo texto_tts va vacío, `texto` es lo que se canta en el plano,
                                           // y el productor: canción → whisper → recorte al tramo cantado → cortes en golpes (librosa).
  "cta": { "hablado": "...", "overlay": "..." },   // copiado de CTA_POR_PASE, no inventado

  "auditoria": {                           // ganchos.auditar_guion() — las 6 reglas
    "marca_en_5s": true, "complicacion_antes_12s": true, "defecto_admitido": true,
    "situacion_no_persona": true, "cifras_no_redondeadas": true, "duracion_30_60": true
  },
  "datos_sin_verificar": [],               // toda cifra sin fuente va aquí, no escondida
  "costo_estimado_usd": null,              // lo llena el productor con parámetros reales
  "notas_produccion": "..."
}
```

## Reglas que el productor verifica antes de gastar

1. `estado == "aprobado"` y `formato == "guion-aprobado/1"`.
2. `estilo`, `nicho`, `pase`, `musica_mood` existen en sus registros.
3. Ninguna línea contiene `descuento`, `EFFIX20`, `taller`, ni palabras de
   `palabras_prohibidas` del brand_dna. Ninguna promete cinco días con `pase_3_dias`.
4. Ningún `prompt_video` contiene `slow`, `deliberate`, `slowest`; todos cierran
   con `no discernible speech`. Ningún `prompt_imagen` pide texto legible.
5. `texto_pantalla` ≤ 7 palabras.
6. Duración estimada = palabras / `PALABRAS_POR_SEGUNDO` + `RESPIRO_S` × líneas,
   entre 30 y 60 s. La real se mide con ffprobe después de la voz.
7. Costo estimado con parámetros reales (duración por línea redondeada a tramos
   de 5/10 s salvo keyframe final, `n_imagenes` = líneas + keyframes). Si pasa
   6 USD, imprime el veredicto 🛑 y **para**.

## Flujo en Claude Code

```
produce scripts/guiones/<archivo>_aprobado.json
```

Claude Code: valida (1–6) → estima costo → muestra veredicto ✅/⚠️/🛑 → **espera
OK de Alexander** → voz (una llamada por línea, `beat_NN.mp3`) → mide con ffprobe
→ reparte clips → imágenes (`@Image1`, `@Image2`) → clips → `ritmo.py` (planos)
→ `mezcla.py` → render en `assets/renders/<job_id>.mp4` → QA (duración, LUFS,
planos) → anota costo real en `logs/` y `ESTADO.md`.

## Estado de la implementación

- ✅ Formato definido (este archivo), dos guiones narrados de ejemplo y 14 guiones musicales `*_por-aprobar.json` en `scripts/guiones/` (ver `outputs/GUIONES-MUSICALES-20260904.md`). Un `_por-aprobar.json` se vuelve producible al renombrarlo `_aprobado.json` con `estado: aprobado`.
- ✅ `scripts/producir.py` existe desde el 2026-09-06 y produjo el primer ad
  (`abogados-musical-pixar`). Valida con `src/guion_aprobado.py`, estima con
  parámetros reales y corre por fases.
- ⏳ Falta portar la **fase de voz del modo `locucion`** (una llamada por línea,
  medir con ffprobe, repartir clips desde el audio). Hasta entonces
  `scripts/_producir_animado2d_la_acera.py` no se borra: es la referencia.

### Cómo se nombra el entregable

El `job_id` sirve para las carpetas de trabajo (`assets/clips/<job>`), pero como
nombre de entregable no dice nada: `p02-pocas-ventas-musical-skeleton.mp4` no
explica a quién le habla el ad. El mp4 final se nombra por su contenido:

```
effix_<estilo>_<nicho o público>_<micro-situación>_<AAAAMMDD>.mp4
```

Ejemplo: `effix_skeleton_duenos-de-tiendas-online_la-tienda-que-vende-poquito_20260907.mp4`

El título del guion **es** el nombre de su micro-situación, así que hace de
resumen sin meter el párrafo entero. Cuando el guion no trae `nicho` con nombre
—la serie de parrilla numerada— se usa `publico`. Lo genera
`guion_aprobado.nombre_de_entrega()`.

### Campos que el productor añadió al esquema

| Campo | Dónde | Para qué |
|---|---|---|
| `ventana_util_s: [desde, hasta]` | en una línea | Acota qué tramo del clip puede usar el montaje. Sirve cuando un clip sale bien los dos primeros segundos y se estropea después: recortarlo a su parte buena no cuesta nada, regenerarlo cuesta un clip. |
| `modelos: {video, imagen, edit}` | raíz | Pisa los modelos por defecto. |
| `duracion_clip_s` | raíz | Segundos por clip. Con Seedance, de 4 a 12. **4 es el valor de casa**: más clips cortos dan más material real y mejor ritmo. |
| `modelos.resolucion` | raíz | `480p`/`720p`/`1080p`. Por defecto 1080p. Cambia el costo: Seedance cobra por tokens y éstos escalan con el área. |
| `musica.genero_prompt` · `ritmo_prompt` · `bpm_exacto` | raíz | Fijan el género y el tempo de la canción. Cuando están, mandan ellos; si no, se usa el default comercial (latin urban pop, +12 BPM). `bpm_exacto: true` respeta el BPM del guion tal cual. |
| `musica.duracion_ms` | raíz | Tope de duración que se le pide al modelo, **no** la duración pedida. Se da con margen (68000 para un ad de ~58s) para que la canción cierre sola en vez de cortarse. |
| `nicho_mapa` + `publico` | raíz | Alternativa a `nicho`: la serie de parrilla numerada (P01–P28) identifica su público así, con un índice y una descripción en texto. |
| `correcciones[]` · `prompts_previos` | raíz / línea | Qué se cambió después de aprobar, quién lo pidió y qué costó. |
| `costo_real_usd` · `duracion_real_s` · `render` | raíz | Los llena el productor al cerrar. |
