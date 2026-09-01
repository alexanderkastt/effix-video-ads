"""Corrida del ad SKELETON "Un año en la vitrina" — nicho tienda_ropa.

Narración en segunda persona sobre nueve planos: la escalada Día 1 → Día 365
del almacén que solo le vende a quien pasa por el frente, y el giro cuando el
esqueleto se monta al bus para Medellín.

Orden de producción (memoria del proyecto): PRIMERO EL AUDIO. La duración real
de cada mp3, medida con ffprobe, decide cuánto dura su clip — Kling o1 acepta
de 3 a 10s, así que cada línea se paga a su medida y no en tramos de 5s.
Las escenas que cambian de estado (colgar la ropa, poner las rebajas, montarse
al bus, despachar) llevan frame inicial Y final.

Fases, en este orden y por separado, porque cada una cuesta:

    python scripts/_producir_skeleton_vitrina.py voz      # 9 mp3     (~$0,10)
    python scripts/_producir_skeleton_vitrina.py musica   # 1 pista   ($0,20)
    python scripts/_producir_skeleton_vitrina.py hero     # 1 imagen  ($0,08)
    python scripts/_producir_skeleton_vitrina.py escenas  # 13 imgs   ($1,04)
    python scripts/_producir_skeleton_vitrina.py clips    # ~45s vid  (~$3,80)
    python scripts/_producir_skeleton_vitrina.py montaje  # gratis
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
import requests

import src.paths  # carga el .env y mapea FAL_API_KEY → FAL_KEY  # noqa: F401
from src.audio_extra import componer_musica, voz_para
from src.estilos_especiales import ESTILOS_ESPECIALES
from src.paths import env
from src.voice_generator import _cliente as cliente_voz, _settings, FORMATO

GUION = Path("scripts/guiones/effix_skeleton_tienda-ropa-un-ano-en-la-vitrina_20260901_aprobado.json")
G = json.loads(GUION.read_text(encoding="utf-8"))
JOB = G["job"]
CARPETA = Path("assets/clips") / JOB
AUDIO = Path("assets/audio") / JOB
RENDERS = Path("assets/renders")

MODELO_IMG = G["modelo_imagen"]
MODELO_EDIT = f"{MODELO_IMG}/edit"
MODELO_VIDEO = G["modelo_video"]

FUENTE = "referencias/esteticas/fuentes/Montserrat-Black.ttf"

# Cero texto en la generación: los overlays se ponen en montaje, donde se leen.
NEG = ("Absolutely no text anywhere: no captions, no words, no letters, no numbers, "
       "no signage text, no brand names, no watermarks, no UI labels. Any sign, tag or "
       "banner shows only abstract shapes and colour blocks.")


def bible() -> str:
    """El bloque Bare-Bones Cinematic verbatim, con el tema de este nicho."""
    estilo = ESTILOS_ESPECIALES["skeleton"]
    texto = estilo["character_bibles"][estilo["bible_por_defecto"]]
    return texto.replace("[THEME]", G["theme"]).replace("[palette]", G["palette"])


def _descargar(url: str, destino: Path) -> Path:
    destino.write_bytes(requests.get(url, timeout=600).content)
    return destino


def _subir(ruta: Path) -> str:
    with open(ruta, "rb") as fh:
        return fal_client.upload(fh.read(), "image/png")


def _duracion(ruta: Path) -> float:
    salida = subprocess.run(
        [env("FFPROBE_BIN", "ffprobe"), "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(ruta)],
        capture_output=True, text=True, check=True,
    )
    return round(float(salida.stdout.strip()), 2)


# ─────────────────────────────── voz ────────────────────────────────

def fase_voz() -> dict[int, float]:
    """Un mp3 por beat, todos con la misma voz y con contexto entre frases.

    `previous_text`/`next_text` mantienen la entonación de una sola lectura
    corrida: sin eso, cada beat arranca como si fuera la primera frase del ad
    y la escalada Día 1 → Día 365 se oye como nueve anuncios pegados.
    """
    AUDIO.mkdir(parents=True, exist_ok=True)
    voz_id, nombre = voz_para(G["voz"])
    cliente = cliente_voz()
    modelo = env("ELEVENLABS_MODEL", "eleven_multilingual_v2")
    settings = _settings()
    print(f"voz: {nombre}\n")

    beats = G["beats"]
    duraciones: dict[int, float] = {}
    caracteres = 0

    for i, beat in enumerate(beats):
        n = beat["n"]
        ruta = AUDIO / f"beat_{n:02d}.mp3"
        if ruta.exists():
            duraciones[n] = _duracion(ruta)
            print(f"  beat {n:02d} ya existe ({duraciones[n]}s)")
            continue

        audio = cliente.text_to_speech.convert(
            voz_id,
            text=beat["texto_tts"],
            model_id=modelo,
            output_format=FORMATO,
            voice_settings=settings,
            previous_text=beats[i - 1]["texto_tts"] if i > 0 else None,
            next_text=beats[i + 1]["texto_tts"] if i + 1 < len(beats) else None,
        )
        ruta.write_bytes(b"".join(audio))
        caracteres += len(beat["texto_tts"])
        duraciones[n] = _duracion(ruta)
        print(f"  beat {n:02d} {duraciones[n]:>5.2f}s  {beat['texto_tts'][:52]}")

    (AUDIO / "duraciones.json").write_text(json.dumps(duraciones, indent=2), encoding="utf-8")
    total = round(sum(duraciones.values()), 2)
    print(f"\nlocución: {total}s en {len(duraciones)} beats · {caracteres} caracteres nuevos")
    return duraciones


def _duraciones() -> dict[int, float]:
    ficha = AUDIO / "duraciones.json"
    if not ficha.exists():
        sys.exit("Primero la fase `voz`: el audio decide la duración de los clips.")
    return {int(k): v for k, v in json.loads(ficha.read_text(encoding="utf-8")).items()}


def fase_musica() -> None:
    """Cama instrumental, al 13% debajo de la locución. Opcional pero barata."""
    destino = AUDIO / "musica.mp3"
    if destino.exists():
        print(f"ya existe: {destino}")
        return
    total = round(sum(_duraciones().values()) + 3, 1)
    ruta = componer_musica(G["musica"], total, job_id=JOB, destino=destino)
    print(f"música: {ruta} ({total}s pedidos)")


# ────────────────────────────── imágenes ────────────────────────────

def fase_hero() -> None:
    """La hoja del esqueleto. Gobierna la consistencia de los nueve planos."""
    CARPETA.mkdir(parents=True, exist_ok=True)
    destino = CARPETA / "hero.png"
    if destino.exists():
        print(f"ya existe: {destino}")
        return
    prompt = (
        f"{bible()} Clean full-body hero shot of the skeleton standing in a relaxed "
        f"neutral pose inside a small Colombian neighbourhood clothing store, racks of "
        f"clothes softly out of focus behind him, even soft warm light. {NEG}"
    )
    salida = fal_client.subscribe(MODELO_IMG, {
        "prompt": prompt, "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1,
    })
    _descargar(salida["images"][0]["url"], destino)
    print(f"HÉROE: {destino}")


def _url_hero() -> str:
    ficha = CARPETA / "hero_url.txt"
    if ficha.exists():
        return ficha.read_text(encoding="utf-8").strip()
    url = _subir(CARPETA / "hero.png")
    ficha.write_text(url, encoding="utf-8")
    return url


def _escena(beat: dict, sufijo: str, clave: str, url_hero: str) -> Path:
    destino = CARPETA / f"clip_{beat['n']:02d}_{sufijo}.png"
    if destino.exists():
        return destino
    prompt = (
        "Keep the exact same skeleton character from the reference image — identical "
        "skull shape, eye style, bone colour and proportions, and the same cinematic "
        f"render style. {bible()} {beat[clave]} {NEG}"
    )
    salida = fal_client.subscribe(MODELO_EDIT, {
        "prompt": prompt, "image_urls": [url_hero],
        "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1,
    })
    return _descargar(salida["images"][0]["url"], destino)


def fase_escenas() -> None:
    """Todas referencian la héroe, nunca la anterior: el error no se acumula."""
    if not (CARPETA / "hero.png").exists():
        sys.exit("Falta la héroe. Corre la fase `hero` primero.")
    url = _url_hero()
    trabajos = [(b, "base", "prompt_imagen") for b in G["beats"]]
    trabajos += [(b, "fin", "prompt_keyframe_final")
                 for b in G["beats"] if b["prompt_keyframe_final"]]
    pendientes = [t for t in trabajos
                  if not (CARPETA / f"clip_{t[0]['n']:02d}_{t[1]}.png").exists()]
    if not pendientes:
        print(f"las {len(trabajos)} imágenes ya están")
        return
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(_escena, b, s, k, url): (b["n"], s) for b, s, k in pendientes}
        for f in as_completed(fut):
            n, s = fut[f]
            print(f"  escena {n:02d} {s}: {f.result().name}")


# ─────────────────────────────── clips ──────────────────────────────

def _segundos(dur_audio: float, con_keyframe: bool) -> str:
    """Con frame final Kling o1 acepta 3..10 enteros y el clip se paga a su
    medida; sin él solo admite 5 o 10, así que la frase que no cabe en cinco
    segundos necesita keyframe final — no un clip de diez pagado a medias."""
    justo = math.ceil(dur_audio + 0.5)
    if con_keyframe:
        return str(min(10, max(3, justo)))
    return "5" if justo <= 5 else "10"


def _clip(beat: dict, duracion: float) -> tuple[int, str]:
    n = beat["n"]
    destino = CARPETA / f"clip_{n:02d}.mp4"
    if destino.exists():
        return n, "ya existía"

    fin = CARPETA / f"clip_{n:02d}_fin.png"
    payload = {
        "start_image_url": _subir(CARPETA / f"clip_{n:02d}_base.png"),
        "prompt": beat["prompt_video"],
        "duration": _segundos(duracion, fin.exists()),
    }
    if fin.exists():
        payload["end_image_url"] = _subir(fin)
        payload["prompt"] = f"Animate the transition from @Image1 to @Image2. {beat['prompt_video']}"

    inicio = time.monotonic()
    salida = fal_client.subscribe(MODELO_VIDEO, payload)
    url = salida["video"]["url"] if isinstance(salida["video"], dict) else salida["video"]
    _descargar(url, destino)
    return n, (f"{payload['duration']}s para {duracion}s de voz"
               f"{' · con keyframe final' if fin.exists() else ''}"
               f" ({time.monotonic() - inicio:.0f}s de espera)")


def fase_clips() -> None:
    duraciones = _duraciones()
    pendientes = [b for b in G["beats"] if not (CARPETA / f"clip_{b['n']:02d}.mp4").exists()]
    if not pendientes:
        print("los nueve clips ya están")
        return
    fallos = []
    with ThreadPoolExecutor(max_workers=3) as pool:
        fut = {pool.submit(_clip, b, duraciones[b["n"]]): b["n"] for b in pendientes}
        for f in as_completed(fut):
            n = fut[f]
            try:
                _, detalle = f.result()
                print(f"  clip {n:02d}: {detalle}")
            except Exception as e:
                fallos.append((n, f"{type(e).__name__}: {e}"))
    for n, e in fallos:
        print(f"  FALLO clip {n:02d}: {e}")


# ────────────────────────────── montaje ─────────────────────────────

def _ff(*args) -> None:
    subprocess.run([env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner",
                    "-loglevel", "error", *args], check=True)


def fase_montaje() -> Path:
    """Cada clip se corta a la duración exacta de su beat y lleva su mp3.

    El video se corta al audio y no al revés: la narración manda el ritmo, y
    un clip que dura de más mete un silencio que se oye como error.
    """
    duraciones = _duraciones()
    RENDERS.mkdir(parents=True, exist_ok=True)
    tmp = CARPETA / "montaje"
    tmp.mkdir(exist_ok=True)
    salida = RENDERS / "EFFIX-tienda-ropa-skeleton-Un-ano-en-la-vitrina.mp4"

    entradas, filtros, etiquetas = [], [], []
    for i, beat in enumerate(G["beats"]):
        n = beat["n"]
        video = CARPETA / f"clip_{n:02d}.mp4"
        if not video.exists():
            sys.exit(f"Falta {video}. Corre la fase `clips`.")
        dur = duraciones[n] + 0.35  # el aire entre frases
        # Si la frase quedó más larga que el clip pagado, se estira el plano en
        # vez de regenerarlo: por debajo del 10% no se nota y no cuesta nada.
        real = _duracion(video)
        estirar = ""
        if dur > real:
            factor = dur / real
            if factor > 1.12:
                sys.exit(f"El clip {n:02d} dura {real}s y la frase pide {dur:.2f}s. "
                         f"Estirarlo un {factor:.0%} se vería: regenéralo con más segundos.")
            estirar = f"setpts=PTS*{factor:.4f},"
        texto = beat["overlay"].replace("'", "").replace(":", r"\:")
        drawtext = (f"drawtext=fontfile='{FUENTE}':text='{texto}':"
                    f"fontcolor=white:fontsize=58:borderw=6:bordercolor=black@0.85:"
                    f"x=(w-text_w)/2:y=h-330:enable='between(t,0.3,{dur - 0.25:.2f})'")
        entradas += ["-i", str(video), "-i", str(AUDIO / f"beat_{n:02d}.mp3")]
        vi, ai = i * 2, i * 2 + 1
        filtros.append(
            f"[{vi}:v]{estirar}trim=0:{dur:.2f},setpts=PTS-STARTPTS,"
            f"scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,{drawtext},fps=24[v{i}]")
        filtros.append(f"[{ai}:a]apad=whole_dur={dur:.2f},atrim=0:{dur:.2f},"
                       f"asetpts=PTS-STARTPTS[a{i}]")
        etiquetas.append(f"[v{i}][a{i}]")

    filtros.append("".join(etiquetas) + f"concat=n={len(G['beats'])}:v=1:a=1[vid][voz]")
    mudo = tmp / "sin_musica.mp4"
    _ff(*entradas, "-filter_complex", ";".join(filtros), "-map", "[vid]", "-map", "[voz]",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(mudo))

    musica = AUDIO / "musica.mp3"
    if musica.exists():
        total = round(sum(duraciones.values()) + 0.35 * len(G["beats"]), 2)
        _ff("-i", str(mudo), "-i", str(musica), "-filter_complex",
            f"[1:a]volume=0.13,afade=t=out:st={max(total - 4, 0):.2f}:d=4[m];"
            f"[0:a][m]amix=inputs=2:duration=first[a]",
            "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest", str(salida))
    else:
        print("  (sin música: corre la fase `musica` si la quieres)")
        _ff("-i", str(mudo), "-c", "copy", str(salida))

    print(f"\nLISTO: {salida}  ({salida.stat().st_size / 1024 / 1024:.1f} MB)")
    return salida


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("fase", choices=["voz", "musica", "hero", "escenas", "clips", "montaje"])
    fase = ap.parse_args().fase
    print(f"{G['titulo']} · {G['estilo']} · {G['nicho']} · "
          f"{len(G['beats'])} beats · job {JOB}\n")
    {"voz": fase_voz, "musica": fase_musica, "hero": fase_hero,
     "escenas": fase_escenas, "clips": fase_clips, "montaje": fase_montaje}[fase]()
