---
name: director-estilos
description: Activa cuando el usuario menciona un estilo visual (crochet, skeleton, Zack Films, object talk, cyberpunk, etc.). Carga el template completo del estilo desde estilos_especiales.py y aplica todas sus reglas de producción a los prompts de imagen y video.
---

Regla: cada estilo tiene reglas de producción diferentes. NUNCA uses el template de
`ugc_realista` para generar prompts de crochet — los modelos de IA los interpretan
completamente distinto.

Módulo: `src/estilos_especiales.py` · `obtener(estilo)`

## Estilos con pipeline propio

| Estilo | Regla que NO se puede romper |
|---|---|
| `crochet` | El MUNDO es un diorama stop-motion, nunca "un personaje tejido". Universal positivo, negativo y cierre I2V se pegan VERBATIM. Sin poses de dedos. |
| `skeleton` | El Character Bible se pega palabra por palabra en todos los prompts. Cada imagen referencia la HÉROE, nunca la anterior. Cero texto en la generación. |
| `zack_films` | Los personajes nunca hablan en pantalla. Anotaciones = formas, no palabras. Verde revela, rojo advierte. |
| `micro_doc_ugc` | El personaje ACTÚA la micro-situación, no la describe. Prohibido: cinematic, professional, stunning, 8k, studio, perfect. |
| `object_talk` | El personaje se diseña ANTES del prompt. Una sola emoción dominante. Poses animation-ready. |

## Reglas transversales

- El bloque de audio de todo prompt cierra con `no discernible speech`: la voz siempre
  entra por ElevenLabs en post.
- Los textos universales de cada estilo son cadenas exactas. Cambiarles una palabra es
  lo que convierte un clip bueno en uno inservible.
- Tipo de clip: **A** (frame inicial, movimiento autocontenido), **B** (inicial + final,
  cambio de estado — el final es el estado ATERRIZADO, nunca a mitad de movimiento),
  **C** (inicial, movimiento mínimo). Ante la duda, A.
- Para agregar un estilo nuevo: una entrada en `ESTILOS_ESPECIALES`. El resto lo recoge solo.


---

## Ritmo, corte y sonido — los decide `ritmo-y-montaje`

Este archivo decide **qué se ve**. La skill transversal `ritmo-y-montaje` decide
**cada cuánto cambia y cómo suena**, para todos los ads sin importar el estilo:

- El corte visual cae cada **1.5–2.5s**, y los planos extra salen del mismo clip
  por reencuadre — no se generan clips nuevos para tener más ritmo.
- El aire entre réplicas son **0.12s**, la voz va a `speed 1.15`.
- **Todo ad lleva música de fondo**, de la librería del repo, con ducking real y
  el master a −14 LUFS.

Implementación: `src/ritmo.py` y `src/mezcla.py`.
