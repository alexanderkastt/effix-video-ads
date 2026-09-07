"""Productor genérico: convierte un guion aprobado en un ad terminado.

Reemplaza a los `_producir_*.py` desechables. Lee el formato único de
`docs/FORMATO-GUION.md` y produce por fases, porque producir todo de una es la
forma más cara de descubrir que la canción canta mal la marca.

    python scripts/producir.py <guion_aprobado.json> <fase>

Fases, en orden y con lo que cuesta cada una:

    validar   gratis · las 6 reglas del formato
    costo     gratis · estimación con los parámetros reales
    cancion   0.15   · MiniMax canta la letra; whisper la transcribe
    hero      0.08   · una hoja con todos los personajes juntos
    escenas   0.08 c/u · cada plano, editado desde la hoja
    clips     lo caro · image-to-video, en paralelo
    montaje   gratis · cortes en los golpes, planos, overlays, master
    qa        gratis · duración, LUFS, planos
    todo      sólo si Alexander lo pide explícitamente

El orden importa y el productor lo hace cumplir: sin canción no hay tiempos, y
sin tiempos el montaje no sabe dónde cortar.
"""

from __future__ import annotations

import argparse
import io
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from pathlib import Path
from typing import Any

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import fal_client

from src import cost_estimator, guion_aprobado, mezcla, ritmo, transcripcion
from src.descargas import recuperar_pendientes
from src.audio_extra import (MODELO_CANCION_11, MODELO_CANCION_MM3,
                             componer_cancion, componer_cancion_elevenlabs,
                             componer_cancion_minimax3)
from src.paths import AUDIO_DIR, CLIPS_DIR, LOGS_DIR, RENDERS_DIR, env, env_int
from src.video_generator import _descargar, _url_de

# Modelos por defecto. El guion puede pisarlos con un bloque "modelos".
MODELO_VIDEO = "fal-ai/kling-video/v2.1/standard/image-to-video"
MODELO_IMG = "fal-ai/nano-banana-2"
MODELO_EDIT = "fal-ai/nano-banana-2/edit"

# Qué endpoints venden frame final, y con qué nombre lo piden. Kling 2.1
# standard no está: sólo acepta `image_url`, y sólo vende tramos de 5 o 10s.
# Verificado con el schema de fal el 2026-09-06.
_ACEPTA_KEYFRAME_FINAL = {
    "fal-ai/kling-video/o1/standard/image-to-video": "end_image_url",
    "fal-ai/kling-video/o1/pro/image-to-video": "end_image_url",
    "fal-ai/bytedance/seedance/v1.5/pro/image-to-video": "end_image_url",
}

# Seedance 1.5 Pro: el modelo de video del proyecto desde el 2026-09-07. Acepta
# frame final (continuidad entre planos), duraciones de 4 a 12s (nada de
# redondear al tramo de 5 o 10 de Kling) y 1080p nativo en 9:16. Cobra por
# tokens de video y no por segundo, así que su costo se calcula aparte.
SEEDANCE = "fal-ai/bytedance/seedance/v1.5/pro/image-to-video"
RESOLUCIONES_TOKENS = {"480p": (480, 854), "720p": (720, 1280), "1080p": (1080, 1920)}


def _cuesta_seedance(ad: "Ad", segundos: int) -> float:
    """tokens = (alto x ancho x fps x duracion) / 1024, y se paga por millon."""
    w, h = RESOLUCIONES_TOKENS.get(ad.resolucion, RESOLUCIONES_TOKENS["1080p"])
    tokens = (h * w * RENDER_FPS * segundos) / 1024
    return tokens / 1_000_000 * _tarifa(f"{SEEDANCE}__por_millon_tokens")

# El texto se dibuja en post, nunca se le pide al modelo: si se le pide, inventa
# letras que parecen palabras y no lo son.
SIN_TEXTO = (" no text, no captions, no words, no letters, no watermark, "
             "no logo, no UI.")

# Nano-banana entiende "character sheet" como hoja de contactos y devuelve la
# misma escena apilada en dos filas. Pasó con la héroe de este ad, y como cada
# escena se edita DESDE la héroe, el díptico se propagó a los doce planos: doce
# imágenes inservibles como cuadro de arranque de un clip 9:16. El modelo no
# acepta negative_prompt, así que la guarda va en el prompt y repetida en el
# system_prompt, que es lo que de verdad sostiene la instrucción.
UN_SOLO_CUADRO = (
    " Single full-frame image, one continuous scene filling the whole frame. "
    "No grid, no collage, no contact sheet, no split screen, no stacked panels, "
    "no repeated rows, no duplicated copies of the scene, no borders."
)
SISTEMA_UN_CUADRO = (
    "Always return exactly one single continuous image that fills the entire "
    "frame. Never produce grids, collages, contact sheets, side-by-side or "
    "stacked panels, or repeated variations of the same scene."
)

# Resolución de entrega. 1080x1920 es lo que piden Reels y TikTok.
RENDER_W = env_int("RENDER_W", 1080)
RENDER_H = env_int("RENDER_H", 1920)
RENDER_FPS = env_int("RENDER_FPS", 24)

# El ancho con el que está calibrado el cuerpo de los overlays en
# postproduccion.cuerpo_para(). Se escala al ancho real del render.
ANCHO_CALIBRACION = 720

# El overlay entra un pelo después del corte y sale antes, para que no se pise
# con el cambio de plano.
MARGEN_OVERLAY_S = 0.12

