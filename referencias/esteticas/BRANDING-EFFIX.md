# Branding Feria Effix 2026 — extraído del sitio oficial

Fuente: feriaeffix.com · extraído 2026-08-28 con inspección de estilos computados
en navegador (no de una descripción, de los valores reales del DOM).

⚠️ **Un primer intento con `curl` devolvió un 403 del hosting.** Los colores teal
(`#226d7a`, `#22b8d1`) que aparecen en esa respuesta son de la página de error, **no
son de Effix**. Si alguien vuelve a extraer con curl, va a caer en la misma trampa.

---

## LA MARCA ES BLANCO Y NEGRO

No hay color de acento. La identidad completa se construye con contraste puro.

| Rol | Hex | Uso |
|---|---|---|
| Fondo dominante | `#000000` | Secciones hero, cards, bloques de contenido |
| Fondo alterno | `#0A0A0F` | Negro con leve tinte frío |
| Blanco | `#FFFFFF` | Texto sobre negro, logo, outlines |
| Fondo claro | `#F5F7F9` | Secciones alternas |
| Texto secundario | `#333333` | Cuerpo sobre fondo claro |
| Gris violáceo | `#73708E` | Barra de countdown (secundario, poco peso) |

## Tipografía

| Uso | Fuente | Peso |
|---|---|---|
| Titulares | **Montserrat** | 900 / 800 |
| Cuerpo | **Montserrat** | 300 |
| Secundaria | **Oswald** | — |

## Estética visual

- **Logo:** script manuscrito "Feria Effix" con **outline blanco grueso**, estilo
  sticker/pegatina. La X del final lleva un trazo tipo brocha que la tacha.
- **Titulares:** caja alta, Montserrat 900, con **outline** — el mismo tratamiento
  sticker del logo.
- **Cards:** rectángulos negros con **esquinas muy redondeadas** y borde blanco.
- **Registro general:** alto contraste, urbano, bold, sin degradados ni texturas.

---

## QUÉ SIGNIFICA PARA EL AD

Esto obliga a una decisión de diseño, no es un detalle menor.

**El problema:** un personaje amigurumi en blanco y negro se ve apagado, y el arco
narrativo de LANA depende de que "gane color" al re-tejerse.

**La solución propuesta — monocromo que gana color:**

| Momento | Tratamiento |
|---|---|
| Mundo del "no he arrancado" | Lana cruda, gris y blanco hueso. Sin color. Coherente con la marca. |
| Entrada a la feria | El color entra por la fibra a medida que se re-teje |
| Feria | Elementos de marca (banners, señalética, logo) **siempre en blanco y negro**; el color vive solo en LANA y en la gente |
| Final | LANA a color pleno, dentro de un mundo B&N de marca |

Esto hace dos cosas a la vez: respeta la identidad B&N de Effix en todo lo que es
marca, y le da al ad la recompensa visual que necesita para funcionar en el feed.

**El mundo sin color es el de quien no ha arrancado. La feria le devuelve el color.**
Y el negro y blanco de los banners deja de ser una limitación: pasa a ser el marco
dentro del cual ella recupera el color.

**Alternativa más radical:** el ad entero en blanco y negro alto contraste, estilo
sticker, sin ningún color. Máxima coherencia de marca y altísima diferenciación en un
feed saturado de color — pero más riesgo de que pase desapercibido en scroll.

---

## PARA LOS PROMPTS

Bloque de estilo a inyectar verbatim en los keyframes:

```
Brand palette locked to pure black #000000 and pure white #FFFFFF with no accent
colour on any signage, banner or graphic element. All fair signage and banners use
heavy white outlined display lettering on black, sticker-style with thick outlines
and heavily rounded corners.
```

Forbidden list de marca:
> NO degradados en elementos de marca. NO colores corporativos inventados.
> NO tipografías con serifas en señalética. NO texto renderizado dentro del video
> (los textos van en post con Montserrat 900).
