"""Lo que la voz dice, nicho por nicho.

FLUIDEZ — por qué las líneas encadenan
    Doce frases correctas puestas una detrás de otra suenan a lista, no a
    persona. Aquí cada beat arrastra al siguiente con un conector real —"y",
    "pero", "entonces", "porque", "así que"— de modo que la locución se lee de
    corrido aunque el corte visual caiga cada cuatro segundos.

    El montaje y la voz van en capas distintas: la imagen corta, la frase no.

PRESUPUESTO
    beats 1, 6 y 7 (momento · causa raíz · mecanismo) → 2 clips, ≤17 palabras
    los otros nueve                                    → 1 clip,  ≤8 palabras
    total: 15 clips × 4s = 60s

REGISTRO
    Tuteo colombiano, como el sitio de Effix ("Ves que otros venden", "Has
    tomado cursos"). Nada de voseo rioplatense.

SIN DESCUENTOS Y SIN EL TALLER
    Ningún guión menciona códigos, rebajas ni promociones. Y ninguno menciona
    el taller de inteligencia artificial: el dato existe en `brand_dna.json`,
    pero por decisión de Alexander no entra en los creativos.
"""

from __future__ import annotations

# Beats que ocupan dos clips: son los que llevan el peso narrativo
BEATS_CON_AIRE = (1, 6, 7)
MAX_PALABRAS_1_CLIP = 8
MAX_PALABRAS_2_CLIPS = 17
PALABRAS_POR_SEGUNDO = 2.2

