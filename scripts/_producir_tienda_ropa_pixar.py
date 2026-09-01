"""Produce el ad Pixar "La venta que no fue" — nicho tienda_ropa.

Fases, en este orden y por separado, porque cada una cuesta:

    python scripts/_producir_tienda_ropa_pixar.py hero      # 1 imagen  ($0.08)
    python scripts/_producir_tienda_ropa_pixar.py escenas   # 15 imgs   ($1.20)
    python scripts/_producir_tienda_ropa_pixar.py clips     # 46s video ($3.86)
    python scripts/_producir_tienda_ropa_pixar.py montaje   # gratis

El audio ya está hecho: `assets/audio/tienda-ropa-pixar-v2/`. Su duración real
(53,9s con la voz Medellin) es la que fija el ritmo del montaje.
"""
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")

from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import fal_client
import requests

import src.paths  # carga el .env y mapea FAL_API_KEY → FAL_KEY, que es la que mira fal_client  # noqa: F401

GUION = Path("scripts/guiones/effix_tienda-ropa_pixar-v2_APROBADO.json")
CARPETA = Path("assets/clips/tienda-ropa-pixar-v2")
AUDIO = Path("assets/audio/tienda-ropa-pixar-v2")
CARPETA.mkdir(parents=True, exist_ok=True)

MODELO_IMG = "fal-ai/nano-banana-2"
MODELO_EDIT = "fal-ai/nano-banana-2/edit"
MODELO_VIDEO = "fal-ai/kling-video/o1/standard/image-to-video"

# Sin texto en la generación: los overlays se ponen en montaje.
NEG = ("Absolutely no text anywhere: no captions, no words, no letters, no signage text, "
       "no watermarks, no UI labels. Any screens show only icons and abstract shapes.")

ESTILO = ("Pixar 3D CGI style, subsurface scattering skin, volumetric warm lighting, "
          "expressive eyes, high detail textures, cinematic color grade, "
          "Disney Pixar quality render")

MILENA = ("a 34-year-old Colombian woman, warm brown skin, dark hair pulled back in a low bun "
          "with loose strands, kind tired eyes, a simple coral blouse, gentle rounded features")

