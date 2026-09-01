"""Corrida del ad ANIMADO 2D "La acera" — nicho tienda_ropa. Se borra al terminar.

Diálogo a dos voces (Rosa y Marce) más la voz de marca en el CTA. Un clip por
línea, planos alternados: en cada clip habla una sola cara, que es lo único que
el lip-sync sincroniza bien.

Orden de producción (memoria del proyecto): PRIMERO EL AUDIO. La duración real
de cada mp3, medida con ffprobe, decide cuánto dura su clip — Kling o1 acepta
de 3 a 10s, así que cada línea se paga a su medida y no en tramos de 5s.

Fases, para no gastar todo de una:
    voz · hojas · escenas · clips · lipsync · montaje · todo
"""
import argparse
import io
import json
import math
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")

import fal_client

from src.audio_extra import voz_para
from src.lipsync import sincronizar_clip
from src.paths import AUDIO_DIR, CLIPS_DIR, RENDERS_DIR, env
from src.video_generator import _descargar, _url_de
from src.voice_generator import _cliente as cliente_voz, _settings, FORMATO

MODELO_VIDEO = "fal-ai/kling-video/o1/standard/image-to-video"  # 3-10s + frame final
MODELO_IMG = "fal-ai/nano-banana-2"
MODELO_EDIT = "fal-ai/nano-banana-2/edit"

RUTA = "scripts/guiones/effix_animado2d_tienda-ropa-la-acera_20260901_aprobado.json"
G = json.loads(Path(RUTA).read_text(encoding="utf-8"))
JOB = G["job_id"]
CARPETA = CLIPS_DIR / JOB
VOZ_DIR = AUDIO_DIR / JOB
NEG = G["negative_prompt"]

SIN_TEXTO = " no text, no captions, no words, no letters, no watermark, no logo, no UI."


# ─────────────────────────────── voz ────────────────────────────────

def _duracion(ruta: Path) -> float:
    salida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(ruta)],
        capture_output=True, text=True, check=True,
    )
    return round(float(salida.stdout.strip()), 2)


def fase_voz() -> dict[int, float]:
    """Un mp3 por línea, cada personaje con su propia voz.

    El contexto (`previous_text`/`next_text`) se pasa sólo dentro del mismo
    hablante: darle a Rosa la frase de Marce como contexto la hace imitar su
    entonación, y el diálogo deja de sonar a dos personas.
    """
    VOZ_DIR.mkdir(parents=True, exist_ok=True)
    ids = {p: voz_para(datos["voz"])[0] for p, datos in G["personajes"].items()}
    perfil_a_pers = {d["voz"]: p for p, d in G["personajes"].items()}
    cliente = cliente_voz()
    modelo = env("ELEVENLABS_MODEL", "eleven_multilingual_v2")
    settings = _settings()

    lineas = G["lineas"]
    duraciones: dict[int, float] = {}
    caracteres = 0

    for i, linea in enumerate(lineas):
        n = linea["n"]
        ruta = VOZ_DIR / f"linea_{n:02d}.mp3"
        if ruta.exists():
            duraciones[n] = _duracion(ruta)
            print(f"  linea {n:02d} ya existe ({duraciones[n]}s)")
            continue

        mismo = [l for l in lineas if l["perfil_voz"] == linea["perfil_voz"]]
        pos = mismo.index(linea)
        previo = mismo[pos - 1]["texto_tts"] if pos > 0 else None
        siguiente = mismo[pos + 1]["texto_tts"] if pos + 1 < len(mismo) else None

        audio = cliente.text_to_speech.convert(
            ids[perfil_a_pers[linea["perfil_voz"]]],
            text=linea["texto_tts"],
            model_id=modelo,
            output_format=FORMATO,
            voice_settings=settings,
            previous_text=previo,
            next_text=siguiente,
        )
        ruta.write_bytes(b"".join(audio))
        caracteres += len(linea["texto_tts"])
        duraciones[n] = _duracion(ruta)
        print(f"  linea {n:02d} {linea['quien']:<10} {duraciones[n]:>5.2f}s  {linea['texto_tts'][:48]}")

    (VOZ_DIR / "duraciones.json").write_text(
        json.dumps(duraciones, indent=2), encoding="utf-8")
    total = round(sum(duraciones.values()), 2)
    print(f"\nlocución: {total}s en {len(duraciones)} líneas · {caracteres} caracteres nuevos")
    return duraciones


def _duraciones() -> dict[int, float]:
    ficha = VOZ_DIR / "duraciones.json"
    if not ficha.exists():
        raise FileNotFoundError("Primero la fase `voz`: el audio decide la duración de los clips.")
    return {int(k): v for k, v in json.loads(ficha.read_text(encoding="utf-8")).items()}


# ────────────────────────── hojas de personaje ──────────────────────

