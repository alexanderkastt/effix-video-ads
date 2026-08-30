"""Framework de micro-situaciones — 7 pasos hacia "ese soy literalmente yo".

Basado en la guía de micro-situaciones. La tesis: un anuncio no falla por elegir
mal el ángulo, sino por describir el problema de forma demasiado amplia. "Tienes
poca energía" es débil porque el cliente ya conoce el síntoma. Lo que detiene el
scroll es el momento EXACTO en que el problema se vuelve real.

    MICRO-SITUACIÓN → SÍNTOMA → REACCIÓN INTERNA → EXPLICACIÓN FALLIDA
    → RECONOCIMIENTO DEL PATRÓN → CAUSA RAÍZ → MECANISMO

Cada paso existe por una razón psicológica concreta:

1. Momento      — reconocimiento antes que explicación. El reconocimiento te da
                  el derecho de explicar.
2. Síntoma      — lenguaje concreto y observable, no la etiqueta abstracta.
3. Reacción     — el pensamiento real que la persona ya tiene, sin dramatismo.
4. Expl. fallida— alineación de creencias. Ignorar lo que ya cree sube su
                  resistencia al cambio.
5. Patrón       — un mal día es azar; la repetición abre el bucle.
6. Causa raíz   — sustitución de creencia. Va aquí, no al principio.
7. Mecanismo    — claridad causal: por qué esta solución tiene sentido.

⚠️ ERROR 3 DE LA GUÍA: "Inventar situaciones hiperespecíficas falsas. La
especificidad solo funciona cuando la situación es real." Por eso cada
micro-situación declara sus `datos_sin_verificar`: las cifras que hay que
confirmar con Effix antes de publicar. `auditar_datos()` las lista.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Any

from .narracion_hablada import (
    HABLADO, PASE_POR_DEFECTO, cta_de, hablado_de, validar_coherencia_de_pase,
)
from .paths import load_brand_dna

# ---------------------------------------------------------------------------
# Mapeo de los 7 componentes a los 11 beats
# ---------------------------------------------------------------------------

MAPEO_BEATS: list[dict[str, str]] = [
    {"n": 1,  "nombre": "MOMENTO",        "campo": "momento",             "emocion": "interrupcion_patron", "emoji": "🪝"},
    {"n": 2,  "nombre": "SÍNTOMA",        "campo": "sintoma",             "emocion": "auto_relevancia",     "emoji": "🫵"},
    {"n": 3,  "nombre": "REACCIÓN",       "campo": "reaccion_interna",    "emocion": "identificacion",      "emoji": "😔"},
    {"n": 4,  "nombre": "EXPL. FALLIDA",  "campo": "explicacion_fallida", "emocion": "reduccion_resistencia", "emoji": "🤷"},
    {"n": 5,  "nombre": "PATRÓN",         "campo": "patron",              "emocion": "tension",             "emoji": "🔁"},
    {"n": 6,  "nombre": "CAUSA RAÍZ",     "campo": "causa_raiz",          "emocion": "cambio_creencia",     "emoji": "💡"},
    {"n": 7,  "nombre": "MECANISMO",      "campo": "mecanismo",           "emocion": "claridad",            "emoji": "⚙️"},
    {"n": 8,  "nombre": "PRUEBA SOCIAL",  "campo": "prueba_social",       "emocion": "confianza",           "emoji": "🤝"},
    {"n": 9,  "nombre": "VISUALIZACIÓN",  "campo": "visualizacion",       "emocion": "aspiracion",          "emoji": "🎬"},
    {"n": 10, "nombre": "URGENCIA + CTA", "campo": "urgencia_cta",        "emocion": "oportunidad",         "emoji": "🎟️"},
    {"n": 11, "nombre": "DEFECTO",        "campo": "defecto_admitido",    "emocion": "honestidad",          "emoji": "🫱"},
    {"n": 12, "nombre": "LOOP",           "campo": "loop_rewatch",        "emocion": "pertenencia",         "emoji": "♻️"},
]

# Ritmo de locución en español medido en MASTER_CONTEXT.md
PALABRAS_POR_SEGUNDO = 2.2

MOVIMIENTO_POR_BEAT = {
    1: "closeup", 2: "handheld", 3: "static", 4: "handheld", 5: "dolly-in",
    6: "closeup", 7: "dolly-in", 8: "pan", 9: "pan", 10: "closeup",
    11: "static", 12: "handheld",
}


@dataclass
class MicroSituacion:
    """Los 7 componentes que construyen relevancia real en un ad.

    Cada campo es una capa de reconocimiento progresivo. Los cuatro campos de
    cierre (prueba social, visualización, CTA y loop) no son parte del framework
    original: completan el guión de 11 beats del Video Factory.
    """

    # --- los 7 del framework ---
    momento: str
    sintoma: str
    reaccion_interna: str
    explicacion_fallida: str
    patron: str
    causa_raiz: str
    mecanismo: str

    # --- cierre del ad ---
    prueba_social: str = ""
    visualizacion: str = ""
    urgencia_cta: str = ""
    defecto_admitido: str = ""
    loop_rewatch: str = ""

    # --- metadatos ---
    angulo: str = ""
    etiqueta: str = ""
    ancla: str = ""
    overlays: list[str] = field(default_factory=list)
    hooks_escritos: list[dict[str, Any]] = field(default_factory=list)
    datos_sin_verificar: list[str] = field(default_factory=list)

    # -- hooks --------------------------------------------------------------

    def generar_hooks(self, n_variantes: int = 3) -> dict[str, dict[str, Any]]:
        """Variantes de hook construidas alrededor del MISMO momento.

        La guía es explícita: una micro-situación potente admite varias entradas
        al mismo momento, y eso es exactamente lo que se prueba en A/B. Cada hook
        apila dos gatillos, va en máximo 14 palabras habladas, y el overlay en
        máximo 7 — tiene que funcionar sin sonido.

        Nada de saludos, logos ni frases de calentamiento.
        """
        salida: dict[str, dict[str, Any]] = {}
        for i, hook in enumerate(self.hooks_escritos[: max(1, n_variantes)]):
            salida[f"variante_{chr(ord('A') + i)}"] = {
                "hablado": hook["hablado"],
                "gatillos": hook["gatillos"],
                "overlay": hook["overlay"],
                "palabras": len(hook["hablado"].split()),
            }
        return salida

    # -- expansión a beats --------------------------------------------------

    def beat_a_beats_con_microsituacion(
        self,
        n_beats: int = 12,
        duracion_beat: int = 4,
        hook_variante: str = "A",
        pase: str = PASE_POR_DEFECTO,
    ) -> list[dict[str, Any]]:
        """Expande la micro-situación al guión de 11 beats.

        El beat 01 usa el hook elegido, no el campo `momento` en crudo: el
        momento es material de investigación, el hook es su versión hablada.
        """
        hooks = self.generar_hooks()
        clave = f"variante_{hook_variante}"
        elegido = hooks.get(clave) or next(iter(hooks.values()))

        # La versión hablada es la que se locuta; los campos largos de la
        # micro-situación se quedan como investigación, dentro del beat.
        hablado = hablado_de(self.angulo) if self.angulo in HABLADO else []

        beats: list[dict[str, Any]] = []
        for meta in MAPEO_BEATS[: min(n_beats, len(MAPEO_BEATS))]:
            n = meta["n"]
            investigacion = getattr(self, meta["campo"], "") or ""

            if hablado:
                narracion = hablado[n - 1]
                # El beat 10 es el único que depende del producto: el evento
                # dura cinco días pero el pase principal da acceso a tres.
                if n == 10:
                    narracion = cta_de(pase)["hablado"]
            elif n == 1:
                narracion = elegido["hablado"]
            else:
                narracion = investigacion

            if n == 1:
                overlay = elegido["overlay"]
            elif n == 10 and hablado:
                overlay = cta_de(pase)["overlay"]
            else:
                overlay = self.overlays[n - 1] if len(self.overlays) >= n else ""

            # Lo que el texto dura de verdad, a 2.2 palabras/segundo en español.
            # Se guarda aparte de `duracion_s` (el objetivo) para que el desajuste
            # sea visible en vez de descubrirse en el montaje.
            locucion_s = round(len(narracion.split()) / PALABRAS_POR_SEGUNDO, 1)

            beats.append(
                {
                    "beat": n,
                    "duracion_s": duracion_beat,
                    "duracion_locucion_s": locucion_s,
                    "cabe_en_el_beat": locucion_s <= duracion_beat,
                    "nombre": meta["nombre"],
                    "emocion": meta["emocion"],
                    "emoji": meta["emoji"],
                    "componente_microsituacion": meta["campo"],
                    "narracion": narracion,
                    "palabras_narracion": len(narracion.split()),
                    "investigacion": investigacion,
                    "texto_pantalla": overlay,
                    "movimiento_camara": MOVIMIENTO_POR_BEAT[n],
                    "descripcion_visual": "",   # lo llena el director de escena
                    "prompt_imagen": "",
                    "prompt_video": "",
                    "tipo_clip": "",
                    "notas_produccion": "",
                }
            )
        return beats

    # -- plan de duración ---------------------------------------------------

    def plan_de_duracion(self, duracion_beat: int = 4, n_beats: int = 12) -> dict[str, Any]:
        """Contrasta lo que dura la locución contra el formato objetivo.

        Existe una tensión de diseño que conviene ver antes de producir: una
        micro-situación bien escrita es específica, y la especificidad ocupa
        palabras. Meterla en beats de 4s obliga a recortar justo el detalle que
        la hace funcionar.

        Devuelve el diagnóstico y la duración por beat que sí cabría.
        """
        beats = self.beat_a_beats_con_microsituacion(n_beats, duracion_beat)
        total_palabras = sum(b["palabras_narracion"] for b in beats)
        locucion_s = round(total_palabras / PALABRAS_POR_SEGUNDO, 1)
        objetivo_s = len(beats) * duracion_beat

        desbordan = [b["beat"] for b in beats if not b["cabe_en_el_beat"]]
        pico = max((b["duracion_locucion_s"] for b in beats), default=0)

        # La duración útil por clip sale del PROMEDIO, no del pico: dimensionar
        # los once clips por el beat más largo infla el video sin necesidad.
        # Los beats que sigan desbordando a esa duración se acortan uno a uno.
        sugerida = max(duracion_beat, int(-(-locucion_s // len(beats))))
        siguen_largos = [
            b["beat"] for b in beats if b["duracion_locucion_s"] > sugerida
        ]
        palabras_a_recortar = max(
            0, total_palabras - int(objetivo_s * PALABRAS_POR_SEGUNDO)
        )

        return {
            "palabras": total_palabras,
            "locucion_s": locucion_s,
            "objetivo_s": objetivo_s,
            "beats_que_desbordan": desbordan,
            "duracion_beat_sugerida": sugerida,
            "duracion_total_sugerida": sugerida * len(beats),
            "beats_a_acortar_aun_asi": siguen_largos,
            "pico_s": pico,
            "palabras_a_recortar_para_44s": palabras_a_recortar,
            "cabe": not desbordan,
            "recomendacion": (
                f"Cabe en el formato de {duracion_beat}s por beat."
                if not desbordan
                else (
                    f"NO cabe: la locución dura {locucion_s}s y el formato da {objetivo_s}s. "
                    f"Opciones: "
                    f"(a) subir a {sugerida}s por clip — {len(beats)} x {sugerida}s = "
                    f"{sugerida * len(beats)}s, y acortar los beats {siguen_largos or 'ninguno'}; "
                    f"(b) mantener {duracion_beat}s y recortar {palabras_a_recortar} palabras, "
                    f"sabiendo que ahí se pierde la especificidad que hace funcionar la "
                    f"micro-situación; "
                    f"(c) partir el guión en dos piezas."
                )
            ),
        }

    # -- auditoría de datos -------------------------------------------------

    def auditar_datos(self) -> list[str]:
        """Lista las cifras que aparecen en el texto y no están confirmadas.

        La guía lo marca como Error 3: la especificidad solo funciona cuando la
        situación es real. Una cifra inventada que suena bien es exactamente el
        tipo de detalle que destruye la credibilidad si alguien la comprueba.
        """
        hallazgos: list[str] = []
        campos = [
            "momento", "sintoma", "reaccion_interna", "explicacion_fallida",
            "patron", "causa_raiz", "mecanismo", "prueba_social",
            "visualizacion", "urgencia_cta", "loop_rewatch",
        ]
        for campo in campos:
            texto = getattr(self, campo, "") or ""
            for cifra in re.findall(r"\b\d[\d.,]*\s*%?\b", texto):
                hallazgos.append(f"{campo}: '{cifra.strip()}'")
        return hallazgos


# ---------------------------------------------------------------------------
# Micro-situaciones de Feria Effix
# ---------------------------------------------------------------------------

# Cifras que aparecen en los textos y NO están verificadas contra datos de Effix.
# Se declaran aquí para que nadie las publique creyendo que son oficiales.
_SIN_VERIFICAR = {
    "comunidad_que_no_tienes": [
        "'facturando 3 veces lo tuyo' — ilustrativo, no es un dato medido",
    ],
    "no_esta_en_cursos": [
        "'18 meses' — plazo ilustrativo del avatar, no medido",
        "'el tercero este año' — ilustrativo",
    ],
    "competencia_va": [
        "'400 personas de tu competencia ya compraron' — no confirmado por Effix",
    ],
    "herramientas": [],
    "proveedores": [],
    "latam_unido": [],
    "de_cero_a_referente": [],
    "por_que_octubre": [],
}


_MICROS: dict[str, dict[str, Any]] = {
    "comunidad_que_no_tienes": {
        "ancla": "solo",
        "momento": "Son las 11 de la noche, ves el resultado de otra tienda en el grupo de Facebook — están facturando 3 veces lo tuyo con el mismo producto — y cierras el teléfono",
        "sintoma": "No es envidia exactamente. Es esa sensación de que alguien sabe algo que tú no sabes y no sabes dónde encontrarlo",
        "reaccion_interna": "Te preguntas si estás haciendo algo mal o si simplemente no tuviste acceso a las personas correctas",
        "explicacion_fallida": "Dices que es suerte. O que ellos tuvieron más capital inicial. O que su mercado es diferente.",
        "patron": "Pero llevas meses viendo ese patrón: los que crecen rápido siempre tienen a alguien que ya lo hizo antes.",
        "causa_raiz": "No es capital ni suerte. Es acceso. A quién conoces, qué conversaciones tienes, qué ves primero.",
        "mecanismo": "En Feria Effix hay más de 350 empresas y 200 ponentes. En tres días podés tener más conversaciones útiles que en dos años solo.",
        "prueba_social": "Cinco países ya confirmaron. Colombia, Ecuador, República Dominicana, Costa Rica y Guatemala.",
        "visualizacion": "Imagínate saliendo el domingo con tres contactos que sí te devuelven el mensaje.",
        "urgencia_cta": "Del quince al diecinueve de octubre, Plaza Mayor. Con el código EFFIX veinte entras con veinte por ciento menos.",
        "defecto_admitido": "No es barato. Y no es para principiantes.",
        "loop_rewatch": "Y esa noche, a las once, ya no eres el que mira el grupo desde afuera.",
        "overlays": [
            "El acceso que no tienes",
            "Alguien sabe algo que tú no",
            "¿Lo estoy haciendo mal?",
            "No es suerte ni capital",
            "Siempre tienen a alguien",
            "Es acceso, no dinero",
            "Cinco días de conversaciones",
            "Cinco países confirmados",
            "Sales con la agenda llena",
            "15–19 oct · Código EFFIX20",
            "No es barato",
            "Ya no miras desde afuera",
        ],
        "hooks": [
            {
                "hablado": "¿Por qué los que crecen rápido siempre conocen a alguien que ya lo hizo?",
                "gatillos": ["curiosidad", "auto_relevancia"],
                "overlay": "El acceso que no tienes",
            },
            {
                "hablado": "El problema no es tu producto. Es con quién lo estás construyendo.",
                "gatillos": ["interrupcion_patron", "auto_relevancia"],
                "overlay": "¿Con quién construyes?",
            },
            {
                "hablado": "Hay información que no está en YouTube. Está en una conversación.",
                "gatillos": ["curiosidad", "activacion_emocional"],
                "overlay": "Lo que no está en cursos",
            },
        ],
    },
    "no_esta_en_cursos": {
        "ancla": "curso",
        "momento": "Terminas otro curso de ecommerce — el tercero este año — y abres tu dashboard de Shopify. Los números son exactamente iguales.",
        "sintoma": "El curso decía exactamente lo que necesitabas. Lo entendiste. Tomaste notas. Pero algo entre entender y ejecutar no está funcionando.",
        "reaccion_interna": "Una parte de ti empieza a pensar que el problema eres tú, no los cursos.",
        "explicacion_fallida": "Dices que necesitas otro curso, más específico. O que necesitas más tiempo. O que el mercado cambió.",
        "patron": "Pero llevas 18 meses y el patrón es siempre el mismo: aprendes, intentas, te atascas en algo que ningún video de YouTube tiene.",
        "causa_raiz": "Los cursos enseñan teoría validada. Lo que necesitas es alguien que está resolviendo el mismo problema AHORA en tu mismo mercado.",
        "mecanismo": "Feria Effix no es un curso. Son 5 días con las personas que están resolviendo lo que tú estás resolviendo, en tiempo real.",
        "prueba_social": "Cinco países en el mismo salón, del quince al diecinueve de octubre.",
        "visualizacion": "Imagínate preguntando en voz alta y que tres personas te respondan de una.",
        "urgencia_cta": "Plaza Mayor, Medellín. Con el código EFFIX veinte te queda veinte por ciento menos.",
        "defecto_admitido": "No te damos plantillas. Son conversaciones.",
        "loop_rewatch": "Y el próximo curso que abras va a ser para repasar, no para buscar la respuesta.",
        "overlays": [
            "Otro curso, mismos números",
            "Entender no es ejecutar",
            "¿El problema soy yo?",
            "No necesitas otro curso",
            "Aprendes, intentas, te atascas",
            "Teoría vs. tiempo real",
            "No es un curso",
            "Cinco países, cinco días",
            "Preguntas y te responden",
            "15–19 oct · Código EFFIX20",
            "Sin plantillas",
            "Ahora es para repasar",
        ],
        "hooks": [
            {
                "hablado": "¿Cuántos cursos llevas y el dashboard sigue diciendo lo mismo?",
                "gatillos": ["auto_relevancia", "curiosidad"],
                "overlay": "Otro curso, mismos números",
            },
            {
                "hablado": "El curso no era el problema. Nunca lo fue.",
                "gatillos": ["interrupcion_patron", "curiosidad"],
                "overlay": "No era el curso",
            },
            {
                "hablado": "Hay preguntas que ningún video de YouTube te responde.",
                "gatillos": ["curiosidad", "activacion_emocional"],
                "overlay": "Lo que YouTube no responde",
            },
        ],
    },
    "competencia_va": {
        "ancla": "competencia",
        "momento": "Octubre va a terminar. Y mientras tú decides si ir o no, 400 personas de tu competencia ya compraron su entrada.",
        "sintoma": "No es que ellos sean mejores. Es que van a tener una conversación que tú no vas a tener. Van a ver algo que tú no vas a ver.",
        "reaccion_interna": "Ya sientes que el mercado se mueve más rápido de lo que puedes seguir. Y la brecha se hace más grande cada mes.",
        "explicacion_fallida": "Dices que el evento es caro. Que puedes aprender lo mismo en YouTube. Que no es el momento.",
        "patron": "Pero cada evento al que no fuiste te dejó sin la conexión o el dato que alguien que sí fue consiguió ese fin de semana.",
        "causa_raiz": "La información está en internet. Las relaciones y el contexto en tiempo real, no.",
        "mecanismo": "Con el código EFFIX20 la entrada cuesta menos que un mes de cursos. La pregunta no es si puedes pagarlo — es si puedes pagarte no ir.",
        "prueba_social": "Cinco países confirmados: Colombia, Ecuador, República Dominicana, Costa Rica y Guatemala.",
        "visualizacion": "Imagínate en noviembre, contando lo que trajiste, en vez de preguntando qué pasó.",
        "urgencia_cta": "Del quince al diecinueve de octubre, en Plaza Mayor. Código EFFIX veinte.",
        "defecto_admitido": "Son cinco días. Hay que sacar la agenda.",
        "loop_rewatch": "Y en octubre tu competencia no va a ser la única que estuvo.",
        "overlays": [
            "Ellos ya reservaron",
            "Van a ver lo que tú no",
            "La brecha crece cada mes",
            "\"Está caro\" · \"No es el momento\"",
            "Cada evento perdido cuesta",
            "El contexto no está en Google",
            "Menos que un mes de cursos",
            "Cinco países confirmados",
            "Noviembre: tú contando",
            "15–19 oct · Código EFFIX20",
            "Cinco días de agenda",
            "No serán los únicos",
        ],
        "hooks": [
            {
                "hablado": "¿Sabes cuántos de tu competencia ya reservaron para octubre?",
                "gatillos": ["curiosidad", "FOMO"],
                "overlay": "Ellos ya reservaron",
            },
            {
                "hablado": "Tu competencia no está mejor. Está mejor acompañada.",
                "gatillos": ["interrupcion_patron", "auto_relevancia"],
                "overlay": "Mejor acompañada",
            },
            {
                "hablado": "La pregunta no es si puedes pagarlo. Es si puedes no ir.",
                "gatillos": ["interrupcion_patron", "activacion_emocional"],
                "overlay": "¿Puedes NO ir?",
            },
        ],
    },
    "proveedores": {
        "ancla": "proveedor",
        "momento": "Le escribes al proveedor un martes y te responde el viernes. Ya perdiste la campaña que ibas a lanzar el fin de semana.",
        "sintoma": "No sabes si el producto es bueno hasta que llega. Y para cuando llega, ya pagaste el envío y el mes.",
        "reaccion_interna": "Empiezas a desconfiar de todos, y esa desconfianza te frena para pedir cantidades que sí te darían margen.",
        "explicacion_fallida": "Dices que te tocó un mal proveedor. Que la próxima vez vas a pedir muestras. Que hay que tener paciencia.",
        "patron": "Pero cada trimestre repites el mismo ciclo: buscas, arriesgas, te falla, vuelves a buscar.",
        "causa_raiz": "El problema no es el proveedor. Es que lo estás eligiendo por foto, sin verle la cara ni tocar el producto.",
        "mecanismo": "En Feria Effix los proveedores están en stands, con muestras físicas, y respondes tus dudas ahí mismo.",
        "prueba_social": "Cinco países en el mismo recinto: Colombia, Ecuador, República Dominicana, Costa Rica y Guatemala.",
        "visualizacion": "Imagínate cerrando con alguien después de tenerle el producto en la mano.",
        "urgencia_cta": "Del quince al diecinueve de octubre, Plaza Mayor. Código EFFIX veinte, veinte por ciento menos.",
        "defecto_admitido": "No todos los stands te van a servir.",
        "loop_rewatch": "Y el próximo martes que escribas, ya sabes quién te va a contestar.",
        "overlays": [
            "Respondió el viernes",
            "No sabes si sirve hasta que llega",
            "Ya no confías en nadie",
            "\"Me tocó uno malo\"",
            "Cada trimestre, lo mismo",
            "Lo eliges por foto",
            "Stands y muestras físicas",
            "Cinco países confirmados",
            "Cierras con el producto en mano",
            "15–19 oct · Código EFFIX20",
            "No todos te sirven",
            "Ya sabes quién contesta",
        ],
        "hooks": [
            {
                "hablado": "¿Cuántas veces te ha respondido un proveedor tres días después?",
                "gatillos": ["auto_relevancia", "curiosidad"],
                "overlay": "Respondió el viernes",
            },
            {
                "hablado": "Un mal proveedor no te cuesta plata. Te cuesta el trimestre.",
                "gatillos": ["interrupcion_patron", "activacion_emocional"],
                "overlay": "Te cuesta el trimestre",
            },
            {
                "hablado": "Estás eligiendo proveedor por foto. Como quien compra a ciegas.",
                "gatillos": ["interrupcion_patron", "auto_relevancia"],
                "overlay": "Lo eliges por foto",
            },
        ],
    },
    "latam_unido": {
        "ancla": "frontera",
        "momento": "Miras tus ventas del mes y todas, absolutamente todas, están dentro del mismo país.",
        "sintoma": "No es que no quieras vender afuera. Es que no sabes con quién hablar del otro lado de la frontera.",
        "reaccion_interna": "Te dices que primero hay que consolidar aquí, aunque en el fondo sabes que es miedo a lo que no conoces.",
        "explicacion_fallida": "Dices que la logística es complicada. Que los pagos no cruzan. Que cada país es un mundo.",
        "patron": "Pero llevas dos años diciendo lo mismo, y el mercado local cada vez tiene más competencia.",
        "causa_raiz": "La frontera no es logística. Es que no conoces a nadie que ya la haya cruzado y te pueda decir cómo.",
        "mecanismo": "Feria Effix junta cinco países en el mismo salón: Colombia, Ecuador, República Dominicana, Costa Rica y Guatemala.",
        "prueba_social": "Los cinco ya confirmaron para octubre.",
        "visualizacion": "Imagínate tu primera venta afuera, y que sabes exactamente a quién preguntarle cuando algo falle.",
        "urgencia_cta": "Del quince al diecinueve de octubre, Plaza Mayor, Medellín. Código EFFIX veinte.",
        "defecto_admitido": "No cubre el vuelo. Solo lo de adentro.",
        "loop_rewatch": "Y el próximo reporte del mes ya no cabe en un solo país.",
        "overlays": [
            "Todo en el mismo país",
            "No sabes con quién hablar",
            "\"Primero consolido aquí\"",
            "\"La logística es complicada\"",
            "Dos años diciendo lo mismo",
            "No es logística. Es contacto",
            "Cinco países, un salón",
            "Los cinco confirmados",
            "Tu primera venta afuera",
            "15–19 oct · Código EFFIX20",
            "El vuelo va por tu cuenta",
            "Ya no cabe en un país",
        ],
        "hooks": [
            {
                "hablado": "¿Todas tus ventas del mes caben dentro de la misma frontera?",
                "gatillos": ["auto_relevancia", "curiosidad"],
                "overlay": "Todo en el mismo país",
            },
            {
                "hablado": "La frontera no es logística. Es que no conoces a nadie allá.",
                "gatillos": ["interrupcion_patron", "curiosidad"],
                "overlay": "No es logística",
            },
            {
                "hablado": "Cinco países se están juntando en octubre. Tú decides.",
                "gatillos": ["FOMO", "activacion_emocional"],
                "overlay": "Cinco países, un salón",
            },
        ],
    },
    "herramientas": {
        "ancla": "herramienta",
        "momento": "Son las nueve de la noche y sigues pegando datos de una pestaña a otra, a mano, como el año pasado.",
        "sintoma": "El trabajo se hace, pero cada mes te toma más horas y ya no sabes cuánto te está costando de verdad.",
        "reaccion_interna": "Sospechas que hay una forma más rápida, pero no tienes cómo saber cuál sin perder un mes probando.",
        "explicacion_fallida": "Dices que cambiar de herramienta es un lío. Que ya te acostumbraste. Que después lo miras.",
        "patron": "Pero llevas cuatro trimestres diciendo 'después', y las horas se acumulan cada semana.",
        "causa_raiz": "No es que no existan mejores herramientas. Es que nadie te ha mostrado cuál funciona con un caso como el tuyo.",
        "mecanismo": "En Feria Effix las ves funcionando en vivo, con datos reales, y preguntas antes de comprometerte.",
        "prueba_social": "Cinco países comparando lo mismo en el mismo lugar, del quince al diecinueve de octubre.",
        "visualizacion": "Imagínate ese martes en la noche libre, porque el proceso ya corre solo.",
        "urgencia_cta": "Plaza Mayor, Medellín. Con el código EFFIX veinte entras con veinte por ciento menos.",
        "defecto_admitido": "Ninguna herramienta se instala sola. Hay que sentarse.",
        "loop_rewatch": "Y a las nueve de la noche ya no estás pegando datos a mano.",
        "overlays": [
            "9 pm, copiando a mano",
            "Cada mes toma más horas",
            "Sabes que hay otra forma",
            "\"Después lo miro\"",
            "Cuatro trimestres igual",
            "Nadie te mostró cuál",
            "Demos en vivo, datos reales",
            "Cinco países comparando",
            "Ese martes libre",
            "15–19 oct · Código EFFIX20",
            "Nada se instala solo",
            "Ya no pegas datos a mano",
        ],
        "hooks": [
            {
                "hablado": "¿Sigues pegando datos a mano a las nueve de la noche?",
                "gatillos": ["auto_relevancia", "curiosidad"],
                "overlay": "9 pm, copiando a mano",
            },
            {
                "hablado": "Tu herramienta no está mala. Está vieja, que es distinto.",
                "gatillos": ["interrupcion_patron", "curiosidad"],
                "overlay": "Vieja, no mala",
            },
            {
                "hablado": "Cada semana que esperas, el proceso te cobra más horas.",
                "gatillos": ["activacion_emocional", "auto_relevancia"],
                "overlay": "Te cobra horas",
            },
        ],
    },
    "de_cero_a_referente": {
        "ancla": "historia",
        "momento": "En el almuerzo familiar te preguntan otra vez de qué vives, y otra vez terminas explicando en dos frases lo que llevas tres años construyendo.",
        "sintoma": "No te falta resultado. Te falta que alguien alrededor entienda de qué se trata y te empuje.",
        "reaccion_interna": "Terminas dudando tú también, porque cuando nadie cerca lo valida, todo parece más pequeño de lo que es.",
        "explicacion_fallida": "Dices que es normal, que ellos son de otra generación, que ya entenderán cuando veas los números.",
        "patron": "Pero cada vez que te atascas, no tienes a quién preguntarle sin explicar primero todo el contexto.",
        "causa_raiz": "No es falta de disciplina. Es falta de gente cerca que ya recorrió lo mismo y te ahorra el error.",
        "mecanismo": "En Feria Effix escuchas casos contados de frente, con los números encima de la mesa, no en una landing.",
        "prueba_social": "Cinco países llevando sus casos: Colombia, Ecuador, República Dominicana, Costa Rica y Guatemala.",
        "visualizacion": "Imagínate contando tu caso en dos años y que alguien tome nota.",
        "urgencia_cta": "Del quince al diecinueve de octubre, Plaza Mayor. Código EFFIX veinte.",
        "defecto_admitido": "No salís siendo referente en cinco días.",
        "loop_rewatch": "Y en el próximo almuerzo tu historia ya no cabe en dos frases.",
        "overlays": [
            "\"¿Y de qué vives?\"",
            "Falta quien te empuje",
            "Nadie cerca lo valida",
            "\"Ya entenderán\"",
            "No tienes a quién preguntar",
            "No es disciplina. Es contexto",
            "Casos con números reales",
            "Cinco países, cinco casos",
            "Que alguien tome nota",
            "15–19 oct · Código EFFIX20",
            "No en cinco días",
            "Ya no cabe en dos frases",
        ],
        "hooks": [
            {
                "hablado": "¿Cuántas veces has explicado de qué vives y nadie entendió?",
                "gatillos": ["auto_relevancia", "activacion_emocional"],
                "overlay": "\"¿Y de qué vives?\"",
            },
            {
                "hablado": "No te falta disciplina. Te falta gente que ya lo hizo.",
                "gatillos": ["interrupcion_patron", "auto_relevancia"],
                "overlay": "No es disciplina",
            },
            {
                "hablado": "Toda historia de cinco cifras empezó con alguien que nadie entendía.",
                "gatillos": ["curiosidad", "activacion_emocional"],
                "overlay": "Empezó igual que tú",
            },
        ],
    },
    "no_tengo_con_quien_ir": {
        "ancla": "nadie",
        "momento": "Ves el evento, te interesa de verdad, y lo primero que pensás no es el precio: es con quién vas a ir.",
        "sintoma": "No es miedo al evento. Es no querer pasar tres días parado en una esquina sin hablarle a nadie.",
        "reaccion_interna": "Te da algo de vergüenza admitirlo, porque manejás un negocio y suena a inseguridad de colegio.",
        "explicacion_fallida": "Te decís que mejor esperás a la próxima edición, cuando ya conozcas a alguien de ese mundo.",
        "patron": "Pero es la tercera vez que decidís lo mismo, y seguís sin conocer a nadie del sector.",
        "causa_raiz": "A un evento así no se va con gente. Se va a conseguirla. Esa es toda la diferencia.",
        "mecanismo": "Hay mesas de trabajo y actividades donde te sentás con desconocidos por diseño, no por casualidad.",
        "prueba_social": "Más de trescientas cincuenta marcas y doscientos ponentes. Nadie llega conociendo a todos.",
        "visualizacion": "Imaginate saliendo el domingo con tres números nuevos en el teléfono.",
        "urgencia_cta": "Viernes dieciséis a domingo dieciocho, Plaza Mayor. Código EFFIX veinte.",
        "defecto_admitido": "Los primeros treinta minutos son incómodos. Después no.",
        "loop_rewatch": "Y a la próxima edición ya no vas a ir solo.",
        "overlay_dolor": "Entrar sin conocer a nadie",
        "visual_clave": "una mesa de trabajo donde se sientan desconocidos",
        "visual_clave_en": "a workshop table where strangers sit down together",
        "overlays": [
            "¿Con quién voy?",
            "Entrar sin conocer a nadie",
            "Da pena decirlo",
            "\"Mejor la próxima edición\"",
            "Tercera vez igual",
            "No se va acompañado",
            "Mesas con desconocidos",
            "350 marcas · 200 ponentes",
            "Tres números nuevos",
            "16–18 oct · Pase 3 días",
            "30 minutos incómodos",
            "Ya no vas solo",
        ],
        "hooks": [
            {"hablado": "¿Te interesó y pensaste con quién ir?", "gatillos": ["auto_relevancia", "curiosidad"], "overlay": "¿Con quién voy?"},
            {"hablado": "A un evento no se va con gente.", "gatillos": ["interrupcion_patron", "curiosidad"], "overlay": "No se va acompañado"},
            {"hablado": "Nadie llega conociendo a nadie. Ese es el punto.", "gatillos": ["interrupcion_patron", "activacion_emocional"], "overlay": "Nadie conoce a nadie"},
        ],
    },
    "vale_lo_que_cuesta": {
        "ancla": "cuesta",
        "momento": "Abrís la página, ves el precio de la entrada y cerrás la pestaña sin pensarlo demasiado.",
        "sintoma": "No es que no tengas la plata. Es que no sabés qué te vas a traer por ella.",
        "reaccion_interna": "Preferís no arriesgar doscientos mil pesos en algo que no podés medir antes de pagarlo.",
        "explicacion_fallida": "Te decís que con ese dinero pagás pauta, y la pauta al menos se mide.",
        "patron": "Pero llevás meses metiéndole a pauta sin resolver lo que te tiene frenado desde el año pasado.",
        "causa_raiz": "Lo que comprás no es una entrada. Es acceso, y el acceso no se consigue pautando.",
        "mecanismo": "Doscientas conferencias por doscientos mil pesos: sale a mil pesos cada una.",
        "prueba_social": "Trescientas cincuenta marcas y doscientos ponentes en un solo lugar.",
        "visualizacion": "Un solo contacto que te resuelva el mes ya pagó la entrada.",
        "urgencia_cta": "Doscientos un mil trescientos, con IVA. Código EFFIX veinte.",
        "defecto_admitido": "Es plata de verdad. Nadie dice lo contrario.",
        "loop_rewatch": "Y la pestaña que cerraste era la barata.",
        "overlay_dolor": "No sabés qué te traés",
        "visual_clave": "una pestaña del navegador cerrándose sobre el precio",
        "visual_clave_en": "a browser tab closing on a price page",
        "overlays": [
            "Cerraste la pestaña",
            "No sabés qué te traés",
            "No querés arriesgar",
            "\"Con eso pago pauta\"",
            "Meses de pauta, mismo freno",
            "No es entrada. Es acceso",
            "200 conferencias · $1.000 c/u",
            "350 marcas · 200 ponentes",
            "Un contacto ya lo paga",
            "$201.300 · Código EFFIX20",
            "Es plata de verdad",
            "Era la barata",
        ],
        "hooks": [
            {"hablado": "¿Viste el precio y cerraste la pestaña?", "gatillos": ["auto_relevancia", "curiosidad"], "overlay": "Cerraste la pestaña"},
            {"hablado": "No comprás una entrada. Comprás acceso.", "gatillos": ["interrupcion_patron", "curiosidad"], "overlay": "No es entrada. Es acceso"},
            {"hablado": "Doscientas conferencias. Mil pesos cada una.", "gatillos": ["curiosidad", "auto_relevancia"], "overlay": "$1.000 por conferencia"},
        ],
    },
    "por_que_octubre": {
        "ancla": "octubre",
        "momento": "Es septiembre otra vez, abres el plan que escribiste en enero y la mitad sigue sin empezar.",
        "sintoma": "No es que no trabajes. Es que el trimestre que factura ya está encima y sigues resolviendo lo mismo de siempre.",
        "reaccion_interna": "Sientes que el año se te fue en operar, no en construir.",
        "explicacion_fallida": "Dices que este año estuvo raro. Que el mercado estuvo lento. Que el otro mes sí arrancas.",
        "patron": "Pero es el tercer año que llegas a septiembre con el mismo plan a medias.",
        "causa_raiz": "El problema no es el plan. Es que nunca reservas los días para salir de la operación y mirar el negocio.",
        "mecanismo": "Effix cae en octubre, justo antes de la temporada que factura: llegas con lo que aprendiste ya montado.",
        "prueba_social": "Cinco países confirmados, del quince al diecinueve de octubre, en Plaza Mayor.",
        "visualizacion": "Imagínate llegando a noviembre con la campaña lista, no improvisando.",
        "urgencia_cta": "Medellín, cinco días. Con el código EFFIX veinte te queda veinte por ciento menos.",
        "defecto_admitido": "Es en octubre. Si no podés, no insistas.",
        "loop_rewatch": "Y en septiembre del otro año, el plan de enero ya va a estar hecho.",
        "overlays": [
            "Septiembre otra vez",
            "El trimestre ya está encima",
            "Se te fue operando",
            "\"El otro mes arranco\"",
            "Tercer año igual",
            "Nunca reservas los días",
            "Justo antes de temporada",
            "Cinco países confirmados",
            "Noviembre con todo listo",
            "15–19 oct · Código EFFIX20",
            "Solo en octubre",
            "El plan ya estará hecho",
        ],
        "hooks": [
            {
                "hablado": "¿Abriste el plan de enero y la mitad sigue sin empezar?",
                "gatillos": ["auto_relevancia", "curiosidad"],
                "overlay": "Septiembre otra vez",
            },
            {
                "hablado": "El año no se te fue. Se te fue operando.",
                "gatillos": ["interrupcion_patron", "activacion_emocional"],
                "overlay": "Se te fue operando",
            },
            {
                "hablado": "Octubre cae justo antes del trimestre que factura. No después.",
                "gatillos": ["curiosidad", "FOMO"],
                "overlay": "Antes de temporada",
            },
        ],
    },
}


def construir_para_effix(angulo: str, marca: str = "effix") -> MicroSituacion:
    """Devuelve la micro-situación completa de un ángulo de contenido."""
    if angulo not in _MICROS:
        disponibles = ", ".join(sorted(_MICROS))
        raise KeyError(f"No hay micro-situación para '{angulo}'. Hay: {disponibles}")

    datos = _MICROS[angulo]
    dna = load_brand_dna(marca)
    etiquetas = dna.get("angulos_de_contenido", [])

    # Empareja el ángulo con su etiqueta larga del brand_dna cuando exista
    etiqueta = next(
        (e for e in etiquetas if _coincide(angulo, e)),
        angulo.replace("_", " "),
    )

    return MicroSituacion(
        momento=datos["momento"],
        sintoma=datos["sintoma"],
        reaccion_interna=datos["reaccion_interna"],
        explicacion_fallida=datos["explicacion_fallida"],
        patron=datos["patron"],
        causa_raiz=datos["causa_raiz"],
        mecanismo=datos["mecanismo"],
        prueba_social=datos["prueba_social"],
        visualizacion=datos["visualizacion"],
        urgencia_cta=datos["urgencia_cta"],
        defecto_admitido=datos["defecto_admitido"],
        loop_rewatch=datos["loop_rewatch"],
        angulo=angulo,
        etiqueta=etiqueta,
        ancla=datos["ancla"],
        overlays=datos["overlays"],
        hooks_escritos=datos["hooks"],
        datos_sin_verificar=_SIN_VERIFICAR.get(angulo, []),
    )


def _coincide(angulo: str, etiqueta: str) -> bool:
    """Empareja el slug del ángulo con su etiqueta larga por palabras compartidas."""
    import unicodedata

    def limpiar(t: str) -> set[str]:
        normal = unicodedata.normalize("NFKD", t.lower())
        sin_tildes = "".join(c for c in normal if not unicodedata.combining(c))
        return {p for p in re.split(r"[^a-z0-9]+", sin_tildes) if len(p) > 3}

    return bool(limpiar(angulo) & limpiar(etiqueta))


def angulos_disponibles() -> list[str]:
    """Ángulos con micro-situación construida."""
    return sorted(_MICROS)