# Las quince imágenes. La clave es el número que usan las escenas del guión.
IMAGENES = {
    "01": ("hero", f"{MILENA}, sitting on a worn sofa in a modest living room in a small "
           "Colombian city, holding a phone in both hands, late afternoon light through a "
           "window, potted plant and family photos behind her, medium shot, vertical framing"),
    "02": ("edit", "The same woman, now seen from behind her shoulder: the phone screen fills "
           "most of the frame, showing a photo of a folded mustard-yellow blouse on a hanger, the image "
           "clearly a forwarded photo. Her thumb rests at the edge of the screen. Close-up, "
           "shallow depth of field, warm afternoon light."),
    "03": ("edit", "The same phone screen, now filling the frame: a messaging conversation "
           "where one message bubble has been sent and nothing has come back, empty space "
           "below it. Only shapes and bubbles, no readable text. The woman's hand holds the "
           "phone steady. Close-up, the room dimmer than before."),
    "04": ("edit", "The same phone lying face down on a wooden table, screen off, next to a "
           "cold cup of coffee. The same living room behind, now at night, the window dark, "
           "a single warm lamp on. The woman out of focus in the background, turned away. "
           "Close-up on the phone, low angle."),
    "05": ("edit", "A small clothing shop seen from the empty sidewalk at night, its window "
           "display lit from inside and glowing on the wet pavement, mannequins wearing "
           "colorful clothes, the metal shutter half down. Nobody in the street. Wide shot, "
           "rain on the glass, warm shop light against cold blue night."),
    "06": ("edit", "The same street seen wider and from further back: the whole sleeping "
           "neighborhood block, the little lit shop small at the end of it, other shutters "
           "closed, a single street lamp, power lines. Very wide shot, cold blue night with "
           "one warm point of light."),
    "07": ("edit", "Extreme close-up of two hands folding a mustard-yellow blouse on a wooden "
           "shop counter. The frame is cropped at the forearms: NO face, NO head, NO shoulders, "
           "nobody visible above the wrists anywhere in the image. Racks of clothes softly out "
           "of focus behind. Warm interior shop light, shallow depth of field."),
    "08": ("edit", "The same mustard-yellow blouse now folded neatly on the shop counter, the hands "
           "leaving the frame at the edge. The counter has a small stack of folded clothes "
           "and an empty cardboard box. Close-up, warm shop light, no face anywhere."),
    "09": ("edit", "The entrance of a large modern convention center in Medellín, glass and "
           "concrete, crowds of Latin American entrepreneurs walking in wearing lanyards, "
           "morning light, tropical plants and mountains in the background. Wide "
           "establishing shot, bright and busy."),
    "10": ("edit", "Inside the convention center: a wide aisle of a packed trade fair, rows of "
           "exhibition booths on both sides, hundreds of anonymous Latin American business "
           "people talking and walking, all seen at medium distance, nobody in the foreground, "
           "no close-up faces. The woman from the reference image does NOT appear in this "
           "scene. Banners show only abstract shapes. Wide shot down the aisle, bright even "
           "venue light, strong depth."),
    "11": ("edit", "The exterior facade of a large convention center in a Colombian city by "
           "day, modern architecture with tall glass panels, flags along the entrance, "
           "green mountains behind the city, people arriving. Wide hero shot, bright "
           "daylight, deep blue sky."),
    "12": ("edit", "Inside a full auditorium: a speaker on stage seen from the back of the "
           "room, hundreds of seated attendees, many taking notes on phones and notebooks, "
           "stage lighting on the speaker, the big screen behind showing only abstract "
           "shapes. Wide shot from the back, warm stage light."),
    "13": ("edit", "Extreme close-up of two hands holding a phone above a wooden shop counter, "
           "one thumb pressing the screen. The screen shows a simple ticket shape and a green "
           "checkmark, no text. NO other person, NO card reader machine, NO customer: only the "
           "hands, cropped at the forearms, no face anywhere. Folded clothes on the counter "
           "below. Warm shop light, shallow focus."),
    "14": ("edit", f"{MILENA}, in the same living room as the first image, kneeling on the "
           "floor beside an open cardboard shipping box, tissue paper pushed aside, both "
           "hands just lifting a folded mustard-yellow blouse out of it. She is clearly "
           "delighted: wide bright eyes, eyebrows raised, a big open smile. Warm daylight "
           "through the window. Medium shot, same sofa and plant behind her."),
    # El final NO cambia de ropa ni de postura respecto al inicial: sigue de
    # rodillas y con su blusa coral. Pedirle a Kling que le cambie el vestuario
    # entre keyframes produjo un morphing feo — el personaje solo levanta la
    # blusa y sonríe más.
    "15": ("edit", f"{MILENA}, kneeling in the same living room beside the same open cardboard "
           "box, now holding the unfolded mustard-yellow blouse up in front of her with both "
           "hands, laughing with joy, head slightly tilted back. She is still wearing her own "
           "coral blouse. Warm daylight, same room, same warm palette as the first image."),
}


def _guion():
    return json.loads(GUION.read_text(encoding="utf-8"))


def _descargar(url: str, destino: Path) -> Path:
    destino.write_bytes(requests.get(url, timeout=600).content)
    return destino


def _subir(ruta: Path) -> str:
    with open(ruta, "rb") as fh:
        return fal_client.upload(fh.read(), "image/png")


def fase_hero():
    """La hoja de Milena. Gobierna la consistencia de todo lo demás."""
    destino = CARPETA / "img_01.png"
    if destino.exists():
        print(f"ya existe: {destino}")
        return
    _, prompt = IMAGENES["01"]
    salida = fal_client.subscribe(MODELO_IMG, {
        "prompt": f"{ESTILO}. {prompt}. {NEG}",
        "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1,
    })
    _descargar(salida["images"][0]["url"], destino)
    print(f"HÉROE: {destino}")


def fase_escenas():
    """Las catorce restantes, todas referenciando la héroe."""
    hero = CARPETA / "img_01.png"
    if not hero.exists():
        sys.exit("Falta la héroe. Corre la fase `hero` primero.")
    url_hero = _subir(hero)

    pendientes = [(k, p) for k, (tipo, p) in IMAGENES.items()
                  if tipo == "edit" and not (CARPETA / f"img_{k}.png").exists()]
    if not pendientes:
        print("las quince ya están")
        return

    def una(clave, prompt):
        salida = fal_client.subscribe(MODELO_EDIT, {
            "prompt": (f"Using the attached image as the style and character reference, keep the "
                       f"exact same {ESTILO} look, the same woman's face and proportions where she "
                       f"appears, and the same warm palette. {prompt}. {NEG}"),
            "image_urls": [url_hero],
            "aspect_ratio": "9:16", "resolution": "1K", "num_images": 1,
        })
        return clave, _descargar(salida["images"][0]["url"], CARPETA / f"img_{clave}.png")

    with ThreadPoolExecutor(max_workers=4) as pool:
        futuros = [pool.submit(una, k, p) for k, p in pendientes]
        for f in as_completed(futuros):
            clave, ruta = f.result()
            print(f"  imagen {clave} → {ruta.name}")


