"""Sistema de música — la librería del repo, briefs y detección de beats.

Cuatro caminos, y el primero es el que se usa casi siempre:

0. Librería: `pista_de_libreria()` devuelve el mp3 que le toca al estilo, de
   `assets/audio/soundtracks/`. Gratis, porque ya se pagó una vez.
1. Fondo: brief para componer una pista nueva, cuando el catálogo no tiene el
   mood que el ad pide.
2. Sincronizada (`musical_sync`): la canción ES el video, el guión es la letra.
3. Detección de beats: librosa lee una canción ya generada y devuelve los
   timestamps reales, para cortar los clips donde de verdad cae el golpe.

Este módulo no llama a ninguna API: sólo construye el brief. La llamada de pago
vive en `src/audio_extra.py`, y la mezcla en `src/mezcla.py`.

Las claves del brief conservan el prefijo `suno_` por compatibilidad con los 21
guiones JSON ya escritos; Suno quedó reemplazado por stable-audio-25.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .paths import ASSETS_DIR, CONFIG_DIR, env_float, env_int, load_brand_dna

# La librería vive en el repo: las pistas se generan una vez y se reusan. Un ad
# no necesita estrenar música — necesita música que no pelee con la voz, y eso
# ya está resuelto en las seis pistas del catálogo.
SOUNDTRACKS_JSON = CONFIG_DIR / "soundtracks.json"
SOUNDTRACKS_DIR = ASSETS_DIR / "audio" / "soundtracks"

# Qué mood le toca a cada estilo cuando el guión no dice otra cosa. Es la misma
# lógica de FALLBACK_POR_ESTILO, pero apuntando a la librería en vez de a un
# prompt para generar.
MOOD_POR_ESTILO: dict[str, str] = {
    "ugc_realista": "energetico",
    "testimonial": "energetico",
    "skeleton": "tenso",
    "cinematic": "aspiracional",
    "zack_films": "aspiracional",
    "pixar_animado": "alegre",
    "claymation": "alegre",
    "animado_2d": "alegre",
    "object_talk": "alegre",
    "crochet": "alegre",
    "cyberpunk": "tenso",
    "minecraft": "alegre",
    "anime": "epico",
    "avengers": "epico",
}

# Y cuando el estilo tampoco está, manda la emoción del tono de marca.
MOOD_POR_EMOCION: dict[str, str] = {
    "energetico": "energetico",
    "emotivo": "emotivo",
    "aspiracional": "aspiracional",
    "alegre": "alegre",
    "tenso": "tenso",
    "epico": "epico",
}

# Brief base por combinación estilo+emoción
MUSIC_BRIEFS: dict[str, dict[str, Any]] = {
    "ugc_realista+energetico": {"prompt": "upbeat lo-fi hip hop, warm bass, positive energy", "bpm": 95},
    "ugc_realista+emotivo": {"prompt": "soft acoustic guitar, warm piano, intimate", "bpm": 72},
    "cinematic+aspiracional": {"prompt": "cinematic orchestral, building strings, triumphant", "bpm": 85},
    "cyberpunk+tenso": {"prompt": "dark synthwave, pulsing bass, electronic tension", "bpm": 128},
    "pixar_animado+alegre": {"prompt": "playful orchestral, pizzicato strings, adventurous", "bpm": 110},
    "anime+epico": {"prompt": "anime ost, powerful brass, dramatic choir", "bpm": 140},
    "musical_sync+cualquiera": {"prompt": "según el brief específico del guión", "bpm": "variable"},
}

# Fallback por estilo cuando la emoción concreta no está en la tabla
FALLBACK_POR_ESTILO: dict[str, dict[str, Any]] = {
    "ugc_realista": {"prompt": "upbeat lo-fi hip hop, warm bass, positive energy", "bpm": 95},
    "cinematic": {"prompt": "cinematic orchestral, building strings, triumphant", "bpm": 85},
    "pixar_animado": {"prompt": "playful orchestral, pizzicato strings, adventurous", "bpm": 110},
    "cyberpunk": {"prompt": "dark synthwave, pulsing bass, electronic tension", "bpm": 128},
    "anime": {"prompt": "anime ost, powerful brass, dramatic choir", "bpm": 140},
    "claymation": {"prompt": "quirky handmade folk, plucked strings, playful percussion", "bpm": 100},
    "minecraft": {"prompt": "ambient chiptune, soft piano loops, nostalgic", "bpm": 90},
    "avengers": {"prompt": "epic orchestral hybrid, heavy percussion, brass hits", "bpm": 120},
    "musical_sync": {"prompt": "latin urban pop, reggaeton groove, catchy hook", "bpm": 96},
}

# El tono del brand_dna decide la emoción musical cuando no se pasa explícita
TONO_A_EMOCION = {
    "energético": "energetico",
    "energetico": "energetico",
    "directo": "energetico",
    "emprendedor": "aspiracional",
    "real": "emotivo",
}


def emocion_desde_tono(tono: str) -> str:
    """La emoción musical que sugiere el tono de marca."""
    bajo = (tono or "").lower()
    for palabra, emocion in TONO_A_EMOCION.items():
        if palabra in bajo:
            return emocion
    return "energetico"


def catalogo() -> dict[str, Any]:
    """El índice de la librería. Vacío si todavía no se generó."""
    if not SOUNDTRACKS_JSON.exists():
        return {}
    import json
    with SOUNDTRACKS_JSON.open(encoding="utf-8") as fh:
        return json.load(fh).get("moods", {})


def mood_para(estilo: str, tono: str = "") -> str:
    """Qué mood le corresponde a un ad. Nunca falla: cae a `energetico`."""
    if estilo in MOOD_POR_ESTILO:
        return MOOD_POR_ESTILO[estilo]
    return MOOD_POR_EMOCION.get(emocion_desde_tono(tono), "energetico")


def pista_de_libreria(estilo: str, tono: str = "", mood: str = "") -> Path | None:
    """La pista que le toca a este ad, si ya está en la librería.

    Devuelve None cuando el mood no existe o el mp3 todavía no se generó, para
    que el llamador decida entre componer una nueva o montar sin música. No
    revienta: quedarse sin música es peor que quedarse sin el mood exacto, pero
    ninguna de las dos cosas justifica tumbar un montaje que ya costó dinero.
    """
    elegido = mood or mood_para(estilo, tono)
    entrada = catalogo().get(elegido)
    if not entrada:
        return None
    ruta = SOUNDTRACKS_DIR / entrada["archivo"]
    return ruta if ruta.exists() else None


class MusicEngine:
    """Construye briefs de música y alinea los clips con los beats reales."""

    def __init__(self, marca: str = "effix") -> None:
        self.marca = marca
        self.dna = load_brand_dna(marca)
        self.duracion_beat = env_int("CLIP_DURATION_SECONDS", 4)
        self.total_clips = env_int("TOTAL_CLIPS", 11)

    # -- modo 1: fondo ------------------------------------------------------

    def generate_background_brief(
        self, tono: str, estilo: str, duracion_s: int | None = None
    ) -> dict[str, Any]:
        """Brief de música de fondo — acompaña, no protagoniza.

        El volumen sale del `.env` (`MUSICA_VOLUMEN`, 0.18) y no de aquí: el
        que manda es el de la mezcla, y tener dos números distintos era
        parte de por qué cada ad sonaba diferente.
        """
        duracion_s = duracion_s or self.total_clips * self.duracion_beat
        emocion = self._emocion_desde_tono(tono)

        clave = f"{estilo}+{emocion}"
        base = MUSIC_BRIEFS.get(clave) or FALLBACK_POR_ESTILO.get(
            estilo, FALLBACK_POR_ESTILO["ugc_realista"]
        )

        bpm = base["bpm"]
        if not isinstance(bpm, int):
            bpm = 100  # 'variable' sólo aplica al modo sincronizado

        return {
            "modo": "fondo",
            "suno_prompt": base["prompt"],
            "suno_style_tags": self._style_tags(estilo, emocion),
            "suno_lyrics": "instrumental",
            "suno_duration_s": duracion_s,
            "volumen_relativo": env_float("MUSICA_VOLUMEN", 0.18),
            "bpm_recomendado": bpm,
            "clave_brief": clave if clave in MUSIC_BRIEFS else f"fallback:{estilo}",
            "nota": "Instrumental. La voz en off de ElevenLabs va encima al 100%.",
        }

    # -- modo 2: sincronizado ----------------------------------------------

    def generate_music_video_song(
        self,
        guion_beats: list[dict[str, Any]],
        estilo_musical: str = "latin urban pop",
        marca: str | None = None,
    ) -> dict[str, Any]:
        """La canción ES el video: convierte las narraciones del guión en letra.

        Agrupa de a cuatro beats: cada grupo es un verso o el coro. La rima no es
        obligatoria, el ritmo sí — por eso se respeta el largo de cada línea.
        """
        marca = marca or self.marca
        lineas = [b.get("narracion", "").strip() for b in guion_beats if b.get("narracion")]

        secciones: list[str] = []
        etiquetas = ["Verse 1", "Chorus", "Verse 2", "Outro"]
        for i in range(0, len(lineas), 4):
            grupo = lineas[i : i + 4]
            etiqueta = etiquetas[min(i // 4, len(etiquetas) - 1)]
            cuerpo = "\n".join(self._a_linea_cantable(l) for l in grupo)
            secciones.append(f"[{etiqueta}]\n{cuerpo}")

        letra = "\n\n".join(secciones)
        duracion = len(guion_beats) * self.duracion_beat

        return {
            "modo": "sincronizado",
            "suno_title": f"{self.dna['nombre_completo']} — himno",
            "suno_custom_lyrics": letra,
            "suno_style_tags": self._style_tags("musical_sync", "energetico", estilo_musical),
            "suno_duration_s": duracion,
            "volumen_relativo": 1.0,
            "bpm_recomendado": 96,
            "beat_timestamps": [i * self.duracion_beat for i in range(len(guion_beats) + 1)],
            "nota": (
                "En este modo la canción manda. Si Suno devuelve otro tempo, "
                "recalcular los cortes con detect_beats_from_audio()."
            ),
        }

    # -- modo 3: detección de beats ----------------------------------------

    @staticmethod
    def detect_beats_from_audio(audio_path: str | Path) -> dict[str, Any]:
        """Lee una canción con librosa y devuelve tempo y timestamps de beat.

        Se usa cuando Suno ya generó la pista y hay que cortar los clips donde
        de verdad cae el golpe, en vez de cada 4 segundos exactos.
        """
        ruta = Path(audio_path)
        if not ruta.exists():
            raise FileNotFoundError(f"No encuentro el audio en {ruta}")

        import librosa  # import diferido: librosa tarda ~2s en cargar
        import numpy as np

        y, sr = librosa.load(str(ruta))
        tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
        beat_times = librosa.frames_to_time(beat_frames, sr=sr)

        # En librosa reciente `tempo` puede venir como array de un elemento
        tempo_bpm = float(np.atleast_1d(tempo)[0])

        return {
            "tempo_bpm": tempo_bpm,
            "beat_timestamps": [float(t) for t in beat_times],
            "duracion_s": float(len(y) / sr),
        }

    def align_clips_to_beats(
        self, beat_timestamps: list[float], clips_count: int
    ) -> list[float]:
        """Reparte `clips_count` clips sobre los beats detectados.

        Devuelve la duración de cada clip. Si no hay beats suficientes, cae a
        duración fija — es preferible un corte parejo a un corte a destiempo.
        """
        if not beat_timestamps or len(beat_timestamps) < clips_count + 1:
            return [float(self.duracion_beat)] * clips_count

        # Toma puntos de corte repartidos uniformemente entre los beats reales
        paso = (len(beat_timestamps) - 1) / clips_count
        cortes = [beat_timestamps[int(round(i * paso))] for i in range(clips_count + 1)]
        return [round(cortes[i + 1] - cortes[i], 3) for i in range(clips_count)]

    # -- internos -----------------------------------------------------------

    def _emocion_desde_tono(self, tono: str) -> str:
        return emocion_desde_tono(tono)

    @staticmethod
    def _style_tags(estilo: str, emocion: str, extra: str = "") -> list[str]:
        tags = ["latin", "latam", estilo.replace("_", " "), emocion]
        if extra:
            tags.append(extra)
        return [t for t in tags if t]

    @staticmethod
    def _a_linea_cantable(texto: str) -> str:
        """Limpia una narración para que funcione como línea de letra."""
        linea = re.sub(r"\s+", " ", texto).strip()
        linea = linea.rstrip(".")           # las letras no llevan punto final
        linea = re.sub(r"^[¿¡]", "", linea)  # abre limpio para cantar
        return linea
