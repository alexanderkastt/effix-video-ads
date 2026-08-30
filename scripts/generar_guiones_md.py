"""Escribe los 30 guiones en Markdown, listos para copiar y pegar.

    python scripts/generar_guiones_md.py

El HTML sirve para revisar y aprobar; el Markdown sirve para trabajar: se pega
en Notion, en Obsidian o en un correo, se edita a mano y se versiona en git con
un diff legible.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from src.narracion_effix import CTA_POR_PASE  # noqa: E402
from src.parrilla import ROLES, construir_parrilla, verificar  # noqa: E402

SALIDA = RAIZ / "outputs" / "GUIONES-EFFIX.md"

ESTILOS = {
    "micro_doc_ugc": "Micro-doc UGC", "ugc_realista": "UGC realista",
    "crochet": "Crochet", "skeleton": "Skeleton", "zack_films": "Zack D Films",
    "object_talk": "Object Talk", "pixar_animado": "Pixar", "cinematic": "Cinematic",
    "claymation": "Claymation", "cyberpunk": "Cyberpunk", "anime": "Anime",
    "minecraft": "Minecraft", "musical_sync": "Musical", "avengers": "Avengers",
}

NIVELES = {
    "unaware": "no sabe que tiene el problema",
    "problem": "siente el dolor",
    "solution": "conoce el tipo de solución",
}

PASOS = [
    ("momento", "Momento"), ("sintoma", "Síntoma"),
    ("reaccion_interna", "Reacción interna"), ("explicacion_fallida", "Explicación fallida"),
    ("patron", "Patrón"), ("causa_raiz", "Causa raíz"), ("mecanismo", "Mecanismo"),
]


def guion_md(g: dict, n_nicho: int, letra: str) -> list[str]:
    """Un guión: cabecera, locución de corrido y su tabla de clips."""
    L: list[str] = []
    L.append(f"### {n_nicho:02d}{letra} · {g['papel']}")
    L.append("")
    L.append(
        f"**Formato:** {ESTILOS.get(g['estilo'], g['estilo'])} · "
        f"**Nivel:** {g['nivel']} ({NIVELES.get(g['nivel'], '')}) · "
        f"**Gatillo:** {g['gatillo_rol']}"
    )
    L.append("")
    L.append(f"**Duración:** {g['total_clips']} clips × 4s = {g['duracion_s']}s · "
             f"locución {g['locucion_s']}s · holgura {g['holgura_s']}s")
    L.append("")
    L.append(f"> {g['nota_rol']}")
    L.append("")

    # La locución seguida — así es como suena de verdad
    L.append("**Locución completa:**")
    L.append("")
    hablado = " ".join(
        c["narracion"] for c in g["linea_tiempo"] if c["lleva_narracion"]
    )
    L.append(f"> {hablado}")
    L.append("")

    # La tabla de rodaje
    L.append("| Clip | Tiempo | Beat | Voz | En pantalla | Cámara |")
    L.append("|---|---|---|---|---|---|")
    for c in g["linea_tiempo"]:
        voz = c["narracion"] if c["lleva_narracion"] else "*(continúa)*"
        L.append(
            f"| {c['clip']:02d} | {c['t_inicio_s']}–{c['t_fin_s']}s | {c['nombre']} | "
            f"{voz} | {c['texto_pantalla']} | {c['movimiento_camara']} |"
        )
    L.append("")
    return L


def main() -> int:
    parrilla = construir_parrilla()
    problemas = verificar(parrilla)

    L: list[str] = []
    L.append("# Guiones — Feria Effix 2026")
    L.append("")
    L.append(
        f"{parrilla['total_nichos']} nichos · **{parrilla['total_guiones']} guiones** · "
        f"{parrilla['total_clips']} clips de 4 segundos · "
        f"{parrilla['total_segundos'] // 60} minutos de video · "
        f"{len(parrilla['estilos_usados'])} formatos visuales"
    )
    L.append("")
    meses = ("enero febrero marzo abril mayo junio julio agosto "
             "septiembre octubre noviembre diciembre").split()
    hoy = date.today()
    L.append(f"*Generado el {hoy.day} de {meses[hoy.month - 1]} de {hoy.year} · "
             f"validación: {', '.join(problemas)}*")
    L.append("")

    L.append("## Cómo está armado")
    L.append("")
    L.append(
        "Cada nicho es un tipo de persona que compraría entrada, con la "
        "micro-situación en la que su problema se vuelve real. Tres guiones por "
        "nicho, y entre ellos cambia el gancho, el formato visual y el punto del embudo."
    )
    L.append("")
    for rol in ROLES:
        cta = CTA_POR_PASE[rol["pase"]]
        L.append(f"- **{rol['id']} — {rol['papel']}.** {rol['nota']} "
                 f"CTA: «{cta['hablado']}» · gatillo: {rol['gatillo']}")
    L.append("")

    L.append("### Reglas que cumple cada guión")
    L.append("")
    L.append("| Regla | Por qué |")
    L.append("|---|---|")
    L.append("| Corte de escena cada 4 segundos | Es la unidad de generación de video |")
    L.append("| 60 segundos en total | Techo del pico de alcance en Reels (30–60s) |")
    L.append("| La locución va de corrido | Cada línea arrastra a la siguiente con un conector |")
    L.append("| Sin descuentos ni códigos | El precio se defiende con lo que incluye |")
    L.append("| Sin mencionar el taller de IA | Decisión de comunicación |")
    L.append("| Nunca promete más días de los que da el pase | El Pasaporte da 3, el evento dura 5 |")
    L.append("| Describe la situación, no a la persona | Política de Meta sobre atributos personales |")
    L.append("| Texto en pantalla de máximo 7 palabras | El video tiene que funcionar sin sonido |")
    L.append("")

    L.append("### Los tres pases")
    L.append("")
    L.append("| Pase | Fechas | Precio | Cómo se vende |")
    L.append("|---|---|---|---|")
    L.append("| **Pasaporte 3 días** | 16, 17 y 18 de octubre | $201.300 | Foco de los 30 guiones. Cae en fin de semana: no hay que pedir permiso |")
    L.append("| Entrada VIP | 15 al 19 de octubre | $1.155.000 | Upsell. Se vende por acceso y sin filas, no por duración |")
    L.append("| Entrada Black | 15 al 19 + premium | $3.997.000 | 400 cupos en todo el mundo. Escasez verificable |")
    L.append("")
    L.append("---")
    L.append("")

    # Índice
    L.append("## Índice")
    L.append("")
    for i, nicho in enumerate(parrilla["nichos"], 1):
        estilos = " · ".join(ESTILOS.get(g["estilo"], g["estilo"]) for g in nicho["guiones"])
        L.append(f"{i:02d}. **{nicho['etiqueta']}** — {estilos}")
    L.append("")
    L.append("---")
    L.append("")

    # Los diez nichos
    for i, nicho in enumerate(parrilla["nichos"], 1):
        L.append(f"## {i:02d} · {nicho['etiqueta']}")
        L.append("")
        L.append(f"**A quién le habla:** {nicho['audiencia']}")
        L.append("")
        L.append(f"**Ancla narrativa:** `{nicho['ancla']}` · "
                 f"**Gatillo del nicho:** {nicho['gatillo_principal']}")
        L.append("")

        L.append("<details>")
        L.append("<summary><b>La micro-situación completa — los 7 pasos</b></summary>")
        L.append("")
        for campo, etiqueta in PASOS:
            L.append(f"**{etiqueta}.** {nicho['micro_situacion'][campo]}")
            L.append("")
        L.append("</details>")
        L.append("")

        for g in nicho["guiones"]:
            L += guion_md(g, i, g["variante"])

        L.append("---")
        L.append("")

    L.append("## Antes de producir")
    L.append("")
    L.append(
        "El número de clips que ves aquí es la **estimación** a 2,2 palabras por "
        "segundo. Cuando la voz esté generada en ElevenLabs, `planificar_desde_audio()` "
        "mide el mp3 real con ffprobe y recalcula: con la velocidad configurada el "
        "desvío llega a siete segundos, suficiente para que los clips no cuadren."
    )
    L.append("")
    L.append("El orden correcto es: estimar → generar la voz → medir → generar los videos.")
    L.append("")

    SALIDA.write_text("\n".join(L), encoding="utf-8")
    kb = SALIDA.stat().st_size // 1024
    print(f"✅ {SALIDA.relative_to(RAIZ)} · {kb} KB · {len(L)} líneas")
    print(f"   {parrilla['total_guiones']} guiones · validación: {', '.join(problemas)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