# Movimiento por escena: uno solo por clip, nunca apilado.
MOVIMIENTO = {
    1: "Slow push-in on the woman as she looks at her phone; she blinks and tilts her head. Subtle handheld.",
    2: "The phone screen slowly fills more of the frame; her thumb hesitates over it. Static camera, gentle breathing motion.",
    3: "Hold on the unanswered conversation; the room light dims slowly around the phone. Very slow drift in.",
    4: "Slow pull-back from the phone lying face down as the room settles into night. The woman turns away in the background.",
    5: "Slow dolly back from the lit shop window into the empty street; rain drifts through the light.",
    6: "Slow crane up over the sleeping street, the single lit shop getting smaller in frame.",
    7: "The hands finish folding the blouse and place it down; camera holds close and still.",
    8: "Slow push-in on the folded blouse as the hands leave frame.",
    9: "Slow forward tracking shot following the crowd into the convention center entrance.",
    10: "Steady forward travelling down the packed fair aisle, people crossing the frame.",
    11: "Slow tilt up the convention center facade against the sky.",
    12: "Slow push-in from the back of the auditorium toward the stage.",
    13: "Close static shot; the thumb taps once and a checkmark appears. Minimal motion.",
    14: "The woman opens the box flaps and her face lights up; slow push-in.",
    15: "She smiles and turns slightly toward the light; slow push-in, warm and calm.",
}


def fase_clips():
    """Diez clips Kling O1, con frame inicial y final donde el guión lo pide."""
    g = _guion()
    pendientes = [e for e in g["escenas"]
                  if not (CARPETA / f"clip_{e['escena']:02d}.mp4").exists()]
    if not pendientes:
        print("los diez clips ya están")
        return

    # Las imágenes se suben una sola vez aunque dos escenas compartan frame.
    claves = set()
    for e in pendientes:
        claves.add(e["start_image"].split()[0])
        if e["end_image"]:
            claves.add(e["end_image"].split()[0])
    urls = {k: _subir(CARPETA / f"img_{k}.png") for k in sorted(claves)}
    print(f"{len(urls)} imágenes subidas, {len(pendientes)} clips por generar")

    def uno(escena):
        n = escena["escena"]
        ini = escena["start_image"].split()[0]
        fin = escena["end_image"].split()[0] if escena["end_image"] else None
        # Kling O1 solo admite 5 o 10 segundos cuando no hay frame final; con
        # frame final acepta cualquier entero de 3 a 10. Las escenas sin end se
        # piden de 5s y el montaje las recorta a su duración real.
        pedida = escena["duracion_s"] if escena["end_image"] else (5 if escena["duracion_s"] <= 5 else 10)
        payload = {
            "start_image_url": urls[ini],
            "prompt": MOVIMIENTO[int(ini)],
            "duration": str(pedida),
        }
        if fin:
            payload["end_image_url"] = urls[fin]
            payload["prompt"] = (f"Animate the transition from @Image1 to @Image2. "
                                 f"{MOVIMIENTO[int(ini)]}")
        salida = fal_client.subscribe(MODELO_VIDEO, payload)
        url = salida["video"]["url"] if isinstance(salida["video"], dict) else salida["video"]
        _descargar(url, CARPETA / f"clip_{n:02d}.mp4")
        return n, escena["duracion_s"], ini, fin

    with ThreadPoolExecutor(max_workers=3) as pool:
        for f in as_completed([pool.submit(uno, e) for e in pendientes]):
            n, dur, ini, fin = f.result()
            print(f"  clip {n:02d} ({dur}s, {ini}→{fin or '—'}) listo")



# ---------------------------------------------------------------------------
# Montaje: gratis, solo ffmpeg
# ---------------------------------------------------------------------------

import subprocess

FUENTE = "referencias/esteticas/fuentes/Montserrat-Black.ttf"

# Un overlay por escena. Máximo siete palabras: tiene que leerse sin sonido.
OVERLAYS = {
    1:  "Una señora en Neiva",
    2:  "«¿Ustedes hacen envíos?»",
    3:  "Nadie le contestó",
    4:  "Esa venta no fue tuya",
    5:  "Te falta el camino",
    6:  "350 empresas",
    7:  "16-18 oct · Plaza Mayor",
    8:  "200 ponentes",
    9:  "feriaeffix.com",
    10: "FERIA EFFIX",
}