# Cuánto se deja sonar la canción después de la última palabra. Sin esto el ad
# corta en seco al terminar el verso y se oye como un error de montaje.
COLA_INSTRUMENTAL_S = 2.5
FADE_FINAL_S = 2.0


# ──────────────────────────── contexto ──────────────────────────────

class Ad:
    """Todo lo que las fases necesitan saber del guion, resuelto una vez."""

    def __init__(self, ruta: str | Path) -> None:
        self.ruta = Path(ruta)
        self.g = guion_aprobado.cargar(self.ruta)
        self.job = self.g["job_id"]
        self.clips_dir = CLIPS_DIR / self.job
        self.audio_dir = AUDIO_DIR / self.job
        modelos = self.g.get("modelos") or {}
        self.modelo_video = modelos.get("video", MODELO_VIDEO)
        self.modelo_img = modelos.get("imagen", MODELO_IMG)
        self.modelo_edit = modelos.get("edit", MODELO_EDIT)
        self.dur_clip = guion_aprobado.duracion_clip_s(self.g)
        self.resolucion = (self.g.get("modelos") or {}).get("resolucion", "1080p")

    @property
    def lineas(self) -> list[dict[str, Any]]:
        return self.g["lineas"]

    @property
    def musical(self) -> bool:
        return self.g.get("modo") == "musical_sync"

    def ruta_cancion(self, util: bool = False) -> Path:
        nombre = "cancion_util.mp3" if util else "cancion.mp3"
        return self.audio_dir / nombre

    def apuntar_gasto(self, concepto: str, unidades: float, usd: float) -> None:
        """Deja constancia de lo que se gastó, cuándo y en qué.

        Un log por ad, una línea por llamada pagada: es lo único que permite
        comparar el costo estimado con el real sin reconstruirlo de memoria.
        """
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        registro = {
            "fecha": date.today().isoformat(),
            "job": self.job,
            "concepto": concepto,
            "unidades": unidades,
            "usd": round(usd, 4),
        }
        with (LOGS_DIR / f"{self.job}_gasto.jsonl").open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(registro, ensure_ascii=False) + "\n")

    def gasto_real(self) -> float:
        ficha = LOGS_DIR / f"{self.job}_gasto.jsonl"
        if not ficha.exists():
            return 0.0
        return round(sum(
            json.loads(l)["usd"] for l in ficha.read_text(encoding="utf-8").splitlines()
            if l.strip()
        ), 4)


def _tarifa(clave: str, grupo: str = "fal_ai_por_unidad") -> float:
    return cost_estimator._cargar().get(grupo, {}).get(clave, 0.0)


def _duracion(ruta: Path) -> float:
    salida = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(ruta)],
        capture_output=True, text=True, check=True,
    )
    return round(float(salida.stdout.strip()), 3)


# ──────────────────────── validar y estimar ─────────────────────────

def fase_validar(ad: Ad) -> guion_aprobado.Resultado:
    r = guion_aprobado.validar(ad.g)
    print(r.texto())
    return r


def fase_costo(ad: Ad) -> dict[str, Any]:
    # Whisper cobra por segundo de cómputo; sobre una canción de ~90s son
    # centavos, pero el presupuesto se mide entero o no se mide.
    extras = round(120 * _tarifa("fal-ai/whisper__por_segundo_de_computo"), 4)
    est = guion_aprobado.estimar_costo(
        ad.g, modelo_video=ad.modelo_video, modelo_imagen=ad.modelo_img,
        costo_extras=extras,
    )
    print(cost_estimator.formatear(est))
    print(f"   detalle: {len(ad.lineas)} clips × {ad.dur_clip}s "
          f"({est['segundos_video']}s de video) · {est['n_imagenes']} imágenes "
          f"(1 héroe + {len(ad.lineas)} escenas"
          + (f" + {est['n_imagenes'] - len(ad.lineas) - 1} keyframes"
             if est['n_imagenes'] > len(ad.lineas) + 1 else "") + ")")
    if ad.musical:
        print(f"   canción: {(ad.g.get('musica') or {}).get('modelo')} · "
              f"regenerarla cuesta {est['costo_musica']} más por intento")
    return est


# ───────────────────────────── canción ──────────────────────────────

