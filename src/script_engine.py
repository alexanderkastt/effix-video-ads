"""Motor de guiones — metodología Kreoon.

Genera guiones beat por beat con la secuencia EMOCIONAL (no cronológica):
Hook -> Tensión -> Re-enganches -> Payoff -> CTA -> Loop.

El motor es determinista: compone las narraciones a partir de plantillas y de
los datos reales de `config/brand_dna.json`. No llama a ningún LLM ni a ninguna
API de pago, para que el guión se pueda generar y validar sin gastar un peso.

Presupuesto de palabras: la locución en español va a ~2.2 palabras por segundo,
así que un beat de 4s admite entre 7 y 11 palabras. Todo el guión de 44s cae
en 96-108 palabras. Las plantillas están escritas para respetar ese límite.
"""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from typing import Any

from .narracion_effix import (
    CTA_POR_PASE, PASE_POR_DEFECTO, PALABRAS_DE_DESCUENTO,
)
from .paths import env_int, load_brand_dna

# ---------------------------------------------------------------------------
# Secuencia emocional fija de los 11 beats
# ---------------------------------------------------------------------------

BEAT_SEQUENCE: list[dict[str, str]] = [
    {"n": 1,  "nombre": "HOOK",           "emocion": "interrupcion_patron", "emoji": "🪝", "aida": "atencion"},
    {"n": 2,  "nombre": "AUTO-RELEVANCIA", "emocion": "auto_relevancia",    "emoji": "🫵", "aida": "atencion"},
    {"n": 3,  "nombre": "DOLOR",          "emocion": "identificacion",      "emoji": "😔", "aida": "interes"},
    {"n": 4,  "nombre": "AMPLIFICACIÓN",  "emocion": "tension",             "emoji": "📉", "aida": "interes"},
    {"n": 5,  "nombre": "PROMESA",        "emocion": "aspiracion",          "emoji": "✨", "aida": "interes"},
    {"n": 6,  "nombre": "PRUEBA SOCIAL",  "emocion": "confianza",           "emoji": "🤝", "aida": "deseo"},
    {"n": 7,  "nombre": "MECANISMO",      "emocion": "claridad",            "emoji": "⚙️", "aida": "deseo"},
    {"n": 8,  "nombre": "VISUALIZACIÓN",  "emocion": "aspiracion",          "emoji": "🎬", "aida": "deseo"},
    {"n": 9,  "nombre": "URGENCIA",       "emocion": "urgencia",            "emoji": "⏳", "aida": "accion"},
    {"n": 10, "nombre": "CTA SUAVE",      "emocion": "oportunidad",         "emoji": "🎟️", "aida": "accion"},
    {"n": 11, "nombre": "LOOP",           "emocion": "pertenencia",         "emoji": "🔁", "aida": "accion"},
]

# Movimiento de cámara sugerido por beat. El SceneBuilder puede sobrescribirlo
# según el estilo, pero esta es la intención narrativa.
MOVIMIENTO_POR_BEAT = {
    1: "closeup", 2: "handheld", 3: "static", 4: "dolly-in", 5: "handheld",
    6: "pan", 7: "dolly-in", 8: "pan", 9: "static", 10: "closeup", 11: "handheld",
}

# ---------------------------------------------------------------------------
# Ángulos narrativos — cada uno reencuadra el mismo evento
# ---------------------------------------------------------------------------

