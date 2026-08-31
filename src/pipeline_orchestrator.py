"""Orquestador — del guión aprobado a los clips, en el orden correcto.

El orden importa y no es negociable: primero la voz, después se mide, y
recién entonces se decide cuántos clips hacen falta. Al revés se generan
clips que no cuadran con la locución y hay que pagarlos otra vez.

Los clips salen en paralelo hasta MAX_CONCURRENT_CLIPS. El paralelismo es
por dinero, no por prisa: cada fallo se aísla en su clip y no tumba a los
demás, así que un error en el beat 07 no obliga a regenerar los otros diez.
"""

from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from .paths import AUDIO_DIR, CLIPS_DIR, env_int
from .personaje import Personaje, crear_personaje
from .plan_clips import planificar_desde_audio
from .video_generator import Clip, generar_clip, generar_imagen_base
from .voice_generator import Locucion, duracion_de, generar_locucion


@dataclass
class Resultado:
    """Lo que dejó una corrida, incluido lo que falló."""

    job_id: str
    locucion: dict[str, Any]
    plan: dict[str, Any]
    clips: list[dict[str, Any]] = field(default_factory=list)
    ventanas: list[dict[str, Any]] = field(default_factory=list)
    personaje: str | None = None
    fallos: list[dict[str, str]] = field(default_factory=list)
    segundos_totales: float = 0.0

    @property
    def completo(self) -> bool:
        return not self.fallos


def _duraciones_por_beat(guion: dict, carpeta_audio: Path) -> dict[int, float]:
    """Mide la locución que ya está en disco, beat por beat."""
    medidas: dict[int, float] = {}
    for beat in guion["beats"]:
        mp3 = carpeta_audio / f"beat_{beat['beat']:02d}.mp3"
        if not mp3.exists():
            raise FileNotFoundError(
                f"Falta {mp3.name}: la voz tiene que existir antes de repartir clips."
            )
        medidas[beat["beat"]] = duracion_de(mp3)
    return medidas


