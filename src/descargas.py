"""Bajar a disco lo que los modelos dejan en URLs temporales.

Existe como módulo propio porque el reintento estaba en un solo sitio y el
agujero se coló por el de al lado: `video_generator._descargar` (imágenes y
clips) aprendió a reintentar tras perder una héroe ya pagada, y media hora
después la canción del ad #3 se perdió igual porque bajaba por
`audio_extra._bajar`, que no lo había aprendido.

La regla que esto encarna: **la generación es lo caro y la descarga es lo
frágil**. Un `Read timed out` de fal no puede tirar trabajo que ya se pagó, y
mucho menos hacerlo de formas distintas según el tipo de archivo.
"""

from __future__ import annotations

import time
from pathlib import Path

import requests

# Cuatro intentos con espera creciente (2, 4, 8s). Los cortes de fal que se han
# visto duran segundos, no minutos.
INTENTOS = 4
TIMEOUT_S = 300


def _ficha(destino: Path) -> Path:
    """Dónde se anota la URL pendiente de un archivo que no llegó a bajarse."""
    return destino.with_name(destino.name + ".url")


def bajar_url(url: str, destino: Path, *, intentos: int = INTENTOS) -> Path:
    """Descarga `url` en `destino`, reintentando ante fallos de red.

    Antes de intentar nada, la URL se escribe al lado del destino. Suena
    excesivo hasta que se cae internet a mitad de una tanda: los modelos cobran
    al generar, y sin la URL guardada los cinco clips de crochet que ya estaban
    pagados sólo se podían recuperar pagándolos otra vez. Con la ficha en disco,
    `recuperar_pendientes()` los baja gratis cuando la red vuelve.

    Se baja en streaming y por trozos: cargar 10 MB de un WAV de golpe con
    `respuesta.content` es justo lo que revienta con `IncompleteRead` en una
    conexión inestable.
    """
    destino.parent.mkdir(parents=True, exist_ok=True)
    _ficha(destino).write_text(url, encoding="utf-8")

    ultimo: Exception | None = None
    for intento in range(intentos):
        try:
            with requests.get(url, timeout=TIMEOUT_S, stream=True) as respuesta:
                respuesta.raise_for_status()
                parcial = destino.with_suffix(destino.suffix + ".parcial")
                with parcial.open("wb") as fh:
                    for trozo in respuesta.iter_content(chunk_size=1 << 16):
                        if trozo:
                            fh.write(trozo)
                parcial.replace(destino)
            _ficha(destino).unlink(missing_ok=True)
            return destino
        except (requests.RequestException, OSError) as exc:
            ultimo = exc
            if intento < intentos - 1:
                time.sleep(2 ** (intento + 1))
    raise RuntimeError(
        f"No se pudo bajar {url} tras {intentos} intentos. El modelo ya cobró, "
        f"pero la URL queda anotada en {_ficha(destino).name}: cuando vuelva la "
        f"red, `recuperar_pendientes()` la baja sin volver a generar. "
        f"Último error: {type(ultimo).__name__}: {ultimo}"
    ) from ultimo


def recuperar_pendientes(carpeta: Path) -> list[Path]:
    """Baja lo que quedó pagado y sin descargar en una carpeta.

    Se llama al principio de cada fase: si la corrida anterior murió con la red
    caída, esto recupera el trabajo antes de plantearse generar nada nuevo.
    """
    recuperados: list[Path] = []
    for ficha in sorted(carpeta.glob("*.url")):
        destino = ficha.with_name(ficha.name[:-4])
        if destino.exists():
            ficha.unlink(missing_ok=True)
            continue
        try:
            recuperados.append(bajar_url(
                ficha.read_text(encoding="utf-8").strip(), destino, intentos=2))
        except Exception:
            # La URL de fal caduca: si ya no sirve, se regenera y punto.
            continue
    return recuperados
