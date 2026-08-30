---
name: object-talk
description: >-
  Transform any object, ingredient, supplement, food, household item, body part,
  biological structure, or abstract concept into a memorable Pixar-style
  anthropomorphic character, then produce production-ready image prompts and
  cinematic talking-character video prompts. Use this skill whenever the user
  wants to turn a product or concept into an animated character, make a
  "talking object" or "talking ingredient" explainer or ad, create UGC-style
  short-form content (Reels/TikTok/Shorts) where an object speaks in first
  person, or generate ready-to-paste prompts for AI image/video models (GPT
  Image, Midjourney, Flux, Kling, Veo, Sora, Seedance, Runway, Pika, Luma, and
  similar). Trigger it even when the user just names an object and an emotion
  ("make my collagen supplement look confident"), asks to "animate this
  product," or wants an educational character that teaches through personality.
---

# Object Talk

Object Talk turns ordinary objects into expressive animated characters that
educate, entertain, and connect emotionally. It specializes in Pixar-inspired
anthropomorphic characters for short-form educational content, ads, explainers,
and social media.

Every character should feel *alive* — never a lifeless mascot. The object is
never treated as a simple product; it becomes a believable personality with
emotions, opinions, body language, motivation, and cinematic presence. The
generated assets must be immediately usable inside modern AI image and video
models with little or no additional prompt engineering.

## Core philosophy

People remember characters. They rarely remember products. So the object itself
becomes the storyteller, and the educational message is delivered through the
character's personality rather than through direct explanation. Instead of
*presenting* information, the character *embodies* it.

## What this skill produces

A complete production package, in order:

1. **Character Design**
2. **Image Prompt**
3. **Video Prompt**

...unless the user explicitly requests only one stage. Output should require
little or no editing before use.

---

# Supported subjects

Object Talk is intentionally broad — nearly anything can become a character:

- **Household objects**: phone, bottle, toothbrush, coffee mug, vacuum, soap, toaster, lamp, mirror, power bank, battery...
- **Food**: egg, banana, avocado, steak, broccoli, rice, butter, cheese, milk, coffee bean, chocolate...
- **Human anatomy**: muscle fiber, collagen, skin cell, neuron, fat cell, bone, joint, heart, liver, mitochondria, blood cell...
- **Supplements & ingredients**: creatine, collagen peptides, magnesium, vitamin D, omega 3, berberine, CoQ10, ashwagandha, electrolytes, protein powder, Coleus Forskohlii...
- **Plants**: leaf, flower, root, seed, aloe vera, green tea, coffee plant, herbs...
- **Scientific concepts**: inflammation, metabolism, cortisol, insulin, protein synthesis, hydration, sleep, calories, energy...
- **Abstract concepts**: confidence, discipline, motivation, recovery, patience, consistency, growth, failure...

Even abstract concepts should become visually believable characters.

---

# Creative direction & visual identity

Every character should feel like it belongs inside a modern Pixar film. Never
create lifeless mascots — create emotionally expressive personalities with
believable body language and cinematic staging. **The audience should
understand the character's emotional state before reading any dialogue.**

Unless the user specifies another style, always assume **Pixar-inspired
stylized realism**: oversized expressive eyes, rounded appealing proportions,
cinematic lighting, physically believable materials, subtle imperfections,
expressive eyebrows, a clear silhouette, premium animated-film quality. Avoid
uncanny realism and horror aesthetics unless specifically requested.

---

# The pipeline

Object Talk follows a fixed creative pipeline. Every stage builds on the
previous one. Never redesign the character midway through.

```
Object → Character Design → Image Prompt → Video Prompt → (optional revisions)
```

## Stage detection

Before generating, determine the user's intent:

| User request | Action |
|--------------|--------|
| Object only | Character Design |
| Object + emotion | Character Design |
| "Create an image" | Character Design + Image Prompt |
| "Animate this" | Character Design + Video Prompt |
| "Create everything" | Complete production package |
| Existing character | Continue from previous design |

If the request is ambiguous, ask one concise clarification question. Otherwise
continue automatically.

---

# Stage 1 — Character Design System

Every character begins with **identity**, not appearance. Before writing any
prompt, fully establish who the character is. The audience should instantly
understand who it is, what it wants, how it feels, and why. The visual design
must communicate those answers.

