"""El método de ganchos aplicado al código — selección y auditoría.

La skill `ganchos-y-retencion` tiene el método completo y el banco de 320 para uso
conversacional. Esto es la parte que corre sola: elegir la categoría correcta según
el nivel de conciencia, y auditar un guión ya escrito contra las reglas que sí
tienen evidencia detrás.

REGLA CERO: no se elige el gancho, se elige el nivel de conciencia y el nivel
decide el gancho (Schwartz, 1966).

Lo que este módulo NO hace: escribir ganchos. Los ganchos se escriben a mano sobre
un hecho real. Un gancho generado sin hecho detrás es una promesa impagable.
"""

from __future__ import annotations

import json
import re
from typing import Any

from .paths import CONFIG_DIR

# ---------------------------------------------------------------------------
# Niveles de conciencia y qué categoría sirve en cada uno
# ---------------------------------------------------------------------------

NIVELES: dict[str, dict[str, Any]] = {
    "unaware": {
        "descripcion": "No sabe que tiene el problema",
        "sirve": ["curiosidad", "historia", "contrarian"],
        "prohibido": ["oferta", "precio", "escasez"],
    },
    "problem": {
        "descripcion": "Siente el dolor, no conoce la solución",
        "sirve": ["dolor_nombrado", "callout"],
        "prohibido": ["detalles_de_producto"],
    },
    "solution": {
        "descripcion": "Sabe que existe un tipo de solución",
        "sirve": ["promesa_con_plazo", "especificidad"],
        "prohibido": ["curiosidad"],
    },
    "product": {
        "descripcion": "Te conoce, duda entre opciones",
        "sirve": ["prueba", "especificidad"],
        "prohibido": ["educacion_basica"],
        # El defecto admitido no es una categoría: es un movimiento que se monta
        # sobre cualquiera de las dos, al final del video.
        "movimientos": ["defecto_admitido"],
    },
    "most_aware": {
        "descripcion": "Ya quiere, falta el empujón",
        # Oferta, escasez y plazo son modificadores de la promesa y del precio,
        # no categorías propias. Las categorías que los vehiculan son estas dos.
        "sirve": ["promesa_con_plazo", "especificidad"],
        "movimientos": ["oferta", "escasez", "plazo"],
        # Curiosidad a un público most aware es tirar la impresión a la basura.
        "prohibido": ["curiosidad"],
    },
}

# Las ocho categorías reales. Toda lista de "100 hooks" es una de estas
# rellenada con sinónimos.
CATEGORIAS: dict[str, dict[str, Any]] = {
    "curiosidad": {
        "nombre": "Brecha de curiosidad",
        "objetivo": "alcance",
        "advertencia": "Gana atención, pierde compradores. Caples la midió última en conversión.",
    },
    "callout": {
        "nombre": "Callout de identidad",
        "objetivo": "ambos",
        "advertencia": "La más subestimada. Si le habla a más de un millón de personas, está mal escrita.",
    },
    "dolor_nombrado": {
        "nombre": "Dolor nombrado",
        "objetivo": "ambos",
        "advertencia": "Con hora y lugar. Si no se puede filmar, no es dolor nombrado: es miedo genérico, y repele.",
    },
    "promesa_con_plazo": {
        "nombre": "Promesa con plazo y sin sacrificio",
        "objetivo": "conversion",
        "advertencia": "Resultado + plazo + el sacrificio que NO hay que hacer. El tercero es el que casi todos omiten.",
    },
    "contrarian": {
        "nombre": "Contrarian / inversión de creencia",
        "objetivo": "alcance",
        "advertencia": "Gana alcance, castiga confianza. Se atacan prácticas, nunca personas ni marcas.",
    },
    "especificidad": {
        "nombre": "Especificidad numérica",
        "objetivo": "conversion",
        "advertencia": "El mecanismo es la precisión implausible, no el número. Si redondeás, perdés la categoría.",
    },
    "prueba": {
        "nombre": "Prueba / autoridad",
        "objetivo": "conversion",
        "advertencia": "La que el espectador verifica solo. Nada de autoridad autoproclamada.",
    },
    "historia": {
        "nombre": "Historia / entrada en escena",
        "objetivo": "alcance",
        "advertencia": "Se entra dentro, nunca se anuncia. Apaga la contraargumentación (ρ = −.20).",
    },
}

# Categorías que nunca deben ir en un creativo que tiene que cerrar la venta
PROHIBIDAS_EN_CONVERSION = ["curiosidad"]

# Formato: en Reels el pico de alcance está entre 30 y 60 segundos, y cae por
# encima de 2 minutos. Los recomendadores corrigen el duration bias.
RANGO_OPTIMO_S = (30, 60)