def fase_cancion(ad: Ad, *, forzar: bool = False) -> Path:
    """Compone la canción, la transcribe y la recorta al tramo cantado.

    Las tres cosas van juntas porque separadas no sirven: un mp3 sin
    transcripción no dice dónde cortar, y la canción cruda arranca con segundos
    de intro instrumental que en un feed son scroll perdido.
    """
    if not ad.musical:
        raise SystemExit("La fase `cancion` es sólo del modo musical_sync.")

    cruda = ad.ruta_cancion()
    if cruda.exists() and not forzar:
        print(f"canción ya existe: {cruda.name} ({_duracion(cruda)}s). "
              f"Usa --forzar para regenerarla (cuesta otra vez).")
    else:
        if forzar and cruda.exists():
            # No se pisa el intento anterior: si el nuevo canta peor, se vuelve.
            previos = len(list(ad.audio_dir.glob("cancion_intento_*.mp3")))
            cruda.rename(ad.audio_dir / f"cancion_intento_{previos + 1:02d}.mp3")
        inicio = time.monotonic()
        musica = ad.g["musica"]
        if musica.get("modelo") == MODELO_CANCION_MM3:
            # `duration` es un tope, no una orden: se pide con margen para
            # que la cancion termine su ultima frase y su cierre en vez de
            # cortarse en seco en el segundo pedido. El video se estira
            # despues para cubrir lo que dure.
            seg = int((musica.get("duracion_ms") or 58000) / 1000)
            cruda = componer_cancion_minimax3(
                musica, job_id=ad.job, destino=cruda, duracion_s=seg)
            ad.apuntar_gasto("cancion (music3)", seg,
                             seg * _tarifa(f"{MODELO_CANCION_MM3}__por_segundo"))
        elif musica.get("modelo") == MODELO_CANCION_11:
            # ElevenLabs Music cobra por minuto y acepta duración objetivo, así
            # que es el único camino que permite encargar un ad dentro del rango
            # de 30-60s en vez de aceptar lo que salga. Cuesta seis veces más
            # que MiniMax: se usa cuando la dicción no es negociable.
            ms = int(musica.get("duracion_ms") or 58000)
            cruda = componer_cancion_elevenlabs(
                musica, job_id=ad.job, destino=cruda, duracion_ms=ms)
            ad.apuntar_gasto("cancion (11labs)", ms / 60000,
                             ms / 60000 * _tarifa(f"{MODELO_CANCION_11}__por_minuto"))
        else:
            cruda = componer_cancion(musica, job_id=ad.job, destino=cruda)
            ad.apuntar_gasto("cancion", 1, _tarifa(
                f"{musica['modelo']}__por_cancion"))
        print(f"canción: {cruda.name} · {_duracion(cruda)}s "
              f"({time.monotonic() - inicio:.0f}s de espera)")

    # Sólo se apunta el gasto si de verdad hubo llamada: la transcripción se
    # cachea, y volver a montar no vuelve a pagarla.
    cacheada = (ad.audio_dir / "transcripcion.json").exists() and not forzar
    t = transcripcion.transcribir(cruda, job_id=ad.job, forzar=forzar)
    if not cacheada:
        ad.apuntar_gasto("whisper (estimado)", 1, round(
            120 * _tarifa("fal-ai/whisper__por_segundo_de_computo"), 4))
    inicio_s, fin_s = transcripcion.tramo_cantado(t)
    util = _recortar(ad, cruda, inicio_s, fin_s)

    print(f"\ntramo cantado: {inicio_s:.2f}s → {fin_s:.2f}s "
          f"({fin_s - inicio_s:.2f}s útiles de {_duracion(cruda):.2f}s)")
    print(f"recorte: {util.name}")
    print(f"\nLo que se oye cantar:\n  {t.get('text', '')[:600]}")
    print("\n👂 Escúchala antes de seguir. Revisa que cante 'Feria Effix' "
          "completo y que no se coma ninguna cifra.")
    return util


def _recortar(ad: Ad, cruda: Path, inicio_s: float, fin_voz_s: float) -> Path:
    """Quita la intro instrumental y deja que la canción TERMINE ENTERA.

    Regla de Alexander (2026-09-07): "la canción no la puedes cortar; si toca,
    complementa los videos". Antes se recortaba en la última palabra más unos
    segundos de cola, y el final se oía arrancado. Ahora el único recorte es por
    delante —la intro instrumental larga, que en un feed es scroll perdido— y la
    canción llega hasta su último frame.

    El video se estira para cubrirla: la última línea se queda en pantalla lo
    que dure la cola, repartida en planos reencuadrados de su propio clip. Eso
    no cuesta nada, y es la razón por la que el audio puede mandar.
    """
    destino = ad.ruta_cancion(util=True)
    total = _duracion(cruda)
    # La canción va ENTERA, de su primer frame al último. Alexander: "no me
    # moches las canciones, me queda mal". Antes se recortaba la intro
    # instrumental por delante y eso arrancaba el ad a mitad de compás; el
    # video se estira para cubrirla, que no cuesta nada.
    inicio_s = 0.0
    fin_s = total
    dur = round(fin_s - inicio_s, 3)
    cola = round(fin_s - fin_voz_s, 3)
    # Fade mínimo, sólo para que no haya un clic en el corte del archivo. Si la
    # canción ya trae su propio cierre, esto es casi imperceptible.
    fade = round(min(max(cola, 0.25), FADE_FINAL_S), 2)
    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         "-ss", str(inicio_s), "-to", str(fin_s), "-i", str(cruda),
         "-af", f"afade=t=in:st=0:d=0.25,"
                f"afade=t=out:st={max(dur - fade, 0):.2f}:d={fade}",
         "-c:a", "libmp3lame", "-b:a", "256k", str(destino)],
        check=True)
    (ad.audio_dir / "tramo.json").write_text(
        json.dumps({"inicio_s": inicio_s, "fin_voz_s": fin_voz_s, "fin_s": fin_s,
                    "duracion_s": dur, "cola_s": cola, "fade_out_s": fade},
                   indent=2), encoding="utf-8")
    print(f"  cola instrumental: {cola:.2f}s · fade de salida {fade:.2f}s")
    return destino


# ────────────────────────── héroe y escenas ─────────────────────────