def fase_hojas() -> None:
    """Una hoja por personaje. Todas las escenas se editan desde ellas.

    El 2D plano engorda el trazo si cada imagen se genera de cero: la hoja es
    la que mantiene el mismo grosor de línea y la misma cara en los doce clips.
    """
    CARPETA.mkdir(parents=True, exist_ok=True)
    for nombre in ("rosa", "marce"):
        destino = CARPETA / f"hoja_{nombre}.png"
        if destino.exists():
            print(f"  hoja {nombre} ya existe")
            continue
        prompt = (
            f"{G['bible']} Character sheet: one single full-body character on a plain "
            f"neutral background, front view, neutral relaxed pose, even flat lighting. "
            f"{G['personajes'][nombre]['ficha']}{SIN_TEXTO}"
        )
        salida = fal_client.subscribe(
            MODELO_IMG,
            {"prompt": prompt, "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1},
        )
        _descargar(_url_de(salida, "images", "image"), destino)
        print(f"  hoja {nombre}: {destino.name}")


def _url_hoja(nombre: str) -> str:
    ficha = CARPETA / f"hoja_{nombre}_url.txt"
    if ficha.exists():
        return ficha.read_text(encoding="utf-8").strip()
    with open(CARPETA / f"hoja_{nombre}.png", "rb") as fh:
        url = fal_client.upload(fh.read(), "image/png")
    ficha.write_text(url, encoding="utf-8")
    return url


# ──────────────────────────── escenas ───────────────────────────────

def _refs(linea: dict) -> list[str]:
    if linea["personaje"]:
        return [_url_hoja(linea["personaje"])]
    return [_url_hoja("rosa"), _url_hoja("marce")]  # el plano abierto lleva a las dos


def _escena(linea: dict, sufijo: str = "base", prompt_key: str = "prompt_imagen") -> Path:
    n = linea["n"]
    destino = CARPETA / f"clip_{n:02d}_{sufijo}.png"
    if destino.exists():
        return destino
    # El plano del recinto no lleva a Rosa ni a Marce: pasarle las hojas de
    # personaje como referencia mete a las dos vecinas dentro de la feria.
    if linea.get("sin_refs"):
        # …y la bible describe la acera como escenario, así que entera mete los
        # locales dentro del recinto. Sólo viaja la mitad de estilo.
        estilo = G["bible"].split("Setting:")[0].strip() + " Vertical 9:16 composition."
        salida = fal_client.subscribe(
            MODELO_IMG,
            {"prompt": f"{estilo} {linea[prompt_key]}{SIN_TEXTO}",
             "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1},
        )
        return _descargar(_url_de(salida, "images", "image"), destino)

    prompt = (
        "Keep the exact same character(s) from the reference image(s) — identical "
        "face, hair, clothing and line weight. "
        f"{G['bible']} {linea[prompt_key]}{SIN_TEXTO}"
    )
    salida = fal_client.subscribe(
        MODELO_EDIT,
        {"prompt": prompt, "image_urls": _refs(linea), "aspect_ratio": "9:16",
         "resolution": "1K", "num_images": 1},
    )
    return _descargar(_url_de(salida, "images", "image"), destino)


def fase_escenas() -> None:
    trabajos = [(l, "base", "prompt_imagen") for l in G["lineas"]]
    trabajos += [(l, "fin", "prompt_keyframe_final")
                 for l in G["lineas"] if l.get("prompt_keyframe_final")]
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(_escena, l, s, k): (l["n"], s) for l, s, k in trabajos}
        for f in as_completed(fut):
            n, s = fut[f]
            print(f"  escena {n:02d} {s}: {f.result().name}")


# ───────────────────────────── clips ────────────────────────────────

def _segundos(dur_audio: float) -> str:
    """Kling o1 acepta 3..10 enteros. El clip cubre la línea con medio segundo
    de aire para que el corte no caiga encima de la última sílaba."""
    return str(min(10, max(3, math.ceil(dur_audio + 0.5))))


def _clip(linea: dict, duracion: float) -> Path:
    n = linea["n"]
    destino = CARPETA / f"clip_{n:02d}.mp4"
    if destino.exists():
        return destino

    with open(CARPETA / f"clip_{n:02d}_base.png", "rb") as fh:
        url_inicio = fal_client.upload(fh.read(), "image/png")
    payload = {"start_image_url": url_inicio}

    # Kling o1 sólo acepta duraciones distintas de 5 y 10 cuando hay frame de
    # referencia. En un plano de diálogo el frame final ES el inicial: la cara
    # actúa y vuelve al mismo encuadre. Eso desbloquea los 3s y de paso impide
    # que el plano derive, que es el defecto del 2D plano entre clips.
    fin = CARPETA / f"clip_{n:02d}_fin.png"
    if fin.exists():
        with open(fin, "rb") as fh:
            payload["end_image_url"] = fal_client.upload(fh.read(), "image/png")
    else:
        payload["end_image_url"] = url_inicio

    payload |= {"prompt": linea["prompt_video"], "duration": _segundos(duracion)}
    inicio = time.monotonic()
    salida = fal_client.subscribe(MODELO_VIDEO, payload)
    url = salida["video"]["url"] if isinstance(salida.get("video"), dict) else salida["video"]
    _descargar(url, destino)
    print(f"  clip {n:02d}: {payload['duration']}s para {duracion}s de voz "
          f"({time.monotonic() - inicio:.0f}s de espera)")
    return destino


def fase_clips() -> None:
    duraciones = _duraciones()
    pendientes = [l for l in G["lineas"] if not (CARPETA / f"clip_{l['n']:02d}.mp4").exists()]
    fallos = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(_clip, l, duraciones[l["n"]]): l["n"] for l in pendientes}
        for f in as_completed(fut):
            try:
                f.result()
            except Exception as e:
                fallos.append((fut[f], f"{type(e).__name__}: {e}"))
    for n, e in fallos:
        print(f"  FALLO clip {n:02d}: {e}")


