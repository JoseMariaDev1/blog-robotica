# Visión del producto: Blog de robótica

## Propósito

Crear un espacio sencillo y accesible para compartir artículos sobre robótica en español. El sitio debe poner la lectura en primer plano y permitir que cualquier visitante encuentre artículos recientes, lea cada publicación completa y conozca al autor.

## Usuarios y necesidades

- **Visitantes:** quieren descubrir contenido reciente de robótica, leerlo cómodamente desde móvil o escritorio y encontrar información sobre el autor.
- **Editor del sitio:** necesita publicar, actualizar y retirar artículos, además de mantener la presentación del autor, sin editar plantillas ni código.

## Experiencia deseada

La portada presenta el nombre del blog y los artículos publicados, ordenados del más nuevo al más antiguo. Cada artículo tiene una página propia con su título, fecha, autoría y contenido estructurado en párrafos y subtítulos. La navegación principal conecta la portada con «Sobre mí» y permite volver a la portada desde un artículo. Si aún no hay publicaciones, la portada ofrece un mensaje claro.

## Principios

- **Lectura primero:** priorizar contenido legible, jerarquía clara y una longitud de línea cómoda.
- **Accesibilidad y adaptación:** usar estructura semántica, enlaces descriptivos y una presentación funcional con teclado, en pantallas pequeñas y grandes.
- **Sencillez:** ofrecer navegación directa y renderizado en servidor con Django, sin JavaScript innecesario.
- **Edición autónoma:** gestionar artículos y presentación del autor mediante el panel administrativo estándar de Django, sin registro público.
- **Publicación controlada:** mostrar públicamente solo artículos publicados y responder con una página 404 para artículos inexistentes.

## Alcance de la primera versión

La primera versión incluye una portada, páginas individuales de artículos, una página «Sobre mí» editable y contenido inicial de ejemplo. No incluye cuentas para lectores, comentarios, suscripciones, búsqueda, interacción social ni flujos editoriales avanzados.

## Criterios de éxito

- Un visitante puede encontrar un artículo reciente desde la portada y leerlo completo.
- Un visitante puede acceder a «Sobre mí» desde la navegación principal.
- El sitio se puede utilizar en móvil y escritorio sin perder contenido ni navegación.
- El editor puede mantener artículos y presentación desde Django Admin sin modificar plantillas.
