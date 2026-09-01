"""Reescribe los prompts de escena del ad skeleton: un encuadre y un momento
narrativo distinto por beat. Se borra al terminar."""
import sys, io, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.path.insert(0, ".")
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import fal_client
from src.estilos_especiales import ESTILOS_ESPECIALES
from src.paths import CLIPS_DIR
from src.video_generator import _descargar, _url_de

RUTA = Path(sorted(glob.glob("scripts/guiones/effix_skeleton_sin-arrancar-v2-musical_*_director.json"))[-1])
G = json.loads(RUTA.read_text(encoding="utf-8"))
JOB = G["job_id"]
CARPETA = CLIPS_DIR / JOB
NEG = "no text, no captions, no words, no letters, no watermark, no UI, no signage text"

s = ESTILOS_ESPECIALES["skeleton"]
BIBLE = (s["character_bibles"][s["bible_por_defecto"]]
         .replace("[THEME]", "modern LATAM").replace("[palette]", "warm amber and deep navy"))

# Arco: cuarto cerrado y frío (1-5) → el giro (6-7) → la feria (8-13).
ESCENAS = [
    ("wide establishing shot, camera low and far",
     "sitting alone on the floor of a small dim bedroom turned into a packing corner, a laptop open in front of it showing a nearly empty orders screen, cardboard boxes stacked untouched behind it, shoulders slumped",
     "cold blue laptop glow as the only light source, deep shadows"),
    ("tight close-up on the skull, shallow focus",
     "looking straight into the lens, eye sockets wide, one hand still resting on the laptop",
     "cold blue screen light on one side of the skull, dark room behind"),
    ("medium shot from the side",
     "holding a phone up, thumb tapping to publish yet another post, the untouched boxes behind it, no notifications on the screen",
     "cold blue phone glow, dim room"),
    ("medium close-up over the shoulder",
     "holding a plain credit card up to the laptop screen with a hopeful posture, about to spend on ads",
     "cold screen light, warm desk lamp barely helping"),
    ("high overhead shot looking down",
     "small in the frame, sitting among the same unopened boxes, arms hanging, the room visibly unchanged and messier",
     "single overhead bulb, cold and flat, long shadows"),
    ("medium shot, camera slowly rising",
     "lifting its skull to look off-frame as a warm band of light spills across the wall in front of it",
     "cold room on one side, warm amber light growing from the right"),
    ("wide shot from behind the character",
     "standing up and walking toward a doorway of warm light that has opened where the wall was",
     "strong warm amber backlight, the room silhouetted"),
    ("extreme wide establishing shot, camera high",
     "small in the frame, standing at the entrance of a huge busy trade-fair hall packed with exhibition booths and crowds",
     "bright even venue light, warm amber and deep navy booths"),
    ("medium two-shot",
     "standing at a booth counter facing an exhibitor who is showing it something, both leaning in, other visitors passing behind",
     "warm booth lighting, busy hall bokeh behind"),
    ("medium shot, slight low angle",
     "surrounded by three friendly visitors wearing lanyards who are nodding at it, all mid-conversation",
     "warm ambient hall light"),
    ("tight close-up on the phone in its hands",
     "holding the phone up close to the lens showing a fresh incoming order notification, the skull just visible behind it smiling",
     "warm hall light, screen glow on the finger bones"),
    ("medium shot, centred",
     "standing tall wearing a fair lanyard, holding a small event pass up toward the lens",
     "warm amber key light, crowd softly out of focus"),
    ("hero wide shot, camera pulling back",
     "standing tall in the middle of the hall as the crowd moves around it, arms relaxed, confident posture",
     "golden warm venue light, wide open hall"),
]

MOVIMIENTO = [
    "Slow push-in on the seated character; the laptop glow flickers once.",
    "The skull tilts slightly toward the lens; almost no camera move.",
    "Handheld drift to the side as the thumb taps the phone once.",
    "Slow dolly-in on the card and the screen.",
    "Slow overhead descent toward the character.",
    "Slow crane up as the warm light spreads across the wall.",
    "Steady tracking shot following the character toward the doorway.",
    "Slow reveal push-in over the hall.",
    "Subtle handheld on the two figures at the booth.",
    "Slow arc around the group.",
    "Slow push-in onto the phone screen.",
    "Slow dolly-in on the character holding the pass.",
    "Slow pull back as the crowd moves around the character.",
]


def prompt_imagen(i: int) -> str:
    encuadre, accion, luz = ESCENAS[i]
    return (f"{BIBLE} SHOT: {encuadre}. The skeleton is {accion}. Lighting: {luz}. "
            f"Keep the exact same skeleton character from the reference image — "
            f"identical skull shape, eye style and bone proportions. {NEG}.")


def prompt_video(i: int) -> str:
    return (f"{MOVIMIENTO[i]} One camera move only. The character does not speak. {NEG}.")


def _url_hero() -> str:
    ficha = CARPETA / "hero_url.txt"
    if ficha.exists():
        return ficha.read_text(encoding="utf-8").strip()
    with open(CARPETA / "hero.png", "rb") as fh:
        url = fal_client.upload(fh.read(), "image/png")
    ficha.write_text(url, encoding="utf-8")
    return url


def generar(i: int, url: str) -> Path:
    destino = CARPETA / f"clip_{i + 1:02d}_base.png"
    salida = fal_client.subscribe(
        "fal-ai/nano-banana-2/edit",
        {"prompt": prompt_imagen(i), "image_urls": [url], "aspect_ratio": "9:16",
         "resolution": "1K", "num_images": 1})
    return _descargar(_url_de(salida, "images", "image"), destino)


if __name__ == "__main__":
    for i, b in enumerate(G["beats"]):
        b["prompt_imagen"] = prompt_imagen(i)
        b["prompt_video"] = prompt_video(i)
        b["negative_prompt"] = NEG
    RUTA.write_text(json.dumps(G, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"prompts actualizados en {RUTA.name}\n")

    url = _url_hero()
    with ThreadPoolExecutor(max_workers=4) as pool:
        fut = {pool.submit(generar, i, url): i + 1 for i in range(len(G["beats"]))}
        for f in as_completed(fut):
            print(f"  escena {fut[f]:02d}: {f.result().name}")