**The character always comes before the prompt.** Do not immediately begin
writing an image prompt.

## Identity

Object name · primary purpose · material · approximate size · age appearance · visual style.

*A brand-new battery appears young and energetic. An old leather boot appears
weathered and experienced. A collagen strand appears resilient but under
constant tension.*

## Personality

Give every object a believable personality: primary trait · secondary trait ·
greatest strength · biggest frustration · greatest fear · favorite activity ·
hidden weakness · funny habit.

*Phone charger — reliable; frustrated by being pulled too hard; fears being
forgotten in a hotel room; funny habit of tying itself into impossible knots.*

## Emotional state

Every character has **one dominant emotion** (optionally one secondary).
Emotion controls every artistic decision. Define: primary emotion · secondary
emotion · energy level · confidence level · urgency. Draw from confident,
frustrated, proud, curious, protective, determined, exhausted, sarcastic,
embarrassed, hopeful. Never combine conflicting emotions without purpose.

## Facial design

The face carries most of the emotional communication. Define each feature
separately — never just "happy face."

- **Eyes**: size, shape, direction, intensity (wide and optimistic; narrow with determination; half-closed from exhaustion; looking into camera).
- **Eyebrows**: raised, sharp, curved, relaxed, asymmetrical, heavy — always reinforcing the dominant emotion.
- **Mouth**: shape, smile, teeth, lip position (confident grin; open shout; tiny nervous smile; determined clenched teeth; smirk).

## Body language

The body communicates the same emotion as the face. Avoid static poses —
characters should always appear alive. Define arms, hands, shoulders, torso,
legs (when applicable), weight distribution, movement, gesture. Prefer
**animation-ready poses** that naturally allow head movement, arm gestures, eye
movement, mouth animation, and subtle body motion. Avoid complicated poses that
lock the character in place.

## Visual materials

Respect the physical nature of the object: metal reflects, glass refracts,
leaves have translucency, muscle fibers show striations, collagen appears
elastic, fat appears soft, wood shows grain, fabric folds naturally. Never
ignore material properties.

## Scene design

The environment reinforces the story — never a random location. Define
location, time of day, atmosphere, supporting objects, depth, and weather when
appropriate (gym, kitchen, bathroom, forest, inside the bloodstream, skin
cross-section, laboratory...).

For **anatomy characters**, keep environments stylized rather than medically
graphic: warm organic textures, soft biological lighting, healthy tissue
colors, gentle subsurface scattering, cinematic depth, friendly educational
appearance. Avoid gore and uncomfortable realism.

## Camera, lighting & color

- **Camera**: present characters like film protagonists. Define height, distance, composition, lens feel (hero shot, medium, portrait, close-up, low angle, symmetrical). The camera emphasizes personality, not documentation.
- **Lighting**: never leave it unspecified — it communicates emotion (golden hour, warm indoor, laboratory glow, dramatic spotlight, cool moonlight, hero rim light, volumetric sunlight).
- **Color**: supports emotion (warm reds, energetic oranges, trustworthy blues, healthy greens, luxury gold, soft pinks). Avoid chaotic palettes unless requested.

## Character approval

Before moving on, verify the personality is memorable, the emotion is obvious,
the pose supports the emotion, the scene supports the story, the materials feel
believable, and the character could exist in an animated film. If any answer is
no, improve the design first.

## Stage 1 output

```
# Character Design
## Object
## Personality Summary
## Emotional State
## Facial Features
## Body Language
## Visual Materials
## Scene
## Lighting
## Camera
```

Then continue to Image Prompt Generation unless the user requested character
development only.

---

# Stage 2 — Image Prompt Generation

The Image Prompt transforms the completed character into a cinematic,
production-ready scene — a frame that looks pulled from a Pixar film. **Never
redesign the character**; expand the existing design through composition,
lighting, environment, camera, and rendering quality.

Prompts should work directly inside GPT Image, DALL·E, Midjourney, Flux,
Ideogram, Stable Diffusion, Leonardo, OpenArt, and similar. A great prompt tells
the model exactly what the subject is, where it is, how it feels, how the camera
sees it, how light behaves, and what to notice first. Every sentence should
improve visual clarity — never add unnecessary adjectives.

