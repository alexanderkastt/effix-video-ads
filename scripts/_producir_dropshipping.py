"""Corrida única del ad épico de dropshipping. Se borra al terminar."""
import sys, io, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from src.pipeline_orchestrator import producir

ruta = sorted(glob.glob("scripts/guiones/effix_avengers_*_aprobado.json"))[-1]
g = json.load(open(ruta, encoding="utf-8"))
print("guión:", ruta, "| job:", g["job_id"], "| modelo:", g["modelo_fal"])

r = producir(
    g,
    reusar_voz=True,                       # la voz ya está en disco y medida
    personaje="andres",
    estilo_en="epic superhero cinematic look, dramatic backlight, high-end VFX",
)
print("\nclips:", len(r.clips), "| plan:", r.plan["total_clips"], "×", r.plan["duracion_clip_s"], "s")
print("personaje:", r.personaje, "| segundos totales:", r.segundos_totales)
for c in r.clips:
    print(f"  clip {c['clip']:02d}  {c['espera_s']}s espera  {c['video']}")
if r.fallos:
    print("\nFALLOS:")
    for f in r.fallos:
        print("  ", f)
else:
    print("\n✅ sin fallos")