def fase_hero(ad: Ad) -> Path:
    """Una sola hoja con todos los personajes del ad, juntos y de cuerpo entero.

    Todas las escenas se editan desde ella. Es lo que impide que el personaje
    cambie de cara entre el clip 3 y el 9, que es el defecto clásico de generar
    cada plano desde cero.
    """
    ad.clips_dir.mkdir(parents=True, exist_ok=True)
    destino = ad.clips_dir / "hero.png"
    if destino.exists():
        print(f"hero ya existe: {destino}")
        return destino

    personajes = ad.g.get("personajes") or {}
    fichas = " ".join(p["ficha"] for p in personajes.values())
    # Con UN personaje, pedir "all the characters together side by side" invita
    # al modelo a llenar la fila: la primera héroe del esqueleto salió rodeada
    # de seis personas y con un set de feria detrás. La hoja de referencia sólo
    # puede contener lo que va a viajar a las doce escenas.
    if len(personajes) <= 1:
        encuadre = ("A single hero shot of the character completely alone, "
                    "centred, full body, front view, neutral relaxed pose")
    else:
        encuadre = ("All the characters of this ad standing together side by side "
                    "in a single row, full body, front view, neutral relaxed pose")
    prompt = componer_prompt(
        f"{ad.g['bible']} {encuadre}, on a plain neutral seamless studio "
        f"background, even soft lighting. {fichas} Reference sheet only: no other "
        f"characters, no people, no human figures, no crowd, no bystanders, no "
        f"scenery, no set, no props beyond the characters themselves.",
        con_referencia=False,
    )
    salida = fal_client.subscribe(
        ad.modelo_img,
        {"prompt": prompt, "aspect_ratio": ad.g.get("aspect_ratio", "9:16"),
         "resolution": "1K", "num_images": 1,
         "system_prompt": SISTEMA_UN_CUADRO},
    )
    ad.apuntar_gasto("hero", 1, _tarifa(f"{ad.modelo_img}__por_imagen"))
    _descargar(_url_de(salida, "images", "image"), destino)
    print(f"hero: {destino}")
    return destino


def _url_hero(ad: Ad) -> str:
    ficha = ad.clips_dir / "hero_url.txt"
    if ficha.exists():
        return ficha.read_text(encoding="utf-8").strip()
    with open(ad.clips_dir / "hero.png", "rb") as fh:
        url = fal_client.upload(fh.read(), "image/png")
    ficha.write_text(url, encoding="utf-8")
    return url


def componer_prompt(base: str, *, con_referencia: bool) -> str:
    """Añade las guardas del productor SIN estropear el prompt del guion.

    Los guiones del formato único traen el prompt ya escrito y cerrado: el
    Character Bible verbatim de skeleton, el universal de crochet con su propio
    bloque `Negative:` al final, el cierre de "no text" de todos. Pegarle cosas
    a ciegas hace daño de dos formas:

    1. **La guarda anti-panel caía dentro del `Negative:` de crochet.** Todo lo
       que va detrás de esa palabra se lee como lista de lo que NO se quiere, así
       que "Single full-frame image" pasaba a ser algo a evitar — pidiéndole al
       modelo exactamente el díptico que la guarda venía a impedir. Por eso se
       inserta ANTES del bloque negativo, no al final.
    2. **Repetir lo que el prompt ya dice lo diluye.** Si el guion ya cierra con
       "no text" o ya manda referenciar la imagen de referencia, no se repite.

    Lo que nunca se toca es el texto del guion: se inserta alrededor, jamás se
    reescribe.
    """
    partes = []
    if con_referencia and "reference image" not in base.lower():
        partes.append(
            "Keep the exact same character(s) from the reference image — identical "
            "design, colours and proportions. Use the reference only for the "
            "characters; the composition and framing come from this description. "
        )
    cola = "" if "no text" in base.lower() else SIN_TEXTO

    corte = base.find("Negative:")
    if corte == -1:
        partes.append(base + cola + UN_SOLO_CUADRO)
    else:
        # La guarda y el cierre entran en la parte positiva; el bloque negativo
        # del guion se queda intacto y al final, que es donde tiene sentido.
        partes.append(base[:corte].rstrip() + cola + UN_SOLO_CUADRO + " " + base[corte:])
    return "".join(partes)


def _escena(ad: Ad, linea: dict, sufijo: str, clave: str, url: str) -> Path:
    n = linea["n"]
    destino = ad.clips_dir / f"clip_{n:02d}_{sufijo}.png"
    if destino.exists():
        return destino
    prompt = componer_prompt(linea[clave], con_referencia=True)
    salida = fal_client.subscribe(
        ad.modelo_edit,
        {"prompt": prompt, "image_urls": [url],
         "aspect_ratio": ad.g.get("aspect_ratio", "9:16"),
         "resolution": "1K", "num_images": 1,
         "system_prompt": SISTEMA_UN_CUADRO},
    )
    ad.apuntar_gasto(f"escena_{n:02d}_{sufijo}", 1,
                     _tarifa(f"{ad.modelo_edit}__por_imagen"))
    return _descargar(_url_de(salida, "images", "image"), destino)


def fase_escenas(ad: Ad) -> None:
    # Si la corrida anterior murió con la red caída, esto baja lo que
    # ya se pagó antes de plantearse generar nada nuevo.
    for r in recuperar_pendientes(ad.clips_dir):
        print(f"  recuperado sin regenerar: {r.name}")
    if not (ad.clips_dir / "hero.png").exists():
        raise SystemExit("Primero la fase `hero`: las escenas se editan desde ella.")
    url = _url_hero(ad)
    trabajos = [(l, "base", "prompt_imagen") for l in ad.lineas]
    trabajos += [(l, "fin", "prompt_keyframe_final")
                 for l in ad.lineas if l.get("prompt_keyframe_final")]
    fallos = []
    with ThreadPoolExecutor(max_workers=env_int("MAX_CONCURRENT_CLIPS", 3)) as pool:
        fut = {pool.submit(_escena, ad, l, s, k, url): (l["n"], s)
               for l, s, k in trabajos}
        for f in as_completed(fut):
            n, s = fut[f]
            try:
                print(f"  escena {n:02d} {s}: {f.result().name}")
            except Exception as e:
                fallos.append((n, s, f"{type(e).__name__}: {e}"))
    for n, s, e in fallos:
        print(f"  FALLO escena {n:02d} {s}: {e}")