# Orden: momento · síntoma · reacción · explicación fallida · patrón ·
#        causa raíz · mecanismo · prueba social · visualización ·
#        urgencia+CTA · defecto · loop
HABLADO: dict[str, list[str]] = {

    "ia": [
        "¿Cuántos posts de inteligencia artificial has visto esta semana? Tres, cuatro, y todos dicen lo mismo.",
        "Y tú ahí, copiando pedidos a mano.",
        "Con la sensación de que queda más lejos.",
        "Entonces te dices que primero ordenas el negocio.",
        "Y llevas todo el año diciendo eso.",
        "Pero el problema nunca fue la herramienta: es que nadie se ha sentado contigo a montarla.",
        "Y en la feria están las agencias que ya la aplican para vender, y te muestran cómo.",
        "Más de doscientos ponentes, en un solo lugar.",
        "Imagínate en noviembre con eso corriendo solo.",
        "Viernes a domingo. Ni pides permiso.",
        "No sales programando. Sales con algo andando.",
        "Y el próximo post ya no te duele.",
    ],

    "ecommerce": [
        "Cierras el mes, abres el panel, y el número se parece muchísimo al del mes pasado.",
        "Porque ya hiciste todo lo que sabías hacer.",
        "Y no se te ocurre qué más mover.",
        "Entonces le echas la culpa al mercado.",
        "Pero ves tiendas con tu mismo producto creciendo.",
        "Y ahí cae: no te falta tienda, te faltan conversaciones que no has tenido.",
        "Son trescientas cincuenta empresas en un recinto, entre proveedores, software, logística y agencias.",
        "Cinco ediciones. Y quien va una vez, vuelve.",
        "Imagínate cerrando noviembre con otro número.",
        "Viernes a domingo. Ni pides permiso.",
        "No resuelven tu negocio. Te dan con quién.",
        "Y el próximo cierre ya no se repite.",
    ],

    # El martes en visto vuelve cuatro veces: abre (1), se paga (2), se
    # multiplica (5) y cierra el loop (12). Es lo que produce el "ese soy yo".
    "dropshipping": [
        "Martes, tres de la tarde. El proveedor te deja en visto. Ya le cobraste a la gente.",
        "Aparece el viernes, pero la campaña ya cayó.",
        "Ahora lanzas con los dedos cruzados.",
        "Te dices que te tocó uno malo.",
        "Cuatro este año. Todos, en visto un martes.",
        "No te falló el proveedor. Lo elegiste por una foto.",
        "En Effix está con stand y muestra física. Le preguntas de frente.",
        "Trescientas cincuenta empresas en un recinto.",
        "Cierras con el producto en la mano.",
        "Viernes a domingo. Ni pides permiso.",
        "No todos sirven. Pero los ves todos.",
        "Y el próximo martes ya sabes quién contesta.",
    ],

    "contadores": [
        "Te llega un cliente que vende por internet, te muestra los números, y no manejas ese modelo.",
        "Lo atiendes igual, pero resolviendo sobre la marcha.",
        "Y sabes que vale más que tres tradicionales.",
        "Entonces dices que lo estudias en temporada baja.",
        "Y la temporada nunca baja.",
        "Pero no te falta estudiar: es que ellos no están en tu oficina, están en otro lado.",
        "Y ese lado son trescientas cincuenta empresas digitales, necesitando quién les cuadre los números.",
        "Doscientos ponentes y el ecosistema completo.",
        "Imagínate saliendo con el semestre resuelto.",
        "Viernes a domingo. Ni pides permiso.",
        "No sales con contratos. Sales con reuniones.",
        "Y el próximo cliente digital no te incomoda.",
    ],

    "abogados": [
        "Te llega una consulta de una tienda online, la lees dos veces, y no sabes cotizarla.",
        "Y no es que no sepas derecho.",
        "Es que ese modelo trae preguntas nuevas.",
        "Entonces dices que es un nicho pequeño.",
        "Pero cada año hay más tiendas y plata.",
        "Así que no es un nicho pequeño: es uno al que no has ido a mostrarte.",
        "Y son trescientas cincuenta empresas digitales en un recinto, casi ninguna con abogado propio.",
        "Cinco ediciones y el ecosistema completo.",
        "Imagínate con tres clientes que crecen cada mes.",
        "Viernes a domingo. Ni pides permiso.",
        "Vas a tener que explicar qué haces.",
        "Y la próxima consulta ya sabes cobrarla.",
    ],

    "laboratorios": [
        "Ves tu propio producto en una tienda online, a un precio que te sorprende bastante.",
        "Y esa diferencia no llega a tu cuenta.",
        "Fabricas bien y el margen es de otro.",
        "Entonces te dices que lo tuyo es producir.",
        "Y llevas años viendo quién se la queda.",
        "Pero no necesitas volverte experto en marketing: necesitas a los que ya lo son, contigo.",
        "Y ahí están todos — tráfico, contenido, logística — en el mismo recinto y al mismo tiempo.",
        "Trescientas cincuenta empresas del ecosistema.",
        "Imagínate vendiendo directo, con quien lo mueva contratado.",
        "Viernes a domingo. Ni pides permiso.",
        "Montar canal toma meses. Ahí conoces a quién.",
        "Y ese precio ya no te molesta.",
    ],

    "importadores": [
        "Llega el contenedor, entra a bodega, y todavía no sabes quién te va a rotar la mitad.",
        "Porque dependes de dos o tres de siempre.",
        "Y si uno se demora, queda plata quieta.",
        "Entonces te dices que así funciona este negocio.",
        "Y van trimestres con inventario parado.",
        "Pero no te falta producto ni te falta precio: te faltan compradores, y están todos juntos.",
        "Trescientas cincuenta empresas, y muchas comprando producto para vender por internet.",
        "Cinco ediciones, todo el ecosistema junto.",
        "Imagínate el próximo contenedor medio comprometido.",
        "Viernes a domingo. Ni pides permiso.",
        "Nadie compra ahí. Compran después, si te conocieron.",
        "Y el próximo contenedor ya tiene quién.",
    ],

    "agencias_contenido": [
        "Entregas un trabajo del que estás orgulloso, el cliente queda feliz, y ahí se acaba.",
        "Porque no sabes de dónde sale el siguiente.",
        "Tu agenda depende de que alguien te recomiende.",
        "Entonces dices que si es bueno, llegan solos.",
        "Y llevas años con el trabajo bueno.",
        "Pero el portafolio no consigue clientes: los consigue estar en la sala donde se decide.",
        "Y esa sala son trescientas cincuenta marcas juntas, todas necesitando contenido que venda.",
        "Doscientos ponentes, el ecosistema digital junto.",
        "Imagínate con el trimestre lleno antes de empezar.",
        "Viernes a domingo. Ni pides permiso.",
        "Vas a hablar con desconocidos. No hay otra.",
        "Y el siguiente ya no depende de eso.",
    ],

    "agencias_pauta": [
        "Sacas un resultado bueno de verdad en una cuenta, lo publicas, y no pasa nada.",
        "Y manejas pauta mejor que muchos.",
        "Pero igual te toca perseguir por mensaje.",
        "Entonces dices que falta publicar más seguido.",
        "Y llevas meses publicando. Cuentas de a una.",
        "Porque los que reparten los presupuestos grandes no te ven el feed: están en otro lado.",
        "Y ese lado son trescientas cincuenta empresas decidiendo con quién pautan el año que viene.",
        "Cinco ediciones, doscientos ponentes.",
        "Imagínate cerrando dos cuentas grandes de una conversación.",
        "Viernes a domingo. Ni pides permiso.",
        "Nadie firma ahí mismo. Pero te conocen.",
        "Y el próximo resultado ya tiene a quién.",
    ],

    "logistica": [
        "Tienes la flota, tienes la bodega, tienes el equipo, y la operación va a media máquina.",
        "Porque los clientes que tienes crecen despacio.",
        "Y la capacidad instalada te cuesta igual.",
        "Entonces dices que los clientes llegan solos.",
        "Pero las que crecen ya eligieron con quién.",
        "Y no se trata de esperar: se trata de estar donde ellas están decidiendo.",
        "Trescientas cincuenta empresas en un recinto, y casi todas despachan producto a diario.",
        "El ecosistema completo, cinco ediciones.",
        "Imagínate la operación a máquina completa en enero.",
        "Viernes a domingo. Ni pides permiso.",
        "Vas a competir con otros operadores ahí mismo.",
        "Y la flota deja de andar a medias.",
    ],
}


