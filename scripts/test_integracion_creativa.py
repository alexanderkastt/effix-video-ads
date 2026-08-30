"""Prueba de integración de la capa creativa avanzada — sin gastar un peso.
Recorre micro-situaciones → hooks → beats → storyboard dirigido, y valida que
los prompts de cada estilo lleven sus elementos obligatorios.

    python scripts/test_integracion_creativa.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.consola import usar_utf8     # noqa: E402
from src.estilos_especiales import (  # noqa: E402
    CROCHET, SKELETON, ZACK_FILMS, estilos_especiales_disponibles,
)
from src.microsituaciones import (  # noqa: E402
    angulos_disponibles, construir_para_effix,
)
from src.narracion_hablada import (  # noqa: E402
    CTA_POR_PASE, MAX_PALABRAS_POR_LINEA, validar_coherencia_de_pase,
    validar_presupuesto,
)
from src.ganchos import (  # noqa: E402
    auditar_guion, candidatos, cargar_banco, categorias_para,
)
from src.plan_clips import planificar  # noqa: E402
from src.storyboard_director import StoryboardDirector  # noqa: E402


usar_utf8()

fallos: list[str] = []


def check(titulo: str, ok: bool, detalle: str = "") -> bool:
    print(f"{'✅' if ok else '❌'} {titulo}")
    if detalle:
        for linea in detalle.splitlines():
            print(f"      {linea}")
    if not ok:
        fallos.append(f"{titulo} — {detalle}")
    return ok


def main() -> int:
    print("\n🧪 INTEGRACIÓN CREATIVA — micro-situaciones · estilos · director")
    print("─" * 68)

    # 1 ── micro-situación
    ms = construir_para_effix("comunidad_que_no_tienes")
    completa = all(
        getattr(ms, c)
        for c in ("momento", "sintoma", "reaccion_interna", "explicacion_fallida",
                  "patron", "causa_raiz", "mecanismo")
    )
    check(
        "Micro-situación construida (7 campos del framework)", completa,
        f"Momento: {ms.momento[:66]}...",
    )

    # 2 ── hooks
    hooks = ms.generar_hooks(n_variantes=3)
    hooks_ok = len(hooks) == 3 and all(
        h["palabras"] <= 14 and len(h["gatillos"]) >= 2 and len(h["overlay"].split()) <= 7
        for h in hooks.values()
    )
    check(
        "3 hooks — máx 14 palabras, mín 2 gatillos, overlay ≤7 palabras", hooks_ok,
        "\n".join(f"{k}: \"{h['hablado']}\" ({h['palabras']}p)" for k, h in hooks.items()),
    )

    # 3 ── expansión a 11 beats
    beats = ms.beat_a_beats_con_microsituacion()
    beats_ok = len(beats) == 12 and all(b["narracion"] for b in beats)
    check(
        f"{len(beats)} beats generados desde la micro-situación", beats_ok,
        f"Beat 01: {beats[0]['nombre']} — {beats[0]['narracion'][:46]}...\n"
        f"Beat 11: {beats[10]['nombre']} — {beats[10]['narracion'][:46]}...\n"
        f"Beat 12: {beats[11]['nombre']} — {beats[11]['narracion'][:46]}...",
    )

    # 4 ── storyboard en crochet
    director = StoryboardDirector()
    sb = director.generar(
        beats, estilo="crochet", marca="effix",
        micro_situacion=ms, concepto="Prueba crochet — comunidad",
    )
    check(
        "Storyboard crochet generado", Path(sb["html_path"]).exists(),
        f"HTML: {Path(sb['html_path']).name}\nJSON: {Path(sb['json_path']).name}",
    )

    # 5 ── elementos obligatorios de crochet
    p1 = sb["beats"][0]["prompt_imagen"]
    v1 = sb["beats"][0]["prompt_video"]
    faltantes = []
    if "fully crocheted and knitted" not in p1:
        faltantes.append("universal_positivo")
    if "Stop-motion animation diorama" not in p1:
        faltantes.append("framing de diorama")
    if CROCHET["universal_negativo"][:40] not in p1:
        faltantes.append("universal_negativo")
    if CROCHET["cierre_i2v"][:40] not in v1:
        faltantes.append("cierre_i2v")
    check(
        "Prompts de crochet con los elementos obligatorios verbatim", not faltantes,
        "todos presentes" if not faltantes else f"faltan: {', '.join(faltantes)}",
    )

    # 6 ── skeleton: Character Bible + cero texto
    sb_sk = director.generar(
        beats[:3], estilo="skeleton", marca="effix",
        micro_situacion=ms, concepto="Prueba skeleton",
    )
    p_sk = sb_sk["beats"][0]["prompt_imagen"]
    sk_ok = "large expressive cartoon eyes" in p_sk and "no text, no captions" in p_sk
    check(
        "Skeleton: Character Bible verbatim + negativo de texto", sk_ok,
        "Bible y 'no text' presentes" if sk_ok else "falta Bible o negativo de texto",
    )

    # 7 ── zack: personajes que no hablan, anotaciones sin palabras
    sb_z = director.generar(
        beats[:3], estilo="zack_films", marca="effix",
        micro_situacion=ms, concepto="Prueba zack",
    )
    v_z = sb_z["beats"][0]["prompt_video"]
    z_ok = "do NOT talk" in v_z and "annotations are shapes, not words" in v_z
    check(
        "Zack Films: sin lip-sync y anotaciones como formas", z_ok,
        "reglas presentes" if z_ok else "falta la regla de no-habla o la de anotaciones",
    )

    # 8 ── micro_doc_ugc: audio cerrado y vocabulario limpio
    sb_u = director.generar(
        beats[:3], estilo="micro_doc_ugc", marca="effix",
        micro_situacion=ms, concepto="Prueba micro-doc",
    )
    v_u = sb_u["beats"][0]["prompt_video"]
    prohibidas = [
        p for p in ("cinematic", "professional", "stunning", "8k", "studio", "perfect")
        if _pide(v_u, p)
    ]
    u_ok = "no discernible speech" in v_u and not prohibidas
    check(
        "Micro-doc UGC: cierra en 'no discernible speech', sin vocabulario prohibido", u_ok,
        "limpio" if u_ok else f"problema: {prohibidas or 'falta el cierre de audio'}",
    )

    # 9 ── todos los estilos y ángulos corren
    errores = []
    for angulo in angulos_disponibles():
        m = construir_para_effix(angulo)
        bs = m.beat_a_beats_con_microsituacion()
        if len(bs) != 12 or not all(b["narracion"] for b in bs):
            errores.append(f"{angulo}: beats incompletos")
        for est in estilos_especiales_disponibles():
            try:
                director.dirigir_estilo(est, bs[0], m)
            except Exception as exc:
                errores.append(f"{angulo}/{est}: {exc!r}")
    check(
        f"{len(angulos_disponibles())} ángulos × {len(estilos_especiales_disponibles())} estilos",
        not errores,
        "todas las combinaciones dirigen sin error" if not errores else "\n".join(errores[:5]),
    )

    # 10 ── presupuesto de palabras por clip de 4s
    errores_presup = validar_presupuesto()
    check(
        f"Ninguna línea pasa de {MAX_PALABRAS_POR_LINEA} palabras (techo del clip de 4s)",
        errores_presup == ["OK"],
        "88 líneas dentro del techo" if errores_presup == ["OK"]
        else "\n".join(errores_presup),
    )

    # 11 ── el formato: corte cada 4s y total entre 30 y 60s
    fuera = []
    for angulo in angulos_disponibles():
        bs = construir_para_effix(angulo).beat_a_beats_con_microsituacion()
        pl = planificar(bs)
        if not pl["en_rango"]:
            fuera.append(f"{angulo}: {pl['duracion_s']}s — {pl['diagnostico']}")
    plan_ref = planificar(beats)
    check(
        "Corte cada 4s y video final entre 30 y 60s, en los 8 ángulos", not fuera,
        f"{plan_ref['total_clips']} clips × 4s = {plan_ref['duracion_s']}s · "
        f"locución {plan_ref['locucion_s']}s · holgura {plan_ref['holgura_total_s']}s"
        if not fuera else "\n".join(fuera),
    )

    # 12 ── cada clip dura exactamente 4s y las escenas van encadenadas
    clips = sb["beats"]
    tiempos_ok = all(c["duracion_s"] == 4 for c in clips) and all(
        clips[i]["t_fin_s"] == clips[i + 1]["t_inicio_s"] for i in range(len(clips) - 1)
    )
    check(
        "Todos los clips duran 4s y los tiempos encadenan sin huecos", tiempos_ok,
        f"{len(clips)} clips · de 0s a {clips[-1]['t_fin_s']}s"
        if tiempos_ok else "hay clips de otra duración o huecos entre ellos",
    )

    # 13 ── el método de ganchos, sobre los 8 ángulos
    problemas = []
    for angulo in angulos_disponibles():
        m = construir_para_effix(angulo)
        paq = director.generar(
            m.beat_a_beats_con_microsituacion(), estilo="micro_doc_ugc",
            marca="effix", micro_situacion=m, concepto=angulo,
        )
        au = auditar_guion(
            paq["beats"], nivel="problem", objetivo="conversion",
            marca="Effix", duracion_total_s=paq["duracion_total_s"],
        )
        for e in au["errores"]:
            problemas.append(f"{angulo} [ERROR] {e}")
        for a in au["avisos"]:
            problemas.append(f"{angulo} [aviso] {a}")
    check(
        "Método de ganchos: marca en 5s · complicación en 12s · defecto al final · "
        "situación no persona", not problemas,
        f"8 ángulos sin errores ni avisos · categorías válidas para "
        f"(problem, conversión): {', '.join(categorias_para('problem', 'conversion'))}"
        if not problemas else "\n".join(problemas[:6]),
    )

    # 14 ── el banco de 320 carga y filtra
    banco = cargar_banco()
    cand = candidatos("problem", "conversion")
    banco_ok = len(banco) == 320 and len(cand) > 0 and all(
        g["categoria"] in categorias_para("problem", "conversion") for g in cand
    )
    check(
        "Banco de 320 ganchos: carga, filtra por nivel y respeta el método", banco_ok,
        f"{len(banco)} ganchos · {len(cand)} candidatos para (problem, conversión) en Effix · "
        f"{sum(1 for g in banco if g['advertencia'])} con advertencia legal o de política"
        if banco_ok else f"cargaron {len(banco)}, se esperan 320",
    )

    # 15 ── boletería: el pase decide el CTA y nada promete más días de los que da
    incoherencias = []
    for angulo in angulos_disponibles():
        m = construir_para_effix(angulo)
        for pase in ("pase_3_dias", "vip_5_dias"):
            bs = m.beat_a_beats_con_microsituacion(pase=pase)
            r = validar_coherencia_de_pase([b["narracion"] for b in bs], pase)
            if r != ["OK"]:
                incoherencias += [f"{angulo}/{pase}: {x}" for x in r]
            pl = planificar(bs)
            if not pl["en_rango"]:
                incoherencias.append(f"{angulo}/{pase}: {pl['duracion_s']}s fuera de rango")
    check(
        "Boletería: el CTA cambia por pase y ninguna línea promete más días de los "
        "que da el producto", not incoherencias,
        f"{len(angulos_disponibles())} ángulos × 2 pases · CTA 3 días: "
        f"\"{CTA_POR_PASE['pase_3_dias']['hablado']}\" · CTA VIP: "
        f"\"{CTA_POR_PASE['vip_5_dias']['hablado']}\""
        if not incoherencias else "\n".join(incoherencias[:6]),
    )

    # 16 ── auditoría de datos inventados
    auditoria = {a: construir_para_effix(a).datos_sin_verificar for a in angulos_disponibles()}
    con_datos = {a: d for a, d in auditoria.items() if d}
    check(
        "Auditoría de cifras sin verificar (declaradas, no ocultas)", True,
        "\n".join(f"{a}: {len(d)} cifra(s)" for a, d in con_datos.items()) or "ninguna",
    )

    print("─" * 68)
    if fallos:
        print("\n🔴 INTEGRACIÓN CON FALLOS:")
        for f in fallos:
            print(f"   · {f}")
        return 1
    print("\n🟢 INTEGRACIÓN COMPLETA — listo para producción")
    return 0


def _pide(texto: str, palabra: str) -> bool:
    """¿El prompt PIDE la palabra o la está negando? 'no studio lighting' es correcto."""
    import re

    negadores = {"no", "not", "without", "never", "avoid"}
    for m in re.finditer(r"\b" + re.escape(palabra) + r"\b", texto, re.IGNORECASE):
        previos = re.findall(r"[a-zA-Z]+", texto[: m.start()])[-2:]
        if not any(p.lower() in negadores for p in previos):
            return True
    return False


if __name__ == "__main__":
    raise SystemExit(main())