# ───────────────────────────── clips ────────────────────────────────

def _url_escena(ad: Ad, n_linea: int) -> str:
    """Sube (una vez) la escena de una línea y devuelve su URL en fal."""
    ficha = ad.clips_dir / f"clip_{n_linea:02d}_base_url.txt"
    if ficha.exists():
        return ficha.read_text(encoding="utf-8").strip()
    base = ad.clips_dir / f"clip_{n_linea:02d}_base.png"
    if not base.exists():
        raise FileNotFoundError(f"Falta la escena {base.name}")
    with open(base, "rb") as fh:
        url = fal_client.upload(fh.read(), "image/png")
    ficha.write_text(url, encoding="utf-8")
    return url


def _clip(ad: Ad, tarea: dict) -> Path:
    """Genera un clip del plan. `tarea` trae su línea, su duración y su destino.

    Con Seedance el clip ya no es "una línea": es un hueco de la rejilla que
    cubre la canción. Varios clips pueden salir de la misma escena y, cuando el
    siguiente pertenece a otra línea, éste se encadena con `end_image_url` para
    que la transición entre ideas sea continua.
    """
    i = tarea["i"]
    destino = ad.clips_dir / f"clip_{i:02d}.mp4"
    if destino.exists():
        return destino

    linea = next(l for l in ad.lineas if l["n"] == tarea["linea"])
    payload: dict[str, Any] = {"image_url": _url_escena(ad, tarea["linea"])}

    # Seedance acepta enteros de 4 a 12; el último hueco de la rejilla puede ser
    # más corto y el montaje lo recorta.
    segundos = max(4, min(12, int(round(tarea["t1"] - tarea["t0"]))))
    payload |= {"prompt": linea["prompt_video"], "duration": str(segundos)}

    campo_final = _ACEPTA_KEYFRAME_FINAL.get(ad.modelo_video)
    if tarea.get("end_linea") and campo_final:
        payload[campo_final] = _url_escena(ad, tarea["end_linea"])
    elif (ad.clips_dir / f"clip_{tarea['linea']:02d}_fin.png").exists() and campo_final:
        with open(ad.clips_dir / f"clip_{tarea['linea']:02d}_fin.png", "rb") as fh:
            payload[campo_final] = fal_client.upload(fh.read(), "image/png")

    if ad.modelo_video == SEEDANCE:
        payload |= {
            "resolution": ad.resolucion,
            "aspect_ratio": ad.g.get("aspect_ratio", "9:16"),
            # La pista es la canción: el audio que genere el modelo se
            # descartaría, y pedirlo sólo añade cosas que no controlamos.
            "generate_audio": False,
        }
        costo = _cuesta_seedance(ad, segundos)
    else:
        if ad.g.get("negative_prompt"):
            payload["negative_prompt"] = ad.g["negative_prompt"]
        costo = segundos * _tarifa(ad.modelo_video, "fal_ai")

    inicio = time.monotonic()
    salida = fal_client.subscribe(ad.modelo_video, payload)
    url = salida["video"]["url"] if isinstance(salida.get("video"), dict) else salida["video"]
    ad.apuntar_gasto(f"clip_{i:02d}", segundos, costo)
    _descargar(url, destino)
    cadena = f" → línea {tarea['end_linea']}" if tarea.get("end_linea") else ""
    print(f"  clip {i:02d}: {segundos}s de la línea {tarea['linea']:02d}{cadena} "
          f"({time.monotonic() - inicio:.0f}s de espera)")
    return destino


def _plan_de_clips(ad: Ad) -> list[dict[str, Any]]:
    """La rejilla de clips, calculada desde la canción y cacheada en disco.

    Se guarda porque la fase `clips` y la de `montaje` tienen que ver
    exactamente el mismo reparto: si se recalculara en cada una, un reintento
    con la canción regenerada dejaría clips que no encajan con el montaje.
    """
    from src import plan_musical

    ficha = ad.clips_dir / "plan_clips.json"
    if ficha.exists():
        return json.loads(ficha.read_text(encoding="utf-8"))
    _, tramos, dur = _tramos_musicales(ad)
    plan = plan_musical.repartir_clips(ad.lineas, tramos, dur, dur_clip=ad.dur_clip)
    ad.clips_dir.mkdir(parents=True, exist_ok=True)
    ficha.write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  {plan_musical.resumen(plan)}")
    return plan