# ---------------------------------------------------------------------------
# CTA por producto — sin descuentos y sin mencionar el taller
# ---------------------------------------------------------------------------

CTA_POR_PASE: dict[str, dict[str, str]] = {
    # Producto principal. El fin de semana responde la objeción de "no puedo
    # dejar el trabajo", que es la que más frena a este avatar.
    "pase_3_dias": {
        "hablado": "Compra tu pasaporte a la Feria Effix. Clic en el enlace.",
        "overlay": "Clic en el enlace",
        "dias": "3",
        "gatillo": "inclusion",
    },
    # Mismo producto, gatillo de escasez: pasa una vez al año y se llena.
    "pase_3_dias_escasez": {
        "hablado": "Compra tu boleta antes de que se llene. Clic aquí.",
        "overlay": "Antes de que llene",
        "dias": "3",
        "gatillo": "escasez",
    },
    # VIP: se vende por estatus y acceso, nunca por duración.
    "vip_5_dias": {
        "hablado": "Compra tu boleta VIP. Da clic en el enlace.",
        "overlay": "Boleta VIP",
        "dias": "5",
        "gatillo": "ego",
    },
    # Black: escasez verificable. Cuatrocientos cupos en todo el mundo.
    "black": {
        "hablado": "Compra tu Black: son cuatrocientos cupos. Clic aquí.",
        "overlay": "Solo 400 cupos",
        "dias": "5",
        "gatillo": "escasez + ego",
    },
    # Genérico: aversión a la pérdida, sin nombrar producto.
    "generico": {
        "hablado": "Compra tu boleta para la Feria Effix. Clic en el enlace.",
        "overlay": "Clic en el enlace",
        "dias": "",
        "gatillo": "dejar_de_ganar",
    },
}

PASE_POR_DEFECTO = "pase_3_dias"

# Nada de esto puede aparecer en un creativo: no ofrecemos descuentos.
PALABRAS_DE_DESCUENTO = [
    "descuento", "rebaja", "promoción", "promocion", "oferta",
    "código", "codigo", "cupón", "cupon", "effix20", "por ciento menos",
    "ahorra", "gratis",
]

# Y tampoco se menciona el taller: es decisión de Alexander, no un olvido.
PALABRAS_DEL_TALLER = [
    "master claude", "taller de inteligencia", "taller de ia",
    "tres de septiembre", "3 de septiembre", "cuatro horas en vivo",
]


