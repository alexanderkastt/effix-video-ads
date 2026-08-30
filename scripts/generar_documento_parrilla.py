"""Genera el documento de producción de la parrilla, listo para publicar.

    python scripts/generar_documento_parrilla.py

Lee `config/parrilla.json` y escribe un HTML autónomo con los 10 nichos, sus
micro-situaciones y los 30 guiones con su línea de tiempo real de clips de 4s.
"""

from __future__ import annotations

import html
import json
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from src.consola import usar_utf8  # noqa: E402

usar_utf8()

ENTRADA = RAIZ / "config" / "parrilla.json"
SALIDA = RAIZ / "outputs" / "parrilla-effix.html"

HOY = date(2026, 8, 29)
TALLER = date(2026, 9, 3)
EVENTO = date(2026, 10, 15)

ESTILOS_LEGIBLES = {
    "micro_doc_ugc": "Micro-doc UGC",
    "ugc_realista": "UGC realista",
    "crochet": "Crochet",
    "skeleton": "Skeleton",
    "zack_films": "Zack D Films",
    "object_talk": "Object Talk",
    "pixar_animado": "Pixar",
    "cinematic": "Cinematic",
    "claymation": "Claymation",
    "cyberpunk": "Cyberpunk",
    "anime": "Anime",
    "minecraft": "Minecraft",
    "musical_sync": "Musical",
    "avengers": "Avengers",
}

NIVELES_LEGIBLES = {
    "unaware": "no sabe que tiene el problema",
    "problem": "siente el dolor",
    "solution": "conoce el tipo de solución",
    "product": "te conoce",
    "most_aware": "ya quiere",
}


def e(x: object) -> str:
    return html.escape(str(x))


