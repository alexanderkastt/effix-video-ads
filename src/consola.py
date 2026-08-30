"""Salida de consola en UTF-8.

En Windows la consola arranca en cp1252 y cualquier `print` con un emoji o una
raya larga revienta con UnicodeEncodeError. Los scripts de este proyecto usan
ambos, así que cada entry point llama a `usar_utf8()` antes de imprimir nada.
"""

from __future__ import annotations

import sys


def usar_utf8() -> None:
    """Pasa stdout y stderr a UTF-8, reemplazando lo que la fuente no dibuje.

    Es idempotente y no falla si la salida está redirigida a un stream que no
    admite reconfiguración (por ejemplo, capturada por un test runner).
    """
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (ValueError, OSError):
            # Stream cerrado o sin soporte: no vale la pena tumbar el script.
            pass
