---
name: storyboard-director
description: Activa cuando el guión está aprobado y hay que producir el storyboard completo. Genera para cada beat: narración, overlay, prompt de imagen, prompt de video I2V, tipo de clip (A/B/C), notas de director y costo estimado.
---

Output: un HTML visual + un JSON ejecutable. El HTML es para que Alexander apruebe.
El JSON es lo que consume el pipeline de generación.

Módulo: `src/storyboard_director.py` · `StoryboardDirector().generar(beats, estilo, marca)`

## Ficha de cada beat

- Número, nombre y emoción del beat
- Componente de micro-situación que está activando
- Narración para ElevenLabs (máx. 11 palabras por beat de 4s — 2.2 palabras/segundo)
- Texto en pantalla (máx. 7 palabras)
- Prompt de imagen base, con las reglas del estilo aplicadas
- Prompt de video I2V
- Tipo de clip A / B / C
- Notas de director: una frase con la decisión creativa y su porqué
- Modelos recomendados y costo estimado

## Antes de entregar

- Si la micro-situación trae `datos_sin_verificar`, el HTML los muestra arriba en rojo.
  No se produce hasta confirmarlos con la fuente.
- El costo se muestra como "SIN CALCULAR" mientras `config/costos.json` tenga
  `verificado: false`. Nunca inventar una tarifa.
- Ningún prompt lleva texto en pantalla quemado: los subtítulos van en el editor.
