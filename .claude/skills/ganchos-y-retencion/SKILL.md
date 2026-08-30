---
name: ganchos-y-retencion
description: Sistema transversal de ganchos, retención y contenido que conecta, para las tres marcas de Alexander (@alexemprendee, @militougc, @kreoon.latam), Feria Effix y clientes de agencia. Contiene las seis categorías reales de hook cruzadas de 14 taxonomías, el marco de niveles de conciencia que decide cuál usar, las reglas de calibración con evidencia medida, la mecánica de retención según la documentación oficial de cada plataforma, y los mitos verificados como falsos. Usa esta skill SIEMPRE que haya que escribir un gancho, abrir un video, diagnosticar por qué un creativo no retiene, elegir entre alcance y conversión, auditar un guion existente, o cuando alguien pida "hooks", "ganchos", "que enganche más", "por qué no retiene" o "hazlo más viral". Es la capa de método: las skills de formato la consultan antes de escribir.
---

# Ganchos y retención — el método

Cruce de **14 taxonomías de hooks** (Hormozi, Brendan Kane, Dan Koe, Justin Welsh,
Cole & Bush, Caples, Ogilvy, Schwartz, MrBeast, Galloway, vidIQ y los referentes en
español), documentación oficial de Instagram, TikTok, YouTube y Meta, y literatura
académica de persuasión narrativa y vínculo parasocial.

**Banco de 320 ganchos:** `references/banco-320.md` · versión ejecutable:
`config/banco_ganchos.json` + `src/ganchos.py`

---

## REGLA CERO — la decisión que va antes de escribir

**No se elige el gancho. Se elige el nivel de conciencia, y el nivel decide el
gancho.** (Eugene Schwartz, 1966. Hormozi construyó su taxonomía de 2025 encima.)

| Nivel | Dónde está la persona | Categoría que sirve | Qué NO usar |
|---|---|---|---|
| **unaware** | No sabe que tiene el problema | Curiosidad · Historia · Contrarian | Oferta, precio, escasez |
| **problem** | Siente el dolor, no conoce la solución | Dolor nombrado · Callout | Detalles de producto |
| **solution** | Sabe que existe un tipo de solución | Promesa con plazo · Especificidad | Curiosidad vaga |
| **product** | Te conoce, duda entre opciones | Prueba · Defecto admitido | Educación básica |
| **most aware** | Ya quiere, falta el empujón | Oferta · Escasez · Plazo | **Curiosidad — tira la impresión** |

**Segunda pregunta, igual de obligatoria: ¿este creativo ALCANZA o CIERRA?**
- **Alcanzar** → curiosidad, contrarian, historia. Aceptá CTR alto con CPA feo: es el precio.
- **Cerrar** → callout, dolor nombrado, promesa con plazo, prueba, especificidad. **Nunca curiosidad.**

---

## LAS SEIS CATEGORÍAS (+2)

1. **Brecha de curiosidad** — *"El problema de tu tienda no está en la tienda."*
2. **Callout de identidad** — *"Esto es para el que ya vendió, ya cobró y al final del mes no le quedó nada."*
3. **Dolor nombrado** (con hora y lugar) — *"Son las once de la noche y todavía estás contestando '¿es contraentrega?' por WhatsApp."*
4. **Promesa con plazo y sin sacrificio** — *"Dame siete días y salís con un producto validado, sin renunciar al trabajo que tenés hoy."*
5. **Contrarian** — *"Nadie compra contraentrega porque confíe en vos. Compra porque no confía."*
6. **Especificidad numérica** — *"El CTR pasó de 0,7% a 2,4%. La foto era la misma."*
7. **Prueba / autoridad** — la que el espectador verifica solo. *"No me creas a mí. Abrí la biblioteca de anuncios de Meta."*
8. **Historia / entrada en escena** — *"Eran las once y media de la noche y el cliente me escribió que no le había llegado el pedido. Tenía razón."*

**Toda lista de "100 hooks" es una de estas seis rellenada con sinónimos.**

---

## LAS CUATRO REGLAS DE CALIBRACIÓN

**1. Dolor concreto sí, miedo genérico no.** Caples lo midió con cupones en 1932:
*"DO YOU MAKE THESE MISTAKES IN ENGLISH?"* ganó; *"ARE YOU AFRAID OF MAKING
MISTAKES?"* perdió. **Si tu dolor no se puede filmar, no es dolor nombrado.**

**2. Curiosidad y contrarian ganan alcance y pierden compradores.** Caples —el
único clásico con datos de conversión— puso la curiosidad última. Los modernos la
ponen primera porque optimizan retención algorítmica, no venta.

**3. La precisión implausible es el mecanismo, no el número.** $847.300 funciona y
"casi ochocientos mil" no. **Si redondeás, perdés la categoría entera.**

**4. El sacrificio negado es el componente que casi todos omiten** y el que más
levanta la conversión. Resultado + plazo + *"sin tener que [X]"*.

---

## EL 79% QUE NO ES EL GANCHO

**El gancho explica el 21% de la variación en conversión en ecommerce** (Meta
Platforms + Universidad de Maryland, ~220.000 videos publicitarios; automóvil 0,66,
CPG 0,50). Optimizarlo al infinito tiene rendimientos decrecientes rápidos.

Lo que explica el resto:

- **Marca y mensaje en los primeros 5 segundos: 1,7x más intención de compra**
  (Meta + Toluna). Branding distribuido, no solo al final: 1,8x. **No retrases la marca.**