def _ff(*args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def fase_montaje():
    g = _guion()
    salida = Path("assets/renders"); salida.mkdir(parents=True, exist_ok=True)
    tmp = CARPETA / "montaje"; tmp.mkdir(exist_ok=True)

    # 1. Voz corrida: las catorce frases una tras otra con una respiración corta
    #    entre ellas. No se alinea frase a escena a propósito — la imagen corta
    #    cada pocos segundos, la frase no, y eso es lo que suena a persona.
    RESPIRO = 0.12
    silencio = tmp / "respiro.wav"
    _ff("-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", str(RESPIRO), str(silencio))

    total_frases = sum(len(e["frases"]) for e in g["escenas"])
    trozos = []
    for i in range(1, total_frases + 1):
        wav = tmp / f"f_{i:02d}.wav"
        _ff("-i", str(AUDIO / f"beat_{i:02d}.mp3"), "-ar", "44100", "-ac", "2", str(wav))
        trozos.append(wav)
        if i < total_frases:
            trozos.append(silencio)

    lista_voz = tmp / "voz.txt"
    lista_voz.write_text("".join(f"file '{t.resolve().as_posix()}'\n" for t in trozos),
                         encoding="utf-8")
    voz = tmp / "voz_completa.wav"
    _ff("-f", "concat", "-safe", "0", "-i", str(lista_voz), "-c", "copy", str(voz))

    # 2. El ritmo sale de comparar la voz real con el video ya comprado: los
    #    clips se estiran lo justo para que la locución quepa entera. Regenerar
    #    video cuesta dólares; ralentizar cuesta cero y en planos de push-in
    #    lento no se nota.
    dur_voz = float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(voz)],
        capture_output=True, text=True, check=True).stdout.strip())
    dur_video = sum(e["duracion_s"] for e in g["escenas"])
    factor = max(1.0, (dur_voz + 0.4) / dur_video)
    print(f"voz {dur_voz:.1f}s · video {dur_video}s · ritmo x{factor:.3f}")

    # 2. Video: los clips en orden, normalizados al mismo formato
    normalizados = []
    for e in g["escenas"]:
        n = e["escena"]
        origen = CARPETA / f"clip_{n:02d}.mp4"
        if not origen.exists():
            sys.exit(f"Falta {origen}. Corre la fase `clips`.")
        destino = tmp / f"norm_{n:02d}.mp4"
        texto = OVERLAYS[n].replace("'", "").replace(":", r"\:")
        estirado = e["duracion_s"] * factor
        drawtext = (f"drawtext=fontfile='{FUENTE}':text='{texto}':"
                    f"fontcolor=white:fontsize=52:borderw=6:bordercolor=black@0.85:"
                    f"x=(w-text_w)/2:y=h-320:enable='between(t,0.4,{estirado - 0.3:.2f})'")
        # El -t va ANTES del -i: recorta el clip de origen. Después del -i
        # recortaría la salida ya ralentizada y anularía el estirado.
        _ff("-t", str(e["duracion_s"]), "-i", str(origen),
            "-vf", f"scale=1080:1920:force_original_aspect_ratio=increase,"
            f"crop=1080:1920,setpts={factor:.4f}*PTS,{drawtext},fps=24",
            "-an", "-c:v", "libx264", "-preset", "medium", "-crf", "20", str(destino))
        normalizados.append(destino)

    lista_video = tmp / "video.txt"
    lista_video.write_text("".join(f"file '{p.resolve().as_posix()}'\n" for p in normalizados),
                           encoding="utf-8")
    mudo = tmp / "video_mudo.mp4"
    _ff("-f", "concat", "-safe", "0", "-i", str(lista_video), "-c", "copy", str(mudo))

    # 3. Mezcla final. Si hay música, entra debajo de la voz; si no, va sin ella.
    musica = AUDIO / "musica.mp3"
    final = salida / "EFFIX-tienda-ropa-pixar-La-venta-que-no-fue.mp4"
    if musica.exists():
        _ff("-i", str(mudo), "-i", str(voz), "-i", str(musica),
            "-filter_complex",
            "[2:a]volume=0.13,afade=t=out:st=48:d=4[m];[1:a][m]amix=inputs=2:duration=first[a]",
            "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest", str(final))
    else:
        _ff("-i", str(mudo), "-i", str(voz), "-map", "0:v", "-map", "1:a",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(final))
    print(f"\nLISTO: {final}")

if __name__ == "__main__":
    fase = sys.argv[1] if len(sys.argv) > 1 else ""
    if fase == "hero":
        fase_hero()
    elif fase == "escenas":
        fase_escenas()
    elif fase == "clips":
        fase_clips()
    elif fase == "montaje":
        fase_montaje()
    else:
        sys.exit(__doc__)
