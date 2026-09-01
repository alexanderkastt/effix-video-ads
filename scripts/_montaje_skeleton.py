"""Montaje del ad skeleton musical sync. Se borra al terminar.

La cancion manda: se recorta al tramo cantado, se detectan sus golpes reales y
los cortes de video caen en el golpe mas cercano al reparto teorico.
"""
import sys, io, json, glob, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from pathlib import Path
import librosa
from src.paths import AUDIO_DIR, CLIPS_DIR, RENDERS_DIR, env
from src.postproduccion import Overlay, cuerpo_para, filtros as filtros_texto

RUTA = Path(sorted(glob.glob("scripts/guiones/effix_skeleton_sin-arrancar-v2-musical_*_director.json"))[-1])
G = json.loads(RUTA.read_text(encoding="utf-8"))
JOB = G["job_id"]
CARPETA = CLIPS_DIR / JOB
INICIO, FIN = 21.66, 77.86          # tramo cantado, de la transcripcion
DUR = round(FIN - INICIO, 2)

# Overlay por linea de letra, en tiempos del tramo ya recortado
TEXTOS = [
    (0.00,  4.96, "Y era tu prima"),
    (4.96, 10.02, "Vendes online y nada"),
    (10.02, 12.52, "Publicas y nada"),
    (12.52, 14.68, "«Me falta pauta»"),
    (14.68, 19.82, "Pusiste pauta. Igual"),
    (19.82, 25.10, "No es el producto"),
    (25.10, 30.00, "Feria Effix · 16–18 oct"),
    (30.00, 34.36, "Plaza Mayor, Medellín"),
    (34.36, 36.70, "350 empresas"),
    (36.70, 41.32, "200 ponentes"),
    (41.32, 46.36, "Quien va, vuelve"),
    (46.36, 51.20, "Clic en el enlace"),
    (51.20, 53.80, "Ya no es tu prima"),
    (53.80, 56.20, "Feria Effix"),
]


def recortar_cancion() -> Path:
    origen = AUDIO_DIR / JOB / "cancion_v2.mp3"
    destino = AUDIO_DIR / JOB / "cancion_v2_util.mp3"
    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         "-ss", str(INICIO), "-to", str(FIN), "-i", str(origen),
         "-af", f"afade=t=in:st=0:d=0.4,afade=t=out:st={DUR - 0.6:.2f}:d=0.6,loudnorm=I=-14",
         "-c:a", "libmp3lame", "-b:a", "256k", str(destino)],
        check=True)
    return destino


def cortes(cancion: Path, n: int) -> list[float]:
    """n+1 marcas de tiempo: el reparto parejo, llevado al golpe mas cercano."""
    y, sr = librosa.load(str(cancion), sr=None, mono=True)
    _, frames = librosa.beat.beat_track(y=y, sr=sr)
    golpes = librosa.frames_to_time(frames, sr=sr).tolist()
    marcas = [0.0]
    for i in range(1, n):
        teorico = DUR * i / n
        cercano = min(golpes, key=lambda g: abs(g - teorico)) if golpes else teorico
        # Un golpe a mas de 0.6s del reparto teorico descuadra el montaje.
        marcas.append(round(cercano if abs(cercano - teorico) <= 0.6 else teorico, 3))
    marcas.append(DUR)
    return marcas


def montar(cancion: Path, marcas: list[float]) -> Path:
    clips = sorted(CARPETA.glob("clip_[0-9][0-9].mp4"))
    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = RENDERS_DIR / "EFFIX-SKELETON-sin-arrancar-musical.mp4"

    entradas, filtros = [], []
    for i, clip in enumerate(clips):
        largo = round(marcas[i + 1] - marcas[i], 3)
        entradas += ["-i", str(clip)]
        filtros.append(
            f"[{i}:v]trim=0:{largo},setpts=PTS-STARTPTS,"
            f"scale=720:1280:force_original_aspect_ratio=increase,crop=720:1280,fps=24[v{i}]")
    cadena = "".join(f"[v{i}]" for i in range(len(clips)))

    overlays = []
    for t0, t1, texto in TEXTOS:
        cuerpo, cabe = cuerpo_para(texto.upper())
        overlays.append(Overlay(texto=texto.upper(), inicio=t0, fin=min(t1, DUR),
                                cuerpo=cuerpo, cabe=cabe))
    no_caben = [o.texto for o in overlays if not o.cabe]
    if no_caben:
        print("   aviso: overlays al minimo legible:", ", ".join(no_caben))
    dibujos = filtros_texto(overlays, CARPETA)

    filtros.append(f"{cadena}concat=n={len(clips)}:v=1:a=0[crudo]")
    filtros.append("[crudo]" + ",".join(dibujos) + "[vid]")
    entradas += ["-i", str(cancion)]

    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         *entradas, "-filter_complex", ";".join(filtros),
         "-map", "[vid]", "-map", f"{len(clips)}:a", "-t", str(DUR),
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(salida)],
        check=True)
    return salida


if __name__ == "__main__":
    cancion = recortar_cancion()
    print(f"cancion util: {cancion.name} · {DUR}s")
    clips = sorted(CARPETA.glob("clip_[0-9][0-9].mp4"))
    marcas = cortes(cancion, len(clips))
    print("cortes:", [f"{m:.2f}" for m in marcas])
    salida = montar(cancion, marcas)
    print(f"\nRENDER: {salida} · {salida.stat().st_size / 1024 / 1024:.1f} MB")
