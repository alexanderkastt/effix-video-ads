"""Convierte el banco de ganchos en markdown a JSON consultable por código.

El markdown es la fuente: es lo que lee la skill `ganchos-y-retencion` y lo que
Alexander edita cuando agrega ganchos. El JSON es derivado — se regenera, no se
edita a mano.

    python scripts/parsear_banco.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MD = RAIZ / ".claude" / "skills" / "ganchos-y-retencion" / "references" / "banco-320.md"
OUT = RAIZ / "config" / "banco_ganchos.json"

CATEGORIAS = {
    "BRECHA DE CURIOSIDAD": "curiosidad",
    "CALLOUT DE IDENTIDAD": "callout",
    "DOLOR NOMBRADO": "dolor_nombrado",
    "PROMESA CON PLAZO Y SIN SACRIFICIO": "promesa_con_plazo",
    "CONTRARIAN / INVERSIÓN DE CREENCIA": "contrarian",
    "ESPECIFICIDAD NUMÉRICA": "especificidad",
    "PRUEBA / AUTORIDAD": "prueba",
    "HISTORIA / ENTRADA EN ESCENA": "historia",
}

MARCAS = {"@alexemprendee": "alexander", "@militougc": "mile"}
NIVELES = ("unaware", "problem", "solution", "product", "most aware")


def parsear(texto: str) -> list[dict]:
    filas: list[dict] = []
    categoria = marca = None

    for linea in texto.splitlines():
        m = re.match(r"^# CATEGORÍA \d+ — (.+)$", linea.strip())
        if m:
            categoria = CATEGORIAS.get(m.group(1).strip())
            continue

        m = re.match(r"^## (@\w+|Genéricos con variable)", linea.strip())
        if m:
            marca = MARCAS.get(m.group(1), "generico")
            continue

        if not linea.startswith("|") or not categoria:
            continue

        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) < 4 or not celdas[0].isdigit():
            continue

        numero, gancho, nivel, objetivo = celdas[:4]
        nota = celdas[4] if len(celdas) > 4 else ""
        if nivel not in NIVELES:
            continue

        filas.append(
            {
                "n": int(numero),
                "categoria": categoria,
                "marca": marca,
                "gancho": gancho,
                "nivel": nivel.replace(" ", "_"),
                "objetivo": "conversion" if objetivo.startswith("conver") else "alcance",
                "nota": nota,
                # Un corchete sin rellenar es una cifra o un dato que hay que
                # traer del cliente. Nunca inventarlo.
                "tiene_variables": "[" in gancho,
                # Advertencia legal (Ley 1480) o de política de plataforma
                "advertencia": nota.startswith("⚠️"),
            }
        )

    return filas


def main() -> int:
    if not MD.exists():
        print(f"❌ No encuentro el banco en {MD}")
        return 1

    filas = parsear(MD.read_text(encoding="utf-8"))

    OUT.write_text(
        json.dumps({"total": len(filas), "ganchos": filas}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"✅ {len(filas)} ganchos → {OUT.relative_to(RAIZ)}")
    for eje in ("categoria", "marca", "objetivo", "nivel"):
        conteo = dict(Counter(f[eje] for f in filas))
        print(f"   {eje}: {conteo}")
    print(f"   con advertencia: {sum(1 for f in filas if f['advertencia'])}")

    if len(filas) != 320:
        print(f"⚠️  Se esperaban 320 y salieron {len(filas)}. Revisá el markdown.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
