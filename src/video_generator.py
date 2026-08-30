"""Generación de clips con fal.ai — la parte cara del pipeline.

Dos pasos por beat, porque el modelo de video del proyecto es
image-to-video: primero una imagen base (barata, rápida) y luego el clip
que la anima. La imagen base es además el punto de control — si sale mal,
se descarta ahí y no se paga el video.

Nada aquí se lanza en paralelo por su cuenta: quien decide cuántos clips
corren a la vez es el orquestador, con MAX_CONCURRENT_CLIPS.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import fal_client
import requests

from .paths import CLIPS_DIR, env, env_int


@dataclass
class Clip:
    """Un beat convertido en video, con lo que costó llegar ahí."""

    beat: int
    video: Path
    imagen: Path | None
    duracion_s: float
    segundos_de_espera: float
    respuesta: dict[str, Any] = field(repr=False, default_factory=dict)


def _descargar(url: str, destino: Path) -> Path:
    destino.parent.mkdir(parents=True, exist_ok=True)
    respuesta = requests.get(url, timeout=300)
    respuesta.raise_for_status()
    destino.write_bytes(respuesta.content)
    return destino


def _url_de(salida: dict[str, Any], *claves: str) -> str:
    """Saca la URL del payload de fal, que la anida distinto según el modelo."""
    for clave in claves:
        valor = salida.get(clave)
        if isinstance(valor, dict) and valor.get("url"):
            return valor["url"]
        if isinstance(valor, list) and valor and isinstance(valor[0], dict):
            if valor[0].get("url"):
                return valor[0]["url"]
    raise KeyError(f"La respuesta de fal no trae URL en {claves}: {list(salida)}")


def generar_imagen_base(beat: dict[str, Any], destino: Path) -> tuple[Path, float]:
    """Primer paso: el fotograma que el modelo de video va a animar."""
    inicio = time.monotonic()
    salida = fal_client.subscribe(
        env("FAL_MODEL_IMAGE", "fal-ai/flux/schnell"),
        {
            "prompt": beat["prompt_imagen_base"],
            "image_size": {"width": 720, "height": 1280},  # 9:16 vertical
            "num_images": 1,
        },
    )
    ruta = _descargar(_url_de(salida, "images", "image"), destino)
    return ruta, round(time.monotonic() - inicio, 1)


def generar_clip(
    beat: dict[str, Any],
    *,
    imagen: Path | None = None,
    duracion_s: float | None = None,
    modelo: str | None = None,
    carpeta: Path | None = None,
    job_id: str = "sin-job",
) -> Clip:
    """Anima la imagen base y devuelve el clip descargado.

    `duracion_s` sale de la locución medida, no del presupuesto teórico: si
    la voz de ese beat dura 4.46s, el clip tiene que cubrirlos.
    """
    modelo = modelo or env("FAL_MODEL_VIDEO", "fal-ai/kling-video/v2.1/standard/image-to-video")
    carpeta = carpeta or (CLIPS_DIR / job_id)
    carpeta.mkdir(parents=True, exist_ok=True)
    n = beat["beat"]

    if imagen is None:
        imagen, _ = generar_imagen_base(beat, carpeta / f"beat_{n:02d}_base.png")

    # Kling cobra por tramos de 5 o 10 segundos: pedir 4.4 no ahorra nada y
    # quedarse corto obliga a repetir el clip entero.
    pedido = "10" if (duracion_s or 0) > 5 else "5"

    inicio = time.monotonic()
    with open(imagen, "rb") as fh:
        url_imagen = fal_client.upload(fh.read(), "image/png")

    salida = fal_client.subscribe(
        modelo,
        {
            "prompt": beat["prompt_video"],
            "image_url": url_imagen,
            "duration": pedido,
            "negative_prompt": beat.get("negative_prompt", ""),
            "aspect_ratio": env("FAL_ASPECT_RATIO", "9:16"),
        },
    )
    espera = round(time.monotonic() - inicio, 1)
    ruta = _descargar(_url_de(salida, "video"), carpeta / f"beat_{n:02d}.mp4")

    return Clip(
        beat=n,
        video=ruta,
        imagen=imagen,
        duracion_s=float(pedido),
        segundos_de_espera=espera,
        respuesta=salida,
    )
