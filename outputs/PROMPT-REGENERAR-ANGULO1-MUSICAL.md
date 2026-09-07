# Prompt para Claude Code — regenerar el ángulo .1 (musical) de los 28 públicos

Pegar tal cual en Claude Code, dentro del repo `skills-video-ads`.
Este trabajo es **solo escritura**: no gasta un peso en fal/ElevenLabs.

---

```
Lee CLAUDE.md, ESTADO.md (última entrada), docs/FORMATO-GUION.md,
.claude/skills/microsituaciones/SKILL.md, .claude/skills/ganchos-y-retencion/SKILL.md,
.claude/skills/ritmo-y-montaje/SKILL.md, config/nichos/ y el lote actual
outputs/GUIONES-MUSICALES-28-publicos-angulo1.md.

TAREA: reescribir el lote completo del ángulo .1 de los 28 públicos. Sigue siendo musical
cantado (sin locución), pero el lote actual tiene un problema que hay que corregir: los 28
usan la MISMA estructura de canción (Verso 1 → Coro → Verso 2 → Coro → Puente → Outro) y las
mismas 12 escenas con los mismos beats. Se leen como el mismo video 28 veces.

NO PRODUZCAS NADA. No llames fal, ElevenLabs ni ffmpeg. No corras producir.py. Esto es solo
texto: documento + JSON. Cuando termines me lo muestras y yo decido qué se produce.

=== REGLA 1: la micro-situación aparece mínimo 3 veces, y las tres son distintas ===
No es repetir la misma frase tres veces. Son tres apariciones con función distinta:
  (a) CRUDA — la escena literal, al aire, en los primeros 5 segundos.
  (b) AGRAVADA — la misma escena otro día / con una vuelta más de tuerca / desde otro
      ángulo (lo que le dice alguien más, lo que él se dice, lo que ya le costó).
  (c) RESUELTA — la misma escena al final, invertida, ya con el mecanismo puesto.
Mínimo DOS de las tres tienen que verse en imagen, no solo cantarse: el espectador sin
sonido tiene que reconocer que es el mismo momento tres veces.
Construye primero la micro-situación de 7 pasos (skill microsituaciones) para cada público
usando su ángulo .1 real de config/nichos/. Sin micro-situación no hay letra.

=== REGLA 2: siete formatos de canción, cuatro públicos cada uno ===
Ningún formato puede repetir la estructura del documento actual ni la de los lotes .2 y .3
(outputs/GUIONES-PIXAR-28-angulo2.md, GUIONES-EQUIPO-AV-28-publicos.md,
GUIONES-SARA-28-formato-director-v2.md). Usa estos siete:

  F1 · PREGÓN Y RESPUESTA — una voz lanza el dolor, un coro le contesta. La micro-situación
       va en la llamada; la respuesta cambia las tres veces.
  F2 · CONTEO — la canción enumera (uno, dos, tres...) los intentos que ya hizo y fallaron;
       la micro-situación es el número que siempre se repite hasta que se rompe la cuenta.
  F3 · RELATO EN TERCERA — le canta la historia de alguien más ("hay un man que...") y solo
       al final se descubre que es el espectador.
  F4 · CARTA CANTADA — le canta a su yo de hace un año, o a su negocio, o al pedido que no
       llegó. Segunda persona todo el tiempo.
  F5 · CORO MUTANTE — el estribillo se repite tres veces con la misma melodía y letra
       distinta: primera vez el dolor, segunda la duda, tercera resuelto.
  F6 · DOS VOCES — el que pone excusas contra el que ya lo resolvió. Se interrumpen.
       La micro-situación se ve desde los dos lados.
  F7 · JINGLE-LOOP — una frase-gancho cortísima que vuelve como cuña de radio, con versos
       cortos entre repeticiones.

Reparte los 28 por AFINIDAD DEL DOLOR, no por rotación mecánica: los dolores de saturación
(WhatsApp, chats, pedidos) piden F2 o F7; los de vergüenza o estancamiento (sé mucho y nadie
me contrata, tengo local y no vendo) piden F3 o F4; los de excusa (me falta un curso más)
piden F6. Justifica en una línea por qué cada público quedó en su formato.

Varía además, por formato: BPM, si el CTA se canta o se habla al final, si el coro entra al
segundo 8 o al 15, el número de escenas (10 a 12, nunca más) y la duración final (30–60 s).
El estilo visual sigue rotando entre los siete del documento actual, pero NO puede coincidir
el mismo par (estilo visual + formato de canción) en dos públicos.

=== REGLA 3: lo que NO cambia ===
Datos verificables y solo esos: quince al diecinueve de octubre, Plaza Mayor Medellín,
más de trescientas cincuenta empresas, más de doscientas conferencias, más de doscientos
ponentes. «Sesenta mil personas» sigue en datos_sin_verificar: NO la metas en ninguna letra
hasta que Effix la confirme. Números en letras. Español neutro colombiano, nunca voseo.
Describir la situación, nunca a la persona. Sin descuentos, sin taller de IA. El CTA cierra
en compra. Texto en pantalla máximo siete palabras. Nunca prometer más días de los que da
el pase. Reglas de estilo visual: las del JSON y de src/estilos_especiales.py, verbatim.

=== REGLA 4: el documento se organiza por FORMATO, no por número de público ===
Siete secciones, una por formato, con los cuatro públicos adentro. Al inicio de cada sección:
qué hace ese formato y por qué esos cuatro dolores viven ahí. Fechas, cifras y CTA van dentro
de la historia, no como beats sueltos al final.

=== ENTREGABLES ===
1. outputs/GUIONES-MUSICALES-28-angulo1-v2.md — no sobreescribas el v1.
2. Los 28 JSON en scripts/guiones/ como *_v2_por-aprobar.json con el esquema de
   docs/FORMATO-GUION.md (formato `lineas`). Deja los actuales quietos.
3. Estimación de costo por video con cost_estimator y parámetros reales, y el total del lote.
4. Entrada fechada en ESTADO.md con las decisiones y el reparto de formatos.

=== PRUEBA ANTES DE ENTREGAR ===
Toma tres guiones al azar de secciones distintas, tápales el título y el nombre del público.
Si se pueden intercambiar sin que se note, el lote está mal: reescríbelos. Verifica también,
guion por guion, las tres apariciones de la micro-situación (cruda / agravada / resuelta) y
que al menos dos se vean en imagen. Muéstrame esa verificación en una tabla de 28 filas.
```

---

## Notas

- La frontera del repo sigue siendo la misma: lo creativo se decide con vos, Claude Code
  escribe y produce. Si preferís que las letras se escriban acá en Cowork y Claude Code solo
  arme los JSON, quitá del prompt el punto 1 de entregables y pasale el documento hecho.
- Costo de esta tarea: cero. La producción de los 28 sigue siendo ~127 USD y no se toca
  hasta que apruebes el v2.
