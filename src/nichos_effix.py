"""Los diez nichos de Feria Effix — verticales de audiencia, no ángulos de dolor.

Cada nicho es un tipo de persona que compraría entrada, con su propia
micro-situación. Un contador y un dropshipper no comparten el momento en que el
problema se les vuelve real, así que no comparten guión.

REGISTRO
    Tuteo colombiano neutro, igual que el sitio de Effix ("Ves que otros venden",
    "Has tomado cursos", "Sabes que te faltan"). Nada de voseo rioplatense — ni
    "vos tenés" ni "comprá": suena importado y rompe la voz de la marca.

GATILLOS PERMITIDOS (sin descuentos ni ofertas, por decisión de Alexander)
    escasez        — se llena, 400 cupos Black en todo el mundo, una vez al año
    inclusion      — todo el ecosistema junto; quien va una vez, vuelve
    ego            — escarapela, zona exclusiva, mentorías, línea dedicada
    aprendizaje    — +200 conferencias, +200 ponentes, taller Master Claude
    dejar_de_ganar — cada día sin las conexiones correctas la competencia sí crece

PRESUPUESTO DE PALABRAS
    Los beats respiran: los que llevan la carga narrativa ocupan dos clips de 4s
    (hasta 17 palabras) y el resto uno (hasta 8). Comprimir todo a ocho palabras
    era lo que hacía sonar los guiones a telegrama.
"""

from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Los diez verticales
# ---------------------------------------------------------------------------