ANGULOS: dict[str, dict[str, str]] = {
    "comunidad_que_no_tienes": {
        "etiqueta": "La comunidad que no tienes como emprendedor solo",
        "ancla": "solo",
        "dolor": "Llevas meses vendiendo solo, sin nadie que entienda.",
        "amplificacion": "Y solo, cada error lo pagas dos veces.",
        "promesa": "En Effix te sientas con gente que ya pasó por ahí.",
        "mecanismo": "Cinco días, mesas de trabajo, y gente que responde.",
        "visual_clave": "una mesa larga con emprendedores hablando entre ellos",
        "overlay_dolor": "Meses vendiendo solo",
        "overlay_hook": "¿Vendes solo?",
        "overlay_amplificacion": "Se paga doble",
        "overlay_mecanismo": "Mesas de trabajo",
        "visualizacion": "Imagínate saliendo de ahí con tu agenda llena.",
        "overlay_visualizacion": "Agenda llena",
        "overlay_cierre": "Nunca más solo",
        "visual_clave_en": "a long table of entrepreneurs talking to each other",
        "cierre": "Y dejas de vender solo. Ese es el punto.",
        "hooks": [
            {"texto": "¿Cuándo fue la última vez que no vendiste solo?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "Nadie te lo dice: vender solo tiene techo.", "gatillos": ['interrupcion_patron', 'auto_relevancia']},
            {"texto": "Cinco países se juntan en octubre. ¿Y tú sigues solo?", "gatillos": ['curiosidad', 'FOMO']}
        ],
    },
    "no_esta_en_cursos": {
        "etiqueta": "Lo que pasa en Effix que no encuentras en ningún curso online",
        "ancla": "curso",
        "dolor": "Ya viste el curso. Ya tomaste notas. Sigues igual.",
        "amplificacion": "Y el siguiente curso te va a dejar igual.",
        "promesa": "Effix te pone la conversación que ningún video te da.",
        "mecanismo": "Preguntas en vivo, casos reales, respuestas de una.",
        "visual_clave": "alguien cerrando el portátil y saliendo de casa",
        "overlay_dolor": "Mismo resultado",
        "overlay_hook": "¿Otro curso?",
        "overlay_amplificacion": "No era el curso",
        "overlay_mecanismo": "Casos reales",
        "visualizacion": "Imagínate resolviendo en un día lo del semestre.",
        "overlay_visualizacion": "Un día = un semestre",
        "overlay_cierre": "Por eso es presencial",
        "visual_clave_en": "someone closing a laptop and stepping out of the house",
        "cierre": "Ningún curso te da eso. Por eso es presencial.",
        "hooks": [
            {"texto": "¿Cuántos cursos llevas y sigues facturando lo mismo?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "El curso no era el problema. Nunca lo fue.", "gatillos": ['interrupcion_patron', 'curiosidad']},
            {"texto": "Ya hiciste el curso. Dime la verdad: ¿te sirvió?", "gatillos": ['auto_relevancia', 'interrupcion_patron']}
        ],
    },
    "latam_unido": {
        "etiqueta": "Los 5 países que ya están en Effix — por qué LATAM va unido",
        "ancla": "frontera",
        "dolor": "Tu mercado se acaba en la frontera de tu país.",
        "amplificacion": "Y esa frontera te la pusiste tú, no el mercado.",
        "promesa": "Effix junta cinco países en el mismo salón.",
        "mecanismo": "Colombia, Ecuador, República Dominicana, Costa Rica y Guatemala.",
        "visual_clave": "banderas o mapa de los cinco países activos",
        "overlay_dolor": "Paras en la frontera",
        "overlay_hook": "¿Paras en la frontera?",
        "overlay_amplificacion": "El vecino ya vende",
        "overlay_mecanismo": "Un solo salón",
        "visualizacion": "Imagínate vendiendo en tres países el año entrante.",
        "overlay_visualizacion": "Tres países",
        "overlay_cierre": "Sin ese techo",
        "visual_clave_en": "flags or a map of the five active countries",
        "cierre": "La frontera deja de ser tu techo. Ese es el punto.",
        "hooks": [
            {"texto": "¿Tu mercado se acaba donde termina la frontera?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "La frontera no es un límite. Es una excusa.", "gatillos": ['interrupcion_patron', 'curiosidad']},
            {"texto": "Cinco países cruzaron la frontera este octubre. ¿Y tú?", "gatillos": ['curiosidad', 'FOMO']}
        ],
    },
    "competencia_va": {
        "etiqueta": "Qué pasa si no vas y tu competencia sí va",
        "ancla": "competencia",
        "dolor": "Tu competencia ya reservó. Tú lo estás pensando.",
        "amplificacion": "En octubre tu competencia sale con red; tú con dudas.",
        "promesa": "Effix es donde se reparten los contactos del año.",
        "mecanismo": "Proveedores, herramientas y aliados, en el mismo lugar.",
        "visual_clave": "dos caminos: uno lleno de gente, otro vacío",
        "overlay_dolor": "Ellos ya reservaron",
        "overlay_hook": "Ya reservaron",
        "overlay_amplificacion": "Él con red",
        "overlay_mecanismo": "Todos juntos",
        "visualizacion": "Imagínate llegando a enero con la red armada.",
        "overlay_visualizacion": "Red armada",
        "overlay_cierre": "Que no vaya solo",
        "visual_clave_en": "two paths: one crowded with people, one empty",
        "cierre": "Que tu competencia no sea la única que fue.",
        "hooks": [
            {"texto": "¿Sabes si tu competencia ya reservó para octubre?", "gatillos": ['auto_relevancia', 'FOMO']},
            {"texto": "Tu competencia no está mejor. Está mejor acompañada.", "gatillos": ['interrupcion_patron', 'curiosidad']},
            {"texto": "Mientras lo piensas, tu competencia ya confirmó asistencia.", "gatillos": ['FOMO', 'interrupcion_patron']}
        ],
    },
    "proveedores": {
        "etiqueta": "Los proveedores que conocerás en un solo lugar",
        "ancla": "proveedor",
        "dolor": "Buscar proveedor por internet es una lotería.",
        "amplificacion": "Un mal proveedor te tumba el mes completo.",
        "promesa": "En Effix los ves de frente y les preguntas.",
        "mecanismo": "Stands, muestras físicas y trato directo, sin intermediarios.",
        "visual_clave": "manos revisando producto físico en un stand",
        "overlay_dolor": "Es una lotería",
        "overlay_hook": "¿Te falló otro?",
        "overlay_amplificacion": "Tumba el mes",
        "overlay_mecanismo": "Muestras físicas",
        "visualizacion": "Imagínate cerrando con el producto en la mano.",
        "overlay_visualizacion": "Producto en mano",
        "overlay_cierre": "Míralo a la cara",
        "visual_clave_en": "hands inspecting a physical product at a trade stand",
        "cierre": "Y tu próximo proveedor lo eliges mirándolo a la cara.",
        "hooks": [
            {"texto": "¿Cuántas veces te ha fallado un proveedor de dropshipping?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "Un mal proveedor no te cuesta plata. Te cuesta meses.", "gatillos": ['interrupcion_patron', 'auto_relevancia']},
            {"texto": "Elegir proveedor a ciegas es una lotería. ¿Seguimos así?", "gatillos": ['curiosidad', 'interrupcion_patron']}
        ],
    },
    "herramientas": {
        "etiqueta": "Las herramientas que están cambiando el ecommerce LATAM ahora mismo",
        "ancla": "herramienta",
        "dolor": "Sigues operando con las mismas herramientas del año pasado.",
        "amplificacion": "Y cada mes con esa herramienta operas más caro.",
        "promesa": "Effix te muestra lo que ya está funcionando hoy.",
        "mecanismo": "Demos en vivo, no promesas de landing page.",
        "visual_clave": "pantalla con un panel de métricas subiendo",
        "overlay_dolor": "Las del año pasado",
        "overlay_hook": "¿Las de siempre?",
        "overlay_amplificacion": "Más caro cada mes",
        "overlay_mecanismo": "Demos en vivo",
        "visualizacion": "Imagínate operando en noviembre a mitad de costo.",
        "overlay_visualizacion": "Mitad de costo",
        "overlay_cierre": "Antes de temporada",
        "visual_clave_en": "a screen showing a metrics dashboard trending up",
        "cierre": "Y cambias la herramienta antes que la temporada.",
        "hooks": [
            {"texto": "¿Con qué herramienta estás operando desde el año pasado?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "La herramienta que usas hoy ya la superaron.", "gatillos": ['interrupcion_patron', 'FOMO']},
            {"texto": "Cada mes con la misma herramienta te cuesta más.", "gatillos": ['auto_relevancia', 'interrupcion_patron']}
        ],
    },
    "de_cero_a_referente": {
        "etiqueta": "De 0 a referente: las historias que se cuentan en Effix",
        "ancla": "historia",
        "dolor": "Nadie en tu casa entiende de qué vives.",
        "amplificacion": "Y sin esa historia cerca, el techo te lo pones tú.",
        "promesa": "En Effix escuchas a los que ya rompieron ese techo.",
        "mecanismo": "Historias contadas de frente, con números encima de la mesa.",
        "visual_clave": "alguien en tarima contando su caso, público atento",
        "overlay_dolor": "Nadie lo entiende",
        "overlay_hook": "¿Nadie entiende?",
        "overlay_amplificacion": "Tu propio techo",
        "overlay_mecanismo": "Números reales",
        "visualizacion": "Imagínate contando tu caso el año entrante.",
        "overlay_visualizacion": "Tu caso, el año entrante",
        "overlay_cierre": "La próxima es tuya",
        "visual_clave_en": "someone on stage telling their case to an attentive audience",
        "cierre": "La próxima historia contada ahí puede ser la tuya.",
        "hooks": [
            {"texto": "¿Cuál sería tu historia si alguien te la pidiera?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "Nadie cuenta esa historia: cómo se rompe el techo.", "gatillos": ['curiosidad', 'interrupcion_patron']},
            {"texto": "Toda historia de cinco cifras empezó con alguien solo.", "gatillos": ['interrupcion_patron', 'auto_relevancia']}
        ],
    },
    "por_que_octubre": {
        "etiqueta": "Por qué octubre 2026 es el momento",
        "ancla": "octubre",
        "dolor": "Llevas todo el año diciendo que el otro mes arrancas.",
        "amplificacion": "Y el cuarto trimestre se te va otra vez encima.",
        "promesa": "Octubre es justo antes de la temporada que factura.",
        "mecanismo": "Del quince al diecinueve, en Plaza Mayor, Medellín.",
        "visual_clave": "calendario marcado en octubre, temporada alta cerca",
        "overlay_dolor": "Todo el año igual",
        "overlay_hook": "¿El otro mes?",
        "overlay_amplificacion": "Q4 encima",
        "overlay_mecanismo": "Plaza Mayor",
        "visualizacion": "Imagínate entrando a temporada alta ya conectado.",
        "overlay_visualizacion": "Ya conectado",
        "overlay_cierre": "Con boleta en mano",
        "visual_clave_en": "a calendar marked in October, high season approaching",
        "cierre": "Octubre otra vez. Esta vez con boleta en mano.",
        "hooks": [
            {"texto": "¿Qué pasó con lo que ibas a hacer en octubre?", "gatillos": ['auto_relevancia', 'curiosidad']},
            {"texto": "Octubre llega antes de la temporada que factura.", "gatillos": ['interrupcion_patron', 'curiosidad']},
            {"texto": "Llevas todo el año diciendo que arrancas. Ya es octubre.", "gatillos": ['auto_relevancia', 'FOMO']}
        ],
    },
}

ANGULO_POR_DEFECTO = "comunidad_que_no_tienes"


def _slug(texto: str) -> str:
    """Convierte texto libre en slug ascii en minúsculas con guiones bajos."""
    normal = unicodedata.normalize("NFKD", texto)
    sin_tildes = "".join(c for c in normal if not unicodedata.combining(c))
    limpio = re.sub(r"[^a-zA-Z0-9]+", "_", sin_tildes).strip("_").lower()
    return limpio or "video"


def _contar_palabras(texto: str) -> int:
    return len([p for p in re.split(r"\s+", texto.strip()) if p])


def resolver_angulo(angulo: str | None) -> tuple[str, dict[str, str]]:
    """Acepta un slug exacto o texto libre y devuelve (slug, datos del ángulo).

    Si el texto no coincide con ninguno, cae al ángulo por defecto en vez de
    reventar: es preferible producir un guión utilizable a bloquear el flujo.
    """
    if not angulo:
        return ANGULO_POR_DEFECTO, ANGULOS[ANGULO_POR_DEFECTO]

    clave = _slug(angulo)
    if clave in ANGULOS:
        return clave, ANGULOS[clave]

    # Búsqueda laxa: alguna palabra del texto dentro de la etiqueta del ángulo
    palabras = {p for p in clave.split("_") if len(p) > 3}
    for slug_angulo, datos in ANGULOS.items():
        etiqueta = _slug(datos["etiqueta"])
        if palabras & set(etiqueta.split("_")):
            return slug_angulo, datos

    return ANGULO_POR_DEFECTO, ANGULOS[ANGULO_POR_DEFECTO]


# ---------------------------------------------------------------------------
# Motor
# ---------------------------------------------------------------------------


class ScriptEngine:
    """Genera guiones de video beat-by-beat con metodología Kreoon.

    Cada beat tiene: narración, prompt_video, prompt_imagen, visual,
    movimiento, emoción y texto_pantalla.
    """

    def __init__(self, marca: str = "effix") -> None:
        self.marca = marca
        self.dna = load_brand_dna(marca)
        self.evento = self.dna["evento"]
        self.avatar = self.dna["avatar_principal"]
        self.duracion_beat = env_int("CLIP_DURATION_SECONDS", 4)

    # -- hooks --------------------------------------------------------------

    def generate_hooks(self, concepto: str, angulo: str | None = None, n: int = 3) -> list[dict]:
        """Genera N variantes de hook para el mismo concepto.

        Cada hook apila mínimo dos gatillos y no pasa de 12 palabras. Nada de
        saludos, logos ni frases de calentamiento: el primer segundo trabaja.
        """
        _, ang = resolver_angulo(angulo)
        ancla = ang["ancla"]

        # Los hooks van escritos a mano por ángulo, no generados por plantilla.
        # Una plantilla ciega produce frases rotas ("vender sin estar proveedor")
        # y además rompe el loop del beat 11, que necesita reencontrar el ancla.
        plantillas = ang["hooks"]

        hooks: list[dict] = []
        for i, plantilla in enumerate(plantillas[: max(1, n)]):
            texto = self.humanize_narration(plantilla["texto"])
            hooks.append(
                {
                    "variante": chr(ord("A") + i),
                    "texto": texto,
                    "palabras": _contar_palabras(texto),
                    "gatillos": plantilla["gatillos"],
                    "ancla": ancla,
                }
            )
        return hooks

    # -- narraciones --------------------------------------------------------

    # El pase manda las fechas: el Pasaporte es de viernes a domingo, y
    # prometer "quince al diecinueve" mientras se cobra un pase de 3 dias
    # es vender un rango que la boleta no da.
    FECHAS_POR_PASE = {
        "3": ("Viernes dieciséis a domingo dieciocho de octubre.",
              "16–18 octubre"),
        "5": ("Del quince al diecinueve de octubre. Plaza Mayor.",
              "15–19 octubre"),
    }

    def _fechas(self, pase: str) -> tuple[str, str]:
        """Narracion y overlay del beat 09, segun los dias que da el pase."""
        dias = CTA_POR_PASE[pase].get("dias") or "5"
        return self.FECHAS_POR_PASE.get(dias, self.FECHAS_POR_PASE["5"])

    def _narraciones(self, hook: str, ang: dict[str, str], pase: str) -> list[str]:
        """Compone las 11 narraciones. Cada una entre 7 y 11 palabras."""
        avatar_rango = "mil y cinco mil"
        paises = self.avatar["paises_activos"]

        return [
            hook,                                                   # 01 HOOK
            f"Para ti que facturas entre {avatar_rango} al mes.",    # 02 AUTO-RELEVANCIA
            ang["dolor"],                                           # 03 DOLOR
            ang["amplificacion"],                                   # 04 AMPLIFICACIÓN
            ang["promesa"],                                         # 05 PROMESA
            "Miles de asistentes confirmados y ponentes de veinte países.",  # 06 PRUEBA
            ang["mecanismo"],                                       # 07 MECANISMO
            ang.get("visualizacion",
                    "Imagínate saliendo de ahí con tu agenda llena."),  # 08 VISUALIZACIÓN
            self._fechas(pase)[0],                                  # 09 URGENCIA
            CTA_POR_PASE[pase]["hablado"],                          # 10 CTA
            ang["cierre"],                                               # 11 LOOP
        ]

    # La locución lee cifras mal: MASTER_CONTEXT.md exige números en letras.
    _LETRAS = {1: "un", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis",
               7: "siete", 8: "ocho", 9: "nueve", 10: "diez", 11: "once", 12: "doce"}

    @classmethod
    def _en_letras(cls, n: int) -> str:
        """Convierte un número pequeño a palabra. ElevenLabs lee '5' de forma inconsistente."""
        return cls._LETRAS.get(n, str(n))

    @staticmethod
    def _recortar_palabras(texto: str, maximo: int = 6) -> str:
        """Recorta por palabra completa, nunca por caracteres.

        Cortar a N caracteres dejaba overlays de 8 y 9 palabras según el ángulo:
        el límite del overlay se cuenta en palabras, así que se recorta igual.
        """
        palabras = [p for p in re.split(r"\s+", texto.strip()) if p]
        return " ".join(palabras[:maximo]).rstrip(",;:")

    def _textos_pantalla(self, ang: dict[str, str], pase: str) -> list[str]:
        """Overlays de máximo 7 palabras. El video tiene que funcionar sin sonido.

        Cinco de estos estaban clavados al ángulo "comunidad": un guión de
        proveedores abría con "¿Vendiendo solo?" y cerraba con "Nunca más
        solo", contradiciendo su propia locución. Ahora los pone el ángulo.
        """
        paises = len(self.avatar["paises_activos"])
        return [
            ang.get("overlay_hook", "¿Vendiendo solo?"),
            "¿Facturas 1K–5K?",
            ang["overlay_dolor"],
            ang.get("overlay_amplificacion", "Cada error se paga doble"),
            "Feria Effix",
            "+20 países",
            ang.get("overlay_mecanismo", "Todo en un lugar"),
            ang.get("overlay_visualizacion", "Sales con la agenda llena"),
            self._fechas(pase)[1],
            CTA_POR_PASE[pase]["overlay"],
            ang.get("overlay_cierre", "Nunca más solo"),
        ]

    # -- guión completo -----------------------------------------------------

    def generate_script(
        self,
        concepto: str,
        estilo: str,
        angulo: str | None = None,
        duracion_beats: int = 11,
        hook_variante: str = "A",
        pase: str = PASE_POR_DEFECTO,
    ) -> dict[str, Any]:
        """Construye el guión completo con la secuencia emocional de 11 beats.

        `duracion_beats` permite recortar para pruebas, pero el guión de
        producción son 11 beats de 4s = 44s.
        """
        slug_angulo, ang = resolver_angulo(angulo)

        hooks = self.generate_hooks(concepto, slug_angulo, n=3)
        elegido = next((h for h in hooks if h["variante"] == hook_variante), hooks[0])

        if pase not in CTA_POR_PASE:
            raise KeyError(f"Pase '{pase}' no existe. Hay: {', '.join(CTA_POR_PASE)}")

        narraciones = self._narraciones(elegido["texto"], ang, pase)
        overlays = self._textos_pantalla(ang, pase)

        total = min(duracion_beats, len(BEAT_SEQUENCE))
        beats: list[dict[str, Any]] = []

        for i in range(total):
            meta = BEAT_SEQUENCE[i]
            narracion = self.humanize_narration(narraciones[i])
            beats.append(
                {
                    "beat": meta["n"],
                    "duracion_s": self.duracion_beat,
                    "nombre": meta["nombre"],
                    "emocion": meta["emocion"],
                    "aida": meta.get("aida", ""),
                    "emoji": meta["emoji"],
                    "narracion": narracion,
                    "palabras_narracion": _contar_palabras(narracion),
                    "texto_pantalla": overlays[i],
                    "descripcion_visual": "",     # lo llena SceneBuilder
                    "prompt_video": "",           # lo llena SceneBuilder
                    "prompt_imagen_base": "",     # lo llena SceneBuilder
                    "escenografia": {},           # lo llena SceneBuilder
                    "movimiento_camara": MOVIMIENTO_POR_BEAT[meta["n"]],
                    "notas_produccion": "",       # lo llena SceneBuilder
                }
            )

        return {
            "concepto": concepto,
            "estilo": estilo,
            "marca": self.marca,
            "angulo": slug_angulo,
            "angulo_etiqueta": ang["etiqueta"],
            "ancla_narrativa": ang["ancla"],
            "visual_clave": ang["visual_clave"],
            "visual_clave_en": ang["visual_clave_en"],
            "hooks_alternativos": hooks,
            "hook_elegido": elegido["variante"],
            "pase": pase,
            "generado_en": datetime.now().isoformat(timespec="seconds"),
            "duracion_total_s": total * self.duracion_beat,
            "beats": beats,
        }

    # -- validación ---------------------------------------------------------

    def validate_script(self, script_json: dict) -> list[str]:
        """Verifica la calidad del guión. Devuelve lista de errores o ["OK"]."""
        errores: list[str] = []
        beats = script_json.get("beats", [])

        if not beats:
            return ["El guión no tiene beats."]

        prohibidas = [p.lower() for p in self.dna["palabras_prohibidas"]]

        for beat in beats:
            n = beat["beat"]
            narracion = beat.get("narracion", "")
            bajo = narracion.lower()

            for palabra in prohibidas:
                # Coincidencia por palabra completa, para no marcar "unidos" por "únete"
                patron = r"\b" + re.escape(palabra) + r"\b"
                if re.search(patron, bajo):
                    errores.append(f"Beat {n:02d}: usa la palabra prohibida '{palabra}'.")

            overlay = beat.get("texto_pantalla", "")
            n_palabras = _contar_palabras(overlay)
            if n_palabras > 7:
                errores.append(
                    f"Beat {n:02d}: texto_pantalla tiene {n_palabras} palabras (máximo 7)."
                )

            # Presupuesto de locución, medido sobre la voz real. El 2.75 que
            # había aquí era un cuarto número distinto —convivía con el 2.2 del
            # encabezado y el 2.96 de plan_clips— y con la voz a speed 1.15
            # rechazaba frases que sí caben.
            from .plan_clips import FACTOR_DESBORDE, PALABRAS_POR_SEGUNDO
            techo = int(
                beat.get("duracion_s", 4) * PALABRAS_POR_SEGUNDO * FACTOR_DESBORDE
            )
            if _contar_palabras(narracion) > techo:
                errores.append(
                    f"Beat {n:02d}: narración de {_contar_palabras(narracion)} palabras "
                    f"no cabe en {beat.get('duracion_s', 4)}s (techo {techo})."
                )

        # El beat final tiene que cerrar el círculo con el hook
        if len(beats) >= 11:
            ancla = script_json.get("ancla_narrativa", "")
            cierre = beats[-1].get("narracion", "").lower()
            apertura = beats[0].get("narracion", "").lower()
            if ancla and ancla.lower() not in cierre:
                errores.append(
                    f"Beat 11: no retoma el ancla '{ancla}' del hook — se rompe el loop."
                )
            if ancla and ancla.lower() not in apertura:
                errores.append(
                    f"Beat 01: el hook no contiene el ancla '{ancla}' que el beat 11 retoma."
                )

        # Politica de marca: no ofrecemos descuentos. Vivia escrita en
        # narracion_effix.py pero nadie la ejecutaba, y por eso un codigo de
        # descuento se colo hasta el guion aprobado.
        for beat in beats:
            n = beat["beat"]
            texto = f"{beat.get('narracion','')} {beat.get('texto_pantalla','')}".lower()
            for palabra in PALABRAS_DE_DESCUENTO:
                patron = r"\b" + re.escape(palabra.lower()) + r"\b"
                if re.search(patron, texto):
                    errores.append(
                        f"Beat {n:02d}: menciona '{palabra}' — no ofrecemos descuentos."
                    )

        # La micro-situacion se martilla: el mismo detalle concreto vuelve
        # entre tres y cuatro veces en 44s. Menos, y el guion no ancla en un
        # momento reconocible; mas, y satura.
        ancla = (script_json.get("ancla_narrativa") or "").lower()
        if ancla and len(beats) >= 11:
            patron = r"\b" + re.escape(ancla)
            menciones = [
                b["beat"] for b in beats
                if re.search(patron, b.get("narracion", "").lower())
            ]
            if len(menciones) < 3:
                errores.append(
                    f"La micro-situacion '{ancla}' suena {len(menciones)} vez/veces "
                    f"(beats {menciones}); el minimo son 3."
                )
            elif len(menciones) > 4:
                errores.append(
                    f"La micro-situacion '{ancla}' suena {len(menciones)} veces "
                    f"(beats {menciones}); el tope son 4."
                )

        # AIDA completo. Un creativo puede quedar bonito con atencion,
        # interes y deseo, y no pedir nada — y entonces no es un anuncio.
        fases = {b.get("aida") for b in beats if b.get("aida")}
        if fases:
            faltan = {"atencion", "interes", "deseo", "accion"} - fases
            if faltan:
                errores.append(
                    "Al guion le faltan fases de AIDA: " + ", ".join(sorted(faltan))
                )

        # Prueba concreta en el tramo 05-07
        tramo = [b for b in beats if 5 <= b["beat"] <= 7]
        if tramo and not any(self._tiene_dato_concreto(b["narracion"]) for b in tramo):
            errores.append(
                "Beats 05-07: ninguno aporta un dato concreto (número, fecha o nombre propio)."
            )

        return errores or ["OK"]

    @staticmethod
    def _tiene_dato_concreto(texto: str) -> bool:
        """Un dato concreto es un número, una cifra escrita o un nombre propio real."""
        if re.search(r"\d", texto):
            return True

        numeros_escritos = (
            "cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce "
            "trece catorce quince dieciséis diecisiete dieciocho diecinueve veinte "
            "treinta cuarenta cincuenta cien mil"
        ).split()
        bajo = texto.lower()
        if any(re.search(r"\b" + n + r"\b", bajo) for n in numeros_escritos):
            return True

        nombres_reales = [
            "effix", "plaza mayor", "medellín", "medellin", "colombia", "ecuador",
            "república dominicana", "republica dominicana", "costa rica", "guatemala",
            "grupo effi", "octubre",
        ]
        return any(nombre in bajo for nombre in nombres_reales)

    # -- humanizado ---------------------------------------------------------

    # Equivalentes coloquiales para las palabras que el brand_dna prohíbe
    REEMPLAZOS = {
        "descubre": "mira",
        "potencia": "sube",
        "revoluciona": "cambia",
        "sumérgete": "métete",
        "increíble": "muy bueno",
        "espectacular": "muy bueno",
        "innovador": "nuevo",
        "transformador": "que sí mueve la aguja",
        "únete": "vente",
        "aprovecha esta oportunidad": "no lo dejes pasar",
    }

    def humanize_narration(self, texto: str) -> str:
        """Filtro anti-IA: saca las palabras prohibidas y deja el texto hablado.

        No añade muletillas al azar. La imperfección de este sistema vive en la
        redacción de las plantillas (frases cortadas, dato hiperespecífico), no
        en un ruido insertado después, que es justo lo que suena a IA.
        """
        salida = texto
        for prohibida, reemplazo in self.REEMPLAZOS.items():
            patron = re.compile(r"\b" + re.escape(prohibida) + r"\b", re.IGNORECASE)
            salida = patron.sub(reemplazo, salida)

        # Normaliza espacios y deja un cierre limpio
        salida = re.sub(r"\s+", " ", salida).strip()

        # Mayúscula inicial, saltando signos de apertura (¿ ¡)
        for i, caracter in enumerate(salida):
            if caracter.isalpha():
                salida = salida[:i] + caracter.upper() + salida[i + 1:]
                break
        return salida
