"""Rehace lip-sync y montaje sobre la locucion masculina. Se borra al terminar."""
import sys, io, json, glob, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from pathlib import Path
from src.pipeline_orchestrator import producir
from src.lipsync import sincronizar
from src.video_assembler import ensamblar
from src.paths import CLIPS_DIR, AUDIO_DIR, RENDERS_DIR

g = json.load(open(sorted(glob.glob("scripts/guiones/effix_avengers_*_aprobado.json"))[-1], encoding="utf-8"))
job = g["job_id"]
carpeta = CLIPS_DIR / job

# Los sync viejos llevan la voz femenina: no sirven ni como respaldo
for viejo in carpeta.glob("clip_*_sync.mp4"):
    viejo.unlink()
    print("borrado:", viejo.name)

# Recalcula el plan sobre la locucion nueva. No regenera clips: los 8 ya estan
# en disco y producir() salta lo que existe.
r = producir(g, reusar_voz=True, personaje="andres",
             estilo_en="epic superhero cinematic look, dramatic backlight, high-end VFX")
plan = r.plan
print(f"plan: {plan['total_clips']} clips · audio {plan['audio_total_s']}s · corte {plan['corte_final_s']}s")
print("clips nuevos generados:", len(r.clips), "| fallos:", r.fallos)

fallos = []
hechos = sincronizar(g, plan, clips_a_camara=[1, 8], fallos=fallos)
print("lip-sync:", [h.clip for h in hechos], "| fallos:", fallos)

anterior = RENDERS_DIR / f"{job}.mp4"
if anterior.exists():
    shutil.move(str(anterior), str(RENDERS_DIR / f"{job}_v2_vozfem.mp4"))

render = ensamblar(g, plan, musica=AUDIO_DIR / job / "musica.mp3")
print(f"\nRENDER FINAL: {render.video} · {render.duracion_s}s · {render.clips} clips")
print(f"tamano: {render.video.stat().st_size/1024/1024:.1f} MB")