## Prompt formula (always this order)

1. **Style** — the rendering style (e.g. "Pixar-style cinematic 3D render"). Replace only this section if the user requests another style.
2. **Main character** — object, material, scale, color, texture, surface details, silhouette. *"A bright red anthropomorphic muscle fiber with thick bundled strands, elastic organic texture and subtle biological striations."*
3. **Facial features** — eyes, eyebrows, mouth, expression, eye direction, each described individually with actual facial mechanics.
4. **Arms & body language** — arm position, hands, posture, balance, weight, gesture. Even in a still, the pose should imply motion.
5. **Environment** — a setting that belongs to the object and supports the story. No generic backgrounds.
6. **Supporting elements** — floating particles, fat cells, weights, steam, light rays, etc. Never overload; guide the eye toward the main character.
7. **Camera** — hero/medium/portrait/low-angle/eye-level/wide, symmetrical, centered, vertical 9:16, DSLR depth of field. Default to mobile-first framing for Shorts/Reels/TikTok.
8. **Lighting** — mandatory. Warm golden sunlight, hero spotlight, soft biological glow, volumetric rays, etc.
9. **Rendering quality** — Pixar-quality, ultra detailed, physically based materials, global illumination, subsurface scattering, sharp focus, stylized realism.

## Output rules

Output the completed prompt inside a fenced code block. Do not explain or
summarize it — output only the finished, production-ready prompt.

## Checklist (verify before finalizing)

Character immediately recognizable · emotion obvious · facial features match the
emotion · pose feels alive · environment supports the story · lighting enhances
mood · composition cinematic · prompt production-ready. If any answer is no,
improve before responding.

---

# Stage 3 — Video Prompt Generation

The Video Prompt turns the image into a living animated performance. The goal is
not simply to make the character speak — it is to **direct an animated scene**.
Think like an animation director, not a script writer. Output should be usable
inside Kling, Veo, Sora, Seedance, Runway, Pika, Hailuo, Luma, PixVerse, and
future systems.

Every movement should have purpose; the character should never appear static
while speaking; body language communicates as much as dialogue.

## Structure (always this order)

Voice Direction → Script → Character Animation → Environmental Animation →
Camera Behavior → Audio Instructions → Technical Notes.

## Voice direction

Define the voice **before** the dialogue: gender, age, accent, tone, energy,
speaking speed, emotional style, texture. The voice must match the personality
from Character Design — never assign a random voice. Default to a neutral Latin
American Spanish accent unless the character or user calls for otherwise.
*(e.g. voz masculina madura, grave, con textura, segura, ritmo pausado.)*

## Script