def hablado_de(nicho: str) -> list[str]:
    if nicho not in HABLADO:
        raise KeyError(f"No hay narración para '{nicho}'. Hay: {', '.join(sorted(HABLADO))}")
    return HABLADO[nicho]


def cta_de(pase: str = PASE_POR_DEFECTO) -> dict[str, str]:
    if pase not in CTA_POR_PASE:
        raise KeyError(f"Pase '{pase}' no existe. Hay: {', '.join(CTA_POR_PASE)}")
    return CTA_POR_PASE[pase]


def clips_del_beat(numero: int) -> int:
    """Cuántos clips de 4s ocupa un beat según su papel narrativo."""
    return 2 if numero in BEATS_CON_AIRE else 1


def _todas_las_lineas() -> list[tuple[str, str]]:
    fuentes: list[tuple[str, str]] = []
    for nicho, lineas in HABLADO.items():
        fuentes += [(f"{nicho} beat {i:02d}", l) for i, l in enumerate(lineas, 1)]
    for pase, cta in CTA_POR_PASE.items():
        fuentes.append((f"CTA {pase}", cta["hablado"]))
        fuentes.append((f"overlay {pase}", cta["overlay"]))
    return fuentes


def validar_presupuesto() -> list[str]:
    """Cada beat dentro de su techo de palabras."""
    errores: list[str] = []

    for nicho, lineas in HABLADO.items():
        if len(lineas) != 12:
            errores.append(f"{nicho}: {len(lineas)} líneas, se esperan 12.")
            continue
        for i, linea in enumerate(lineas, start=1):
            n = len(linea.split())
            techo = MAX_PALABRAS_2_CLIPS if i in BEATS_CON_AIRE else MAX_PALABRAS_1_CLIP
            if n > techo:
                errores.append(
                    f"{nicho} beat {i:02d}: {n} palabras "
                    f"({n / PALABRAS_POR_SEGUNDO:.1f}s) — techo {techo}."
                )

    for pase, cta in CTA_POR_PASE.items():
        if len(cta["hablado"].split()) > MAX_PALABRAS_1_CLIP:
            errores.append(f"CTA {pase}: pasa de {MAX_PALABRAS_1_CLIP} palabras.")
        if len(cta["overlay"].split()) > 7:
            errores.append(f"CTA {pase}: overlay de más de 7 palabras.")

    return errores or ["OK"]


def validar_sin_descuentos() -> list[str]:
    """No ofrecemos descuentos. Ni en las líneas, ni en los CTA, ni en overlays."""
    errores = [
        f"{donde}: contiene '{palabra}' — no ofrecemos descuentos."
        for donde, texto in _todas_las_lineas()
        for palabra in PALABRAS_DE_DESCUENTO
        if palabra in texto.lower()
    ]
    return errores or ["OK"]


def validar_sin_taller() -> list[str]:
    """El taller no se menciona en los creativos."""
    errores = [
        f"{donde}: menciona el taller ('{palabra}')."
        for donde, texto in _todas_las_lineas()
        for palabra in PALABRAS_DEL_TALLER
        if palabra in texto.lower()
    ]
    return errores or ["OK"]


def fluidez(nicho: str) -> dict[str, object]:
    """Cuántas líneas arrastran a la siguiente con un conector.

    Una línea que empieza con conector encadena; una que empieza en seco corta.
    No todas deben encadenar —el hook y el CTA abren— pero si casi ninguna lo
    hace, el guión se lee como una lista y no como alguien hablando.
    """
    conectores = (
        "y ", "pero ", "entonces ", "porque ", "así que ", "y ahí ",
        "y es que ", "y en ", "y ese ", "y esa ", "y van ", "y llevas ",
    )
    lineas = hablado_de(nicho)
    encadenan = [
        i for i, l in enumerate(lineas, 1)
        if l.lower().startswith(conectores)
    ]
    return {
        "encadenan": len(encadenan),
        "de": len(lineas),
        "beats": encadenan,
        "proporcion": round(len(encadenan) / len(lineas), 2),
    }
