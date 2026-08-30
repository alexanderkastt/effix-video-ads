"""Prueba de extremo a extremo SIN gastar un peso.
Recorre toda la capa creativa con datos reales del proyecto y verifica cada
eslabón. No hace ni una llamada a fal.ai, ElevenLabs o Suno.

    python scripts/test_dry_run.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.consola import usar_utf8                  # noqa: E402
from src import cost_estimator                     # noqa: E402
from src.music_engine import MusicEngine           # noqa: E402
from src.paths import BRAND_DNA_JSON, ensure_dirs  # noqa: E402
from src.scene_builder import SceneBuilder         # noqa: E402
from src.script_engine import ScriptEngine         # noqa: E402
from src.storyboard_builder import StoryboardBuilder  # noqa: E402


usar_utf8()

CONCEPTO = "Por qué todo emprendedor de ecommerce LATAM debe estar en Feria Effix 2026"
ESTILO = "ugc_realista"
MARCA = "effix"
ANGULO = "comunidad_que_no_tienes"

fallos: list[str] = []


def check(n: int, titulo: str, ok: bool, detalle: str = "") -> bool:
    marca = "✅" if ok else "❌"
    print(f"{marca} {n}. {titulo}")
    if detalle:
        for linea in detalle.splitlines():
            print(f"      {linea}")
    if not ok:
        fallos.append(f"{n}. {titulo} — {detalle}")
    return ok


def main() -> int:
    ensure_dirs()
    print("\n🧪 DRY RUN — capa creativa Video Factory\n" + "─" * 62)

    # 1 ── brand_dna.json
    try:
        engine = ScriptEngine(marca=MARCA)
        dna_ok = bool(engine.dna.get("angulos_de_contenido"))
        check(
            1, "brand_dna.json se carga correctamente", dna_ok,
            f"{BRAND_DNA_JSON.name} · {len(engine.dna['angulos_de_contenido'])} ángulos · "
            f"{len(engine.dna['palabras_prohibidas'])} palabras prohibidas",
        )
    except Exception as exc:
        check(1, "brand_dna.json se carga correctamente", False, str(exc))
        return resumen()

    # 2 ── guión de 11 beats
    script = engine.generate_script(CONCEPTO, ESTILO, ANGULO)
    n_beats = len(script["beats"])
    palabras = sum(b["palabras_narracion"] for b in script["beats"])
    check(
        2, "ScriptEngine genera un guión de 11 beats", n_beats == 11,
        f"{n_beats} beats · {script['duracion_total_s']}s · {palabras} palabras de locución "
        f"(presupuesto 96-108)",
    )

    # 3 ── validación del guión
    errores = engine.validate_script(script)
    check(
        3, "validate_script() no encuentra errores", errores == ["OK"],
        "\n".join(errores) if errores != ["OK"] else "sin errores",
    )

    # 4 ── prompts de video en rango
    builder = SceneBuilder(ESTILO)
    script = builder.apply_to_script(script)
    errores_prompt = builder.validate_prompts(script)
    longitudes = [b["palabras_prompt"] for b in script["beats"]]
    check(
        4, "SceneBuilder produce prompts de 120-200 palabras", errores_prompt == ["OK"],
        "\n".join(errores_prompt) if errores_prompt != ["OK"]
        else f"min {min(longitudes)} · max {max(longitudes)} palabras · modelo {script['modelo_fal']}",
    )

    # 5 ── brief de música
    music = MusicEngine(marca=MARCA)
    musica = music.generate_background_brief(
        tono=engine.dna["tono"], estilo=ESTILO, duracion_s=script["duracion_total_s"]
    )
    musica_ok = bool(musica.get("suno_prompt")) and musica["volumen_relativo"] == 0.25
    check(
        5, "MusicEngine genera el brief de música correcto", musica_ok,
        f"{musica['suno_prompt']} · {musica['bpm_recomendado']} BPM · "
        f"volumen {int(musica['volumen_relativo'] * 100)}%",
    )

    # 5b ── modo sincronizado (no cuenta como check numerado, pero debe correr)
    cancion = music.generate_music_video_song(script["beats"])
    versos = cancion["suno_custom_lyrics"].count("[")
    print(f"      modo sincronizado OK · {versos} secciones de letra")

    # 6 ── storyboard HTML
    story = StoryboardBuilder(marca=MARCA)
    try:
        html_path = story.generate_html(script, musica)
        existe = html_path.exists() and html_path.stat().st_size > 2000
        check(
            6, "StoryboardBuilder genera el HTML sin errores", existe,
            f"{html_path.name} · {html_path.stat().st_size // 1024} KB",
        )
    except Exception as exc:
        check(6, "StoryboardBuilder genera el HTML sin errores", False, repr(exc))
        html_path = None

    # 7 ── el HTML es válido y autónomo
    if html_path and html_path.exists():
        contenido = html_path.read_text(encoding="utf-8")
        autonomo = (
            "<!doctype html>" in contenido.lower()
            and "http://" not in contenido
            and "https://" not in contenido
            and contenido.count("<article") == n_beats
        )
        check(
            7, "El HTML se abre correctamente (autónomo, sin internet)", autonomo,
            f"{contenido.count('<article')} tarjetas · cero recursos externos"
            if autonomo else "tiene referencias externas o le faltan tarjetas",
        )
    else:
        check(7, "El HTML se abre correctamente (autónomo, sin internet)", False, "no se generó")

    # 8 ── JSON aprobado
    caracteres = sum(len(b["narracion"]) for b in script["beats"])
    est = cost_estimator.estimar(
        n_clips=n_beats,
        duracion_clip_s=script["beats"][0]["duracion_s"],
        modelo_fal=script["modelo_fal"],
        caracteres_voz=caracteres,
        con_musica=True,
    )
    script["costo_estimado_usd"] = est["total"]

    json_path = story.save_json(script, musica, estado="aprobado")
    datos = json.loads(json_path.read_text(encoding="utf-8"))
    claves = {"job_id", "timestamp", "concepto", "estilo", "marca", "estado",
              "beats", "musica", "costo_estimado_usd", "duracion_total_s"}
    faltan = claves - set(datos)
    check(
        8, "El JSON aprobado se guarda con estructura correcta", not faltan,
        f"{json_path.name} · {len(datos['beats'])} beats · estado {datos['estado']}"
        if not faltan else f"faltan claves: {', '.join(sorted(faltan))}",
    )

    print("─" * 62)
    print(cost_estimator.formatear(est))
    return resumen()


def resumen() -> int:
    print()
    if fallos:
        print("🔴 DRY RUN CON FALLOS:")
        for f in fallos:
            print(f"   · {f}")
        return 1
    print("🟢 DRY RUN COMPLETO — listo para producción real")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