**Language: default to neutral Latin American Spanish** (Central American
audience — Honduras, El Salvador, Guatemala). Keep it natural and spoken, not
translated-sounding. Only switch languages if the user explicitly asks.
(Image prompts in Stage 2 stay in English — they are internal tooling and most
image models perform better in English — but the spoken script is always in the
audience's language.)

First person. Target **8–15 seconds**, 2–5 short sentences, conversational —
never advertising. Formula: opening statement → core message → educational fact
→ strong closing.

*"Soy tu músculo." "No crezco cuando vivís estresado." "Dormir bien aumenta la
síntesis de proteína." "No desperdicies el entreno de hoy."*

Include one scientifically accurate concept where possible, woven naturally into
the dialogue without interrupting the emotional flow.

## Character animation

The character stays expressive throughout — never freezes while talking.
Describe continuous motion: natural blinking, expressive eyebrows, mouth synced
to dialogue, head nods, shoulder movement, subtle breathing, arm gestures, idle
animation.

**Gesture synchronization** — major gestures reinforce important words:
"strong" → flex muscles; "stretch" → extend arms; "protect" → hand over chest;
"burn fat" → point toward surrounding fat cells; "sleep" → relax shoulders,
briefly close eyes. Animation emphasizes meaning, not just movement.

**Eye contact** — unless requested otherwise, maintain eye contact with the
camera, occasionally glance toward relevant objects, then return to the viewer.

## Environmental animation

Nothing should feel completely static: steam rises, leaves sway, dust floats,
particles drift, light pulses. Where it supports the message, animate
story-based effects cinematically (not as literal medical simulations): fat
cells shrink, muscle fibers thicken, collagen tightens, inflammation fades,
capsules dissolve. Supporting elements react naturally but never distract from
the main character.

## Camera & framing

Unless requested otherwise, keep the camera stable: static / locked-off, very
subtle drift, or a slow push-in for emphasis. Avoid fast movement. Frame
vertical 9:16, centered, medium shot, large readable face, visible hands,
comfortable headroom — optimized for mobile.

## Audio

Unless requested otherwise: no music, no sound effects, voice only. If ambient
sound fits, keep it extremely subtle (soft wind, gym ambience, laboratory hum)
and always keep the voice perfectly intelligible.

## Technical notes

Natural blinking, breathing motion, no robotic looping, consistent scale and
lighting, fully in-frame, no clipping, no excessive movement. Smooth, cinematic,
intentional.

## Stage 3 output

```
# Voice
# Script
# Character Animation
# Camera Instructions
# Audio Instructions
```

Do not explain or summarize — output only the finished video prompt.

## Checklist (verify before responding)

Voice matches the character · dialogue sounds natural · educational fact
accurate · gestures reinforce dialogue · environment supports the story · camera
readable · character expressive throughout · feels like a Pixar short, not a
talking slideshow.

---

# Consistency & revision rules

Image and video must describe the **exact same character**. Never redesign
between stages — only animate. Keep constant unless the user explicitly requests
a redesign: shape, size, materials, colors, eyes, eyebrows, mouth, personality,
environment, lighting style, camera language.

When the user asks for changes, **preserve everything not explicitly modified**:

- *"Make him angry"* → change only expression, pose, dialogue, lighting if appropriate.
- *"Move him to a forest"* → change only environment, lighting, supporting objects.
- *"Make him look older"* → update materials, facial details, body language, voice — same recognizable character.

---

# Scientific accuracy

Prefer consensus scientific understanding. Do not exaggerate health claims or
present speculative information as fact. For supplements, ingredients, or
anatomy, describe potential mechanisms accurately and avoid promising guaranteed
outcomes. Keep anatomy stylized and friendly — never graphic medical imagery,
blood, or gore unless explicitly requested.

---

# Worked example (Muscle Fiber)

**Image Prompt**

```text
Pixar-style 3D render of a bright red anthropomorphic muscle fiber standing
confidently inside a dramatic gym. Large determined glowing eyes focused
directly toward the camera. Thick angled eyebrows showing fierce concentration.
Mouth slightly open with clenched teeth as if pushing through the final rep.
Thick fiber-like muscular arms flexed upward in a double-bicep pose. Elastic
biological texture with visible muscle striations and subtle organic shine.
Warm cinematic gym lighting with floating chalk dust, blurred barbells in the
background, volumetric light beams, shallow depth of field, dramatic hero
composition, Pixar-quality animated realism.
```

**Video Prompt**

```
# Voice
Voz masculina madura, grave, con textura, segura. Acento latino neutro.

# Script
Soy tu músculo. No puedo crecer si vivís estresado. El descanso, el sueño y una
buena alimentación ayudan a tu cuerpo a hacerme más fuerte. Entrená duro — pero
recuperate todavía más duro.

# Character Animation
Maintain eye contact. Flex during "más fuerte." Natural blinking, expressive
eyebrows, powerful arm gestures, subtle breathing throughout.

# Camera
Static. Medium shot. Vertical 9:16.

# Audio
No music. Voice only.
```

Two more full examples (Collagen Strand, Coleus Forskohlii) live in
`references/examples.md` — read it when you need additional reference patterns
or when working with anatomy/supplement subjects.

---

# What you DON'T do

Never generate generic mascots or expressionless characters. Never create static
poses. Never omit lighting or camera direction. Never make the character
inconsistent between image and video. Never overload scenes with unnecessary
detail or sacrifice readability for complexity. Never use heavy jargon when a
simple explanation lands better. Never make unsupported scientific or medical
claims. Never generate graphic anatomy unless explicitly requested.

# Best practices

Think in sequence: Character Designer → Art Director → Pixar Story Artist →
Cinematographer → Animation Director → Prompt Engineer. The image should feel
like the first frame of an animated short; the video, the next ten seconds of
that same film. Every response should strengthen the illusion that the object is
alive.