- **La historia apaga la contraargumentación: ρ = −.20.** No convence más —
  desactiva el modo defensa.
- **Narrativo r = .39 vs analítico r = .24** (N = 54.715).
- Tres ingredientes del transporte: **trama imaginable (ρ=.29), verosimilitud
  (ρ=.27), personaje identificable (ρ=.20)**. En la práctica: complicación antes
  del segundo 12, detalles no redondos, protagonista = un cliente, no la marca.
- **El defecto va al final y débil** (blemishing, Ein-Gar 2012). Al principio anula
  el efecto; grave, lo revierte.
- **Mostrar fracasos funciona en cuentas grandes, no en chicas** (Ye & Li 2025:
  efecto con 813.000 seguidores, nulo con 14.000).

---

## LOS TRES DIAGNÓSTICOS

**Test ABT.** Leé el guion en voz alta. Si podés unir las frases con *"y… y… y…"*,
no tenés historia. Falta un **PERO** explícito antes del segundo 12.

**Test de blemishing.** ¿Dónde está el defecto? Antes del positivo → movelo.
Grave → cambialo. No hay → agregá uno trivial.

**Test de homofilia.** En los primeros 5 segundos, ¿nombraste la situación del
espectador o hablaste de vos? Si es lo segundo, perdiste el predictor más fuerte.

---

## MITOS QUE NO USAMOS (y hay que corregir si alguien los cita)

| Mito | Realidad |
|---|---|
| "Tenés 3 segundos" | Nació como umbral de **facturación** de Facebook, no de atención. TikTok dice **6 segundos** |
| "La atención dura 8 segundos" | Microsoft Canadá 2015, sin fuente verificable. El dato real (Gloria Mark) es 47s y es sobre multitarea |
| "Los loops abiertos funcionan por Zeigarnik" | Metaanálisis 2025, 59 publicaciones: **ratio 0,99, ninguna ventaja de memoria** |
| "Las historias liberan oxitocina" | El laboratorio de Zak excluyó esos datos. **No decirlo en una presentación** |
| "El 85% se ve sin sonido" | Digiday 2016, auto-reportado. Hoy: **88% de usuarios de TikTok dicen que el sonido es vital** |
| "Los subtítulos suben las vistas 80%" | El único experimento controlado midió **+7,32%** |
| "El loop perfecto multiplica vistas" | Cero fuentes primarias. YouTube: los replays **no afectan la promoción** |
| "Tengo la cuenta quemada" | TikTok, textual: ni seguidores ni rendimiento previo son factores directos |
| "Videos más largos acumulan watch time" | Los recomendadores corrigen el *duration bias*. **En Reels el pico está en 30–60s** |

---

## QUÉ MIDE CADA PLATAFORMA (según ellas)

- **Instagram** — orden textual del blog oficial para Reels: *compartir → ver
  completo → like → ir al audio*. Mosseri (ene. 2025): watch time, likes, sends.
- **TikTok** — terminar un video largo es señal **fuerte**. Gancho en los primeros
  **6 segundos**, 5–10 palabras por segundo en texto, 3–5 creativos por grupo.
- **YouTube Shorts** — métrica: *"Viewed vs. Swiped away"*. El umbral en segundos
  **no está documentado**.
- **Meta** — con Andromeda el sistema elige entre decenas de millones de
  candidatos. **Volumen y diversidad creativa importan más que antes.**
- **Benchmark honesto:** skip rate real de **60–65%** en 140.000 Reels de empresa.
  Los benchmarks públicos de hook rate no tienen dataset.

---

## VOZ POR MARCA

- **@alexemprendee** — autoridad serena paisa, cero hype de gurú. "Parce" y
  "hagámosle" caben; la euforia gritada no. Todo beneficio se traduce a plata,
  tiempo o clientes.
- **@militougc** — creíble, cálida, profesional. Doble audiencia: marcas que
  contratan y creadoras. Nunca infantilizar. Cero promesas médicas sobre piel.
- **@kreoon.latam** — dual marcas/creadores. El gancho habla de producción y
  resultado, no de la herramienta.
- **Feria Effix** — el avatar del evento (emprendedor de ecommerce LATAM que
  factura entre mil y cinco mil al mes) **coincide con el de @alexemprendee**. Los
  ganchos de esa columna del banco aplican casi directo; los de @militougc no.
- **Clientes de agencia** — plantillas genéricas, rellenando los `[corchetes]` con
  datos reales. Nunca inventarlos.

---

## FLUJO DE TRABAJO

1. Nivel de conciencia → categoría.
2. Alcance o conversión → filtra candidatos.
3. Abrir `references/banco-320.md` (o `src/ganchos.py` para filtrar por código).
4. Adaptar el gancho a un hecho real. **Sin hecho, no hay gancho.**
5. Verificar los tres diagnósticos sobre el guion completo.
6. Producir 3–5 ganchos distintos por creativo, no variaciones del mismo.
7. Revisar riesgos: cifras inventadas (Ley 1480), atributos personales del
   espectador (política de Meta), promesas de retorno económico.

## INTEGRACIÓN EN ESTE PROYECTO

- `src/ganchos.py` — el método en código: filtra el banco por nivel y objetivo,
  y corre los validadores sobre un guión ya escrito.
- `src/microsituaciones.py` — cada micro-situación declara su nivel de conciencia
  y su objetivo; los hooks se validan contra estas reglas.
- `scripts/test_integracion_creativa.py` — los validadores corren en cada prueba.
