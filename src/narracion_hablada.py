"""Versión HABLADA de cada micro-situación — lo que la voz dice de verdad.

La micro-situación completa (`microsituaciones.py`) es material de investigación:
larga, específica, escrita para que el equipo entienda el momento. Medida, dura
76-88 segundos de locución. No es guión, es research.

Esto es el guión: la misma micro-situación dicha en voz alta, dentro del
presupuesto real de un ad con corte cada 4 segundos. La guía ya hace esa
distinción con el hook ("el momento" se investiga, el hook es su versión
hablada); aquí se aplica a los once beats.

PRESUPUESTO — de dónde sale el techo de 8 palabras
    2.2 palabras por segundo de locución en español (MASTER_CONTEXT.md).
    Un clip dura 4 segundos → 4 × 2.2 = 8.8 palabras.
    Techo práctico: 8 palabras por línea (3.64s), dejando ~0.4s de aire.

    A 9 palabras la línea ya pide 4.09s y se lleva un segundo clip: el video
    salta de 44s a 48s por una sola palabra. Por eso el límite es duro.

    11 beats × 1 clip = 11 clips × 4s = 44s, dentro del rango 30-60s.
    Locución ~40s sobre 44s de video: ~4s de aire repartido entre beats, que
    es la respiración natural entre frases, no silencio muerto.

Un beat que necesite más de 8 palabras ocupará dos clips — dos escenas
distintas contando el mismo beat. El corte visual sigue cayendo cada 4s.
"""

from __future__ import annotations

