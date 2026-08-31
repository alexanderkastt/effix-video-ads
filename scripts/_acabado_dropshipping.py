"""Acabado del ad de dropshipping: musica, lip-sync y montaje. Se borra al terminar."""
import sys, io, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from pathlib import Path
from src.audio_extra import componer_musica
from src.lipsync import sincronizar
from src.video_assembler import ensamblar, unir_locucion

ruta = sorted(glob.glob("scripts/guiones/effix_avengers_*_aprobado.json"))[-1]
g = json.load(open(ruta, encoding="utf-8"))
job = g["job_id"]
plan = json.load(open(f"assets/clips/{job}/manifiesto.json", encoding="utf-8"))["plan"]
print(f"job {job} · {plan['total_clips']} clips · corte {plan['corte_final_s']}s")

# 1. La pista de voz completa: la necesita el lip-sync y el montaje
voz = unir_locucion(job)
print("voz unida:", voz.name)

# 2. Musica por fal (stable-audio-25, $0.20 la pista)
musica = componer_musica(g["musica"], plan["corte_final_s"], job_id=job)
print("musica:", musica.name, f"{musica.stat().st_size//1024} KB")

# 3. Lip-sync solo donde el personaje habla al lente: el hook y el loop
fallos = []
hechos = sincronizar(g, plan, clips_a_camara=[1, 8], fallos=fallos)
print(f"lip-sync: {len(hechos)} clip(s)", [h.clip for h in hechos])
for f in fallos:
    print("   fallo:", f)

# 4. Montaje final
render = ensamblar(g, plan, musica=musica)
print(f"\nRENDER: {render.video}  ·  {render.duracion_s}s  ·  {render.clips} clips")
print(f"tamano: {render.video.stat().st_size/1024/1024:.1f} MB")
