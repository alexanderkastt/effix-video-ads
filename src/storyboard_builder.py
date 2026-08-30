"""Storyboard — HTML para revisión humana y JSON para el pipeline.

El HTML es autónomo: CSS embebido, cero peticiones a internet, se abre con doble
clic. El botón "Aprobar guión" descarga el JSON aprobado desde el navegador.

⚠️ Los colores salen de `config/brand.json`, que hoy declara rojo y dorado. La
paleta real de Feria Effix es blanco y negro estricto según
`referencias/esteticas/BRANDING-EFFIX.md` (extraída del DOM del sitio). Mientras
ese conflicto no se resuelva, el storyboard se ve con la paleta de brand.json —
que es la que el equipo dijo usar — pero no es la identidad verificada.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from .paths import GUIONES_DIR, STORYBOARDS_DIR, ensure_dirs, load_brand_tokens

PALETA_FALLBACK = {
    "primario": "#E31B23",
    "secundario": "#1A1A2E",
    "acento": "#FFD700",
    "texto": "#FFFFFF",
}


def _slug(texto: str, largo: int = 40) -> str:
    normal = unicodedata.normalize("NFKD", texto)
    sin_tildes = "".join(c for c in normal if not unicodedata.combining(c))
    limpio = re.sub(r"[^a-zA-Z0-9]+", "-", sin_tildes).strip("-").lower()
    return (limpio[:largo].rstrip("-")) or "video"


def _timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


class StoryboardBuilder:
    """Genera el storyboard visual y el JSON que consume el pipeline."""

    def __init__(self, marca: str = "effix") -> None:
        self.marca = marca
        tokens = load_brand_tokens(marca)
        self.colores = {**PALETA_FALLBACK, **tokens.get("colores", {})}
        self.hashtags = tokens.get("hashtags", [])
        ensure_dirs()

    # -- HTML ---------------------------------------------------------------

    def generate_html(
        self, script_json: dict[str, Any], musica: dict[str, Any] | None = None
    ) -> Path:
        """Escribe el storyboard HTML y devuelve su ruta."""
        slug = _slug(script_json.get("concepto", "video"))
        ruta = STORYBOARDS_DIR / f"storyboard_{slug}_{_timestamp()}.html"

        beats_html = "\n".join(self._tarjeta(b) for b in script_json["beats"])
        aprobado = self._payload_aprobado(script_json, musica)

        ruta.write_text(
            self._documento(script_json, beats_html, musica, aprobado),
            encoding="utf-8",
        )
        return ruta

    def _tarjeta(self, beat: dict[str, Any]) -> str:
        e = html.escape
        dur = beat.get("duracion_s", 4)
        prompt = e(beat.get("prompt_video", "") or "(sin prompt de video)")
        notas = e(beat.get("notas_produccion", "") or "—")

        return f"""
    <article class="beat">
      <header class="beat-head">
        <span class="num">{beat['beat']:02d}</span>
        <span class="nombre">{e(beat['nombre'])}</span>
        <span class="emoji" title="{e(beat.get('emocion', ''))}">{beat.get('emoji', '')}</span>
        <span class="badge">{e(beat.get('movimiento_camara', ''))}</span>
      </header>

      <div class="tiempo"><span style="width:100%"></span><em>{dur}s</em></div>

      <p class="label">Narración (ElevenLabs)</p>
      <p class="narracion">{e(beat.get('narracion', ''))}</p>

      <p class="label">Texto en pantalla</p>
      <p class="overlay">{e(beat.get('texto_pantalla', ''))}</p>

      <p class="label">Visual</p>
      <p class="visual">{e(beat.get('descripcion_visual', ''))}</p>

      <details>
        <summary>Prompt de video ({beat.get('palabras_prompt', 0)} palabras)</summary>
        <pre>{prompt}</pre>
      </details>

      <p class="notas">{notas}</p>
    </article>"""

    def _documento(
        self,
        script: dict[str, Any],
        beats_html: str,
        musica: dict[str, Any] | None,
        aprobado: dict[str, Any],
    ) -> str:
        e = html.escape
        c = self.colores
        payload = json.dumps(aprobado, ensure_ascii=False, indent=2)
        # Se inyecta como JSON dentro de un <script type="application/json">;
        # hay que romper cualquier </script> literal que venga en el contenido.
        payload_seguro = payload.replace("</", "<\\/")

        musica_html = ""
        if musica:
            musica_html = f"""
    <section class="musica">
      <h2>🎵 Brief de música</h2>
      <p><strong>Modo:</strong> {e(str(musica.get('modo', '')))}</p>
      <p><strong>Prompt Suno:</strong> {e(str(musica.get('suno_prompt', musica.get('suno_title', ''))))}</p>
      <p><strong>Tags:</strong> {e(', '.join(musica.get('suno_style_tags', [])))}</p>
      <p><strong>BPM:</strong> {e(str(musica.get('bpm_recomendado', '')))} ·
         <strong>Volumen:</strong> {int(float(musica.get('volumen_relativo', 0.25)) * 100)}%</p>
    </section>"""

        hooks_html = "".join(
            f"<li><b>{h['variante']}</b> — {e(h['texto'])} "
            f"<span class='mini'>({h['palabras']} palabras · {', '.join(h['gatillos'])})</span></li>"
            for h in script.get("hooks_alternativos", [])
        )

        return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Storyboard — {e(script.get('concepto', ''))}</title>
<style>
  :root {{
    --primario: {c['primario']};
    --secundario: {c['secundario']};
    --acento: {c['acento']};
    --texto: {c['texto']};
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 32px 20px 80px;
    background: var(--secundario); color: var(--texto);
    font: 15px/1.55 -apple-system, "Segoe UI", Roboto, sans-serif;
  }}
  .wrap {{ max-width: 1180px; margin: 0 auto; }}
  h1 {{ font-size: 26px; margin: 0 0 6px; }}
  .meta {{ opacity: .75; font-size: 13px; margin-bottom: 22px; }}
  .meta b {{ color: var(--acento); }}
  section.info, section.musica {{
    background: rgba(255,255,255,.05); border-left: 3px solid var(--acento);
    padding: 14px 18px; border-radius: 8px; margin-bottom: 22px;
  }}
  section h2 {{ font-size: 15px; margin: 0 0 8px; text-transform: uppercase; letter-spacing: .06em; }}
  ul {{ margin: 6px 0 0; padding-left: 20px; }}
  .mini {{ opacity: .6; font-size: 12px; }}
  .grid {{ display: grid; gap: 16px; grid-template-columns: repeat(auto-fill, minmax(330px, 1fr)); }}
  .beat {{
    background: rgba(255,255,255,.04); border: 1px solid rgba(255,255,255,.1);
    border-radius: 12px; padding: 16px;
  }}
  .beat-head {{ display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }}
  .num {{
    background: var(--primario); color: #fff; font-weight: 700;
    padding: 3px 9px; border-radius: 6px; font-size: 13px;
  }}
  .nombre {{ font-weight: 700; letter-spacing: .04em; font-size: 13px; }}
  .emoji {{ font-size: 18px; }}
  .badge {{
    margin-left: auto; font-size: 11px; opacity: .7;
    border: 1px solid rgba(255,255,255,.25); padding: 2px 7px; border-radius: 20px;
  }}
  .tiempo {{ display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }}
  .tiempo span {{ height: 4px; background: var(--acento); border-radius: 2px; display: block; }}
  .tiempo em {{ font-size: 11px; opacity: .65; font-style: normal; }}
  .label {{
    font-size: 10px; text-transform: uppercase; letter-spacing: .09em;
    opacity: .5; margin: 12px 0 3px;
  }}
  .narracion {{ margin: 0; font-size: 15px; }}
  .overlay {{
    margin: 0; font-weight: 700; color: var(--acento); text-transform: uppercase;
    font-size: 13px; letter-spacing: .03em;
  }}
  .visual {{ margin: 0; font-size: 13px; opacity: .8; }}
  details {{ margin-top: 12px; }}
  summary {{ cursor: pointer; font-size: 12px; opacity: .7; }}
  pre {{
    white-space: pre-wrap; font-size: 11.5px; line-height: 1.5;
    background: rgba(0,0,0,.35); padding: 10px; border-radius: 6px; margin: 8px 0 0;
  }}
  .notas {{ font-size: 11px; opacity: .5; margin: 10px 0 0; }}
  .aprobar {{ text-align: center; margin-top: 36px; }}
  button {{
    background: var(--primario); color: #fff; border: 0; cursor: pointer;
    padding: 14px 30px; border-radius: 8px; font-size: 15px; font-weight: 700;
  }}
  button:hover {{ filter: brightness(1.12); }}
  #ok {{ margin-top: 12px; font-size: 13px; color: var(--acento); }}
</style>
</head>
<body>
<div class="wrap">
  <h1>{e(script.get('concepto', ''))}</h1>
  <p class="meta">
    Estilo <b>{e(script.get('estilo', ''))}</b> ·
    Ángulo <b>{e(script.get('angulo_etiqueta', ''))}</b> ·
    {len(script.get('beats', []))} beats ·
    <b>{script.get('duracion_total_s', 0)}s</b> ·
    generado {e(script.get('generado_en', ''))}
  </p>

  <section class="info">
    <h2>Hooks alternativos (elegido: {e(script.get('hook_elegido', 'A'))})</h2>
    <ul>{hooks_html}</ul>
  </section>
{musica_html}
  <div class="grid">
{beats_html}
  </div>

  <div class="aprobar">
    <button id="btn">✅ Aprobar guión</button>
    <p id="ok"></p>
  </div>
</div>

<script type="application/json" id="payload">{payload_seguro}</script>
<script>
  document.getElementById('btn').addEventListener('click', function () {{
    var datos = JSON.parse(document.getElementById('payload').textContent);
    datos.estado = 'aprobado';
    datos.aprobado_en = new Date().toISOString();
    var blob = new Blob([JSON.stringify(datos, null, 2)], {{ type: 'application/json' }});
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'storyboard_aprobado.json';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    document.getElementById('ok').textContent =
      'Descargado storyboard_aprobado.json — muévelo a scripts/guiones/ para producir.';
  }});
</script>
</body>
</html>
"""

    # -- JSON ---------------------------------------------------------------

    def _payload_aprobado(
        self, script: dict[str, Any], musica: dict[str, Any] | None
    ) -> dict[str, Any]:
        return {
            "job_id": script.get("job_id") or str(uuid.uuid4()),
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "concepto": script.get("concepto", ""),
            "estilo": script.get("estilo", ""),
            "marca": self.marca,
            "angulo": script.get("angulo", ""),
            "estado": "pendiente_aprobacion",
            "beats": script.get("beats", []),
            "musica": musica or {},
            "costo_estimado_usd": script.get("costo_estimado_usd", 0.0),
            "duracion_total_s": script.get("duracion_total_s", 0),
            "modelo_fal": script.get("modelo_fal", ""),
            "fps": script.get("fps", 24),
            "hashtags": self.hashtags,
        }

    def save_json(
        self,
        script_json: dict[str, Any],
        musica: dict[str, Any] | None = None,
        estado: str = "aprobado",
    ) -> Path:
        """Guarda el JSON que consume el pipeline y devuelve su ruta."""
        payload = self._payload_aprobado(script_json, musica)
        payload["estado"] = estado

        slug = _slug(script_json.get("concepto", "video"), largo=24)
        estilo = _slug(script_json.get("estilo", "estilo"), largo=16)
        ruta = GUIONES_DIR / f"{self.marca}_{estilo}_{slug}_{_timestamp()}_{estado}.json"

        ruta.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        return ruta
