"""Rutas del proyecto y carga de configuración.

Punto único donde se resuelven rutas y se leen los JSON de marca. Cualquier
módulo que necesite el ADN de marca lo pide aquí, no lee archivos por su cuenta.
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv

# La raíz del proyecto es el padre de src/
ROOT = Path(__file__).resolve().parent.parent

CONFIG_DIR = ROOT / "config"
SCRIPTS_DIR = ROOT / "scripts"
GUIONES_DIR = SCRIPTS_DIR / "guiones"
STORYBOARDS_DIR = SCRIPTS_DIR / "storyboards"
ASSETS_DIR = ROOT / "assets"
CLIPS_DIR = ASSETS_DIR / "clips"
AUDIO_DIR = ASSETS_DIR / "audio"
RENDERS_DIR = ASSETS_DIR / "renders"
OUTPUTS_DIR = ROOT / "outputs"
LOGS_DIR = ROOT / "logs"

BRAND_JSON = CONFIG_DIR / "brand.json"
BRAND_DNA_JSON = CONFIG_DIR / "brand_dna.json"

# Carga el .env una sola vez al importar
load_dotenv(ROOT / ".env")


def env(key: str, default: str | None = None) -> str | None:
    """Lee una variable del .env con valor por defecto."""
    return os.getenv(key, default)


def env_int(key: str, default: int) -> int:
    """Lee una variable numérica del .env; si viene vacía o rota, usa el default."""
    try:
        return int(str(os.getenv(key, default)).strip())
    except (TypeError, ValueError):
        return default


def env_float(key: str, default: float) -> float:
    """Lee una variable decimal del .env; si viene vacía o rota, usa el default."""
    try:
        return float(str(os.getenv(key, default)).strip())
    except (TypeError, ValueError):
        return default


def _load_json(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(
            f"No encuentro {path.name} en {path.parent}. "
            f"Este archivo es obligatorio para generar guiones."
        )
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_brand_dna(marca: str = "effix") -> dict:
    """Devuelve el ADN creativo de la marca (estrategia de contenido)."""
    data = _load_json(BRAND_DNA_JSON)
    if marca not in data:
        disponibles = ", ".join(sorted(data)) or "ninguna"
        raise KeyError(f"La marca '{marca}' no está en brand_dna.json. Hay: {disponibles}")
    return data[marca]


def load_brand_tokens(marca: str = "effix") -> dict:
    """Devuelve los tokens visuales de la marca (colores, fuentes, hashtags)."""
    data = _load_json(BRAND_JSON)
    return data.get(marca, {})


def ensure_dirs() -> None:
    """Crea las carpetas de trabajo si faltan."""
    for d in (GUIONES_DIR, STORYBOARDS_DIR, CLIPS_DIR, AUDIO_DIR, RENDERS_DIR, LOGS_DIR):
        d.mkdir(parents=True, exist_ok=True)
