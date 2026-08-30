"""CLI de producción — el comando del día a día.

Genera el guión, la escenografía, el brief de música y el storyboard, y PARA
para que un humano apruebe antes de gastar un peso en APIs.

Ejemplos:

    python scripts/crear_video.py \
      --concepto "Por qué todo ecommerce LATAM debe ir a Feria Effix" \
      --estilo ugc_realista --marca effix --angulo comunidad_que_no_tienes

    python scripts/crear_video.py --concepto "Himno Feria Effix 2026" \
      --estilo musical_sync --marca effix --solo-musica

    python scripts/crear_video.py --desde-guion scripts/guiones/xxx_aprobado.json --producir
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Permite ejecutar el script directamente sin instalar el paquete
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import cost_estimator                     # noqa: E402
from src.music_engine import MusicEngine           # noqa: E402
from src.paths import ensure_dirs                  # noqa: E402
from src.scene_builder import SceneBuilder, estilos_disponibles  # noqa: E402
from src.script_engine import ANGULOS, ScriptEngine              # noqa: E402
from src.storyboard_builder import StoryboardBuilder             # noqa: E402


def construir_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="crear_video.py",
        description="Genera guión, storyboard y brief de música para un video de Feria Effix.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("--concepto", help="De qué trata el video.")
    p.add_argument(
        "--estilo",
        default="ugc_realista",
        choices=estilos_disponibles(),
        help="Estilo visual del video.",
    )
    p.add_argument("--marca", default="effix", help="Marca del brand_dna.json.")
    p.add_argument(
        "--angulo",
        default=None,
        help=f"Ángulo narrativo. Disponibles: {', '.join(sorted(ANGULOS))}",
    )
    p.add_argument("--voz", default="alexander", help="Perfil de voz para ElevenLabs.")
    p.add_argument("--hook", default="A", choices=["A", "B", "C"], help="Variante de hook.")
    p.add_argument("--solo-musica", action="store_true", help="Sólo el brief de música.")
    p.add_argument("--solo-guion", action="store_true", help="Sólo el guión, sin storyboard.")
    p.add_argument("--musical", action="store_true", help="Activa la canción sincronizada.")
    p.add_argument("--desde-guion", help="Ruta a un JSON de guión ya aprobado.")
    p.add_argument("--producir", action="store_true", help="Lanza la generación real (gasta).")
    p.add_argument("--solo-beats", help="Beats a producir, ej: 1,2,3")
    p.add_argument("--si", action="store_true", help="Aprueba sin preguntar (no interactivo).")
    return p


def _parse_beats(spec: str | None) -> list[int] | None:
    if not spec:
        return None
    return [int(x) for x in spec.replace(" ", "").split(",") if x]


def flujo_creativo(args) -> int:
    ensure_dirs()

    engine = ScriptEngine(marca=args.marca)
    builder = SceneBuilder(args.estilo)
    music = MusicEngine(marca=args.marca)
    story = StoryboardBuilder(marca=args.marca)

    # 1-2. Guión
    print(f"\n🧠 Generando guión — estilo {args.estilo}, marca {args.marca}")
    script = engine.generate_script(
        concepto=args.concepto,
        estilo=args.estilo,
        angulo=args.angulo,
        hook_variante=args.hook,
    )
    print(f"   Ángulo: {script['angulo_etiqueta']}")

    # 3. Validación del guión
    errores = engine.validate_script(script)
    if errores != ["OK"]:
        print("\n❌ El guión no pasó la validación:")
        for e in errores:
            print(f"   · {e}")
        return 1
    print(f"✅ Guión válido — {len(script['beats'])} beats · {script['duracion_total_s']}s")

    # 4. Escenografía
    script = builder.apply_to_script(script)
    errores_prompt = builder.validate_prompts(script)
    if errores_prompt != ["OK"]:
        print("\n❌ Los prompts de video no pasaron la validación:")
        for e in errores_prompt:
            print(f"   · {e}")
        return 1
    print(f"✅ Escenografía aplicada — modelo {script['modelo_fal']}")

    # 5. Música
    if args.musical or args.estilo == "musical_sync":
        musica = music.generate_music_video_song(script["beats"], marca=args.marca)
        print("🎵 Canción sincronizada — letra construida desde el guión")
    else:
        musica = music.generate_background_brief(
            tono=engine.dna["tono"], estilo=args.estilo, duracion_s=script["duracion_total_s"]
        )
        print(f"🎵 Música de fondo — {musica['suno_prompt']} · {musica['bpm_recomendado']} BPM")

    # 6. Costo
    caracteres = sum(len(b["narracion"]) for b in script["beats"])
    est = cost_estimator.estimar(
        n_clips=len(script["beats"]),
        duracion_clip_s=script["beats"][0]["duracion_s"],
        modelo_fal=script["modelo_fal"],
        caracteres_voz=caracteres,
        con_musica=True,
    )
    script["costo_estimado_usd"] = est["total"]

    if args.solo_guion:
        ruta = story.save_json(script, musica, estado="borrador")
        print(f"\n📄 Guión guardado: {ruta.relative_to(Path.cwd())}")
        return 0

    # 7. Storyboard
    html_path = story.generate_html(script, musica)

    print("\n" + "─" * 62)
    print(f"✅ Guión generado — {len(script['beats'])} beats")
    print(f"🎬 Storyboard: {html_path}")
    print("🎵 Brief de música listo")
    print(cost_estimator.formatear(est))
    print("─" * 62)

    # 8. Aprobación humana
    if args.si:
        respuesta = "s"
    else:
        try:
            respuesta = input("\n¿Apruebas el guión? [s/N]: ").strip().lower()
        except EOFError:
            print("\n(sin terminal interactiva — se guarda como borrador)")
            respuesta = "n"

    if respuesta == "s":
        ruta = story.save_json(script, musica, estado="aprobado")
        print(f"\n✅ Guión aprobado: {ruta}")
        print("   Para producir:")
        print(f'   python scripts/crear_video.py --desde-guion "{ruta}" --producir')
        return 0

    ruta = story.save_json(script, musica, estado="borrador")
    print(f"\n📝 Guardado como borrador: {ruta}")
    print("   Ajusta el ángulo (--angulo) o el hook (--hook) y vuelve a correrlo.")
    return 0


def flujo_produccion(args) -> int:
    ruta = Path(args.desde_guion)
    if not ruta.exists():
        print(f"❌ No encuentro el guión en {ruta}")
        return 1

    with ruta.open(encoding="utf-8") as fh:
        guion = json.load(fh)

    beats = _parse_beats(args.solo_beats)
    total = len(beats) if beats else len(guion.get("beats", []))

    print(f"\n📂 Guión: {guion.get('concepto', '(sin concepto)')}")
    print(f"   Estado: {guion.get('estado')} · estilo: {guion.get('estilo')}")
    print(f"   Beats a producir: {total}")

    if guion.get("estado") != "aprobado":
        print("\n⚠️  Este guión no está aprobado. Ábrelo en el storyboard y apruébalo primero.")
        return 1

    print("\n⛔ El pipeline de generación todavía no está construido.")
    print("   Esta fase sólo cubre la capa creativa: guión, escenografía,")
    print("   música y storyboard. Faltan los módulos que gastan dinero:")
    print("     · src/voice_generator.py   (ElevenLabs)")
    print("     · src/video_generator.py   (fal.ai)")
    print("     · src/pipeline_orchestrator.py")
    print("     · src/video_assembler.py   (ffmpeg)")
    print("\n   El guión aprobado ya queda listo para cuando existan.")
    return 2


def flujo_solo_musica(args) -> int:
    ensure_dirs()
    music = MusicEngine(marca=args.marca)
    engine = ScriptEngine(marca=args.marca)

    if args.estilo == "musical_sync" and args.concepto:
        script = engine.generate_script(args.concepto, args.estilo, args.angulo)
        brief = music.generate_music_video_song(script["beats"], marca=args.marca)
    else:
        brief = music.generate_background_brief(
            tono=engine.dna["tono"], estilo=args.estilo
        )

    print("\n🎵 Brief de música")
    print(json.dumps(brief, ensure_ascii=False, indent=2))
    return 0


def main(argv: list[str] | None = None) -> int:
    args = construir_parser().parse_args(argv)

    if args.desde_guion:
        return flujo_produccion(args)

    if args.solo_musica:
        return flujo_solo_musica(args)

    if not args.concepto:
        print("❌ Falta --concepto (o usa --desde-guion para producir).")
        return 1

    return flujo_creativo(args)


if __name__ == "__main__":
    raise SystemExit(main())
