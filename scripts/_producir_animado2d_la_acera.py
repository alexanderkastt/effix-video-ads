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

from src import mezcla, ritmo
from src.audio_extra import voz_para
from src.lipsync import sincronizar_clip
from src.music_engine import pista_de_libreria
from src.paths import AUDIO_DIR, CLIPS_DIR, RENDERS_DIR, env
from src.video_generator import _descargar, _url_de
from src.voice_generator import (
    _cliente as cliente_voz, _settings, FORMATO, respiro_s,
)

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

def _overlays(duraciones: dict[int, float]) -> list[str]:
    """Los `texto_pantalla` del guión, ubicados sobre la línea de tiempo real.

    `postproduccion.resolver()` espera beats y un plan de reparto, que este ad
    no tiene: aquí cada overlay vive el tramo de su línea. El cuerpo se calcula
    sobre 720px —el ancho con el que está calibrada la marca— y se escala a los
    1080 del render, para que el texto se vea del mismo tamaño relativo que en
    los otros ads y no más chico.
    """
    from src.postproduccion import Overlay, cuerpo_para, filtros as dibujar

    ESCALA = 1080 / 720
    MARGEN = 0.12  # el overlay entra un pelo después de la voz y sale antes

    overlays: list[Overlay] = []
    t = 0.0
    for linea in G["lineas"]:
        dur = duraciones[linea["n"]] + respiro_s()
        textos = linea.get("texto_pantalla")
        if textos:
            textos = textos if isinstance(textos, list) else [textos]
            tramo = (dur - 2 * MARGEN) / len(textos)
            for i, texto in enumerate(textos):
                cuerpo, cabe = cuerpo_para(texto, 720)
                if not cabe:
                    print(f"  ⚠ overlay largo, se lee chico: {texto!r}")
                inicio = t + MARGEN + i * tramo
                overlays.append(Overlay(
                    texto=texto.upper(), inicio=round(inicio, 2),
                    fin=round(inicio + tramo, 2),
                    cuerpo=int(cuerpo * ESCALA), cabe=cabe))
        t += dur

    for o in overlays:
        print(f"  overlay {o.inicio:>5.2f}–{o.fin:<5.2f} {o.cuerpo}px  {o.texto}")
    return dibujar(overlays, CARPETA, alto=1920)


def fase_montaje(destino: Path | None = None) -> Path:
    """Cada línea se corta a su duración exacta y se parte en planos cortos.

    El video se corta al audio y no al revés: la conversación manda el ritmo, y
    un clip que dura medio segundo más que su frase mete un silencio que en un
    diálogo se oye como error.

    Y dentro de esa duración el clip ya no es un plano solo: `ritmo.py` lo parte
    en tomas de 1.5–2.5s reencuadradas. La réplica de cinco segundos deja de ser
    cinco segundos de la misma cámara, sin generar un clip más.
    """
    duraciones = _duraciones()
    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = destino or (RENDERS_DIR / f"{JOB}.mp4")

    respiro = respiro_s()
    largos = [duraciones[l["n"]] + respiro for l in G["lineas"]]
    grupos = ritmo.repartir(largos)
    print(f"  ritmo: {ritmo.resumen(grupos)}")

    entradas, filtros, etiquetas = [], [], []
    for i, (linea, planos) in enumerate(zip(G["lineas"], grupos)):
        n = linea["n"]
        sync = CARPETA / f"clip_{n:02d}_sync.mp4"
        video = sync if sync.exists() else CARPETA / f"clip_{n:02d}.mp4"
        if not video.exists():
            raise FileNotFoundError(f"Falta el clip {n:02d} en {CARPETA}")
        entradas += ["-i", str(video), "-i", str(VOZ_DIR / f"linea_{n:02d}.mp3")]
        vi, ai = i * 2, i * 2 + 1
        for j, plano in enumerate(planos):
            # El lip-sync devuelve el clip cortado a la voz
            # (`sync_mode=cut_off`), así que el último plano de la línea pide
            # más de lo que dura el clip: `tpad` —dentro de filtro_video—
            # clona el último frame. El aire entre réplicas es la cara
            # sosteniendo el gesto, que es lo que hace en una conversación.
            filtros.append(ritmo.filtro_video(plano, f"{vi}:v", f"v{i}_{j}"))
            filtros.append(ritmo.filtro_audio(plano, f"{ai}:a", f"a{i}_{j}"))
            etiquetas.append(f"[v{i}_{j}][a{i}_{j}]")

    n_planos = len(etiquetas)
    cadena = "".join(etiquetas) + f"concat=n={n_planos}:v=1:a=1"
    dibujos = _overlays(duraciones)
    if dibujos:
        filtros.append(cadena + "[crudo][voz]")
        filtros.append("[crudo]" + ",".join(dibujos) + "[vid]")
    else:
        filtros.append(cadena + "[vid][voz]")

    # La música ya no es opcional: sale de la librería según el estilo del ad.
    total = round(sum(largos), 2)
    pista = pista_de_libreria(G.get("estilo") or "", G.get("tono") or "")
    if pista:
        print(f"  música: {pista.name} ({total:.1f}s de video)")
        # Cada línea aportó dos entradas (video y voz); la música va después.
        i_musica = len(G["lineas"]) * 2
        entradas += ["-stream_loop", "-1", "-i", str(pista)]
        filtros.append(mezcla.cadena_audio(
            "voz", f"{i_musica}:a", "aud", duracion_s=total))
        mapa_audio = "[aud]"
    else:
        print("  aviso: sin pista en la librería. "
              "Corre `python scripts/generar_soundtracks.py`.")
        mapa_audio = "[voz]"

    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         *entradas, "-filter_complex", ";".join(filtros),
         "-map", "[vid]", "-map", mapa_audio,
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
    # Para probar un montaje sin pisar el render ya entregado.
    ap.add_argument("--salida", type=Path, default=None)
    args = ap.parse_args()
    fase = args.fase
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
        fase_montaje(args.salida)
