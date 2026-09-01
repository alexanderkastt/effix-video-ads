"""Corrida del ad skeleton musical sync del nicho sin_arrancar. Se borra al terminar.

Fases, para no gastar todo de una:
    cancion  ·  hero  ·  escenas  ·  clips  ·  montaje  ·  todo
"""
import sys, io, json, glob, argparse, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fal_client

from src.audio_extra import componer_cancion
from src.estilos_especiales import ESTILOS_ESPECIALES
from src.paths import AUDIO_DIR, CLIPS_DIR, RENDERS_DIR, env
from src.personaje import Personaje
from src.video_generator import _descargar, _url_de, generar_clip

MODELO_VIDEO = "fal-ai/kling-video/v2.1/standard/image-to-video"
MODELO_IMG = "fal-ai/nano-banana-2"
MODELO_EDIT = "fal-ai/nano-banana-2/edit"

RUTA = sorted(glob.glob("scripts/guiones/effix_skeleton_sin-arrancar-v2-musical_*_director.json"))[-1]
G = json.loads(Path(RUTA).read_text(encoding="utf-8"))
JOB = G["job_id"]
CARPETA = CLIPS_DIR / JOB


def bible() -> str:
    s = ESTILOS_ESPECIALES["skeleton"]
    b = s["character_bibles"][s["bible_por_defecto"]]
    return b.replace("[THEME]", "modern LATAM trade-fair").replace(
        "[palette]", "warm amber and deep navy")


def fase_cancion() -> Path:
    ruta = componer_cancion(G["musica"], job_id=JOB)
    print(f"cancion: {ruta}  ({ruta.stat().st_size // 1024} KB)")
    return ruta


def fase_hero() -> Path:
    CARPETA.mkdir(parents=True, exist_ok=True)
    destino = CARPETA / "hero.png"
    if destino.exists():
        print(f"hero ya existe: {destino}")
        return destino
    prompt = (
        f"{bible()} Clean neutral full-body hero shot of the skeleton, relaxed "
        f"standing pose, even soft lighting, simple out-of-focus trade-fair hall "
        f"background. no text, no captions, no words, no letters, no watermark, no UI."
    )
    salida = fal_client.subscribe(
        MODELO_IMG,
        {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1},
    )
    _descargar(_url_de(salida, "images", "image"), destino)
    print(f"hero: {destino}")
    return destino


def _url_hero() -> str:
    ficha = CARPETA / "hero_url.txt"
    if ficha.exists():
        return ficha.read_text(encoding="utf-8").strip()
    with open(CARPETA / "hero.png", "rb") as fh:
        url = fal_client.upload(fh.read(), "image/png")
    ficha.write_text(url, encoding="utf-8")
    return url


def _escena(beat: dict, url: str) -> Path:
    n = beat["clip"]
    destino = CARPETA / f"clip_{n:02d}_base.png"
    if destino.exists():
        return destino
    prompt = (
        "Keep the exact same skeleton character from the reference image — "
        "identical skull shape, eye style and bone proportions. "
        f"{beat['prompt_imagen']}"
    )
    salida = fal_client.subscribe(
        MODELO_EDIT,
        {"prompt": prompt, "image_urls": [url], "aspect_ratio": "9:16",
         "resolution": "1K", "num_images": 1},
    )
    return _descargar(_url_de(salida, "images", "image"), destino)


def fase_escenas() -> None:
    url = _url_hero()
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(_escena, b, url): b["clip"] for b in G["beats"]}
        for f in as_completed(fut):
            print(f"  escena {fut[f]:02d}: {f.result().name}")


def fase_clips() -> None:
    def uno(beat: dict):
        n = beat["clip"]
        escena = dict(beat, beat=n)
        return generar_clip(
            escena, imagen=CARPETA / f"clip_{n:02d}_base.png", duracion_s=5,
            modelo=MODELO_VIDEO, carpeta=CARPETA, job_id=JOB, etiqueta="clip",
        )

    pendientes = [b for b in G["beats"]
                  if not (CARPETA / f"clip_{b['clip']:02d}.mp4").exists()]
    fallos = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(uno, b): b["clip"] for b in pendientes}
        for f in as_completed(fut):
            n = fut[f]
            try:
                c = f.result()
                print(f"  clip {n:02d}: {c.video.name} ({c.segundos_de_espera}s espera)")
            except Exception as e:
                fallos.append((n, f"{type(e).__name__}: {e}"))
    for n, e in fallos:
        print(f"  FALLO clip {n:02d}: {e}")


def _plan() -> dict:
    reparto = {}
    for b in G["beats"]:
        r = reparto.setdefault(b["beat_origen"], {"beat": b["beat_origen"],
                                                  "t_inicio_s": b["t_inicio_s"],
                                                  "t_fin_s": b["t_fin_s"]})
        r["t_inicio_s"] = min(r["t_inicio_s"], b["t_inicio_s"])
        r["t_fin_s"] = max(r["t_fin_s"], b["t_fin_s"])
    return {"duracion_clip_s": G["duracion_clip_s"],
            "corte_final_s": G["duracion_total_s"],
            "total_clips": G["total_clips"],
            "reparto": sorted(reparto.values(), key=lambda r: r["t_inicio_s"])}


def fase_montaje() -> Path:
    from src.postproduccion import filtros as filtros_texto, resolver

    clips = sorted(CARPETA.glob("clip_[0-9][0-9].mp4"))
    if not clips:
        raise FileNotFoundError(f"No hay clips en {CARPETA}")
    plan = _plan()
    guion_overlays = {"beats": [{"beat": b["beat_origen"],
                                 "texto_pantalla": b["texto_pantalla"]}
                                for b in G["beats"]]}
    cancion = AUDIO_DIR / JOB / "cancion_v2_util.mp3"
    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = RENDERS_DIR / f"{JOB}_skeleton_sin_arrancar.mp4"

    entradas, filtros = [], []
    for i, c in enumerate(clips):
        entradas += ["-i", str(c)]
        filtros.append(
            f"[{i}:v]trim=0:{plan['duracion_clip_s']},setpts=PTS-STARTPTS,"
            f"scale=720:1280:force_original_aspect_ratio=increase,"
            f"crop=720:1280,fps=24[v{i}]")
    cadena = "".join(f"[v{i}]" for i in range(len(clips)))
    dibujos = filtros_texto(resolver(guion_overlays, plan), CARPETA)
    if dibujos:
        filtros.append(f"{cadena}concat=n={len(clips)}:v=1:a=0[crudo]")
        filtros.append("[crudo]" + ",".join(dibujos) + "[vid]")
    else:
        filtros.append(f"{cadena}concat=n={len(clips)}:v=1:a=0[vid]")

    entradas += ["-i", str(cancion)]
    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         *entradas, "-filter_complex", ";".join(filtros),
         "-map", "[vid]", "-map", f"{len(clips)}:a",
         "-t", str(plan["corte_final_s"]),
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(salida)],
        check=True)
    print(f"RENDER: {salida}  ({salida.stat().st_size / 1024 / 1024:.1f} MB)")
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fase", choices=["cancion", "hero", "escenas", "clips", "montaje", "todo"])
    fase = ap.parse_args().fase
    print(f"guión: {Path(RUTA).name} · job {JOB} · {G['total_clips']} clips · {G['duracion_total_s']}s\n")
    if fase in ("cancion", "todo"):
        fase_cancion()
    if fase in ("hero", "todo"):
        fase_hero()
    if fase in ("escenas", "todo"):
        fase_escenas()
    if fase in ("clips", "todo"):
        fase_clips()
    if fase in ("montaje", "todo"):
        fase_montaje()