NICHOS: dict[str, dict[str, Any]] = {

    "ia": {
        "etiqueta": "Inteligencia artificial — el que sabe que se está quedando atrás",
        "audiencia": "Emprendedor digital que ve a todos hablando de IA y sigue operando a mano",
        "ancla": "inteligencia artificial",
        "gatillo_principal": "aprendizaje",
        "momento": "Abres LinkedIn y el tercer post seguido es de alguien que automatizó algo con inteligencia artificial. Cierras la app y vuelves a copiar pedidos a mano.",
        "sintoma": "No es que no entiendas la tecnología. Es que cada vez que te sientas a probarla no sabes por dónde empezar y terminas usándola para escribir textos.",
        "reaccion_interna": "Te está empezando a dar la sensación de que esto se va a poner peor: mientras más esperas, más lejos queda.",
        "explicacion_fallida": "Te dices que primero tienes que ordenar el negocio, y después sí te metes con eso.",
        "patron": "Pero llevas todo el año diciéndolo, y en ese año salieron tres herramientas que ya usa medio mercado.",
        "causa_raiz": "El problema no es la herramienta. Es que nadie te ha sentado cuatro horas a montarla contigo, desde cero, en tu negocio.",
        "mecanismo": "En la feria están las agencias de inteligencia artificial que ya la aplican para vender, y te muestran cómo lo hacen.",
        "prueba_social": "Más de doscientos ponentes. Y agencias de inteligencia artificial que ya la están aplicando para vender.",
        "visualizacion": "Imagínate en noviembre, con el proceso corriendo solo mientras tú miras otra cosa.",
        "urgencia_cta": "Viernes a domingo, del dieciséis al dieciocho de octubre.",
        "defecto_admitido": "No sales programando. Sales con una cosa funcionando.",
        "loop_rewatch": "Y el próximo post que veas ya no te va a doler.",
        "overlay_dolor": "Copiando pedidos a mano",
        "visual_clave": "una pantalla con datos copiándose a mano de una pestaña a otra",
        "visual_clave_en": "a screen where data is being copied by hand between two tabs",
        "overlays": [
            "Otro post de IA",
            "Copiando a mano",
            "Y empeora",
            "“Primero ordeno”",
            "Todo el año igual",
            "No es la herramienta",
            "Agencias que ya la aplican",
            "200 ponentes",
            "Corriendo solo",
            "3 de septiembre",
            "No sales programando",
            "Ya no te duele",
        ],
        "hooks": [
            {"hablado": "¿Cuántos posts de inteligencia artificial viste hoy?", "gatillos": ["auto_relevancia", "curiosidad"], "overlay": "El tercer post seguido"},
            {"hablado": "El problema no es la herramienta. Es que nadie te la montó.", "gatillos": ["interrupcion_patron", "curiosidad"], "overlay": "Nadie te la montó"},
            {"hablado": "Hay agencias que ya la aplican. Y están ahí.", "gatillos": ["aprendizaje", "inclusion"], "overlay": "Ya la aplican"},
        ],
    },

    "ecommerce": {
        "etiqueta": "Ecommerce con tienda propia — el que ya vende y se estancó",
        "audiencia": "Dueño de tienda online que factura pero lleva meses en el mismo número",
        "ancla": "estancado",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Cierras el mes, abres el panel, y el número se parece demasiado al del mes pasado. Y al del anterior.",
        "sintoma": "No es que la tienda esté mal. Es que hiciste todo lo que sabías hacer y ya no se te ocurre qué más mover.",
        "reaccion_interna": "Y ahí aparece la duda incómoda: si esto ya llegó a su techo, o si el techo te lo estás poniendo tú.",
        "explicacion_fallida": "Le echas la culpa al mercado, a la competencia, a que el producto ya se quemó.",
        "patron": "Pero ves otras tiendas con tu mismo producto creciendo, y esa explicación deja de servirte.",
        "causa_raiz": "Lo que te falta no está adentro de tu tienda. Está en las conversaciones a las que no has llegado.",
        "mecanismo": "Más de trescientas cincuenta empresas en un recinto: proveedores, software, logística, agencias.",
        "prueba_social": "Cinco ediciones. La gente que va una vez, vuelve. Esa es toda la prueba que hay.",
        "visualizacion": "Imagínate cerrando el mes de noviembre con un número que no habías visto.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, en Plaza Mayor.",
        "defecto_admitido": "No te van a resolver el negocio. Te van a dar con quién.",
        "loop_rewatch": "Y el próximo cierre de mes ya no se parece al anterior.",
        "overlay_dolor": "El mismo número otra vez",
        "visual_clave": "un panel de métricas plano mes tras mes",
        "visual_clave_en": "a metrics dashboard that stays flat month after month",
        "overlays": [
            "Mismo número",
            "Ya hiciste todo",
            "¿Qué más muevo?",
            "“Es el mercado”",
            "Otros sí crecen",
            "No está en tu tienda",
            "350 empresas",
            "Quien va, vuelve",
            "Otro número en nov",
            "16–18 oct",
            "Te dan con quién",
            "El cierre cambia",
        ],
        "hooks": [
            {"hablado": "¿Cerraste el mes y el número se parecía al anterior?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "El mismo número"},
            {"hablado": "Hay tiendas con tu mismo producto que sí están creciendo.", "gatillos": ["interrupcion_patron", "dejar_de_ganar"], "overlay": "Tu mismo producto"},
            {"hablado": "Lo que te falta no está adentro de tu tienda.", "gatillos": ["curiosidad", "interrupcion_patron"], "overlay": "No está en tu tienda"},
        ],
    },

    "dropshipping": {
        "etiqueta": "Dropshipping — el que depende de proveedores que le fallan",
        "audiencia": "Vendedor sin inventario propio, atado a proveedores que no responden",
        "ancla": "proveedor",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Le escribes al proveedor un martes para confirmar stock y te contesta el viernes. Ya se te cayó la campaña del fin de semana.",
        "sintoma": "Cada lanzamiento te toca hacerlo con los dedos cruzados, porque no sabes si el producto va a llegar como en la foto.",
        "reaccion_interna": "Terminas pidiendo cantidades pequeñas para no arriesgar, y así el margen nunca da.",
        "explicacion_fallida": "Te dices que te tocó uno malo, que el siguiente va a ser distinto.",
        "patron": "Pero es el cuarto proveedor del año y el ciclo es exactamente el mismo.",
        "causa_raiz": "Los estás eligiendo por foto y por WhatsApp. Nunca le has visto la cara a ninguno.",
        "mecanismo": "En la feria están con stand, con muestra física, y les preguntas de frente lo que quieras.",
        "prueba_social": "Más de trescientas cincuenta empresas: marcas, dropshipping, software y logística.",
        "visualizacion": "Imagínate cerrando con alguien después de tenerle el producto en la mano.",
        "urgencia_cta": "Dieciséis, diecisiete y dieciocho de octubre. Plaza Mayor, Medellín.",
        "defecto_admitido": "No todos los stands te van a servir. Pero los ves todos.",
        "loop_rewatch": "Y el próximo martes que escribas, ya sabes quién contesta.",
        "overlay_dolor": "Contestó el viernes",
        "visual_clave": "manos revisando producto físico en un stand de feria",
        "visual_clave_en": "hands inspecting a physical product at a trade-fair booth",
        "overlays": [
            "Contestó el viernes",
            "Se cayó la campaña",
            "Dedos cruzados",
            "“Me tocó uno malo”",
            "El cuarto del año",
            "Lo elegiste por foto",
            "Stand y muestra física",
            "350 empresas",
            "Producto en la mano",
            "16–18 oct",
            "No todos sirven",
            "Ya sabes quién",
        ],
        # Uno por categoría del método de ganchos, no tres versiones del mismo
        # dolor: el flujo de la skill pide 3-5 ganchos DISTINTOS por creativo.
        # A y B son los que sirven en conversión (nivel problem); el contrarian
        # gana alcance pero castiga confianza, por eso va de cuarto y no de hook
        # en el ad de venta — vive dentro del guión, en la causa raíz.
        "hooks": [
            {"hablado": "Martes, tres de la tarde. El proveedor te deja en visto. Ya le cobraste a la gente.",
             "categoria": "dolor_nombrado", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "En visto. Un martes."},
            {"hablado": "Vendes sin bodega y dependes de que alguien conteste el WhatsApp: treinta segundos.",
             "categoria": "callout", "gatillos": ["auto_relevancia"], "overlay": "Si vendes sin bodega"},
            {"hablado": "Cuatro proveedores este año. Los cuatro, en visto un martes.",
             "categoria": "especificidad", "gatillos": ["auto_relevancia", "dejar_de_ganar"], "overlay": "El cuarto del año"},
            {"hablado": "No te falló el proveedor. Lo elegiste por una foto.",
             "categoria": "contrarian", "gatillos": ["interrupcion_patron"], "overlay": "Lo elegiste por foto"},
            {"hablado": "Tres días en Plaza Mayor y sales con proveedor visto en persona. Sin rogarle a nadie.",
             "categoria": "promesa_con_plazo", "gatillos": ["dejar_de_ganar"], "overlay": "Sin rogarle a nadie"},
        ],
    },

    # El único pedido en noventa días, y era de la familia. El ancla vuelve
    # cuatro veces: abre (1), se multiplica pese a la pauta (5), se invierte en
    # la visualización (9) y cierra el loop (12). Territorio compartido con el
    # ad de LANA, pero otro ángulo: allá era emocional, aquí es una escalada
    # temporal en segunda persona.
    "sin_arrancar": {
        "etiqueta": "Sin arrancar — el que lo intentó todo y no ha vendido",
        "audiencia": "Emprendedor con tienda publicada y sin una sola venta a un desconocido",
        "ancla": "primera_venta",
        "gatillo_principal": "auto_relevancia",
        "momento": "Tu tienda lleva noventa días abierta y el único pedido lo hizo tu prima.",
        "sintoma": "Publicas todos los días, revisas el panel, y el contador de ventas no se mueve.",
        "reaccion_interna": "Y ya empezaste a dudar de si el problema es el producto o eres tú.",
        "explicacion_fallida": "Te dices que lo que falta es pauta, que con presupuesto sí arranca.",
        "patron": "Pusiste la pauta. Y el único pedido volvió a ser de la familia.",
        "causa_raiz": "No te falta producto ni presupuesto: te falta que alguien que ya vende te vea el negocio por dentro.",
        "mecanismo": "Trescientas cincuenta empresas y doscientos ponentes que viven de vender por internet, en un solo recinto.",
        "prueba_social": "Cinco ediciones. La gente que va una vez, vuelve.",
        "visualizacion": "Imagínate el primer pedido de alguien que no sabe tu apellido.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, en Plaza Mayor.",
        "defecto_admitido": "No sales de ahí con ventas. Sales con las conversaciones que las producen.",
        "loop_rewatch": "Y el próximo pedido ya no es de tu prima.",
        "overlay_dolor": "Un pedido. Y era tu prima",
        "visual_clave": "un panel de ventas en cero con una sola notificación",
        "visual_clave_en": "a sales dashboard at zero with a single lonely order notification",
        "overlays": [
            "Y era tu prima",
            "Publicas y nada",
            "¿Será el producto?",
            "«Me falta pauta»",
            "Pusiste pauta. Igual",
            "No es el producto",
            "350 empresas · 200 ponentes",
            "Quien va, vuelve",
            "Un pedido de un desconocido",
            "16–18 oct",
            "Sales con contactos",
            "Ya no es tu prima",
        ],
        "hooks": [
            {
                "hablado": "Tu tienda lleva noventa días abierta y el único pedido lo hizo tu prima.",
                "gatillos": ["auto_relevancia", "interrupcion_patron"],
                "overlay": "Y era tu prima",
            },
            {
                "hablado": "Noventa días de tienda abierta. Un pedido. Y era de la familia.",
                "gatillos": ["interrupcion_patron", "activacion_emocional"],
                "overlay": "Un pedido en 90 días",
            },
            {
                "hablado": "Probaste tienda, redes y pauta. Y sigues esperando al primer desconocido.",
                "gatillos": ["auto_relevancia", "dejar_de_ganar"],
                "overlay": "Falta el primer desconocido",
            },
        ],
    },

    # ------------------------------------------------------------------
    # Negocio tradicional de ropa: vende bien, pero solo a quien pasa por el
    # frente. No fracasó vendiendo online — nunca empezó. El ancla es la
    # vitrina, y vuelve seis veces a lo largo del guión.
    # ------------------------------------------------------------------
    "tienda_ropa": {
        "etiqueta": "Tienda de ropa física — el que vende por vitrina y no por internet",
        "audiencia": "Dueño de almacén de ropa con local, que vende de mostrador y WhatsApp y no tiene canal online",
        "ancla": "vitrina",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Llovió todo el sábado, no entró nadie, y ahí caes en cuenta de que tu mes depende del clima y del andén.",
        "sintoma": "Le mandas la foto por WhatsApp a las mismas clientas de siempre, y ya sabes cuáles te van a contestar.",
        "reaccion_interna": "Y por dentro ya lo aceptaste: tu almacén vende hasta donde llega la gente que pasa por el frente.",
        "explicacion_fallida": "Te dices que tu ropa se vende es viéndola, tocándola, midiéndosela.",
        "patron": "Pero la marca del local de al lado ya la están comprando en otra ciudad. Misma ropa, mismo precio.",
        "causa_raiz": "No es que tu ropa no sirva para internet. Es que nadie te ha mostrado cómo se vende ropa por internet.",
        "mecanismo": "En la feria están las plataformas, las pasarelas de pago, la logística y las agencias que ya visten a las tiendas que sí venden online.",
        "prueba_social": "Doscientos ponentes que viven de vender por internet. Cinco ediciones, y quien va una vez, vuelve.",
        "visualizacion": "Imagínate empacando un pedido para alguien de otra ciudad que nunca ha entrado a tu local.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, en Plaza Mayor.",
        "defecto_admitido": "No sales de ahí con la tienda montada. Sales sabiendo qué te falta y quién te lo hace.",
        "loop_rewatch": "Y la próxima venta ya no la hace la vitrina.",
        "overlay_dolor": "Llovió. Y no entró nadie",
        "visual_clave": "una vitrina de ropa vista desde adentro, con lluvia en el vidrio y la acera vacía",
        "visual_clave_en": "a clothing shop window seen from inside, rain on the glass and an empty sidewalk",
        # Segmentación de identidad: entra en el segundo clip del beat 1, entre
        # el MOMENTO y el SÍNTOMA, para que en pauta fría el nicho se reconozca
        # antes del segundo corte.
        "codas": {
            1: {
                "nombre": "CALLOUT",
                "emoji": "📣",
                "emocion": "auto_relevancia",
                "hablado": "Tienes almacén de ropa y no vendes por internet: esto es para ti.",
                "overlay": "¿Almacén de ropa?",
            },
            7: {
                "nombre": "FECHAS",
                "emoji": "📍",
                "emocion": "oportunidad",
                "hablado": "Dieciséis al dieciocho de octubre, en Plaza Mayor.",
                "overlay": "16–18 oct · Plaza Mayor",
            },
        },
        "overlays": [
            "Llovió. Y no entró nadie",
            "Las mismas clientas de siempre",
            "Vendes hasta la esquina",
            "«Se vende es viéndola»",
            "La del lado vende en otra ciudad",
            "No es tu ropa",
            "350 empresas en un recinto",
            "200 ponentes que ya venden",
            "Un pedido de otra ciudad",
            "16–18 oct · Plaza Mayor",
            "Sales sabiendo qué te falta",
            "La vitrina ya no vende sola",
        ],
        # Los tres salen del banco de 320, filtrado por (problem, conversión):
        # el 39 de dolor_nombrado y el 33 y el 11 de callout. Se pasaron de
        # voseo a colombiano y los corchetes se rellenaron con el hecho real
        # del micronicho: su facturación depende del clima y del andén.
        # Son tres dolores distintos del mismo techo, no tres versiones de uno.
        "hooks": [
            {
                "hablado": "Llovió el sábado, no entró nadie, y el mes se te cayó.",
                "gatillos": ["dolor_nombrado", "auto_relevancia"],
                "banco": 39,
                "overlay": "Llovió. Y no entró nadie",
            },
            {
                "hablado": "Si vives de que la gente pase por el frente de tu almacén, quédate.",
                "gatillos": ["callout", "auto_relevancia"],
                "banco": 33,
                "overlay": "¿Vives del que pasa?",
            },
            {
                "hablado": "Tu ropa se vende bien. Pero solo a diez cuadras a la redonda.",
                "gatillos": ["interrupcion_patron", "dejar_de_ganar"],
                "banco": 11,
                "overlay": "Vendes a diez cuadras",
            },
        ],
    },

    "contadores": {
        "etiqueta": "Contadores — el que ve pasar los clientes de ecommerce sin poder atenderlos",
        "audiencia": "Contador que quiere entrar al nicho digital y no sabe dónde están esos clientes",
        "ancla": "ecommerce",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Te llega un cliente que vende por internet, te muestra sus movimientos, y por dentro sabes que ese modelo no lo manejas todavía.",
        "sintoma": "Lo atiendes igual, pero te queda la sensación de estar cobrando por algo que estás resolviendo sobre la marcha.",
        "reaccion_interna": "Y lo peor: sabes que ese cliente vale más que tres de los tradicionales, y se te puede ir con alguien que sí sepa.",
        "explicacion_fallida": "Te dices que ya vas a estudiar el tema, cuando baje la temporada.",
        "patron": "Pero la temporada nunca baja, y cada mes entran más negocios digitales al mercado.",
        "causa_raiz": "No te falta estudiar. Te falta estar donde están ellos, y ellos no están en tu oficina.",
        "mecanismo": "Trescientas cincuenta empresas digitales en un solo recinto, todas necesitando quien les cuadre los números.",
        "prueba_social": "Más de doscientos ponentes y todo el ecosistema del ecommerce hispano, junto.",
        "visualizacion": "Imagínate saliendo del domingo con la agenda del semestre resuelta.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, Plaza Mayor, Medellín.",
        "defecto_admitido": "No vas a salir con contratos firmados. Vas a salir con reuniones.",
        "loop_rewatch": "Y el próximo cliente de ecommerce ya no te va a incomodar.",
        "overlay_dolor": "Un modelo que no manejas",
        "visual_clave": "un escritorio de contador frente a movimientos de una tienda online",
        "visual_clave_en": "an accountant's desk facing an online store's transaction records",
        "overlays": [
            "Un modelo que no manejas",
            "Sobre la marcha",
            "Vale por tres",
            "“Cuando baje temporada”",
            "Nunca baja",
            "Estar donde están",
            "350 empresas digitales",
            "200 ponentes",
            "El semestre resuelto",
            "16–18 oct",
            "Sales con reuniones",
            "Ya no incomoda",
        ],
        "hooks": [
            {"hablado": "¿Te llegó un cliente de ecommerce y te sentiste corto?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "Un modelo que no manejas"},
            {"hablado": "Ese cliente digital vale más que tres tradicionales.", "gatillos": ["curiosidad", "dejar_de_ganar"], "overlay": "Vale por tres"},
            {"hablado": "No te falta estudiar. Te falta estar donde están ellos.", "gatillos": ["interrupcion_patron", "auto_relevancia"], "overlay": "Estar donde están"},
        ],
    },

    "abogados": {
        "etiqueta": "Abogados — el que quiere el nicho digital antes de que se llene",
        "audiencia": "Abogado que ve el ecommerce crecer y todavía no tiene un solo cliente de ahí",
        "ancla": "digital",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Ves una consulta sobre términos y condiciones de una tienda online, y te das cuenta de que no sabes ni por dónde cotizarla.",
        "sintoma": "No es que no sepas derecho. Es que ese modelo tiene preguntas que en la facultad nunca aparecieron.",
        "reaccion_interna": "Y mientras tanto ves que hay colegas que ya se especializaron y no paran de recibir clientes.",
        "explicacion_fallida": "Te dices que es un nicho pequeño, que todavía no justifica meterse.",
        "patron": "Pero cada año hay más tiendas, más pasarelas, más plata moviéndose sin abogado que la acompañe.",
        "causa_raiz": "No es un nicho pequeño. Es un nicho al que no has ido a mostrarte.",
        "mecanismo": "Trescientas cincuenta empresas digitales en un recinto, y casi ninguna tiene abogado propio.",
        "prueba_social": "Cinco ediciones y el ecosistema completo del ecommerce hispano en un lugar.",
        "visualizacion": "Imagínate con tres retainers nuevos de negocios que crecen todos los meses.",
        "urgencia_cta": "Dieciséis, diecisiete y dieciocho de octubre. Plaza Mayor.",
        "defecto_admitido": "Vas a tener que explicar qué haces. Nadie te conoce ahí.",
        "loop_rewatch": "Y la próxima consulta de ese tipo ya sabes cobrarla.",
        "overlay_dolor": "No sabes ni cotizarla",
        "visual_clave": "un escritorio jurídico con la pantalla de una tienda online abierta",
        "visual_clave_en": "a law office desk with an online store page open on screen",
        "overlays": [
            "No sabes cotizarla",
            "Sabes derecho",
            "Preguntas nuevas",
            "“Nicho pequeño”",
            "Más tiendas cada año",
            "No has ido",
            "Casi ninguna tiene abogado",
            "Cinco ediciones",
            "Tres clientes que crecen",
            "16–18 oct",
            "Explicar qué haces",
            "Ya sabes cobrarla",
        ],
        "hooks": [
            {"hablado": "¿Te llegó una consulta digital y no supiste cotizarla?", "gatillos": ["auto_relevancia", "curiosidad"], "overlay": "No supiste cotizarla"},
            {"hablado": "No es un nicho pequeño. Es uno al que no has ido.", "gatillos": ["interrupcion_patron", "dejar_de_ganar"], "overlay": "No has ido"},
            {"hablado": "Trescientas cincuenta empresas. Casi ninguna tiene abogado.", "gatillos": ["curiosidad", "dejar_de_ganar"], "overlay": "Casi ninguna tiene"},
        ],
    },

    "laboratorios": {
        "etiqueta": "Laboratorios y fabricantes — el que tiene el producto y no el canal",
        "audiencia": "Fabricante o laboratorio con producto propio que vende por terceros y quiere vender directo",
        "ancla": "canal",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Ves tu propio producto en una tienda online, a un precio que te sorprende, y esa diferencia no llega a tu cuenta.",
        "sintoma": "Fabricas bien. Cumples. Pero el que se queda con el margen es el que sabe vender por internet, no el que hace el producto.",
        "reaccion_interna": "Y te queda claro que sin canal propio siempre vas a depender de que otro decida cuánto te compra.",
        "explicacion_fallida": "Te dices que lo tuyo es producir, que vender en línea es otro oficio.",
        "patron": "Pero llevas años viendo cómo ese otro oficio se queda con la parte más grande.",
        "causa_raiz": "No necesitas volverte experto en marketing. Necesitas a los que ya lo son, trabajando para ti.",
        "mecanismo": "Agencias de tráfico, creadores de contenido y operadores logísticos, todos en el mismo recinto.",
        "prueba_social": "Más de trescientas cincuenta empresas del ecosistema, y más de doscientos ponentes.",
        "visualizacion": "Imagínate vendiendo tu producto directo, con quien lo mueva ya contratado.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, Plaza Mayor, Medellín.",
        "defecto_admitido": "Montar canal propio toma meses. Ahí solo conoces a quién.",
        "loop_rewatch": "Y el precio de esa tienda ya no te va a molestar.",
        "overlay_dolor": "El margen no llega a ti",
        "visual_clave": "un producto de fábrica junto a la página donde alguien más lo revende",
        "visual_clave_en": "a factory product beside the web page where someone else resells it",
        "overlays": [
            "Tu producto, otro precio",
            "No llega a ti",
            "El margen es de otro",
            "“Lo mío es producir”",
            "Años viendo",
            "No tienes que aprenderlo",
            "Tráfico, contenido, logística",
            "350 empresas",
            "Vender directo",
            "16–18 oct",
            "Ahí conoces a quién",
            "Ya no te molesta",
        ],
        "hooks": [
            {"hablado": "¿Viste tu producto en una tienda a un precio que te sorprendió?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "Tu producto, otro precio"},
            {"hablado": "Fabricas tú. El margen se lo lleva el que vende.", "gatillos": ["interrupcion_patron", "dejar_de_ganar"], "overlay": "El margen es de otro"},
            {"hablado": "No necesitas volverte experto. Necesitas a los que ya lo son.", "gatillos": ["curiosidad", "interrupcion_patron"], "overlay": "No tienes que aprenderlo"},
        ],
    },

    "importadores": {
        "etiqueta": "Importadores — el que trae el contenedor y no sabe quién lo va a mover",
        "audiencia": "Importador con producto en bodega que depende de dos o tres clientes para rotarlo",
        "ancla": "rotar",
        "gatillo_principal": "dejar_de_ganar",
        "momento": "Llega el contenedor, entra a bodega, y todavía no sabes con seguridad quién te va a rotar la mitad de eso.",
        "sintoma": "Dependes de dos o tres clientes de siempre, y si uno se demora, se te queda la plata quieta en el piso.",
        "reaccion_interna": "Cada importación se te vuelve una apuesta, y eso te frena para traer las cantidades que sí darían margen.",
        "explicacion_fallida": "Te dices que es normal en este negocio, que así funciona para todos.",
        "patron": "Pero llevas trimestres con inventario parado mientras hay tiendas buscando exactamente lo que tienes.",
        "causa_raiz": "No te falta producto ni te falta precio. Te faltan compradores, y están todos en el mismo sitio tres días.",
        "mecanismo": "Trescientas cincuenta empresas, muchas comprando producto para vender por internet.",
        "prueba_social": "Cinco ediciones, todo el ecosistema del ecommerce hispano en un recinto.",
        "visualizacion": "Imagínate el próximo contenedor entrando con la mitad ya comprometida.",
        "urgencia_cta": "Dieciséis, diecisiete y dieciocho de octubre, en Plaza Mayor.",
        "defecto_admitido": "Nadie compra en la feria. Compran después, si te conocieron.",
        "loop_rewatch": "Y el próximo contenedor ya sabes quién lo mueve.",
        "overlay_dolor": "Inventario quieto en bodega",
        "visual_clave": "cajas apiladas en una bodega, sin movimiento",
        "visual_clave_en": "boxes stacked in a warehouse, nothing moving",
        "overlays": [
            "¿Quién lo rota?",
            "Dos o tres clientes",
            "Plata quieta",
            "“Así funciona”",
            "Inventario parado",
            "Te faltan compradores",
            "350 comprando producto",
            "Cinco ediciones",
            "Medio comprometido",
            "16–18 oct",
            "Compran después",
            "Ya tiene quién",
        ],
        "hooks": [
            {"hablado": "¿Entró el contenedor y no sabes quién lo va a rotar?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "¿Quién lo va a rotar?"},
            {"hablado": "Hay tiendas buscando justo lo que tienes en bodega.", "gatillos": ["curiosidad", "dejar_de_ganar"], "overlay": "Buscan lo que tienes"},
            {"hablado": "No te falta producto. Te faltan compradores.", "gatillos": ["interrupcion_patron", "auto_relevancia"], "overlay": "Te faltan compradores"},
        ],
    },

    "agencias_contenido": {
        "etiqueta": "Agencias de contenido — el que produce bien y vive de referidos",
        "audiencia": "Filmmaker o agencia de contenido cuya facturación depende de que lo recomienden",
        "ancla": "referidos",
        "gatillo_principal": "inclusion",
        "momento": "Entregas un trabajo del que estás orgulloso, el cliente queda feliz, y aun así no sabes de dónde va a salir el siguiente.",
        "sintoma": "Tu agenda depende de que alguien te recomiende, y eso no lo controlas tú.",
        "reaccion_interna": "Es raro estar seguro de tu trabajo y a la vez inseguro de tu mes.",
        "explicacion_fallida": "Te dices que si el trabajo es bueno, los clientes van a llegar solos.",
        "patron": "Pero llevas años con el trabajo bueno y los meses siguen siendo impredecibles.",
        "causa_raiz": "El portafolio no consigue clientes. Los consigue estar en la sala donde ellos deciden.",
        "mecanismo": "Trescientas cincuenta marcas en un recinto, todas necesitando contenido que venda.",
        "prueba_social": "Más de doscientos ponentes y todo el ecosistema digital hispano, junto.",
        "visualizacion": "Imagínate con el trimestre lleno antes de que empiece.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, Plaza Mayor, Medellín.",
        "defecto_admitido": "Vas a tener que hablar con desconocidos. No hay otra.",
        "loop_rewatch": "Y el siguiente trabajo ya no depende de que te recomienden.",
        "overlay_dolor": "Todo llega por referidos",
        "visual_clave": "un montaje terminado en pantalla y una agenda vacía al lado",
        "visual_clave_en": "a finished edit on screen beside an empty calendar",
        "overlays": [
            "Trabajo entregado",
            "¿Y el siguiente?",
            "Todo por referidos",
            "“Si es bueno, llegan”",
            "Años igual",
            "El portafolio no basta",
            "350 marcas",
            "200 ponentes",
            "Trimestre lleno",
            "16–18 oct",
            "Hablar con desconocidos",
            "Ya no depende",
        ],
        "hooks": [
            {"hablado": "¿Tu agenda depende de que alguien te recomiende?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "Todo por referidos"},
            {"hablado": "El portafolio no consigue clientes. La sala sí.", "gatillos": ["interrupcion_patron", "curiosidad"], "overlay": "El portafolio no basta"},
            {"hablado": "Trescientas cincuenta marcas necesitando contenido que venda.", "gatillos": ["curiosidad", "inclusion"], "overlay": "350 marcas · un recinto"},
        ],
    },

    "agencias_pauta": {
        "etiqueta": "Agencias de pauta — el que maneja presupuesto y no consigue cuentas",
        "audiencia": "Trafficker o agencia de medios que sabe pautar pero no sabe vender su servicio",
        "ancla": "cuentas",
        "gatillo_principal": "ego",
        "momento": "Sacas un resultado bueno de verdad en una cuenta, lo publicas, y no pasa absolutamente nada.",
        "sintoma": "Sabes que manejas el pauta mejor que muchos que facturan el triple, y no logras que eso se note.",
        "reaccion_interna": "Duele un poco, porque el resultado está ahí y aun así te toca perseguir clientes por mensaje.",
        "explicacion_fallida": "Te dices que te falta contenido, que hay que publicar más seguido.",
        "patron": "Pero llevas meses publicando resultados y las cuentas siguen llegando de a una.",
        "causa_raiz": "Los que reparten presupuestos grandes no te están viendo el feed. Están en otro lado.",
        "mecanismo": "Trescientas cincuenta empresas en un recinto, muchas decidiendo con quién pautan el año que viene.",
        "prueba_social": "Cinco ediciones, más de doscientos ponentes, el ecosistema completo.",
        "visualizacion": "Imagínate cerrando dos cuentas grandes de una sola conversación.",
        "urgencia_cta": "Dieciséis, diecisiete y dieciocho de octubre. Plaza Mayor.",
        "defecto_admitido": "Nadie te va a firmar ahí mismo. Pero te van a conocer.",
        "loop_rewatch": "Y el próximo resultado que publiques ya va a tener a quién.",
        "overlay_dolor": "Publicas y no pasa nada",
        "visual_clave": "un panel de campaña con buen resultado y cero mensajes nuevos",
        "visual_clave_en": "a campaign dashboard with strong numbers and no new messages",
        "overlays": [
            "No pasó nada",
            "Mejor que el triple",
            "Perseguir por mensaje",
            "“Publicar más”",
            "De a una",
            "No te ven el feed",
            "350 decidiendo",
            "Cinco ediciones",
            "Dos cuentas grandes",
            "16–18 oct",
            "Nadie firma ahí",
            "Ya tiene a quién",
        ],
        "hooks": [
            {"hablado": "¿Publicaste un buen resultado y no pasó nada?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "No pasó nada"},
            {"hablado": "Los que reparten presupuestos no te están viendo el feed.", "gatillos": ["interrupcion_patron", "curiosidad"], "overlay": "No te ven el feed"},
            {"hablado": "Manejas pauta mejor que muchos que facturan el triple.", "gatillos": ["ego", "auto_relevancia"], "overlay": "Mejor que el triple"},
        ],
    },

    "logistica": {
        "etiqueta": "Logística y operadores — el que mueve paquetes y quiere mover más",
        "audiencia": "Operador logístico o de última milla que quiere volumen de tiendas online",
        "ancla": "volumen",
        "gatillo_principal": "inclusion",
        "momento": "Tienes la flota, tienes la bodega, tienes el equipo listo. Y la operación va a media máquina.",
        "sintoma": "Los clientes que tienes están bien, pero son pocos y crecen despacio, y la capacidad instalada te está costando igual.",
        "reaccion_interna": "Sabes que con dos o tres tiendas grandes más el negocio cambiaría de tamaño, y no sabes cómo llegarles.",
        "explicacion_fallida": "Te dices que en este negocio los clientes llegan por recomendación, y hay que esperar.",
        "patron": "Pero llevas trimestres esperando mientras las tiendas que crecen ya eligieron con quién despachan.",
        "causa_raiz": "No se trata de esperar. Se trata de estar el fin de semana donde ellas deciden.",
        "mecanismo": "Trescientas cincuenta empresas en un recinto, casi todas despachando producto todos los días.",
        "prueba_social": "El ecosistema completo del ecommerce hispano, cinco ediciones, un solo lugar.",
        "visualizacion": "Imagínate la operación a máquina completa desde enero.",
        "urgencia_cta": "Del dieciséis al dieciocho de octubre, en Plaza Mayor, Medellín.",
        "defecto_admitido": "Vas a competir con otros operadores ahí mismo. Es así.",
        "loop_rewatch": "Y la flota deja de andar a media máquina.",
        "overlay_dolor": "Operación a media máquina",
        "visual_clave": "una bodega con capacidad de sobra y pocos paquetes",
        "visual_clave_en": "a warehouse with plenty of spare capacity and few packages",
        "overlays": [
            "A media máquina",
            "Crecen despacio",
            "Cuesta igual",
            "“Llegan por recomendación”",
            "Ya eligieron",
            "Estar donde deciden",
            "350 despachando a diario",
            "El ecosistema completo",
            "Máquina completa",
            "16–18 oct",
            "Compites ahí mismo",
            "Deja de andar a medias",
        ],
        "hooks": [
            {"hablado": "¿Tienes la capacidad y la operación va a media máquina?", "gatillos": ["auto_relevancia", "activacion_emocional"], "overlay": "A media máquina"},
            {"hablado": "Las tiendas que crecen ya eligieron con quién despachan.", "gatillos": ["dejar_de_ganar", "interrupcion_patron"], "overlay": "Ya eligieron"},
            {"hablado": "Trescientas cincuenta empresas despachando todos los días.", "gatillos": ["curiosidad", "inclusion"], "overlay": "350 despachando"},
        ],
    },
}


def nichos_disponibles() -> list[str]:
    return sorted(NICHOS)


def obtener(nicho: str) -> dict[str, Any]:
    if nicho not in NICHOS:
        raise KeyError(f"'{nicho}' no existe. Hay: {', '.join(nichos_disponibles())}")
    return NICHOS[nicho]
