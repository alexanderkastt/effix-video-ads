"""Regenera el clip 08 con la feria visible y vuelve a montar."""
import sys, io, json, glob, shutil
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from pathlib import Path
from src.pipeline_orchestrator import producir
from src.lipsync import sincronizar
from src.video_assembler import ensamblar
from src.paths import CLIPS_DIR, RENDERS_DIR

ruta = sorted(glob.glob("scripts/guiones/effix_avengers_*_aprobado.json"))[-1]
g = json.load(open(ruta, encoding="utf-8"))
job = g["job_id"]
carpeta = CLIPS_DIR / job
plan = json.load(open(carpeta / "manifiesto.json", encoding="utf-8"))["plan"]

# El render anterior se guarda: si el clip nuevo sale peor, hay a qué volver.
anterior = RENDERS_DIR / f"{job}.mp4"
if anterior.exists():
    shutil.move(str(anterior), str(RENDERS_DIR / f"{job}_v1.mp4"))
    print("render v1 guardado")

# Fuera el clip 08 y sus derivados: sin borrarlos, producir() los da por hechos
for f in ("clip_08.mp4", "clip_08_base.png", "clip_08_sync.mp4"):
    p = carpeta / f
    if p.exists():
        p.unlink()
        print("borrado:", f)

r = producir(g, solo_beats=[8], reusar_voz=True, personaje="andres",
             estilo_en="epic superhero cinematic look, dramatic backlight, high-end VFX")
print("clips regenerados:", [c["clip"] for c in r.clips], "| fallos:", r.fallos)

fallos = []
hechos = sincronizar(g, plan, clips_a_camara=[8], fallos=fallos)
print("lip-sync:", [h.clip for h in hechos], "| fallos:", fallos)

render = ensamblar(g, plan, musica=Path(f"assets/audio/{job}/musica.mp3"))
print(f"\nRENDER v2: {render.video} · {render.duracion_s}s · {render.clips} clips")
print(f"tamano: {render.video.stat().st_size/1024/1024:.1f} MB")
