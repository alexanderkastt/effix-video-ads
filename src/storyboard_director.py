"""Director de storyboard — integra micro-situación + estilo en la ficha de rodaje.

Para cada beat produce la ficha completa de producción: narración, overlay,
componente de micro-situación activo, prompt de imagen base, prompt I2V, tipo de
clip (A/B/C), notas de director, modelos recomendados y costo estimado.

Cada estilo tiene su propio pipeline de prompts. Usar el template de UGC para
generar prompts de crochet produce basura: los modelos los interpretan de forma
completamente distinta. Por eso `dirigir_estilo()` enruta por estilo en vez de
tener una sola plantilla.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from . import cost_estimator
from .estilos_especiales import ESTILOS_ESPECIALES
from .paths import GUIONES_DIR, STORYBOARDS_DIR, ensure_dirs, load_brand_tokens
from .plan_clips import DURACION_CLIP_S, expandir_a_clips, planificar
from .scene_builder import ESTILOS as ESTILOS_GENERICOS
from .scene_builder import SceneBuilder

PALETA_FALLBACK = {
    "primario": "#E31B23", "secundario": "#1A1A2E",
    "acento": "#FFD700", "texto": "#FFFFFF",
}

# Tipo de clip por beat. Los beats de cambio de estado piden frame inicial + final;
# los de reconocimiento se sostienen con movimiento mínimo.
TIPO_CLIP_POR_BEAT = {
    1: "A",   # el momento se abre y resuelve dentro del clip
    2: "C",   # reconocimiento — movimiento mínimo, la cara hace el trabajo
    3: "C",
    4: "A",
    5: "A",
    6: "B",   # causa raíz: cambio de estado, el giro se ve
    7: "B",   # mecanismo: transición concreta
    8: "A",
    9: "A",
    10: "C",  # CTA sostenido
    11: "B",  # el loop cierra en un estado distinto al del beat 01
}


def _slug(texto: str, largo: int = 40) -> str:
    normal = unicodedata.normalize("NFKD", texto)
    sin_tildes = "".join(c for c in normal if not unicodedata.combining(c))
    limpio = re.sub(r"[^a-zA-Z0-9]+", "-", sin_tildes).strip("-").lower()
    return (limpio[:largo].rstrip("-")) or "video"


class StoryboardDirector:
    """Dirige cada beat según su estilo y arma el paquete de producción."""

    def __init__(self, marca: str = "effix") -> None:
        self.marca = marca
        tokens = load_brand_tokens(marca)
        self.colores = {**PALETA_FALLBACK, **tokens.get("colores", {})}
        ensure_dirs()

    # -- API principal ------------------------------------------------------

    def generar(
        self,
        beats: list[dict[str, Any]],
        estilo: str = "micro_doc_ugc",
        marca: str = "effix",
        micro_situacion: Any = None,
        concepto: str = "",
    ) -> dict[str, Any]:
        """Dirige todos los beats y escribe HTML + JSON. Devuelve el paquete.

        Los beats se expanden primero a clips de 4 segundos: la unidad de corte
        es el clip, no el beat. Un beat que habla más de 4s ocupa dos clips —
        dos escenas distintas del mismo beat — para que el cambio de escena
        siga cayendo cada 4 segundos.
        """
        plan = planificar(beats)
        clips = expandir_a_clips(beats)
        dirigidos = [
            self.dirigir_estilo(estilo, clip, micro_situacion) for clip in clips
        ]

        modelos = self._modelos(estilo)
        caracteres = sum(len(b.get("narracion", "")) for b in dirigidos)
        est = cost_estimator.estimar(
            n_clips=len(dirigidos),
            duracion_clip_s=dirigidos[0]["duracion_s"] if dirigidos else 4,
            modelo_fal=modelos["video"],
            caracteres_voz=caracteres,
            con_musica=False,
        )

        paquete = {
            "job_id": str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "concepto": concepto or (micro_situacion.etiqueta if micro_situacion else ""),
            "estilo": estilo,
            "marca": marca,
            "angulo": getattr(micro_situacion, "angulo", ""),
            "estado": "pendiente_aprobacion",
            "beats": dirigidos,
            "modelos": modelos,
            "duracion_total_s": plan["duracion_s"],
            "total_clips": plan["total_clips"],
            "duracion_clip_s": DURACION_CLIP_S,
            "plan_clips": plan,
            "costo_estimado_usd": est["total"],
            "costo_verificado": est["verificado"],
            "datos_sin_verificar": getattr(micro_situacion, "datos_sin_verificar", []),
            "plan_duracion": (
                micro_situacion.plan_de_duracion(
                    dirigidos[0]["duracion_s"] if dirigidos else 4, len(dirigidos)
                )
                if hasattr(micro_situacion, "plan_de_duracion")
                else {}
            ),
        }

        paquete["html_path"] = str(self._escribir_html(paquete))
        paquete["json_path"] = str(self._escribir_json(paquete))
        return paquete

    def dirigir_estilo(
        self, estilo: str, beat: dict[str, Any], micro_situacion: Any = None
    ) -> dict[str, Any]:
        """Aplica las reglas del estilo a un beat y devuelve la ficha completa."""
        b = dict(beat)
        b.setdefault("duracion_s", DURACION_CLIP_S)
        b["tipo_clip"] = TIPO_CLIP_POR_BEAT.get(b.get("beat_origen", b["beat"]), "A")
        b["estilo"] = estilo

        # La marca entra desde el primer clip como identidad visual, no como
        # locución: marca y mensaje en los primeros 5s dan 1,7x más intención de
        # compra, y el branding distribuido a lo largo del video 1,8x.
        b["marca_en_pantalla"] = self.marca
        b["branding_visible"] = True

        # Segunda escena de un mismo beat: cambia el encuadre para que el corte
        # se lea como corte y no como un salto de continuidad en el mismo plano.
        if b.get("escena_del_beat", 1) > 1:
            b["movimiento_camara"] = self._encuadre_alterno(b.get("movimiento_camara", "handheld"))

        if estilo == "crochet":
            b.update(self._dirigir_crochet(b, micro_situacion))
        elif estilo == "skeleton":
            b.update(self._dirigir_skeleton(b, micro_situacion))
        elif estilo == "zack_films":
            b.update(self._dirigir_zack(b, micro_situacion))
        elif estilo == "object_talk":
            b.update(self._dirigir_object_talk(b, micro_situacion))
        elif estilo == "micro_doc_ugc":
            b.update(self._dirigir_ugc(b, estilo, micro_situacion))
        elif estilo in ESTILOS_GENERICOS:
            b.update(self._dirigir_generico(b, estilo, micro_situacion))
        else:
            disponibles = sorted(set(ESTILOS_ESPECIALES) | set(ESTILOS_GENERICOS))
            raise KeyError(f"Estilo '{estilo}' no existe. Hay: {', '.join(disponibles)}")

        b["modelos"] = self._modelos(estilo)
        return b

    # -- pipelines por estilo ----------------------------------------------

    def _dirigir_crochet(self, beat: dict, ms: Any) -> dict[str, Any]:
        """5 partes en la imagen, 4 en el video, universales verbatim.

        El mundo se enmarca como diorama, nunca el personaje como 'crocheted man'.
        Las poses se simplifican: el modelo no renderiza dedos en lana.
        """
        c = ESTILOS_ESPECIALES["crochet"]
        luz = self._luz_crochet(beat["beat"])
        accion = self._accion_simple(beat["beat"])

        escena = (
            f"Stop-motion animation diorama scene, handmade knitted and crocheted "
            f"miniature world. Full-body small yarn-textured Latin American entrepreneur "
            f"character, early thirties, wearing a knitted casual shirt, {accion}, inside a "
            f"small crocheted {self._set_crochet(beat['beat'])}. Every element is a handmade "
            f"fabric prop physically crafted from wool and yarn."
        )

        prompt_imagen = (
            f"{escena}\n\n{c['universal_positivo']}\n\n"
            f"Lighting: {luz}.\n\nNegative: {c['universal_negativo']}"
        )

        movimiento = self._movimiento_crochet(beat["beat"])
        prompt_video = (
            f"{movimiento} The crocheted set and background stay completely still; "
            f"only the yarn fibers move slightly. Camera locked. {c['cierre_i2v']}"
        )

        nota = (
            f"Tipo {beat['tipo_clip']} — "
            f"{c['tipos_de_clip'][beat['tipo_clip']].split('—')[0].strip()}. "
            f"Pose simplificada a propósito: el modelo no renderiza dedos en lana."
        )

        return {
            "prompt_imagen": prompt_imagen,
            "prompt_video": prompt_video,
            "negative_prompt": c["universal_negativo"],
            "descripcion_visual": f"Diorama tejido: {accion}",
            "notas_produccion": nota,
            "palabras_prompt_video": len(prompt_video.split()),
        }

    def _dirigir_skeleton(self, beat: dict, ms: Any) -> dict[str, Any]:
        """Character Bible verbatim en cada prompt, sin texto en la generación."""
        s = ESTILOS_ESPECIALES["skeleton"]
        bible = s["character_bibles"][s["bible_por_defecto"]]
        bible = bible.replace("[THEME]", "modern LATAM trade-fair").replace(
            "[palette]", "warm amber and deep navy"
        )

        marcador = self._marcador_escalada(beat["beat"])
        accion = self._accion_simple(beat["beat"])

        prompt_imagen = (
            f"{bible} SHOT: the skeleton {accion}, {marcador}. "
            f"Setting: a busy trade-fair hall with booths and moving crowds. "
            f"Reference image 1 for the character. {s['negativo_texto']}."
        )
        prompt_video = (
            f"The skeleton {self._movimiento_skeleton(beat['beat'])}. "
            f"One camera move only: slow push-in. Characters do not speak. "
            f"{s['negativo_texto']}."
        )

        return {
            "prompt_imagen": prompt_imagen,
            "prompt_video": prompt_video,
            "negative_prompt": s["negativo_texto"],
            "descripcion_visual": f"Esqueleto — {marcador}",
            "notas_produccion": (
                f"Tipo {beat['tipo_clip']}. Character Bible pegado verbatim. "
                f"Referencia SIEMPRE la imagen héroe, nunca la anterior — así no deriva. "
                f"Los subtítulos van en el editor, jamás en el prompt."
            ),
            "palabras_prompt_video": len(prompt_video.split()),
        }

    def _dirigir_zack(self, beat: dict, ms: Any) -> dict[str, Any]:
        """3D glossy, anotaciones verde/rojo, personajes que no hablan."""
        z = ESTILOS_ESPECIALES["zack_films"]
        anotacion = self._anotacion_zack(beat["beat"])

        prompt_imagen = (
            f"Stylized-realistic glossy 3D render, warm sunlight, cobalt sky, PBR "
            f"materials, vertical 9:16. Scene: {self._set_zack(beat['beat'])}. "
            f"No on-screen text, no letters, no brand names."
        )
        prompt_video = (
            f"{self._movimiento_zack(beat['beat'])} "
            f"Annotation: {anotacion}. "
            f"6 to 9 hard cuts across the block, varying shot size and angle on every cut. "
            f"Characters only emote and gesture, they do NOT talk. "
            f"Diegetic audio only, no speech. No on-screen text — annotations are shapes, not words."
        )

        return {
            "prompt_imagen": prompt_imagen,
            "prompt_video": prompt_video,
            "negative_prompt": "on-screen text, letters, brand names, lip-sync, talking characters",
            "descripcion_visual": f"3D documental — {anotacion}",
            "notas_produccion": (
                f"Tipo {beat['tipo_clip']}. Anotación baked en el video. "
                f"Verde = revelación, rojo = peligro/física. Sin lip-sync: el narrador es externo."
            ),
            "palabras_prompt_video": len(prompt_video.split()),
        }

    def _dirigir_ugc(self, beat: dict, estilo: str, ms: Any) -> dict[str, Any]:
        """El personaje ACTÚA la micro-situación; nunca la describe."""
        u = ESTILOS_ESPECIALES[estilo]
        componente = beat.get("componente_microsituacion", "")
        accion = self._accion_microsituacion(beat["beat"], componente)

        prompt_imagen = (
            f"{u['prefijo_prompt']} still frame, vertical 9:16. "
            f"A Latin American entrepreneur in their early thirties, casual shirt, "
            f"unstyled hair, {accion}. Setting: a modest Latin American home interior "
            f"with everyday clutter, a laptop and a phone on the table. "
            f"Lighting: {self._luz_ugc(beat['beat'])}. {u['sufijo_prompt']}."
        )
        prompt_video = (
            f"{u['prefijo_prompt']} Shot: loose handheld camera with natural micro-shake, "
            f"vertical 9:16 framing. Action: {accion}. "
            f"Emotional read: shown through body language only, never explained to camera. "
            f"Lighting: {self._luz_ugc(beat['beat'])}. "
            f"Audio: ambient room tone and natural background texture, no music, "
            f"no discernible speech. {u['sufijo_prompt']}."
        )

        return {
            "prompt_imagen": prompt_imagen,
            "prompt_video": prompt_video,
            "negative_prompt": u["negative"],
            "descripcion_visual": accion,
            "notas_produccion": (
                f"Tipo {beat['tipo_clip']}. Componente activo: {componente or 'n/d'}. "
                f"La cámara lo ENCUENTRA en el momento — no es una presentación."
            ),
            "palabras_prompt_video": len(prompt_video.split()),
        }

    def _dirigir_object_talk(self, beat: dict, ms: Any) -> dict[str, Any]:
        """Objeto antropomorfo Pixar — la fórmula de 9 partes, en orden.

        El personaje va antes del prompt: una sola emoción dominante por beat, y
        la pose tiene que ser animation-ready (que permita mover cabeza, brazos,
        ojos y boca). Una pose complicada deja al personaje trabado.
        """
        emocion = self._emocion_object_talk(beat["beat"])
        pose = self._pose_object_talk(beat["beat"])

        # 1 estilo · 2 personaje · 3 cara · 4 cuerpo · 5 entorno · 6 apoyo
        # 7 cámara · 8 luz · 9 render
        prompt_imagen = (
            "Pixar-style cinematic 3D render. "
            "An anthropomorphic shopping cart character with brushed metal frame, "
            "rounded friendly proportions, visible weld seams and a worn rubber bumper. "
            f"Face: oversized expressive eyes {emocion['ojos']}, eyebrows {emocion['cejas']}, "
            f"mouth {emocion['boca']}. "
            f"Body language: {pose}, weight shifted onto one wheel, pose implying motion. "
            "Environment: a small online-store stockroom with shipping boxes and a laptop, "
            "belonging to the character's world. "
            "Supporting elements: a few floating order-slip papers, never crowding the frame. "
            "Camera: hero shot, slightly low angle, centered, vertical 9:16, shallow depth of field. "
            f"Lighting: {emocion['luz']}. "
            "Rendering: Pixar-quality, ultra detailed, physically based materials, "
            "global illumination, subsurface scattering, sharp focus, stylized realism."
        )

        prompt_video = (
            f"The cart character {self._movimiento_object_talk(beat['beat'])}, "
            f"holding its {emocion['nombre']} expression throughout. "
            "Head, eyes and eyebrows animate; the body stays grounded. "
            "Camera: slow push-in, single move. "
            "Audio: ambient room tone only, no music, no discernible speech."
        )

        return {
            "prompt_imagen": prompt_imagen,
            "prompt_video": prompt_video,
            "negative_prompt": (
                "uncanny realism, horror aesthetic, lifeless mascot, flat lighting, "
                "generic background, conflicting emotions, locked static pose"
            ),
            "descripcion_visual": f"Carrito antropomorfo — {emocion['nombre']}",
            "notas_produccion": (
                f"Tipo {beat['tipo_clip']}. Emoción dominante única: {emocion['nombre']}. "
                f"Pose animation-ready. El personaje NO se rediseña entre beats."
            ),
            "palabras_prompt_video": len(prompt_video.split()),
        }

    @staticmethod
    def _emocion_object_talk(n: int) -> dict[str, str]:
        """Una sola emoción dominante por beat. Nunca emociones en conflicto."""
        emociones = {
            1: {"nombre": "sorprendido", "ojos": "wide and alert, looking into camera",
                "cejas": "raised high", "boca": "slightly open",
                "luz": "warm indoor key light from the left"},
            2: {"nombre": "curioso", "ojos": "wide and optimistic, tilted toward camera",
                "cejas": "one raised", "boca": "small closed smile",
                "luz": "warm indoor key light from the left"},
            3: {"nombre": "exhausto", "ojos": "half-closed from exhaustion",
                "cejas": "heavy and drooping", "boca": "flat, slightly downturned",
                "luz": "cool dim light from a single overhead bulb"},
            4: {"nombre": "resignado", "ojos": "looking away from camera",
                "cejas": "relaxed", "boca": "a small resigned smirk",
                "luz": "cool dim light from a single overhead bulb"},
            5: {"nombre": "frustrado", "ojos": "narrow with tension",
                "cejas": "sharp and angled down", "boca": "pressed tight",
                "luz": "cool dim light from a single overhead bulb"},
            6: {"nombre": "iluminado", "ojos": "wide, catching a highlight",
                "cejas": "raised", "boca": "open in realization",
                "luz": "a warm hero rim light cutting in from behind"},
            7: {"nombre": "determinado", "ojos": "narrow with determination",
                "cejas": "sharp and level", "boca": "determined clenched line",
                "luz": "a warm hero rim light cutting in from behind"},
            8: {"nombre": "confiado", "ojos": "steady, looking into camera",
                "cejas": "relaxed and even", "boca": "confident grin",
                "luz": "bright volumetric daylight from above-left"},
            9: {"nombre": "esperanzado", "ojos": "wide and optimistic, looking up",
                "cejas": "gently curved", "boca": "open smile",
                "luz": "bright volumetric daylight from above-left"},
            10: {"nombre": "orgulloso", "ojos": "steady into camera",
                 "cejas": "level", "boca": "warm closed smile",
                 "luz": "golden hour sunlight through a window"},
            11: {"nombre": "honesto", "ojos": "steady, meeting the lens",
                 "cejas": "level", "boca": "a small honest half-smile",
                 "luz": "golden hour sunlight through a window"},
            12: {"nombre": "sereno", "ojos": "calm, turning away",
                 "cejas": "relaxed", "boca": "soft satisfied smile",
                 "luz": "golden hour sunlight through a window"},
        }
        return emociones.get(n, emociones[1])

    @staticmethod
    def _pose_object_talk(n: int) -> str:
        if n <= 3:
            return "handle bars slumped forward like tired shoulders"
        if n <= 7:
            return "frame straightening upward, one side lifting"
        return "standing tall, handle bar squared toward camera"

    @staticmethod
    def _movimiento_object_talk(n: int) -> str:
        if n <= 3:
            return "sags slowly, then blinks once"
        if n <= 7:
            return "straightens up in one smooth motion and tilts its head"
        return "rolls forward half a turn and settles, squaring up to camera"

    def _dirigir_generico(self, beat: dict, estilo: str, ms: Any) -> dict[str, Any]:
        """Estilos del SceneBuilder (ugc_realista, pixar, cyberpunk, anime…)."""
        builder = SceneBuilder(estilo)
        escena = builder.build_scene_prompt(beat, estilo, "")
        return {
            "prompt_imagen": escena["prompt_imagen_base"],
            "prompt_video": escena["prompt_video"],
            "negative_prompt": escena["negative_prompt"],
            "descripcion_visual": escena["descripcion_visual"],
            "notas_produccion": f"Tipo {beat['tipo_clip']}. {escena['notas_produccion']}",
            "palabras_prompt_video": escena["palabras_prompt"],
        }

    # -- fragmentos por beat ------------------------------------------------

    @staticmethod
    def _accion_microsituacion(n: int, componente: str) -> str:
        acciones = {
            1: "stops mid-task and looks straight into the lens, caught off guard",
            2: "leans slightly toward the lens, one hand gesturing to themselves",
            3: "sits alone late at night in front of a screen, shoulders dropped",
            4: "shrugs and half-laughs, dismissing it the way people dismiss what they cannot explain",
            5: "flips through a calendar, the same thing marked again and again",
            6: "looks up sharply, the moment an explanation lands",
            7: "watches a physical demonstration on a table, following it closely",
            8: "stands in a crowded hall where several conversations run at once",
            9: "walks through a busy venue greeting people, phone full of new contacts",
            10: "holds a ticket or badge toward the lens, relaxed and direct",
            11: "shrugs once and half-smiles, conceding something small",
            12: "walks out of frame into the crowd, the empty chair left behind",
        }
        return acciones.get(n, acciones[1])

    @staticmethod
    def _accion_simple(n: int) -> str:
        """Poses simplificadas: de pie, sentado, un brazo, inclinado, caminando."""
        poses = {
            1: "sitting alone, head turning toward camera",
            2: "leaning forward slightly, one arm resting on the table",
            3: "sitting with shoulders dropped, head lowered",
            4: "standing still, one arm hanging loose",
            5: "standing, head lifted toward an open doorway",
            6: "standing upright, single-arm gesture outward",
            7: "leaning over a small table, one arm extended",
            8: "walking slowly across the set",
            9: "standing beside a large hanging sign",
            10: "standing, holding a small knitted ticket in one hand",
            11: "standing still, one arm loose at the side",
            12: "walking away from camera into the set",
        }
        return poses.get(n, poses[1])

    @staticmethod
    def _set_crochet(n: int) -> str:
        return "apartment living room" if n <= 5 else "trade-fair hall with tiny knitted booths"

    @staticmethod
    def _luz_crochet(n: int) -> str:
        c = ESTILOS_ESPECIALES["crochet"]["iluminacion"]
        if n == 3:
            return c["sala_acogedora"]
        if n <= 5:
            return c["interior_dia"]
        return c["exterior"]

    @staticmethod
    def _movimiento_crochet(n: int) -> str:
        if n == 6:
            return (
                "The knitted character lifts its head once and straightens up, landing in "
                "a settled upright pose."
            )
        if n == 11:
            return (
                "The knitted character turns and walks away from camera in a steady "
                "stop-motion judder, ending fully inside the crowd."
            )
        return (
            "The knitted character makes one small single-arm gesture and settles, "
            "yarn fibers swaying gently."
        )

    @staticmethod
    def _marcador_escalada(n: int) -> str:
        marcadores = {
            1: "Day 1", 2: "Day 1", 3: "Day 1", 4: "Week 1", 5: "Week 1",
            6: "Month 3", 7: "Month 3", 8: "Month 3", 9: "Year 2",
            10: "Year 2", 11: "Year 2", 12: "Year 2",
        }
        return marcadores.get(n, "Day 1")

    @staticmethod
    def _movimiento_skeleton(n: int) -> str:
        if n <= 4:
            return "slumps slightly, blinks, shoulders dropping"
        if n <= 8:
            return "straightens up, head turning as people pass by"
        return "stands tall as the crowd turns toward it"

    @staticmethod
    def _set_zack(n: int) -> str:
        sets = {
            1: "a stack of glowing ad dashboards, one of them oversized",
            2: "the same dashboards, now dwarfed by a wide open hall",
            3: "a cutaway of a room where information passes hand to hand",
            4: "a wide hall packed with people, paths of movement between them",
            5: "the hall from above, the paths resolving into a single shape",
        }
        return sets.get(min(n, 5), sets[1])

    @staticmethod
    def _movimiento_zack(n: int) -> str:
        if n <= 2:
            return "Whip-in to the subject, then a crash zoom onto the detail."
        if n <= 4:
            return "Macro push onto the mechanism, then a hard cut to a wide reveal."
        return "Slow pull back to the widest angle as the kicker lands."

    @staticmethod
    def _anotacion_zack(n: int) -> str:
        if n in (3, 4, 6, 7):
            return "neon-green glowing outline tracing how it works"
        if n in (5, 9):
            return "red dashed trajectory marking the cost of the wrong path"
        return "neon-green arrow pointing at the element being revealed"

    @staticmethod
    def _luz_ugc(n: int) -> str:
        if n == 3:
            return "only the cold glow of the screen lighting the face in a dark room"
        if n >= 8:
            return "even ambient venue light, warm and busy"
        return "soft directional daylight from a side window, mild overexposure"

    @staticmethod
    def _encuadre_alterno(movimiento: str) -> str:
        """Encuadre para la segunda escena de un beat.

        Dos clips seguidos con el mismo encuadre se leen como un error de
        montaje, no como un corte. Cambiar tamaño o eje resuelve el corte.
        """
        alternos = {
            "closeup": "pan",
            "handheld": "closeup",
            "static": "dolly-in",
            "dolly-in": "static",
            "pan": "handheld",
        }
        return alternos.get(movimiento, "handheld")

    @staticmethod
    def _modelos(estilo: str) -> dict[str, str]:
        if estilo in ESTILOS_ESPECIALES:
            m = ESTILOS_ESPECIALES[estilo]["modelos"]
            return {"imagen": m.get("imagen", ""), "video": m.get("video", "")}
        gen = ESTILOS_GENERICOS.get(estilo, {})
        return {"imagen": "fal-ai/flux/schnell", "video": gen.get("modelo_fal", "")}

    # -- salida -------------------------------------------------------------

    def _escribir_json(self, paquete: dict[str, Any]) -> Path:
        slug = _slug(paquete.get("concepto") or paquete["estilo"], 24)
        ruta = (
            GUIONES_DIR
            / f"{self.marca}_{_slug(paquete['estilo'], 16)}_{slug}_"
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_director.json"
        )
        ruta.write_text(
            json.dumps(paquete, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return ruta

    def _escribir_html(self, paquete: dict[str, Any]) -> Path:
        slug = _slug(paquete.get("concepto") or paquete["estilo"])
        ruta = (
            STORYBOARDS_DIR
            / f"director_{slug}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        )
        ruta.write_text(self._html(paquete), encoding="utf-8")
        return ruta

    def _html(self, p: dict[str, Any]) -> str:
        e = html.escape
        c = self.colores

        avisos = ""
        if p.get("datos_sin_verificar"):
            filas = "".join(f"<li>{e(d)}</li>" for d in p["datos_sin_verificar"])
            avisos = f"""
  <section class="aviso">
    <h2>⚠️ Datos sin verificar en este guión</h2>
    <p>La guía de micro-situaciones es explícita: la especificidad solo funciona
       cuando la situación es real. Confirmar estas cifras con Effix antes de publicar.</p>
    <ul>{filas}</ul>
  </section>"""

        pc = p.get("plan_clips") or {}
        if pc and not pc.get("en_rango", True):
            avisos += f"""
  <section class="aviso">
    <h2>⏱️ El video se sale del rango 30-60s</h2>
    <p>{e(str(pc.get('total_clips')))} clips x {e(str(pc.get('duracion_clip_s')))}s =
       {e(str(pc.get('duracion_s')))}s · locución {e(str(pc.get('locucion_s')))}s.</p>
    <p><b>{e(str(pc.get('diagnostico', '')))}</b></p>
  </section>"""

        tarjetas = "\n".join(self._tarjeta(b) for b in p["beats"])

        costo = (
            f"{p['costo_estimado_usd']} USD"
            if p.get("costo_verificado")
            else "SIN CALCULAR (tarifas sin verificar en config/costos.json)"
        )

        return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Storyboard director — {e(p.get('concepto',''))}</title>
<style>
  :root {{
    --primario: {c['primario']}; --secundario: {c['secundario']};
    --acento: {c['acento']}; --texto: {c['texto']};
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin:0; padding:32px 20px 80px; background:var(--secundario); color:var(--texto);
    font:15px/1.55 -apple-system, "Segoe UI", Roboto, sans-serif;
  }}
  .wrap {{ max-width:1200px; margin:0 auto; }}
  h1 {{ font-size:26px; margin:0 0 6px; }}
  .meta {{ opacity:.75; font-size:13px; margin-bottom:22px; }}
  .meta b {{ color:var(--acento); }}
  section.aviso {{
    background:rgba(227,27,35,.12); border-left:3px solid var(--primario);
    padding:14px 18px; border-radius:8px; margin-bottom:22px;
  }}
  section h2 {{ font-size:14px; margin:0 0 8px; text-transform:uppercase; letter-spacing:.06em; }}
  .grid {{ display:grid; gap:16px; grid-template-columns:repeat(auto-fill,minmax(360px,1fr)); }}
  .beat {{
    background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.1);
    border-radius:12px; padding:16px;
  }}
  .head {{ display:flex; align-items:center; gap:8px; margin-bottom:10px; flex-wrap:wrap; }}
  .num {{ background:var(--primario); color:#fff; font-weight:700; padding:3px 9px;
          border-radius:6px; font-size:13px; }}
  .nombre {{ font-weight:700; font-size:13px; letter-spacing:.04em; }}
  .tiempo {{ font-size:11px; opacity:.55; }}
  .tipo {{ margin-left:auto; font-size:11px; border:1px solid var(--acento);
           color:var(--acento); padding:2px 8px; border-radius:20px; }}
  .comp {{ font-size:10px; text-transform:uppercase; letter-spacing:.08em;
           opacity:.55; border:1px solid rgba(255,255,255,.2);
           padding:2px 7px; border-radius:20px; }}
  .label {{ font-size:10px; text-transform:uppercase; letter-spacing:.09em;
            opacity:.5; margin:12px 0 3px; }}
  .narracion {{ margin:0; font-size:15px; }}
  .overlay {{ margin:0; font-weight:700; color:var(--acento);
              text-transform:uppercase; font-size:13px; }}
  .visual {{ margin:0; font-size:13px; opacity:.8; }}
  details {{ margin-top:10px; }}
  summary {{ cursor:pointer; font-size:12px; opacity:.7; }}
  pre {{ white-space:pre-wrap; font-size:11.5px; line-height:1.5;
         background:rgba(0,0,0,.35); padding:10px; border-radius:6px; margin:8px 0 0; }}
  .notas {{ font-size:11px; opacity:.55; margin:10px 0 0; }}
  .modelos {{ font-size:11px; opacity:.65; margin:6px 0 0; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>{e(p.get('concepto',''))}</h1>
  <p class="meta">
    Estilo <b>{e(p['estilo'])}</b> · Ángulo <b>{e(p.get('angulo',''))}</b> ·
    <b>{p.get('total_clips', len(p['beats']))} clips x {p.get('duracion_clip_s', 4)}s = {p['duracion_total_s']}s</b> ·
    Imagen: <b>{e(p['modelos']['imagen'])}</b> · Video: <b>{e(p['modelos']['video'])}</b><br>
    Costo estimado: <b>{e(costo)}</b>
  </p>
{avisos}
  <div class="grid">
{tarjetas}
  </div>
</div>
</body>
</html>
"""

    def _tarjeta(self, b: dict[str, Any]) -> str:
        e = html.escape
        comp = b.get("componente_microsituacion", "")
        comp_html = f'<span class="comp">{e(comp)}</span>' if comp else ""

        return f"""
    <article class="beat">
      <div class="head">
        <span class="num">{b.get('clip', b['beat']):02d}</span>
        <span class="nombre">{e(b.get('nombre',''))}</span>
        <span class="tiempo">{b.get('t_inicio_s','?')}-{b.get('t_fin_s','?')}s</span>
        <span>{b.get('emoji','')}</span>
        {comp_html}
        <span class="tipo">Tipo {e(b.get('tipo_clip','A'))}</span>
      </div>

      <p class="label">Narración (ElevenLabs) — {b.get('duracion_locucion_s','?')}s{'' if b.get('cabe_en_el_beat', True) else ' ⚠️ NO CABE'}</p>
      <p class="narracion">{e(b.get('narracion',''))}</p>

      <p class="label">Marca en pantalla (desde el clip 01)</p>
      <p class="visual">{e(str(b.get('marca_en_pantalla','')))} · logo persistente</p>

      <p class="label">Texto en pantalla</p>
      <p class="overlay">{e(b.get('texto_pantalla',''))}</p>

      <p class="label">Visual</p>
      <p class="visual">{e(b.get('descripcion_visual',''))}</p>

      <details>
        <summary>Prompt de imagen base</summary>
        <pre>{e(b.get('prompt_imagen',''))}</pre>
      </details>

      <details>
        <summary>Prompt de video I2V ({b.get('palabras_prompt_video',0)} palabras)</summary>
        <pre>{e(b.get('prompt_video',''))}</pre>
      </details>

      <p class="notas">{e(b.get('notas_produccion',''))}</p>
      <p class="modelos">Imagen: {e(b.get('modelos',{}).get('imagen',''))}<br>
         Video: {e(b.get('modelos',{}).get('video',''))}</p>
    </article>"""