def construir() -> str:
    datos = json.loads(ENTRADA.read_text(encoding="utf-8"))
    payload = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")

    dias_taller = (TALLER - HOY).days
    dias_evento = (EVENTO - HOY).days
    minutos = datos["total_segundos"] // 60
    segundos_resto = datos["total_segundos"] % 60

    return f"""<title>Parrilla Effix</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>
:root {{
  --ground: #FAFAF7;
  --surface: #FFFFFF;
  --surface-2: #F1F0EC;
  --line: #DEDCD5;
  --line-soft: #EAE8E2;
  --ink: #16181C;
  --ink-2: #4A4E57;
  --ink-3: #85888F;
  --accent: #D4401F;
  --alcance: #2C6FB5;
  --conversion: #1F7A52;
  --urgencia: #B07417;
  --alerta: #C0392B;
  --shadow: 0 1px 2px rgba(20,22,26,.06), 0 4px 14px rgba(20,22,26,.05);
  --display: Oswald, "Arial Narrow", sans-serif;
  --body: "IBM Plex Sans", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  --mono: "IBM Plex Mono", ui-monospace, "SF Mono", Consolas, monospace;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --ground: #16181C;
    --surface: #1D2026;
    --surface-2: #23272E;
    --line: #32373F;
    --line-soft: #282C33;
    --ink: #F2F1ED;
    --ink-2: #B3B7BE;
    --ink-3: #7C818A;
    --accent: #FF5A36;
    --alcance: #5B9BE0;
    --conversion: #3FB77E;
    --urgencia: #E8A33D;
    --alerta: #F0685A;
    --shadow: 0 1px 2px rgba(0,0,0,.3), 0 6px 18px rgba(0,0,0,.25);
  }}
}}
:root[data-theme="dark"] {{
  --ground: #16181C;
  --surface: #1D2026;
  --surface-2: #23272E;
  --line: #32373F;
  --line-soft: #282C33;
  --ink: #F2F1ED;
  --ink-2: #B3B7BE;
  --ink-3: #7C818A;
  --accent: #FF5A36;
  --alcance: #5B9BE0;
  --conversion: #3FB77E;
  --urgencia: #E8A33D;
  --alerta: #F0685A;
  --shadow: 0 1px 2px rgba(0,0,0,.3), 0 6px 18px rgba(0,0,0,.25);
}}

* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--ground); color: var(--ink);
  font-family: var(--body); font-size: 15px; line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 0 24px 96px; }}

/* ── Cabecera ─────────────────────────────────────────── */
header {{ padding: 44px 0 28px; border-bottom: 2px solid var(--ink); margin-bottom: 28px; }}
.eyebrow {{
  font-family: var(--mono); font-size: 11px; letter-spacing: .14em;
  text-transform: uppercase; color: var(--accent); margin: 0 0 10px;
}}
h1 {{
  font-family: var(--display); font-weight: 600; font-size: clamp(34px, 6vw, 54px);
  line-height: .98; margin: 0 0 12px; text-transform: uppercase;
  letter-spacing: -.01em; text-wrap: balance;
}}
.lede {{ margin: 0; max-width: 62ch; color: var(--ink-2); font-size: 16px; }}
.topbar {{ display: flex; justify-content: space-between; align-items: flex-start; gap: 24px; flex-wrap: wrap; }}
button.tema {{
  font-family: var(--mono); font-size: 11px; letter-spacing: .08em; text-transform: uppercase;
  background: transparent; color: var(--ink-2); border: 1px solid var(--line);
  padding: 8px 14px; border-radius: 2px; cursor: pointer; white-space: nowrap;
}}
button.tema:hover {{ color: var(--ink); border-color: var(--ink-3); }}

/* ── Cifras ───────────────────────────────────────────── */
.cifras {{
  display: grid; gap: 1px; background: var(--line);
  grid-template-columns: repeat(auto-fit, minmax(128px, 1fr));
  border: 1px solid var(--line); margin: 28px 0;
}}
.cifra {{ background: var(--surface); padding: 16px 18px; }}
.cifra b {{
  display: block; font-family: var(--display); font-weight: 500;
  font-size: 32px; line-height: 1; font-variant-numeric: tabular-nums;
}}
.cifra span {{
  display: block; margin-top: 6px; font-family: var(--mono); font-size: 10.5px;
  letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3);
}}

/* ── Alerta de deadline ───────────────────────────────── */
.deadline {{
  border-left: 3px solid var(--alerta); background: var(--surface);
  padding: 16px 20px; margin: 0 0 28px; box-shadow: var(--shadow);
}}
.deadline h2 {{
  font-family: var(--display); font-weight: 500; font-size: 18px;
  text-transform: uppercase; letter-spacing: .02em; margin: 0 0 6px; color: var(--alerta);
}}
.deadline p {{ margin: 0; color: var(--ink-2); font-size: 14.5px; max-width: 74ch; }}
.deadline .cuenta {{
  font-family: var(--mono); font-weight: 500; color: var(--ink);
  font-variant-numeric: tabular-nums;
}}

/* ── Precios ──────────────────────────────────────────── */
.pases {{ display: grid; gap: 14px; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-bottom: 34px; }}
.pase {{ background: var(--surface); border: 1px solid var(--line); padding: 18px 20px; box-shadow: var(--shadow); }}
.pase.principal {{ border-color: var(--accent); }}
.pase h3 {{ font-family: var(--display); font-weight: 500; font-size: 19px; margin: 0 0 2px; text-transform: uppercase; }}
.pase .fechas {{ font-family: var(--mono); font-size: 11.5px; color: var(--ink-3); margin: 0 0 12px; }}
.pase .precio {{ font-family: var(--display); font-size: 27px; font-variant-numeric: tabular-nums; line-height: 1; }}
.pase .precio small {{ font-family: var(--mono); font-size: 11px; color: var(--ink-3); display: block; margin-top: 5px; letter-spacing: .04em; }}
.pase ul {{ margin: 14px 0 0; padding-left: 16px; font-size: 13.5px; color: var(--ink-2); }}
.pase li {{ margin-bottom: 3px; }}
.etiqueta-uso {{
  display: inline-block; font-family: var(--mono); font-size: 10px; letter-spacing: .1em;
  text-transform: uppercase; padding: 3px 8px; margin-bottom: 10px;
  background: var(--surface-2); color: var(--ink-2); border: 1px solid var(--line);
}}

/* ── Filtros ──────────────────────────────────────────── */
.filtros {{
  position: sticky; top: 0; z-index: 30; background: var(--ground);
  padding: 14px 0; border-bottom: 1px solid var(--line); margin-bottom: 24px;
  display: flex; gap: 8px; flex-wrap: wrap; align-items: center;
}}
.filtros .grupo {{ display: flex; gap: 6px; flex-wrap: wrap; }}
.chip {{
  font-family: var(--mono); font-size: 11px; letter-spacing: .05em;
  background: var(--surface); border: 1px solid var(--line); color: var(--ink-2);
  padding: 6px 11px; cursor: pointer; border-radius: 2px; white-space: nowrap;
}}
.chip:hover {{ border-color: var(--ink-3); color: var(--ink); }}
.chip[aria-pressed="true"] {{ background: var(--ink); border-color: var(--ink); color: var(--ground); }}
.chip.rol-A[aria-pressed="true"] {{ background: var(--alcance); border-color: var(--alcance); color: #fff; }}
.chip.rol-B[aria-pressed="true"] {{ background: var(--conversion); border-color: var(--conversion); color: #fff; }}
.chip.rol-C[aria-pressed="true"] {{ background: var(--urgencia); border-color: var(--urgencia); color: #16181C; }}
.divisor {{ width: 1px; align-self: stretch; background: var(--line); margin: 0 4px; }}
.conteo {{ font-family: var(--mono); font-size: 11px; color: var(--ink-3); margin-left: auto; }}

/* ── Nicho ────────────────────────────────────────────── */
.nicho {{ margin-bottom: 44px; border-top: 1px solid var(--line); padding-top: 22px; }}
.nicho-cab {{ display: flex; gap: 14px; align-items: baseline; flex-wrap: wrap; margin-bottom: 4px; }}
.nicho-num {{
  font-family: var(--mono); font-size: 12px; color: var(--accent);
  font-variant-numeric: tabular-nums; padding-top: 4px;
}}
.nicho h2 {{
  font-family: var(--display); font-weight: 500; font-size: 25px; margin: 0;
  text-transform: uppercase; letter-spacing: -.005em; line-height: 1.1;
}}
.ancla {{ font-family: var(--mono); font-size: 11px; color: var(--ink-3); }}
.nicho-sub {{ margin: 0 0 18px; color: var(--ink-2); font-size: 14.5px; max-width: 74ch; }}

/* ── Micro-situación: los 7 pasos ─────────────────────── */
details.micro {{ margin-bottom: 20px; border: 1px solid var(--line-soft); background: var(--surface); }}
details.micro > summary {{
  cursor: pointer; padding: 11px 16px; font-family: var(--mono); font-size: 11px;
  letter-spacing: .1em; text-transform: uppercase; color: var(--ink-2); list-style: none;
}}
details.micro > summary::-webkit-details-marker {{ display: none; }}
details.micro > summary::before {{ content: "▸ "; color: var(--accent); }}
details.micro[open] > summary::before {{ content: "▾ "; }}
.pasos {{ padding: 0 16px 16px; display: grid; gap: 1px; background: var(--line-soft); }}
.paso {{ background: var(--surface); padding: 10px 0 10px 0; display: grid; grid-template-columns: 132px 1fr; gap: 14px; align-items: start; }}
.paso dt {{
  font-family: var(--mono); font-size: 10px; letter-spacing: .09em; text-transform: uppercase;
  color: var(--ink-3); padding-top: 3px;
}}
.paso dd {{ margin: 0; font-size: 14px; color: var(--ink); }}

/* ── Guiones ──────────────────────────────────────────── */
.guiones {{ display: grid; gap: 14px; }}
.guion {{ border: 1px solid var(--line); background: var(--surface); box-shadow: var(--shadow); }}
.guion.A {{ border-left: 3px solid var(--alcance); }}
.guion.B {{ border-left: 3px solid var(--conversion); }}
.guion.C {{ border-left: 3px solid var(--urgencia); }}
.guion-cab {{ padding: 14px 18px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
.variante {{
  font-family: var(--display); font-size: 21px; font-weight: 600; line-height: 1;
  width: 27px; text-align: center;
}}
.guion.A .variante {{ color: var(--alcance); }}
.guion.B .variante {{ color: var(--conversion); }}
.guion.C .variante {{ color: var(--urgencia); }}
.papel {{ font-weight: 600; font-size: 14.5px; }}
.meta-guion {{ display: flex; gap: 6px; flex-wrap: wrap; margin-left: auto; }}
.tag {{
  font-family: var(--mono); font-size: 10px; letter-spacing: .06em;
  padding: 3px 8px; border: 1px solid var(--line); color: var(--ink-2);
  white-space: nowrap; background: var(--surface-2);
}}
.tag.estilo {{ border-color: var(--accent); color: var(--accent); background: transparent; }}
.tag.dur {{ font-variant-numeric: tabular-nums; }}
.guion-cuerpo {{ padding: 0 18px 18px; }}
.nota-rol {{ font-size: 13px; color: var(--ink-3); margin: 0 0 14px; }}

.hook {{ background: var(--surface-2); padding: 13px 15px; margin-bottom: 16px; border-left: 2px solid var(--ink-3); }}
.hook .label {{ font-family: var(--mono); font-size: 9.5px; letter-spacing: .11em; text-transform: uppercase; color: var(--ink-3); display: block; margin-bottom: 5px; }}
.hook p {{ margin: 0; font-size: 16px; font-weight: 500; }}
.hook .gatillos {{ font-family: var(--mono); font-size: 10.5px; color: var(--ink-3); margin-top: 7px; }}

/* ── Timeline de clips ────────────────────────────────── */
.timeline {{ display: grid; gap: 1px; background: var(--line-soft); border: 1px solid var(--line-soft); }}
.clip {{ background: var(--surface); display: grid; grid-template-columns: 62px 116px 1fr 190px; gap: 12px; padding: 8px 12px; align-items: start; }}
.clip:hover {{ background: var(--surface-2); }}
.tc {{ font-family: var(--mono); font-size: 11px; color: var(--ink-3); font-variant-numeric: tabular-nums; padding-top: 2px; }}
.beat {{ font-family: var(--mono); font-size: 10px; letter-spacing: .06em; text-transform: uppercase; color: var(--ink-2); padding-top: 3px; }}
.voz {{ font-size: 14px; }}
.overlay {{
  font-family: var(--display); font-size: 12.5px; letter-spacing: .04em; text-transform: uppercase;
  color: var(--accent); text-align: right; padding-top: 2px;
}}
@media (max-width: 720px) {{
  .clip {{ grid-template-columns: 56px 1fr; }}
  .beat {{ grid-column: 2; }}
  .voz, .overlay {{ grid-column: 2; text-align: left; }}
}}

.aviso-datos {{
  margin-top: 12px; padding: 10px 14px; border-left: 2px solid var(--alerta);
  background: var(--surface); font-size: 13px; color: var(--ink-2);
}}
.aviso-datos b {{ color: var(--alerta); font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase; display: block; margin-bottom: 4px; }}

footer {{ margin-top: 60px; padding-top: 22px; border-top: 1px solid var(--line); color: var(--ink-3); font-size: 13px; }}
footer p {{ max-width: 74ch; }}
code {{ font-family: var(--mono); font-size: .88em; background: var(--surface-2); padding: 1px 5px; }}

@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; transition: none !important; }} }}
:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
</style>

<div class="wrap">
<header>
  <div class="topbar">
    <div>
      <p class="eyebrow">Feria Effix 2026 · Parrilla de producción</p>
      <h1>Diez nichos,<br>treinta guiones</h1>
      <p class="lede">
        Estructura completa antes de generar un solo clip. Cada nicho es un tipo
        de persona que compraría entrada — un contador, un importador, un
        laboratorio — con la micro-situación en la que su problema se vuelve real.
        Tres guiones por nicho, cada uno con otro gancho, otro formato y otro
        punto del embudo.
      </p>
    </div>
    <button class="tema" onclick="alternarTema()">Modo claro</button>
  </div>

  <div class="cifras">
    <div class="cifra"><b>10</b><span>Nichos</span></div>
    <div class="cifra"><b>30</b><span>Guiones</span></div>
    <div class="cifra"><b>14</b><span>Formatos</span></div>
    <div class="cifra"><b>{datos['total_clips']}</b><span>Clips de 4s</span></div>
    <div class="cifra"><b>{minutos}:{segundos_resto:02d}</b><span>Minutos de video</span></div>
    <div class="cifra"><b>60<small style="font-size:14px">s</small></b><span>Por video</span></div>
  </div>
</header>

<section class="deadline">
  <h2>El taller de IA es el 3 de septiembre</h2>
  <p>
    Está incluido en los dos pases y ocurre <strong>antes</strong> del evento. Quien compre
    después pierde un beneficio que ya venía pagado. Es la escasez más fuerte del embudo y es
    verificable: <span class="cuenta">faltan {dias_taller} días</span>, contra los
    <span class="cuenta">{dias_evento}</span> que faltan para octubre.
    Los diez guiones <strong>C</strong> la usan como CTA — y caducan ese día.
  </p>
</section>

<div class="pases">
  <div class="pase principal">
    <span class="etiqueta-uso">Foco de los 30 guiones</span>
    <h3>Pasaporte 3 días</h3>
    <p class="fechas">Viernes 16 · sábado 17 · domingo 18 de octubre</p>
    <div class="precio">$201.300 <small>COP · IVA incluido</small></div>
    <ul>
      <li>+350 empresas y marcas</li>
      <li>+200 conferencias, paneles y talleres</li>
      <li>+200 ponentes nacionales e internacionales</li>
      <li>Taller Master Claude de IA, 4 horas</li>
    </ul>
  </div>
  <div class="pase">
    <span class="etiqueta-uso">Upsell · gatillo de ego</span>
    <h3>Entrada VIP</h3>
    <p class="fechas">Jueves 15 al lunes 19 de octubre</p>
    <div class="precio">$1.155.000 <small>COP · IVA incluido</small></div>
    <ul>
      <li>Escarapela VIP · entrada y salida ilimitada</li>
      <li>Ingreso sin filas</li>
      <li>Inauguración privada 15 · clausura 19</li>
      <li>Zona VIP y áreas reservadas</li>
    </ul>
  </div>
  <div class="pase">
    <span class="etiqueta-uso">Escasez real · 400 cupos</span>
    <h3>Entrada Black</h3>
    <p class="fechas">5 días + experiencia premium · 400 cupos en el mundo</p>
    <div class="precio">$3.997.000 <small>COP · IVA incluido — 4 cuotas o pago único</small></div>
    <ul>
      <li>Todo lo del VIP</li>
      <li>9 mentorías con ponentes premium</li>
      <li>Desayuno, almuerzo y cena 3 días</li>
      <li>Línea Black dedicada todo el año</li>
    </ul>
  </div>
</div>

<section class="deadline" style="border-left-color: var(--accent)">
  <h2 style="color: var(--accent)">Sin descuentos, cinco gatillos</h2>
  <p>
    Ningún guión ofrece rebajas ni códigos. El precio se defiende con lo que incluye.
    Lo que sí usan: <strong>escasez</strong> (400 cupos Black, pasa una vez al año),
    <strong>inclusión</strong> (quien va una vez, vuelve), <strong>ego</strong> (escarapela,
    zona exclusiva), <strong>aprendizaje</strong> (+200 conferencias, Master Claude) y
    <strong>dejar de ganar</strong> (la competencia sí está creciendo).
  </p>
</section>

<div class="filtros">
  <div class="grupo" id="filtro-rol"></div>
  <div class="divisor"></div>
  <div class="grupo" id="filtro-estilo"></div>
  <div class="divisor"></div>
  <button class="chip" onclick="limpiar()">Ver todo</button>
  <span class="conteo" id="conteo"></span>
</div>

<main id="lista"></main>

<footer>
  <p>
    Cada guión dura 60 segundos con corte de escena cada 4 — el techo del pico de alcance
    de Reels. Los beats de momento, causa raíz y mecanismo ocupan dos clips para que
    respiren; los otros nueve, uno. La narración va a 2,2 palabras por segundo; el número final de clips
    se recalcula con <code>planificar_desde_audio()</code> cuando la voz de ElevenLabs esté
    generada y medida con ffprobe. Ningún guión se produce hasta que su storyboard esté aprobado.
  </p>
</footer>
</div>

<script type="application/json" id="datos">{payload}</script>
<script>
const D = JSON.parse(document.getElementById('datos').textContent);
const ESTILOS = {json.dumps(ESTILOS_LEGIBLES, ensure_ascii=False)};
const NIVELES = {json.dumps(NIVELES_LEGIBLES, ensure_ascii=False)};
const PASOS = [
  ['momento', '1 · Momento'], ['sintoma', '2 · Síntoma'],
  ['reaccion_interna', '3 · Reacción interna'], ['explicacion_fallida', '4 · Explicación fallida'],
  ['patron', '5 · Patrón'], ['causa_raiz', '6 · Causa raíz'], ['mecanismo', '7 · Mecanismo'],
];
let fRol = null, fEstilo = null;

function esc(s) {{
  return String(s).replace(/[&<>"]/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}})[c]);
}}
function alternarTema() {{
  const r = document.documentElement;
  const claro = r.getAttribute('data-theme') === 'light';
  r.setAttribute('data-theme', claro ? 'dark' : 'light');
  document.querySelector('.tema').textContent = claro ? 'Modo claro' : 'Modo oscuro';
}}

const roles = [['A','Alcance'],['B','Conversión'],['C','Urgencia']];
document.getElementById('filtro-rol').innerHTML = roles.map(([k,v]) =>
  `<button class="chip rol-${{k}}" data-rol="${{k}}" aria-pressed="false" onclick="togRol('${{k}}')">${{k}} · ${{v}}</button>`
).join('');

const estilosUsados = [...new Set(D.nichos.flatMap(n => n.guiones.map(g => g.estilo)))].sort();
document.getElementById('filtro-estilo').innerHTML = estilosUsados.map(s =>
  `<button class="chip" data-estilo="${{s}}" aria-pressed="false" onclick="togEstilo('${{s}}')">${{ESTILOS[s] || s}}</button>`
).join('');

function togRol(k) {{ fRol = fRol === k ? null : k; sincronizar(); }}
function togEstilo(s) {{ fEstilo = fEstilo === s ? null : s; sincronizar(); }}
function limpiar() {{ fRol = null; fEstilo = null; sincronizar(); }}

function sincronizar() {{
  document.querySelectorAll('.chip[data-rol]').forEach(c =>
    c.setAttribute('aria-pressed', c.dataset.rol === fRol));
  document.querySelectorAll('.chip[data-estilo]').forEach(c =>
    c.setAttribute('aria-pressed', c.dataset.estilo === fEstilo));
  pintar();
}}

function tarjetaGuion(g) {{
  const clips = g.linea_tiempo.map(c => `
      <div class="clip">
        <span class="tc">${{c.t_inicio_s}}–${{c.t_fin_s}}s</span>
        <span class="beat">${{esc(c.nombre)}}</span>
        <span class="voz">${{c.lleva_narracion ? esc(c.narracion) : '<em style="opacity:.45">↳ continúa el beat</em>'}}</span>
        <span class="overlay">${{esc(c.texto_pantalla)}}</span>
      </div>`).join('');

  return `
    <article class="guion ${{g.variante}}">
      <div class="guion-cab">
        <span class="variante">${{g.variante}}</span>
        <span class="papel">${{esc(g.papel)}}</span>
        <div class="meta-guion">
          <span class="tag estilo">${{ESTILOS[g.estilo] || g.estilo}}</span>
          <span class="tag">${{esc(g.nivel)}} · ${{esc(NIVELES[g.nivel] || '')}}</span>
          <span class="tag">${{esc(g.gatillo_rol)}}</span>
          <span class="tag dur">${{g.total_clips}} clips · ${{g.duracion_s}}s</span>
        </div>
      </div>
      <div class="guion-cuerpo">
        <p class="nota-rol">${{esc(g.nota_rol)}}</p>
        <div class="hook">
          <span class="label">Gancho ${{g.hook_variante}} · CTA: ${{esc(g.cta.overlay)}}</span>
          <p>${{esc(g.linea_tiempo[0].narracion)}}</p>
          <div class="gatillos">${{esc(g.cta.hablado)}}</div>
        </div>
        <div class="timeline">${{clips}}</div>
      </div>
    </article>`;
}}

function pintar() {{
  let visibles = 0;
  const html = D.nichos.map((n, i) => {{
    const guiones = n.guiones.filter(g =>
      (!fRol || g.variante === fRol) && (!fEstilo || g.estilo === fEstilo));
    if (!guiones.length) return '';
    visibles += guiones.length;

    const pasos = PASOS.map(([k, etiqueta]) =>
      `<div class="paso"><dt>${{etiqueta}}</dt><dd>${{esc(n.micro_situacion[k])}}</dd></div>`).join('');

    const aviso = '';

    return `
      <section class="nicho">
        <div class="nicho-cab">
          <span class="nicho-num">${{String(i + 1).padStart(2, '0')}}</span>
          <h2>${{esc(n.etiqueta)}}</h2>
          <span class="ancla">${{esc(n.audiencia)}}</span>
        </div>
        <p class="nicho-sub">${{esc(n.micro_situacion.momento)}}</p>
        <details class="micro">
          <summary>Micro-situación completa — los 7 pasos</summary>
          <dl class="pasos">${{pasos}}</dl>
        </details>
        <div class="guiones">${{guiones.map(tarjetaGuion).join('')}}</div>
        ${{aviso}}
      </section>`;
  }}).join('');

  document.getElementById('lista').innerHTML = html;
  document.getElementById('conteo').textContent = `${{visibles}} de 30 guiones`;
}}

pintar();
</script>
"""


def main() -> int:
    if not ENTRADA.exists():
        print(f"❌ Falta {ENTRADA}. Corré primero la construcción de la parrilla.")
        return 1

    SALIDA.parent.mkdir(parents=True, exist_ok=True)
    SALIDA.write_text(construir(), encoding="utf-8")
    kb = SALIDA.stat().st_size // 1024
    print(f"✅ {SALIDA.relative_to(RAIZ)} · {kb} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