def fase_clips(ad: Ad) -> None:
    # Si la corrida anterior murió con la red caída, esto baja lo que
    # ya se pagó antes de plantearse generar nada nuevo.
    for r in recuperar_pendientes(ad.clips_dir):
        print(f"  recuperado sin regenerar: {r.name}")

    if ad.musical and ad.modelo_video == SEEDANCE:
        tareas = _plan_de_clips(ad)
    else:
        # Modo antiguo: un clip por línea, sin encadenar.
        tareas = [{"i": l["n"], "linea": l["n"], "t0": 0.0,
                   "t1": float(ad.dur_clip), "end_linea": None} for l in ad.lineas]

    pendientes = [t for t in tareas
                  if not (ad.clips_dir / f"clip_{t['i']:02d}.mp4").exists()]
    if not pendientes:
        print("  todos los clips ya están.")
        return
    fallos = []
    with ThreadPoolExecutor(max_workers=env_int("MAX_CONCURRENT_CLIPS", 3)) as pool:
        fut = {pool.submit(_clip, ad, t): t["i"] for t in pendientes}
        for f in as_completed(fut):
            try:
                f.result()
            except Exception as e:
                fallos.append((fut[f], f"{type(e).__name__}: {e}"))
    for n, e in fallos:
        print(f"  FALLO clip {n:02d}: {e}")
    if fallos:
        print("  vuelve a correr la fase: los que sí salieron no se regeneran.")


# ──────────────────────────── montaje ───────────────────────────────

def _tramos_musicales(ad: Ad) -> tuple[Path, list[tuple[float, float]], float]:
    """Dónde cae cada línea de la letra dentro de la canción, imantado a golpes."""
    util = ad.ruta_cancion(util=True)
    if not util.exists():
        raise SystemExit("Primero la fase `cancion`: sin ella no hay tiempos.")
    tramo = json.loads((ad.audio_dir / "tramo.json").read_text(encoding="utf-8"))
    # La transcripción está cacheada sobre la canción CRUDA: sus tiempos son
    # absolutos y `alinear` los baja al recorte con `inicio_s`.
    t = transcripcion.transcribir(ad.ruta_cancion(), job_id=ad.job)

    tramos = transcripcion.alinear(
        [l["texto"] for l in ad.lineas], t,
        inicio_s=tramo["inicio_s"], fin_s=tramo["fin_s"],
    )
    dur = _duracion(util)

    # Los bordes de las líneas, llevados al golpe más cercano de la canción.
    cortes = [t0 for t0, _ in tramos] + [dur]
    cortes = ritmo.imantar(cortes, transcripcion.golpes(util))
    cortes = _sin_tramos_imposibles(cortes)
    return util, [(cortes[i], cortes[i + 1]) for i in range(len(tramos))], dur


def _sin_tramos_imposibles(cortes: list[float]) -> list[float]:
    """Ningún tramo puede quedar por debajo del piso de un plano.

    Whisper ancla cada línea donde la oye, y en el ad de contadores oyó la
    última tan pegada al final que le tocaron 0.26 segundos: un plano de seis
    frames, que se ve como un parpadeo, no como un corte. El sitio donde eso se
    arregla es el reparto, no el piso.

    Una sola pasada hacia atrás, empujando cada corte lo que haga falta sin
    mirar si eso deja corto al vecino: el déficit se propaga hacia el principio
    y se resuelve al llegar allí, donde siempre hay holgura porque los primeros
    versos duran más. Limitar el robo al vecino inmediato —el primer intento—
    no converge en cuanto hay dos líneas seguidas justas.
    """
    salida = list(cortes)
    for i in range(len(salida) - 1, 0, -1):
        falta = ritmo.PLANO_PISO_S - (salida[i] - salida[i - 1])
        if falta > 0.001:
            salida[i - 1] = round(max(salida[i - 1] - falta, 0.0), 3)
    return salida


def _overlays(ad: Ad, tramos: list[tuple[float, float]]) -> list:
    from src.postproduccion import Overlay, ajustar

    escala = RENDER_W / ANCHO_CALIBRACION
    salida = []
    for linea, (t0, t1) in zip(ad.lineas, tramos):
        textos = linea.get("texto_pantalla") or ""
        textos = textos if isinstance(textos, list) else [textos]
        textos = [t for t in textos if t]
        if not textos:
            continue
        util = max(t1 - t0 - 2 * MARGEN_OVERLAY_S, 0.4)
        paso = util / len(textos)
        for i, texto in enumerate(textos):
            # En dos renglones si hace falta: siete palabras en una sola línea
            # obligan a bajar al piso de 40px, y ahí el overlay ya no se lee.
            envuelto, cuerpo, cabe = ajustar(texto.upper(), ANCHO_CALIBRACION)
            if not cabe:
                print(f"  ⚠ overlay largo, se lee chico: {texto!r}")
            arranca = t0 + MARGEN_OVERLAY_S + i * paso
            salida.append(Overlay(
                texto=envuelto, inicio=round(arranca, 2),
                fin=round(arranca + paso, 2),
                cuerpo=int(cuerpo * escala), cabe=cabe))
    return salida


def _momentos_logo(ad: Ad, tramos: list[tuple[float, float]],
                   dur: float) -> list[tuple[float, float, str]]:
    """Cuándo aparece el logo, deducido del propio guion.

    Tres apariciones, cada una por un motivo distinto:

    1. **Arranque**, en esquina. La auditoría de ganchos exige que la marca
       esté en los primeros cinco segundos; esto lo cumple sin gastar copy.
    2. **Cuando la canción nombra la marca**, grande y centrado. Es el momento
       en que se canta "Feria Effix", y los tiempos ya los tenemos de whisper:
       el logo entra exactamente con la palabra. Puesto ahí es memorable;
       puesto en cualquier otro sitio es decoración.
    3. **Cierre**, grande, junto al CTA.
    """
    momentos: list[tuple[float, float, str]] = [(0.4, 4.4, "esquina")]
    for linea, (t0, t1) in zip(ad.lineas, tramos):
        if "feria effix" in str(linea.get("texto", "")).lower():
            momentos.append((round(t0, 2), round(min(t0 + 3.2, t1), 2), "centro"))
            break
    momentos.append((round(max(dur - 4.0, 0.0), 2), round(dur, 2), "centro"))
    return momentos


