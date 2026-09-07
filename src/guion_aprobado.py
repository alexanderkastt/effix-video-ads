"""Carga y validación del formato único de guion aprobado.

`docs/FORMATO-GUION.md` define un solo JSON como frontera entre la parte
creativa (Cowork, a mano) y la producción (este repo). Aquí vive lo que el
productor comprueba **antes de gastar un peso**, para que la validación sea
una sola y no una copia por cada `_producir_*.py`.

La regla de fondo: si algo no cuadra, se dice qué y se para. El guion no se
arregla aquí — se devuelve a quien lo escribió.

Dos modos, con validaciones distintas donde tienen que serlo:

- `locucion`: la voz de ElevenLabs manda. La duración sale de las palabras
  divididas por `PALABRAS_POR_SEGUNDO` más el respiro por línea.
- `musical_sync`: la canción manda. `texto_tts` va vacío a propósito, así que
  contar palabras no dice nada; el techo real es cuánto video se generó
  (`n_clips × duracion_clip_s`) y el piso es lo que dure el tramo cantado.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .paths import CONFIG_DIR, env_float, load_brand_dna

FORMATO_ESPERADO = "guion-aprobado/1"
ESTADO_ESPERADO = "aprobado"

# Rango de duración de un ad, en segundos. Fuera de aquí no es un creativo de
# feed: por debajo no cabe la micro-situación, por encima se pierde el scroll.
DURACION_MIN_S = 30.0
DURACION_MAX_S = 60.0

MAX_PALABRAS_OVERLAY = 7

# Lo que ningún ad de Effix puede decir, por decisión comercial (sin descuentos
# ni códigos) y de comunicación (el taller no se menciona).
PROHIBIDAS_FIJAS = ("descuento", "effix20", "taller")

# Cámara lenta: sale lenta de verdad y arreglarlo en post cuesta calidad.
PROHIBIDAS_EN_PROMPT = ("slow", "deliberate", "slowest")

CIERRE_AUDIO = "no discernible speech"

# Separadores tipográficos que un overlay usa como adorno; no son palabras.
_ADORNOS = {"·", "|", "—", "–", "-", "+"}


@dataclass
class Resultado:
    """Lo que la validación encontró, separado por gravedad.

    `errores` para y `avisos` no: la diferencia es si producir con eso genera
    un ad inservible o solamente uno que hay que mirar con cuidado.
    """

    errores: list[str] = field(default_factory=list)
    avisos: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errores

    def texto(self) -> str:
        lineas = [f"🛑 {e}" for e in self.errores] + [f"⚠️  {a}" for a in self.avisos]
        if not lineas:
            return "✅ Las 6 reglas de docs/FORMATO-GUION.md pasan sin avisos."
        cabeza = (
            f"{len(self.errores)} error(es) y {len(self.avisos)} aviso(s):"
            if self.errores
            else f"Sin errores. {len(self.avisos)} aviso(s):"
        )
        return "\n".join([cabeza, *lineas])


def cargar(ruta: str | Path) -> dict[str, Any]:
    """Lee el JSON del guion. No valida nada todavía."""
    p = Path(ruta)
    if not p.exists():
        raise FileNotFoundError(f"No existe el guion {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def _palabras_de_overlay(texto: str) -> list[str]:
    return [t for t in texto.split() if t not in _ADORNOS]


def _estilos_registrados() -> set[str]:
    from .estilos_especiales import ESTILOS_ESPECIALES

    return set(ESTILOS_ESPECIALES)


def _moods_registrados() -> set[str]:
    ruta = CONFIG_DIR / "soundtracks.json"
    if not ruta.exists():
        return set()
    return set(json.loads(ruta.read_text(encoding="utf-8")).get("moods", {}))


def _regla_1(g: dict[str, Any], r: Resultado) -> None:
    if g.get("formato") != FORMATO_ESPERADO:
        r.errores.append(
            f"1· formato es {g.get('formato')!r}, se esperaba {FORMATO_ESPERADO!r}.")
    if g.get("estado") != ESTADO_ESPERADO:
        r.errores.append(
            f"1· estado es {g.get('estado')!r}: el productor sólo corre sobre "
            f"{ESTADO_ESPERADO!r}.")


def _regla_2(g: dict[str, Any], r: Resultado) -> None:
    from .narracion_hablada import CTA_POR_PASE
    from .nichos_effix import NICHOS

    # Dos series conviven en el formato: los guiones por nicho con nombre
    # ("abogados", "contadores") y los de la parrilla numerada, que traen
    # `nicho_mapa` (un indice) y `publico` en texto libre. Los segundos son
    # validos: describen a quien le hablan sin pasar por src/nichos_effix.py.
    if g.get("nicho") is not None:
        if g["nicho"] not in NICHOS:
            r.errores.append(
                f"2· nicho {g['nicho']!r} no existe en src/nichos_effix.py.")
    elif not (g.get("nicho_mapa") is not None and str(g.get("publico") or "").strip()):
        r.errores.append(
            "2· el guion no dice a quien le habla: falta `nicho` (de "
            "src/nichos_effix.py) o el par `nicho_mapa` + `publico`.")
    if g.get("pase") not in CTA_POR_PASE:
        r.errores.append(
            f"2· pase {g.get('pase')!r} no existe en CTA_POR_PASE. "
            f"Hay: {', '.join(CTA_POR_PASE)}.")

    estilo = g.get("estilo")
    if estilo not in _estilos_registrados():
        # No es error: un guion que trae su propio `bible` no necesita el
        # template del registro — los prompts ya vienen escritos y el estilo
        # viaja dentro del JSON. Sí lo es cuando además viene sin bible,
        # porque entonces nada define el look.
        if (g.get("bible") or "").strip():
            r.avisos.append(
                f"2· estilo {estilo!r} no está en src/estilos_especiales.py "
                f"({', '.join(sorted(_estilos_registrados()))}); el guion trae su "
                f"propio 'bible', así que se produce con ese.")
        else:
            r.errores.append(
                f"2· estilo {estilo!r} no está registrado y el guion no trae 'bible': "
                f"nada define el look de las imágenes.")

    # El mood sólo se usa cuando la música sale de la librería. En musical_sync
    # la pista es la canción del guion y el mood queda como dato informativo.
    if g.get("modo") != "musical_sync":
        moods = _moods_registrados()
        if moods and g.get("musica_mood") not in moods:
            r.errores.append(
                f"2· musica_mood {g.get('musica_mood')!r} no está en "
                f"config/soundtracks.json ({', '.join(sorted(moods))}).")


def _regla_3(g: dict[str, Any], r: Resultado) -> None:
    from .narracion_hablada import validar_coherencia_de_pase

    dna = load_brand_dna(g.get("marca", "effix"))
    prohibidas = [p.lower() for p in dna.get("palabras_prohibidas", [])]
    prohibidas += list(PROHIBIDAS_FIJAS)

    hablado: list[str] = []
    for linea in g.get("lineas", []):
        # Todo lo que el espectador va a oír o leer. Los prompts van en inglés
        # y se revisan en la regla 4.
        visible = " ".join(
            str(linea.get(c) or "")
            for c in ("texto", "texto_tts", "texto_pantalla")
        )
        hablado.append(str(linea.get("texto") or ""))
        bajo = visible.lower()
        for mala in prohibidas:
            if re.search(rf"\b{re.escape(mala)}\b", bajo):
                r.errores.append(
                    f"3· línea {linea.get('n')}: dice {mala!r}, que está prohibida.")

    # La letra completa también, no sólo las líneas: en musical_sync es lo que
    # de verdad se canta, y las líneas son un reflejo de ella.
    letra = str((g.get("musica") or {}).get("suno_custom_lyrics") or "")
    if letra:
        for mala in prohibidas:
            if re.search(rf"\b{re.escape(mala)}\b", letra.lower()):
                r.errores.append(f"3· la letra de la canción dice {mala!r}.")
        hablado += [l for l in letra.splitlines() if l.strip() and not l.startswith("[")]

    for problema in validar_coherencia_de_pase(hablado, g.get("pase", "")):
        if problema != "OK":
            r.errores.append(f"3· {problema}")

    cta = " ".join(str(v) for v in (g.get("cta") or {}).values()).lower()
    for mala in prohibidas:
        if re.search(rf"\b{re.escape(mala)}\b", cta):
            r.errores.append(f"3· el CTA dice {mala!r}.")


def _regla_4(g: dict[str, Any], r: Resultado) -> None:
    for linea in g.get("lineas", []):
        n = linea.get("n")
        pv = str(linea.get("prompt_video") or "")
        if not pv:
            r.errores.append(f"4· línea {n}: sin prompt_video.")
            continue
        bajo = pv.lower()
        for mala in PROHIBIDAS_EN_PROMPT:
            if re.search(rf"\b{mala}\w*\b", bajo):
                r.errores.append(
                    f"4· línea {n}: prompt_video pide {mala!r} — sale cámara lenta real.")
        if CIERRE_AUDIO not in bajo:
            r.errores.append(
                f"4· línea {n}: prompt_video no cierra con '{CIERRE_AUDIO}'.")
        if "@image1" not in bajo:
            r.avisos.append(f"4· línea {n}: prompt_video no referencia @Image1.")

        pi = str(linea.get("prompt_imagen") or "")
        if not pi:
            r.errores.append(f"4· línea {n}: sin prompt_imagen.")
        elif re.search(r"\b(legible|readable|visible)\s+text\b", pi.lower()):
            r.errores.append(
                f"4· línea {n}: prompt_imagen pide texto legible; el modelo "
                f"inventa letras. El texto va en post.")


def _regla_5(g: dict[str, Any], r: Resultado) -> None:
    for linea in g.get("lineas", []):
        texto = linea.get("texto_pantalla") or ""
        textos = texto if isinstance(texto, list) else [texto]
        for t in textos:
            palabras = _palabras_de_overlay(str(t))
            if len(palabras) > MAX_PALABRAS_OVERLAY:
                r.errores.append(
                    f"5· línea {linea.get('n')}: overlay de {len(palabras)} palabras "
                    f"(máx {MAX_PALABRAS_OVERLAY}): {t!r}")


def duracion_estimada_s(g: dict[str, Any]) -> float:
    """Cuánto va a durar el ad, con la vara que corresponde a su modo.

    En `locucion` sale del texto: palabras entre la velocidad medida de la voz,
    más el respiro entre líneas. En `musical_sync` no hay texto que locutar, y
    lo único que se sabe antes de generar la canción es cuánto video se va a
    pagar — que es el techo duro del montaje.
    """
    lineas = g.get("lineas", [])
    if g.get("modo") == "musical_sync":
        return float(len(lineas) * duracion_clip_s(g))
    palabras = sum(len(str(l.get("texto_tts") or "").split()) for l in lineas)
    pps = env_float("PALABRAS_POR_SEGUNDO", 3.69)
    return round(palabras / pps + env_float("RESPIRO_S", 0.12) * len(lineas), 2)


def duracion_clip_s(g: dict[str, Any]) -> int:
    """Segundos que se le pagan a Kling por clip.

    Kling sólo vende tramos de 5 o 10s cuando no hay frame final, así que un
    guion musical sin keyframes se produce en clips de 5.
    """
    return int(g.get("duracion_clip_s") or 5)


def _regla_6(g: dict[str, Any], r: Resultado) -> None:
    dur = duracion_estimada_s(g)
    objetivo = float(g.get("duracion_objetivo_s") or 0)
    etiqueta = (
        "video generado" if g.get("modo") == "musical_sync" else "locución estimada"
    )
    if not DURACION_MIN_S <= dur <= DURACION_MAX_S:
        r.errores.append(
            f"6· {dur:.1f}s de {etiqueta} queda fuera de "
            f"{DURACION_MIN_S:.0f}–{DURACION_MAX_S:.0f}s.")
    if objetivo and not DURACION_MIN_S <= objetivo <= DURACION_MAX_S:
        r.errores.append(
            f"6· duracion_objetivo_s = {objetivo:.0f} queda fuera de "
            f"{DURACION_MIN_S:.0f}–{DURACION_MAX_S:.0f}s.")
    if objetivo and dur < objetivo - 0.5:
        r.avisos.append(
            f"6· hay {dur:.1f}s de {etiqueta} para un objetivo de {objetivo:.0f}s: "
            f"si la canción sale más larga, sobra audio sin imagen.")


def _regla_7_diccion(g: dict[str, Any], r: Resultado) -> None:
    """Palabras que el modelo de canto no sabe decir.

    No es una de las 6 reglas del formato: es la lección de la tanda 2, donde
    "resultados" costó cinco intentos de canción repartidos en cuatro pistas
    antes de que alguien se diera cuenta de que el modelo simplemente no sabe
    articularla. Comprobarlo aquí es gratis; descubrirlo generando, no.

    Va como aviso y no como error porque el que decide si una palabra se
    sacrifica es quien escribió la letra.
    """
    if g.get("modo") != "musical_sync":
        return
    from .audio_extra import PALABRAS_QUE_NO_CANTA

    letra = str((g.get("musica") or {}).get("suno_custom_lyrics") or "")
    for palabra, sintoma in PALABRAS_QUE_NO_CANTA.items():
        veces = len(re.findall(rf"\b{palabra}\b", letra, re.IGNORECASE))
        if veces:
            r.avisos.append(
                f"7· la letra dice {palabra!r} {veces}× y el modelo la deforma: "
                f"{sintoma}. Cámbiala antes de pagar la canción.")


def validar(g: dict[str, Any]) -> Resultado:
    """Las 6 reglas de docs/FORMATO-GUION.md, con evidencia línea a línea."""
    r = Resultado()
    for regla in (_regla_1, _regla_2, _regla_3, _regla_4, _regla_5, _regla_6,
                  _regla_7_diccion):
        try:
            regla(g, r)
        except Exception as exc:  # una regla rota no puede tapar a las demás
            r.errores.append(f"{regla.__name__}: {type(exc).__name__}: {exc}")
    return r


def estimar_costo(g: dict[str, Any], *, modelo_video: str, modelo_imagen: str,
                  costo_extras: float = 0.0) -> dict[str, Any]:
    """Costo con los parámetros REALES del guion, no con los de ejemplo.

    Cuenta lo que de verdad se va a pagar: los clips a su duración final, la
    imagen héroe además de las de escena, los keyframes finales si los hay, y
    la canción si el modo es musical.
    """
    from . import cost_estimator

    lineas = g.get("lineas", [])
    keyframes = sum(1 for l in lineas if l.get("prompt_keyframe_final"))
    # Escenas + la héroe que sirve de referencia a todas + los keyframes finales.
    n_imagenes = len(lineas) + 1 + keyframes
    musical = g.get("modo") == "musical_sync"
    caracteres = 0 if musical else sum(
        len(str(l.get("texto_tts") or "")) for l in lineas)

    return cost_estimator.estimar(
        n_clips=len(lineas),
        duracion_clip_s=duracion_clip_s(g),
        modelo_fal=modelo_video,
        caracteres_voz=caracteres,
        n_imagenes=n_imagenes,
        modelo_imagen=modelo_imagen,
        modelo_cancion=(g.get("musica") or {}).get("modelo") if musical else None,
        duracion_cancion_ms=(g.get("musica") or {}).get("duracion_ms"),
        costo_extras=costo_extras,
    )