# Cada lista tiene 11 entradas, una por beat, en el orden del MAPEO_BEATS:
# momento · síntoma · reacción · explicación fallida · patrón · causa raíz ·
# mecanismo · prueba social · visualización · urgencia+CTA · loop
#
# Ninguna línea pasa de 8 palabras. `validar_presupuesto()` lo verifica.
HABLADO: dict[str, list[str]] = {
    "comunidad_que_no_tienes": [
        "¿Los que crecen rápido siempre conocen a alguien?",
        "Alguien sabe algo que tú no sabes.",
        "¿Lo haces mal, o te faltó gente?",
        "Dices que es suerte. O más capital.",
        "Siempre igual: el que crece tiene a alguien.",
        "No es capital ni suerte. Es acceso.",
        "Salas llenas de quienes ya lo resolvieron.",
        "Más de trescientas cincuenta marcas confirmadas.",
        "Sales con tres contactos que sí contestan.",
        "Del quince al diecinueve. Apártalo en feriaeffix.com.",
        "No es barato. Y no es para principiantes.",
        "Y ya no miras el grupo desde afuera.",
    ],
    "no_esta_en_cursos": [
        "¿Cuántos cursos llevas y facturas lo mismo?",
        "Lo entendiste, tomaste notas, y nada cambió.",
        "Pero la duda ya no es del curso.",
        "Dices que necesitas otro curso más específico.",
        "Siempre te atascas donde ningún video llega.",
        "El curso da teoría. Necesitas a alguien resolviendo.",
        "Con quienes tienen tu mismo problema, en vivo.",
        "Doscientos ponentes. Doscientas conferencias y talleres.",
        "Preguntas en voz alta y te responden.",
        "Plaza Mayor, Medellín. Apártalo en feriaeffix.com.",
        "No te damos plantillas. Son conversaciones.",
        "Y el próximo curso ya es para repasar.",
    ],
    "latam_unido": [
        "¿Tus ventas caben todas en la misma frontera?",
        "Pero no faltan ganas: falta un contacto.",
        "Te dices que primero hay que consolidar aquí.",
        "Dices que la logística es un lío.",
        "Dos años igual, y aquí hay más competencia.",
        "La frontera no es logística. Es contacto.",
        "Cinco países en el mismo salón.",
        "Colombia, Ecuador, República Dominicana, Costa Rica, Guatemala.",
        "Tu primera venta afuera, sabiendo a quién preguntar.",
        "Del quince al diecinueve. Apártalo en feriaeffix.com.",
        "No cubre el vuelo. Solo lo de adentro.",
        "Y el reporte ya no cabe en uno.",
    ],
    "competencia_va": [
        "¿Cuántos de tu competencia ya reservaron octubre?",
        "Pero van a una conversación que vos no.",
        "Sientes que el mercado va más rápido.",
        "Dices que está caro. Que YouTube alcanza.",
        "Cada evento perdido se lo ganó alguien más.",
        "La información está en internet. El contexto no.",
        "Ahí se reparten los contactos del año.",
        "Trescientas cincuenta marcas. Doscientos ponentes.",
        "En noviembre cuentas lo que trajiste.",
        "Plaza Mayor, Medellín. Apártalo en feriaeffix.com.",
        "Hay que sacar la agenda. No es online.",
        "Y tu competencia no será la única.",
    ],
    "proveedores": [
        "¿Le escribes martes y contesta el viernes?",
        "No sabes si sirve hasta que llega.",
        "Terminas desconfiando, y eso te frena.",
        "Dices que te tocó uno malo, nada más.",
        "Pero cada trimestre repites el mismo ciclo.",
        "No es el proveedor. Lo eliges por foto.",
        "Stands, muestras físicas, y preguntas de frente.",
        "Cinco países en el mismo recinto.",
        "Cierras con el producto en la mano.",
        "Del quince al diecinueve. Apártalo en feriaeffix.com.",
        "No todos los stands te van a servir.",
        "Y ya sabes quién contesta el martes.",
    ],
    "herramientas": [
        "¿Nueve de la noche copiando datos a mano?",
        "Se hace, pero cada mes toma más horas.",
        "Sospechas que hay otra forma. No cuál.",
        "Dices que cambiar es un lío. Después.",
        "Cuatro trimestres diciendo después. Las horas suman.",
        "No es que no existan. Nadie te mostró.",
        "Las ves funcionando en vivo, con datos reales.",
        "Cinco países comparando lo mismo.",
        "Ese martes en la noche queda libre.",
        "Del quince al diecinueve. Apártalo en feriaeffix.com.",
        "Ninguna herramienta se instala sola. Hay que sentarse.",
        "Y a las nueve ya no copias nada.",
    ],
    "de_cero_a_referente": [
        "¿Otra vez explicando en dos frases qué haces?",
        "Pero no falta resultado. Falta quien empuje.",
        "Y dudas tú, porque nadie cerca lo valida.",
        "Dices que son de otra generación.",
        "Cuando te atascas, no tienes a quién preguntar.",
        "No es disciplina. Es no tener referentes cerca.",
        "Casos contados con los números encima.",
        "Cinco países llevando el suyo, en octubre.",
        "En dos años cuentas el tuyo.",
        "Plaza Mayor, Medellín. Apártalo en feriaeffix.com.",
        "No salís siendo referente por ir una vez.",
        "Y tu historia ya no cabe en dos.",
    ],
    "no_tengo_con_quien_ir": [
        "¿Te interesó y pensaste con quién ir?",
        "No es el evento. Es entrar sin nadie.",
        "Pero da pena decirlo en voz alta.",
        "Te decís que mejor esperás la próxima.",
        "Tercera vez que lo decidís. Seguís igual.",
        "No se va acompañado. Se va a conseguir.",
        "Hay mesas donde te sentás con desconocidos.",
        "Trescientas cincuenta marcas. Nadie conoce a todos.",
        "Salís el domingo con tres números nuevos.",
        "Del quince al diecinueve. Apártalo en feriaeffix.com.",
        "Los primeros treinta minutos son incómodos. Después no.",
        "Y a la próxima ya no vas solo.",
    ],
    "vale_lo_que_cuesta": [
        "¿Viste el precio y cerraste la pestaña?",
        "No es la plata. No sabés qué traés.",
        "Pero no arriesgás en algo que no medís.",
        "Te decís que con eso pagás pauta.",
        "Meses metiéndole a pauta, y seguís frenado.",
        "Pero no comprás entrada. Comprás acceso.",
        "Doscientas conferencias. Mil pesos cada una.",
        "Trescientas cincuenta marcas y doscientos ponentes.",
        "Un solo contacto útil ya lo pagó.",
        "Del quince al diecinueve. Apártalo en feriaeffix.com.",
        "Es plata de verdad. Nadie dice lo contrario.",
        "Y la pestaña que cerraste era la barata.",
    ],
    "por_que_octubre": [
        "¿Abriste el plan de enero, sigue a medias?",
        "Pero trabajaste. Lo que llegó fue el trimestre.",
        "Sientes que el año se fue operando.",
        "Dices que el otro mes sí arrancas.",
        "Tercer año llegando con el mismo plan.",
        "No es el plan. Nunca reservas los días.",
        "Octubre cae antes de la temporada que factura.",
        "Cinco países, del quince al diecinueve, Plaza Mayor.",
        "Llegas a noviembre con la campaña lista.",
        "Plaza Mayor, Medellín. Apártalo en feriaeffix.com.",
        "Es en octubre. Si no podés, no insistas.",
        "Y el plan de enero ya estará hecho.",
    ],
}

# Techo por línea: a 2.2 palabras/segundo, 8 palabras = 3.64s y caben en un
# clip de 4s. A 9 ya pide 4.09s y se lleva un clip entero de más.
MAX_PALABRAS_POR_LINEA = 8