# El gancho explica el 21% de la varianza en conversión en ecommerce
# (Meta Platforms + Universidad de Maryland, ~220.000 videos).
VARIANZA_DEL_GANCHO = {
    "automovil": 0.66, "cpg": 0.50, "salud": 0.33,
    "entretenimiento": 0.25, "ecommerce": 0.21,
}

# Marca y mensaje en los primeros 5 segundos: 1,7x más intención de compra.
# Branding distribuido a lo largo del video: 1,8x.
SEGUNDOS_PARA_LA_MARCA = 5

# Complicación (el "PERO") antes del segundo 12 — trama imaginable, ρ = .29
SEGUNDOS_PARA_LA_COMPLICACION = 12

# El gancho tiene 6 segundos, no 3. Los 3 segundos eran un umbral de
# facturación de Facebook, no un hallazgo de atención.
SEGUNDOS_DE_GANCHO = 6


def categorias_para(nivel: str, objetivo: str = "ambos") -> list[str]:
    """Categorías válidas para un nivel de conciencia y un objetivo.

    `objetivo` es 'alcance' o 'conversion'. Un creativo que tiene que cerrar
    nunca lleva curiosidad, aunque el nivel de conciencia la permita.
    """
    if nivel not in NIVELES:
        disponibles = ", ".join(NIVELES)
        raise KeyError(f"Nivel '{nivel}' no existe. Hay: {disponibles}")

    candidatas = list(NIVELES[nivel]["sirve"])

    if objetivo == "conversion":
        candidatas = [c for c in candidatas if c not in PROHIBIDAS_EN_CONVERSION]
        candidatas = [
            c for c in candidatas
            if CATEGORIAS.get(c, {}).get("objetivo") in ("conversion", "ambos")
        ]
    elif objetivo == "alcance":
        candidatas = [
            c for c in candidatas
            if CATEGORIAS.get(c, {}).get("objetivo") in ("alcance", "ambos")
        ]

    return candidatas


# ---------------------------------------------------------------------------
# El banco de 320
# ---------------------------------------------------------------------------

# Marcas cuyos ganchos aplican a Feria Effix: el avatar del evento —emprendedor
# de ecommerce LATAM que factura entre mil y cinco mil al mes— es el mismo de
# @alexemprendee. Los de @militougc (skincare, UGC) no aplican.
MARCAS_PARA_EFFIX = ("alexander", "generico")


def cargar_banco() -> list[dict[str, Any]]:
    """Los 320 ganchos, parseados del banco de la skill."""
    ruta = CONFIG_DIR / "banco_ganchos.json"
    if not ruta.exists():
        raise FileNotFoundError(
            f"No encuentro {ruta.name}. Se genera parseando "
            f".claude/skills/ganchos-y-retencion/references/banco-320.md"
        )
    with ruta.open(encoding="utf-8") as fh:
        return json.load(fh)["ganchos"]


def buscar(
    nivel: str | None = None,
    objetivo: str | None = None,
    marca: str | None = None,
    categoria: str | None = None,
    solo_effix: bool = False,
    sin_variables: bool = False,
) -> list[dict[str, Any]]:
    """Filtra el banco. Sin filtros devuelve los 320.

    El flujo del método es: nivel de conciencia → objetivo → lo que queda son
    los candidatos. `solo_effix` descarta los ganchos de @militougc.
    """
    ganchos = cargar_banco()

    if nivel:
        ganchos = [g for g in ganchos if g["nivel"] == nivel]
    if objetivo:
        ganchos = [g for g in ganchos if g["objetivo"] == objetivo]
    if marca:
        ganchos = [g for g in ganchos if g["marca"] == marca]
    if categoria:
        ganchos = [g for g in ganchos if g["categoria"] == categoria]
    if solo_effix:
        ganchos = [g for g in ganchos if g["marca"] in MARCAS_PARA_EFFIX]
    if sin_variables:
        ganchos = [g for g in ganchos if not g["tiene_variables"]]

    return ganchos


def candidatos(nivel: str, objetivo: str, solo_effix: bool = True) -> list[dict[str, Any]]:
    """Los ganchos que sirven para un nivel y un objetivo, ya cruzados con el método.

    Aplica las dos capas: primero las categorías que el nivel de conciencia
    permite, después el filtro de objetivo. Un creativo de conversión nunca
    recibe curiosidad, aunque el banco tenga ganchos de curiosidad en ese nivel.
    """
    permitidas = categorias_para(nivel, objetivo)
    return [
        g for g in buscar(nivel=nivel, objetivo=objetivo, solo_effix=solo_effix)
        if g["categoria"] in permitidas
    ]