def asignar_clips(plan: dict[str, Any], beats: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Decide qué escena rueda cada clip.

    Los clips son ventanas fijas de 4s sobre una línea de tiempo continua,
    así que no hay un clip por beat: el beat 05 puede caber entero dentro de
    una ventana y el 07 puede ocupar tres. A cada ventana le toca la escena
    del beat que más segundos ocupa dentro de ella, que es la regla que ya
    fija plan_clips.
    """
    dur = plan["duracion_clip_s"]
    por_beat = {b["beat"]: b for b in beats}
    ventanas: list[dict[str, Any]] = []

    for i in range(plan["total_clips"]):
        inicio, fin = i * dur, (i + 1) * dur
        solapes = []
        for r in plan["reparto"]:
            cubierto = min(fin, r["t_fin_s"]) - max(inicio, r["t_inicio_s"])
            if cubierto > 0:
                solapes.append((cubierto, r["beat"]))
        if not solapes:  # cola final sin voz: la cubre el ultimo beat
            solapes = [(0.0, plan["reparto"][-1]["beat"])]
        dominante = max(solapes)[1]
        ventanas.append({
            "clip": i + 1,
            "beat": dominante,
            "t_inicio_s": round(inicio, 2),
            "t_fin_s": round(fin, 2),
            "escena": por_beat[dominante],
            "comparte_con": sorted({b for _, b in solapes if b != dominante}),
        })
    return ventanas


def producir(
    guion: dict[str, Any],
    *,
    solo_beats: list[int] | None = None,
    reusar_voz: bool = True,
    concurrencia: int | None = None,
    personaje: str | None = None,
    estilo_en: str = "Pixar-style 3D animation, soft global illumination",
) -> Resultado:
    """Genera la locución y los clips del guión aprobado.

    `reusar_voz` evita volver a facturar caracteres cuando la locución ya
    está en disco, que es lo normal al reintentar clips sueltos.
    `solo_beats` limita la corrida a esos beats, para reintentos puntuales.
    """
    job_id = str(guion.get("job_id") or "sin-job")
    carpeta_audio = AUDIO_DIR / job_id
    carpeta_clips = CLIPS_DIR / job_id
    arranque = time.monotonic()

    # ── 1. Voz ────────────────────────────────────────────────────────────
    ya_locutado = carpeta_audio.exists() and any(carpeta_audio.glob("beat_*.mp3"))
    if ya_locutado and reusar_voz:
        locucion = Locucion(
            beats=sorted(carpeta_audio.glob("beat_*.mp3")),
            caracteres=0,  # no se facturó nada en esta corrida
            duraciones_s=[],
        )
    else:
        locucion = generar_locucion(guion, destino=carpeta_audio)

    medidas = _duraciones_por_beat(guion, carpeta_audio)

    # ── 2. Plan sobre el audio real ───────────────────────────────────────
    plan = planificar_desde_audio(guion["beats"], duraciones=medidas)

    # ── 3. El personaje, uno solo para todo el video ──────────────────────
    protagonista: Personaje | None = None
    if personaje:
        protagonista = crear_personaje(
            personaje, estilo_en=estilo_en, job_id=job_id, carpeta=carpeta_clips
        )

    # ── 4. Clips ──────────────────────────────────────────────────────────
    ventanas = asignar_clips(plan, guion["beats"])
    pendientes = [
        v for v in ventanas
        if solo_beats is None or v["clip"] in solo_beats
    ]
    # Un clip ya descargado no se vuelve a pagar.
    pendientes = [
        v for v in pendientes
        if not (carpeta_clips / f"clip_{v['clip']:02d}.mp4").exists()
    ]

    # El estilo elige el modelo de video (SceneBuilder lo escribe en el guion);
    # el .env solo pone el default para guiones que no traigan uno. Antes el
    # guion anunciaba un modelo y se generaba con otro, y el costo estimado no
    # correspondia a lo que se pagaba.
    modelo_video = guion.get("modelo_fal") or None

    maximo = concurrencia or env_int("MAX_CONCURRENT_CLIPS", 3)
    clips: list[Clip] = []
    fallos: list[dict[str, str]] = []

    def _uno(ventana: dict[str, Any]) -> Clip:
        n = ventana["clip"]
        base = carpeta_clips / f"clip_{n:02d}_base.png"
        escena = dict(ventana["escena"], beat=n)  # el archivo se nombra por clip
        imagen = base if base.exists() else None
        return generar_clip(
            escena,
            imagen=imagen,
            duracion_s=plan["duracion_clip_s"],
            modelo=modelo_video,
            carpeta=carpeta_clips,
            job_id=job_id,
            etiqueta="clip",
            personaje=protagonista,
        )

    with ThreadPoolExecutor(max_workers=maximo) as pool:
        futuros = {pool.submit(_uno, v): v for v in pendientes}
        for futuro in as_completed(futuros):
            ventana = futuros[futuro]
            try:
                clips.append(futuro.result())
            except Exception as error:  # el fallo de un clip no tumba la corrida
                fallos.append({
                    "clip": ventana["clip"],
                    "error": f"{type(error).__name__}: {error}",
                })

    # Los que ya estaban en disco cuentan como hechos.
    existentes = sorted(carpeta_clips.glob("clip_*.mp4"))

    resultado = Resultado(
        job_id=job_id,
        locucion={
            "caracteres_facturados": locucion.caracteres,
            "archivos": len(existentes),
            "duracion_total_s": round(sum(medidas.values()), 2),
        },
        plan=plan,
        personaje=protagonista.nombre if protagonista else None,
        clips=sorted(
            [{"clip": c.beat, "video": str(c.video), "espera_s": c.segundos_de_espera,
              "duracion_pedida_s": c.duracion_s} for c in clips],
            key=lambda c: c["clip"],
        ),
        ventanas=[{k: v for k, v in w.items() if k != "escena"} for w in ventanas],
        fallos=fallos,
        segundos_totales=round(time.monotonic() - arranque, 1),
    )

    manifiesto = carpeta_clips / "manifiesto.json"
    manifiesto.parent.mkdir(parents=True, exist_ok=True)
    manifiesto.write_text(
        json.dumps(asdict(resultado), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return resultado