# ──────────────────────────── lip-sync ──────────────────────────────

def fase_lipsync() -> None:
    """Sólo las líneas con `lipsync: true` — el plano abierto del CTA va en off."""
    def uno(linea: dict):
        n = linea["n"]
        destino = CARPETA / f"clip_{n:02d}_sync.mp4"
        if destino.exists():
            return destino
        return sincronizar_clip(
            CARPETA / f"clip_{n:02d}.mp4", VOZ_DIR / f"linea_{n:02d}.mp3",
            destino=destino,
        ).video

    fallos = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(uno, l): l["n"] for l in G["lineas"] if l["lipsync"]}
        for f in as_completed(fut):
            n = fut[f]
            try:
                print(f"  sync {n:02d}: {Path(f.result()).name}")
            except Exception as e:
                fallos.append((n, f"{type(e).__name__}: {e}"))
    for n, e in fallos:
        print(f"  FALLO sync {n:02d}: {e} — ese clip queda con la voz en off")


# ──────────────────────────── montaje ───────────────────────────────

def fase_montaje() -> Path:
    """Cada clip se corta a la duración exacta de su línea y lleva su audio.

    El video se corta al audio y no al revés: la conversación manda el ritmo, y
    un clip que dura medio segundo más que su frase mete un silencio que en un
    diálogo se oye como error.
    """
    duraciones = _duraciones()
    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = RENDERS_DIR / f"{JOB}.mp4"

    entradas, filtros, etiquetas = [], [], []
    for i, linea in enumerate(G["lineas"]):
        n = linea["n"]
        sync = CARPETA / f"clip_{n:02d}_sync.mp4"
        video = sync if sync.exists() else CARPETA / f"clip_{n:02d}.mp4"
        if not video.exists():
            raise FileNotFoundError(f"Falta el clip {n:02d} en {CARPETA}")
        dur = duraciones[n] + 0.25  # el aire mínimo entre réplicas
        entradas += ["-i", str(video), "-i", str(VOZ_DIR / f"linea_{n:02d}.mp3")]
        vi, ai = i * 2, i * 2 + 1
        # El lip-sync devuelve el clip cortado a la voz (`sync_mode=cut_off`),
        # así que pedirle un cuarto de segundo más deja el video más corto que
        # su audio y el diálogo se desfasa. `tpad` clona el último frame: el
        # aire entre réplicas es la cara sosteniendo el gesto, que es lo que
        # hace en una conversación real.
        filtros.append(
            f"[{vi}:v]tpad=stop_mode=clone:stop_duration=2,"
            f"trim=0:{dur:.2f},setpts=PTS-STARTPTS,"
            f"scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,fps=24[v{i}]")
        filtros.append(f"[{ai}:a]apad=whole_dur={dur:.2f},atrim=0:{dur:.2f},"
                       f"asetpts=PTS-STARTPTS[a{i}]")
        etiquetas.append(f"[v{i}][a{i}]")

    filtros.append("".join(etiquetas) + f"concat=n={len(G['lineas'])}:v=1:a=1[vid][aud]")
    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         *entradas, "-filter_complex", ";".join(filtros),
         "-map", "[vid]", "-map", "[aud]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(salida)],
        check=True)
    print(f"RENDER: {salida}  ({salida.stat().st_size / 1024 / 1024:.1f} MB)")
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("fase", choices=["voz", "hojas", "escenas", "clips",
                                     "lipsync", "montaje", "todo"])
    fase = ap.parse_args().fase
    print(f"{G['titulo']} · {G['estilo']} · {G['nicho']} · "
          f"{len(G['lineas'])} líneas · job {JOB}\n")
    if fase in ("voz", "todo"):
        fase_voz()
    if fase in ("hojas", "todo"):
        fase_hojas()
    if fase in ("escenas", "todo"):
        fase_escenas()
    if fase in ("clips", "todo"):
        fase_clips()
    if fase in ("lipsync", "todo"):
        fase_lipsync()
    if fase in ("montaje", "todo"):
        fase_montaje()