# ---------------------------------------------------------------------------
# Auditoría de un guión ya escrito
# ---------------------------------------------------------------------------

# Meta rechaza creativos que afirman una característica personal del espectador.
# "Sos desordenado" tumba el anuncio; "son las once y todavía estás contestando
# WhatsApps" no. Se describe la SITUACIÓN, nunca a la persona.
PATRONES_ATRIBUTO_PERSONAL = [
    r"\bsos\s+(?:un[ao]?\s+)?\w+",
    r"\beres\s+(?:un[ao]?\s+)?\w+",
    r"\bt[uú]\s+problema\s+es\s+que\s+sos\b",
    r"\bno\s+serv[ií]s\b",
    r"\bten[ée]s\s+la\s+culpa\b",
]

# Excepciones: construcciones que usan "sos/eres" sin atribuir un defecto
EXCEPCIONES_ATRIBUTO = [
    r"\bsos\s+(?:vos\s+)?(?:el|la|quien)\b",
    r"\beres\s+(?:el|la|quien)\b",
]


def auditar_guion(
    beats: list[dict[str, Any]],
    nivel: str,
    objetivo: str,
    marca: str = "Effix",
    duracion_total_s: int | None = None,
) -> dict[str, Any]:
    """Corre las reglas con evidencia sobre un guión completo.

    Devuelve hallazgos separados en `errores` (rompen una regla dura) y
    `avisos` (contradicen un hallazgo medido, pero pueden ser decisión
    deliberada).
    """
    errores: list[str] = []
    avisos: list[str] = []

    if not beats:
        return {"errores": ["El guión no tiene beats."], "avisos": [], "ok": False}

    total = duracion_total_s or sum(b.get("duracion_s", 4) for b in beats)

    # -- 1. Formato: pico de alcance entre 30 y 60 segundos ----------------
    piso, techo = RANGO_OPTIMO_S
    if not piso <= total <= techo:
        avisos.append(
            f"Duración {total}s fuera del pico de alcance en Reels ({piso}-{techo}s). "
            f"Por encima de 2 minutos el alcance cae."
        )

    # -- 2. La marca, en los primeros 5 segundos ---------------------------
    iniciales = [b for b in beats if b.get("t_inicio_s", 0) < SEGUNDOS_PARA_LA_MARCA]
    texto_inicial = " ".join(
        b.get("narracion", "") + " " + b.get("texto_pantalla", "")
        + " " + str(b.get("marca_en_pantalla", ""))
        for b in iniciales
    ).lower()

    if marca.lower() not in texto_inicial:
        segundo = _primer_segundo_con(beats, marca)
        avisos.append(
            f"La marca '{marca}' no aparece en los primeros {SEGUNDOS_PARA_LA_MARCA}s"
            + (f" (entra en el segundo {segundo})." if segundo is not None else ".")
            + " Marca y mensaje en los primeros 5s dan 1,7x más intención de compra "
              "(Meta + Toluna). Retrasar la marca es un consejo que la medición contradice."
        )

    # -- 3. Test ABT: complicación antes del segundo 12 --------------------
    if not _tiene_complicacion_temprana(beats):
        avisos.append(
            f"No se detecta una complicación (un 'pero') antes del segundo "
            f"{SEGUNDOS_PARA_LA_COMPLICACION}. Sin complicación no hay trama "
            f"imaginable, que es el ingrediente de más peso del transporte "
            f"narrativo (ρ = .29)."
        )

    # -- 4. Meta: situación, nunca la persona ------------------------------
    for beat in beats:
        for campo in ("narracion", "texto_pantalla"):
            texto = beat.get(campo, "")
            hallazgo = _atributo_personal(texto)
            if hallazgo:
                errores.append(
                    f"Beat {beat.get('beat', '?'):02d} ({campo}): '{hallazgo}' describe "
                    f"a la persona, no la situación. Meta rechaza creativos que afirman "
                    f"una característica personal del espectador."
                )

    # -- 5. Cifras redondas en categoría de especificidad ------------------
    redondas = _cifras_redondas(beats)
    if redondas:
        avisos.append(
            "Cifras redondas en la locución: "
            + ", ".join(redondas)
            + ". La precisión implausible es el mecanismo: una cifra rara implica "
              "que hubo medición. Si redondeás, perdés la categoría entera."
        )

    # -- 6. Blemishing: el defecto va al final y débil ----------------------
    if not _tiene_defecto_al_final(beats):
        avisos.append(
            "No hay un defecto admitido en el último tercio. Un negativo pequeño "
            "DESPUÉS del positivo aumenta la evaluación (Ein-Gar 2012). Al principio "
            "anula el efecto; grave, lo revierte."
        )

    # -- 7. Coherencia nivel / objetivo ------------------------------------
    try:
        validas = categorias_para(nivel, objetivo)
        if not validas:
            errores.append(
                f"No hay ninguna categoría válida para nivel '{nivel}' con objetivo "
                f"'{objetivo}'. Revisá la combinación."
            )
    except KeyError as exc:
        errores.append(str(exc))

    return {
        "errores": errores,
        "avisos": avisos,
        "ok": not errores,
        "duracion_s": total,
        "categorias_validas": categorias_para(nivel, objetivo) if nivel in NIVELES else [],
        "varianza_del_gancho": VARIANZA_DEL_GANCHO["ecommerce"],
        "nota": (
            "El gancho explica el 21% de la variación en conversión en ecommerce. "
            "El otro 79% está en el resto del video."
        ),
    }