def hablado_de(angulo: str) -> list[str]:
    """Las 11 líneas habladas de un ángulo."""
    if angulo not in HABLADO:
        disponibles = ", ".join(sorted(HABLADO))
        raise KeyError(f"No hay narración hablada para '{angulo}'. Hay: {disponibles}")
    return HABLADO[angulo]


def validar_presupuesto() -> list[str]:
    """Verifica que ninguna línea se pase del techo de palabras.

    Una línea de más rompe el formato en silencio: agrega 4 segundos al video
    y desalinea el corte con el audio.
    """
    errores: list[str] = []

    for pase, cta in CTA_POR_PASE.items():
        n = len(cta["hablado"].split())
        if n > MAX_PALABRAS_POR_LINEA:
            errores.append(
                f"CTA de {pase}: {n} palabras ({n / 2.2:.1f}s) — "
                f"techo {MAX_PALABRAS_POR_LINEA}. Se lleva un clip extra."
            )
        if len(cta["overlay"].split()) > 7:
            errores.append(
                f"CTA de {pase}: overlay de {len(cta['overlay'].split())} palabras "
                f"(máximo 7)."
            )

    for angulo, lineas in HABLADO.items():
        if len(lineas) != 12:
            errores.append(f"{angulo}: {len(lineas)} líneas, se esperan 12.")
        for i, linea in enumerate(lineas, start=1):
            n = len(linea.split())
            if n > MAX_PALABRAS_POR_LINEA:
                errores.append(
                    f"{angulo} beat {i:02d}: {n} palabras "
                    f"({n / 2.2:.1f}s) — techo {MAX_PALABRAS_POR_LINEA}. "
                    f"Se lleva un clip extra."
                )
    return errores or ["OK"]


# ---------------------------------------------------------------------------
# El CTA depende del pase que se esté vendiendo
# ---------------------------------------------------------------------------

# El beat 10 (URGENCIA + CTA) es el único que cambia según el producto. Todo lo
# demás describe el evento y sirve para los dos pases.
#
# Regla: el evento dura cinco días, pero el pase principal da acceso a TRES.
# Un creativo que vende el pase de 3 no puede prometer los cinco.
CTA_POR_PASE: dict[str, dict[str, str]] = {
    # Producto principal. Las fechas concretas convierten mejor que "tres días",
    # y que caiga viernes-domingo es argumento contra "no puedo dejar el trabajo".
    "pase_3_dias": {
        "hablado": "Viernes a domingo. Ni pedís permiso.",
        "overlay": "16–18 oct · Pase 3 días",
        "dias": "3",
    },
    # Mientras el taller del 3 de septiembre siga en pie, esta es la urgencia
    # real del embudo: está incluido en el pase y ocurre ANTES del evento.
    # Después del 3 de septiembre, volver a `pase_3_dias`.
    "pase_3_dias_taller": {
        "hablado": "Comprá antes del tres y entrás al taller.",
        "overlay": "Taller IA · 3 sept",
        "dias": "3",
    },
    # Upsell. No para pauta fría: se vende por acceso y sin filas, no por días.
    "vip_5_dias": {
        "hablado": "VIP: sin filas y los días exclusivos.",
        "overlay": "VIP · 15–19 oct",
        "dias": "5",
    },
    # Cuando el creativo no empuja un pase concreto sino la página
    "generico": {
        "hablado": "Quince al diecinueve de octubre. Plaza Mayor.",
        "overlay": "15–19 oct · Plaza Mayor",
        "dias": "",
    },
}

PASE_POR_DEFECTO = "pase_3_dias"


def cta_de(pase: str = PASE_POR_DEFECTO) -> dict[str, str]:
    """El CTA hablado y su overlay para el pase que se está vendiendo."""
    if pase not in CTA_POR_PASE:
        disponibles = ", ".join(CTA_POR_PASE)
        raise KeyError(f"Pase '{pase}' no existe. Hay: {disponibles}")
    return CTA_POR_PASE[pase]


def validar_coherencia_de_pase(lineas: list[str], pase: str) -> list[str]:
    """Ninguna línea puede prometer más días de los que da el pase.

    El error que esto evita: el evento dura cinco días y es tentador decirlo,
    pero quien compra el pase de tres recibe tres. Prometer cinco en ese
    creativo es publicidad que el producto no cumple.
    """
    import re

    dias = int(CTA_POR_PASE.get(pase, {}).get("dias") or 5)
    if dias >= 5:
        return ["OK"]

    errores: list[str] = []
    patron = re.compile(r"\bcinco d[ií]as\b|\b5 d[ií]as\b", re.IGNORECASE)
    for i, linea in enumerate(lineas, start=1):
        if patron.search(linea):
            errores.append(
                f"beat {i:02d}: '{linea}' promete cinco días, pero "
                f"{CTA_POR_PASE[pase]['overlay']} da {dias}."
            )
    return errores or ["OK"]