def fase_montaje(ad: Ad, destino: Path | None = None) -> Path:
    """Corta en los golpes, parte cada tramo en planos y masteriza a −14 LUFS.

    La canción es la pista principal: no hay locución debajo, así que no hay
    nada que duckear y `mezcla.cadena_master()` sólo pone fades y loudness.
    """
    from src.postproduccion import filtros as dibujar

    if not ad.musical:
        raise SystemExit(
            "Este montaje es el del modo musical_sync. Para `locucion` falta "
            "portar la fase de voz.")

    cancion, tramos, dur = _tramos_musicales(ad)

    # Dos repartos conviven. El nuevo (Seedance) es una rejilla de clips cortos
    # sobre la canción; el viejo (Kling) ataba un clip a cada línea. Se detecta
    # por el plan en disco para que los ads ya producidos se sigan montando.
    ficha_plan = ad.clips_dir / "plan_clips.json"
    if ficha_plan.exists():
        tareas = json.loads(ficha_plan.read_text(encoding="utf-8"))
    else:
        tareas = [{"i": l["n"], "linea": l["n"], "t0": a, "t1": b, "end_linea": None}
                  for l, (a, b) in zip(ad.lineas, tramos)]

    clips = {t["i"]: ad.clips_dir / f"clip_{t['i']:02d}.mp4" for t in tareas}
    faltan = sorted(i for i, p in clips.items() if not p.exists())
    if faltan:
        raise FileNotFoundError(f"Faltan los clips {faltan} en {ad.clips_dir}")

    entradas, filtros, etiquetas = [], [], []
    cursor, detalle = 0, []
    for i, tarea in enumerate(tareas):
        n_linea = tarea["linea"]
        linea = next(l for l in ad.lineas if l["n"] == n_linea)
        t0, t1 = tarea["t0"], tarea["t1"]
        # `ventana_util_s: [desde, hasta]` acota qué parte del clip se puede
        # usar. Existe porque un clip puede salir bien los dos primeros
        # segundos y estropearse después —el modelo le da vida a un objeto que
        # debía quedarse quieto—, y tirar el clip entero cuesta otro clip.
        desde_s, fuente = 0.0, _duracion(clips[tarea["i"]])
        ventana = linea.get("ventana_util_s")
        if ventana:
            desde_s = float(ventana[0])
            fuente = min(float(ventana[1]), fuente) - desde_s
            print(f"  clip {tarea['i']:02d}: ventana útil {desde_s:.2f}–"
                  f"{desde_s + fuente:.2f}s")
        planos = ritmo.planos_en_fuente(t1 - t0, fuente, desde=cursor)
        if desde_s:
            planos = [ritmo.Plano(round(p.inicio_s + desde_s, 3),
                                  round(p.fin_s + desde_s, 3), p.encuadre)
                      for p in planos]
        cursor += len(planos)
        entradas += ["-i", str(clips[tarea["i"]])]
        for j, plano in enumerate(planos):
            filtros.append(ritmo.filtro_video(
                plano, f"{i}:v", f"v{i}_{j}", w=RENDER_W, h=RENDER_H,
                fps=RENDER_FPS, clonar_cola_s=0.0))
            etiquetas.append(f"[v{i}_{j}]")
        detalle.append({"clip": tarea["i"], "linea": n_linea,
                        "inicio_s": round(t0, 3), "fin_s": round(t1, 3),
                        "encadenado": tarea.get("end_linea"),
                        "planos": [p.duracion_s for p in planos]})

    todos = [d for x in detalle for d in x["planos"]]
    print(f"  ritmo: {len(todos)} planos · {min(todos):.2f}–{max(todos):.2f}s "
          f"· promedio {sum(todos) / len(todos):.2f}s")

    cadena = "".join(etiquetas) + f"concat=n={len(etiquetas)}:v=1:a=0"
    dibujos = dibujar(_overlays(ad, tramos), ad.clips_dir, alto=RENDER_H)
    if dibujos:
        filtros.append(cadena + "[crudo]")
        filtros.append("[crudo]" + ",".join(dibujos) + "[vid]")
    else:
        filtros.append(cadena + "[vid]")

    entradas += ["-i", str(cancion)]
    # El fade final necesita saber hasta dónde se canta: sin eso apaga el
    # último verso, que suele ser el CTA.
    fin_voz = json.loads(
        (ad.audio_dir / "tramo.json").read_text(encoding="utf-8")
    ).get("fin_voz_s")
    filtros.append(mezcla.cadena_master(
        f"{len(tareas)}:a", "aud", duracion_s=dur, fin_voz_s=fin_voz))

    # El logo va al final de la cadena de video: por encima de los subtítulos,
    # nunca debajo. Cada aparición necesita su propia copia del PNG porque se
    # escala distinto y un input no se puede consumir dos veces.
    from src.postproduccion import filtros_logo, logo_marca

    momentos = _momentos_logo(ad, tramos, dur)
    if momentos:
        indice = len(tareas) + 1
        etiquetas = []
        for k in range(len(momentos)):
            entradas += ["-loop", "1", "-i", str(logo_marca())]
            etiquetas.append(f"{indice + k}:v")
        filtros.append("[vid]null[vid_txt]")
        filtros += filtros_logo(momentos, "vid_txt", "vid_final",
                                w=RENDER_W, h=RENDER_H, entradas_logo=etiquetas)
        mapa_video = "[vid_final]"
        print("  logo: " + " · ".join(
            f"{a:.1f}-{b:.1f}s {s}" for a, b, s in momentos))
    else:
        mapa_video = "[vid]"

    RENDERS_DIR.mkdir(parents=True, exist_ok=True)
    salida = destino or (RENDERS_DIR / f"{ad.job}.mp4")
    subprocess.run(
        [env("FFMPEG_BIN", "ffmpeg"), "-y", "-hide_banner", "-loglevel", "error",
         *entradas, "-filter_complex", ";".join(filtros),
         "-map", mapa_video, "-map", "[aud]", "-t", f"{dur:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", str(salida)],
        check=True)

    (ad.clips_dir / "plan_montaje.json").write_text(
        json.dumps({"duracion_s": dur, "lineas": detalle, "render": str(salida)},
                   ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"RENDER: {salida}  ({salida.stat().st_size / 1024 / 1024:.1f} MB)")
    return salida


# ─────────────────────────────── QA ─────────────────────────────────

def fase_qa(ad: Ad, render: Path | None = None) -> bool:
    """Lo que hay que mirar antes de decir que está entregado."""
    render = render or (RENDERS_DIR / f"{ad.job}.mp4")
    if not render.exists():
        raise SystemExit(f"No hay render en {render}")

    plan = json.loads((ad.clips_dir / "plan_montaje.json").read_text(encoding="utf-8"))
    planos = [d for l in plan["lineas"] for d in l["planos"]]
    dur = _duracion(render)
    loud = mezcla.medir_loudness(render)

    print(f"\nQA de {render.name}")
    checks: list[tuple[bool, str]] = [
        (guion_aprobado.DURACION_MIN_S <= dur <= guion_aprobado.DURACION_MAX_S,
         f"duración {dur:.2f}s (rango {guion_aprobado.DURACION_MIN_S:.0f}–"
         f"{guion_aprobado.DURACION_MAX_S:.0f}s)"),
        (abs(loud.get("lufs", 0) - mezcla.LUFS_OBJETIVO) <= 1.0,
         f"loudness {loud.get('lufs', 0):.1f} LUFS "
         f"(objetivo {mezcla.LUFS_OBJETIVO})"),
        (loud.get("true_peak", 0) <= mezcla.TRUE_PEAK_MAX + 0.5,
         f"true peak {loud.get('true_peak', 0):.1f} dBTP "
         f"(máx {mezcla.TRUE_PEAK_MAX})"),
        (min(planos) >= ritmo.PLANO_PISO_S - 0.01,
         f"plano más corto {min(planos):.2f}s (piso {ritmo.PLANO_PISO_S})"),
        (max(planos) <= ritmo.PLANO_MAX_S + 0.01,
         f"plano más largo {max(planos):.2f}s (techo {ritmo.PLANO_MAX_S})"),
    ]
    for ok, texto in checks:
        print(f"  {'✅' if ok else '🛑'} {texto}")
    print(f"  ℹ️  {len(planos)} planos · promedio "
          f"{sum(planos) / len(planos):.2f}s · gasto real {ad.gasto_real():.4f} USD")
    return all(ok for ok, _ in checks)


# ──────────────────────────────── CLI ───────────────────────────────

FASES = ["validar", "costo", "cancion", "hero", "escenas", "clips",
         "montaje", "qa", "todo"]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("guion", type=Path)
    ap.add_argument("fase", choices=FASES)
    ap.add_argument("--salida", type=Path, default=None)
    ap.add_argument("--forzar", action="store_true",
                    help="regenera la canción aunque ya exista (vuelve a cobrar)")
    args = ap.parse_args()

    ad = Ad(args.guion)
    print(f"{ad.g['titulo']} · {ad.g['estilo']} · "
          f"{ad.g.get('nicho') or ad.g.get('publico') or 'sin nicho'} · "
          f"modo {ad.g.get('modo')} · {len(ad.lineas)} líneas · job {ad.job}\n")

    # Nada que cueste dinero corre sobre un guion que no pasa las 6 reglas.
    if args.fase not in ("validar", "costo", "qa"):
        r = guion_aprobado.validar(ad.g)
        if not r.ok:
            print(r.texto())
            print("\n🛑 No se produce sobre un guion con errores.")
            return 1
        for aviso in r.avisos:
            print(f"⚠️  {aviso}")
        if r.avisos:
            print()

    if args.fase == "validar":
        return 0 if fase_validar(ad).ok else 1
    if args.fase == "costo":
        fase_costo(ad)
        return 0
    if args.fase == "qa":
        return 0 if fase_qa(ad, args.salida) else 1

    if args.fase in ("cancion", "todo"):
        fase_cancion(ad, forzar=args.forzar)
    if args.fase in ("hero", "todo"):
        fase_hero(ad)
    if args.fase in ("escenas", "todo"):
        fase_escenas(ad)
    if args.fase in ("clips", "todo"):
        fase_clips(ad)
    if args.fase in ("montaje", "todo"):
        fase_montaje(ad, args.salida)
    if args.fase == "todo":
        fase_qa(ad, args.salida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