# ---------------------------------------------------------------------------
# Internos
# ---------------------------------------------------------------------------

def _primer_segundo_con(beats: list[dict[str, Any]], marca: str) -> int | None:
    """En qué segundo entra la marca por primera vez."""
    for beat in beats:
        texto = (beat.get("narracion", "") + " " + beat.get("texto_pantalla", "")).lower()
        if marca.lower() in texto:
            return beat.get("t_inicio_s", 0)
    return None


# Marcadores de complicación: la conjunción adversativa que convierte una lista
# en una historia. "Y… y… y…" no es trama; "pero" sí.
MARCADORES_COMPLICACION = [
    "pero", "aunque", "sin embargo", "y aun así", "aun así",
    "resulta que", "hasta que", "salvo que", "o si",
]


def _tiene_complicacion_temprana(beats: list[dict[str, Any]]) -> bool:
    for beat in beats:
        if beat.get("t_inicio_s", 0) >= SEGUNDOS_PARA_LA_COMPLICACION:
            continue
        texto = beat.get("narracion", "").lower()
        if any(re.search(r"\b" + re.escape(m) + r"\b", texto) for m in MARCADORES_COMPLICACION):
            return True
        # Una pregunta que contrasta también abre la complicación
        if "?" in texto and any(p in texto for p in (" o ", "¿lo ", "¿y ")):
            return True
    return False


def _atributo_personal(texto: str) -> str | None:
    bajo = texto.lower()
    for patron in PATRONES_ATRIBUTO_PERSONAL:
        m = re.search(patron, bajo)
        if not m:
            continue
        fragmento = m.group(0)
        if any(re.search(exc, fragmento) for exc in EXCEPCIONES_ATRIBUTO):
            continue
        return fragmento
    return None


def _cifras_redondas(beats: list[dict[str, Any]]) -> list[str]:
    """Cifras que terminan en dos o más ceros: sospechosas de no haber sido medidas."""
    hallazgos: list[str] = []
    for beat in beats:
        for cifra in re.findall(r"\b\d[\d.,]*\b", beat.get("narracion", "")):
            limpio = cifra.replace(".", "").replace(",", "")
            if len(limpio) >= 3 and limpio.endswith("00"):
                hallazgos.append(f"beat {beat.get('beat', '?')}: {cifra}")
    return hallazgos


# Un defecto admitido suena a concesión, no a queja
MARCADORES_DEFECTO = [
    "no es para todos", "no es barato", "no te sirve si", "eso sí",
    "lo único", "la verdad es que no", "no vas a", "tampoco",
    "no incluye", "cuesta", "te lo digo",
]


def _tiene_defecto_al_final(beats: list[dict[str, Any]]) -> bool:
    """El blemishing solo funciona si el defecto va DESPUÉS del positivo."""
    if len(beats) < 3:
        return False
    ultimo_tercio = beats[int(len(beats) * 2 / 3):]
    for beat in ultimo_tercio:
        # Si el guión viene de una micro-situación, el componente lo dice exacto
        if beat.get("componente_microsituacion") == "defecto_admitido":
            return True
        # Si no, hay que olfatearlo por el texto
        texto = beat.get("narracion", "").lower()
        if any(m in texto for m in MARCADORES_DEFECTO):
            return True
    return False


def formatear(auditoria: dict[str, Any]) -> str:
    """Salida legible para el CLI."""
    lineas: list[str] = []
    if auditoria["errores"]:
        lineas.append("❌ Errores (rompen una regla dura):")
        lineas += [f"   · {e}" for e in auditoria["errores"]]
    if auditoria["avisos"]:
        lineas.append("⚠️  Avisos (contradicen un hallazgo medido):")
        lineas += [f"   · {a}" for a in auditoria["avisos"]]
    if not auditoria["errores"] and not auditoria["avisos"]:
        lineas.append("✅ El guión pasa todas las reglas del método.")
    return "\n".join(lineas)
