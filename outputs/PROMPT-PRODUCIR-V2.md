# Prompts de producción — musicales v2 (ángulo .1)

Para pegar en Claude Code, dentro del repo `skills-video-ads`. La parte creativa viene cerrada
desde Cowork: Claude Code **no reescribe** letra, planos ni prompts.

## A · Un solo video (empezar por aquí)

```
Lee CLAUDE.md, docs/FORMATO-GUION.md y la última entrada de ESTADO.md.

Produce scripts/guiones/effix_pixar_p01-empezar-musical_v2_por-aprobar.json

Antes de nada: lee el JSON completo y respétalo. La letra, los planos, los prompts de imagen y
video, el formato de canción y las tres apariciones de la micro-situación vienen cerrados desde
Cowork. No los reescribas, no los "mejores", no los completes con tu criterio. Si encuentras
algo que viola una regla del repo, PARA y dime qué línea y qué regla; no lo corrijas por tu
cuenta.

Pasos, parando en cada uno:

1. Renombra el archivo a _v2_aprobado.json y pon "estado": "aprobado". Nada más cambia.
2. Valida las 6 reglas de FORMATO-GUION.md y además: ningún prompt_video con slow/deliberate,
   todos cierran con "no discernible speech", texto_pantalla de 7 palabras o menos, texto_tts
   vacío (es modo musical_sync), y cada "texto" de línea existe literal en
   musica.suno_custom_lyrics.
3. Estima el costo con cost_estimator y parámetros reales: Seedance 1.5 Pro a 1080p, clips de
   4 s, imágenes con nano-banana-2, canción con el modelo del campo musica.modelo.
   Muéstrame el veredicto y ESPERA MI OK. Tope 6 USD, promedio 5.
4. Canción → whisper. Avísame y para si: no rima al oído, canta mal «Feria Effix» o «quince al
   diecinueve», no alcanza a cantar el outro (ahí va el CTA, es lo que más importa), o la intro
   instrumental pasa de 20 s. Regenerar cuesta 0,15 USD, así que me preguntas antes.
5. Héroe (imagen del personaje) → la reviso yo antes de seguir.
6. Escenas → clips → ritmo.py con los cortes en los golpes (librosa) → overlays Montserrat con
   texto_pantalla → mezcla.py con musica=False y −14 LUFS → render.
7. QA: duración entre 30 y 60 s, ningún plano por debajo de 1,25 s, y las tres apariciones de la
   micro-situación reconocibles en imagen — están en el campo microsituacion_apariciones del
   JSON, con el número de línea de cada una. Si alguna no se reconoce, dímelo antes de cerrar.
8. El mp4 se nombra con el campo nombre_entrega del JSON, que ya viene numerado por público
   (P01_, P02_…). Si guion_aprobado.nombre_de_entrega() no antepone ese número, ajústala y
   actualiza CLAUDE.md en el mismo commit.
9. Anota el costo real en logs/ y la entrega en ESTADO.md.
```

## B · Tanda de tres (después de que el primero salga bien)

```
Lee CLAUDE.md, docs/FORMATO-GUION.md y la última entrada de ESTADO.md.

Produce esta tanda de musicales v2, uno por uno, en este orden, sin empezar el siguiente hasta
cerrar el anterior:
  1. scripts/guiones/effix_skeleton_p02-pocas-ventas-musical_v2_por-aprobar.json
  2. scripts/guiones/effix_claymation_p04-whatsapp-musical_v2_por-aprobar.json
  3. scripts/guiones/effix_cyberpunk_p06-marca-digital-musical_v2_por-aprobar.json

Mismo procedimiento del primero: la parte creativa del JSON no se toca; renombrar a
_v2_aprobado.json con estado aprobado; validar las 6 reglas más las de arriba; estimar costo con
parámetros reales y esperar mi OK; fases separadas parando en canción y en héroe; QA de duración,
piso de plano y las tres apariciones de microsituacion_apariciones; nombrar el mp4 con
nombre_entrega; costo real en logs/ y entrega en ESTADO.md.

Cada estilo tiene reglas propias en su JSON (bible, negative_prompt, notas_produccion): el
productor las lee de ahí, no las inventa. Skeleton y crochet llevan su bible verbatim en todos
los prompts. Presupuesto 5 USD promedio, tope 6 por video.
```

Los siete v2 escritos hasta ahora:

```
effix_pixar_p01-empezar-musical_v2_por-aprobar.json            F6 dos voces
effix_skeleton_p02-pocas-ventas-musical_v2_por-aprobar.json    F7 jingle-loop
effix_claymation_p04-whatsapp-musical_v2_por-aprobar.json      F2 conteo
effix_cyberpunk_p06-marca-digital-musical_v2_por-aprobar.json  F4 carta cantada
effix_skeleton_p09-audiencia-ventas-musical_v2_por-aprobar.json F1 pregón y respuesta
effix_crochet_p10-consultor-clientes-musical_v2_por-aprobar.json F3 relato en tercera
effix_anime_p12-checkout-musical_v2_por-aprobar.json           F5 coro mutante
```
