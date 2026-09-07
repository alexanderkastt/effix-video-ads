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

from .descargas import bajar_url
from .paths import CLIPS_DIR, env, env_int
from .personaje import MODELO_ESCENA, Personaje, prompt_de_escena


@dataclass
class Clip:
    """Un beat convertido en video, con lo que costó llegar ahí."""

    beat: int
    video: Path
    imagen: Path | None
    duracion_s: float
    segundos_de_espera: float
    respuesta: dict[str, Any] = field(repr=False, default_factory=dict)


def _descargar(url: str, destino: Path, *, intentos: int = 4) -> Path:
    """Baja lo que fal dejó en una URL temporal. Ver `src/descargas.py`."""
    return bajar_url(url, destino, intentos=intentos)


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


def generar_imagen_base(
    beat: dict[str, Any],
    destino: Path,
    *,
    personaje: Personaje | None = None,
) -> tuple[Path, float]:
    """Primer paso: el fotograma que el modelo de video va a animar.

    Con `personaje`, la escena se genera por edición sobre la hoja de
    referencia y sale la misma protagonista de siempre. Sin él, cada
    escena inventa a alguien nuevo — que es lo que hacía antes.
    """
    inicio = time.monotonic()

    if personaje is not None:
        salida = fal_client.subscribe(
            MODELO_ESCENA,
            {
                "prompt": prompt_de_escena(beat, personaje),
                "image_urls": [personaje.url_referencia],
                "aspect_ratio": env("FAL_ASPECT_RATIO", "9:16"),
                "resolution": "1K",
                "num_images": 1,
            },
        )
    else:
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
    etiqueta: str = "beat",
    personaje: Personaje | None = None,
) -> Clip:
    """Anima la imagen base y devuelve el clip descargado.

    `duracion_s` sale de la locución medida, no del presupuesto teórico: si
    la voz de ese beat dura 4.46s, el clip tiene que cubrirlos.

    `etiqueta` nombra los archivos. El orquestador pasa "clip" porque los
    clips son ventanas de 4s y no coinciden uno a uno con los beats; dejar
    el nombre en manos del llamador evita que el montaje después no los
    encuentre.
    """
    modelo = modelo or env("FAL_MODEL_VIDEO", "fal-ai/kling-video/v2.1/standard/image-to-video")
    carpeta = carpeta or (CLIPS_DIR / job_id)
    carpeta.mkdir(parents=True, exist_ok=True)
    n = beat["beat"]

    if imagen is None:
        imagen, _ = generar_imagen_base(
            beat, carpeta / f"{etiqueta}_{n:02d}_base.png", personaje=personaje
        )

    # Kling cobra por tramos de 5 o 10 segundos: pedir 4.4 no ahorra nada y
    # quedarse corto obliga a repetir el clip entero.
    pedido = "10" if (duracion_s or 0) > 5 else "5"

    inicio = time.monotonic()
    with open(imagen, "rb") as fh:
        url_imagen = fal_client.upload(fh.read(), "image/png")

    payload = {
        "prompt": beat["prompt_video"],
        "image_url": url_imagen,
        "duration": pedido,
        "negative_prompt": beat.get("negative_prompt", ""),
    }
    # Kling 2.5 turbo no declara `aspect_ratio`: hereda el encuadre de la
    # imagen base, que ya sale 9:16. Mandarselo arriesga un rechazo de
    # validacion, y un clip rechazado tarde se paga igual que uno bueno.
    if "v2.5-turbo" not in modelo:
        payload["aspect_ratio"] = env("FAL_ASPECT_RATIO", "9:16")

    salida = fal_client.subscribe(modelo, payload)
    espera = round(time.monotonic() - inicio, 1)
    ruta = _descargar(_url_de(salida, "video"), carpeta / f"{etiqueta}_{n:02d}.mp4")

    return Clip(
        beat=n,
        video=ruta,
        imagen=imagen,
        duracion_s=float(pedido),
        segundos_de_espera=espera,
        respuesta=salida,
    )
