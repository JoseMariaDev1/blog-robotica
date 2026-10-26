# Criterios de aceptación: Blog de robótica

## RF-01: Portada

- Al acceder a `/`, se muestra el nombre del blog y una lista de artículos publicados.
- Los artículos aparecen ordenados por fecha de publicación, del más reciente al más antiguo.
- Cada elemento de la lista muestra el título, la fecha y un extracto, y enlaza a la página individual del artículo.
- Si no hay artículos publicados, la portada muestra un mensaje informativo.
- Los artículos en borrador no aparecen en la portada.

## RF-02: Lectura de artículos

- Cada artículo publicado dispone de una ruta individual en `/articulos/<slug>/`.
- La página del artículo muestra título, fecha de publicación, autoría y contenido.
- El contenido conserva sus párrafos y subtítulos y se presenta con una estructura legible.
- Al solicitar una ruta de artículo inexistente, el servidor responde con HTTP 404.
- Desde la página de un artículo se puede volver a la portada mediante un enlace claramente identificado.

## RF-03: Sobre mí

- Existe una página `/sobre-mi/` identificable como «Sobre mí».
- La navegación principal incluye un enlace a esta página.
- La página muestra la presentación del autor.
- Un editor autorizado puede actualizar esa presentación desde el panel administrativo, sin editar plantillas.

## RF-04: Navegación

- La navegación principal permite llegar a la portada y a «Sobre mí» desde las páginas del sitio.
- Los enlaces tienen nombres descriptivos y comprensibles.
- La navegación básica funciona sin JavaScript.
- Los enlaces principales y los enlaces a artículos conducen a las rutas correspondientes.

## RF-05: Gestión de contenido

- Un editor autorizado puede crear, editar y retirar artículos desde el panel administrativo de Django.
- Un editor autorizado puede actualizar la presentación del autor desde dicho panel.
- Las operaciones de edición requieren autenticación; un visitante anónimo no puede acceder a ellas.
- Los artículos no publicados no se muestran en las páginas públicas.
- No existe un flujo de registro público para lectores.

## Requisitos transversales

- Las páginas se pueden utilizar en pantallas pequeñas y grandes sin desplazamiento horizontal innecesario.
- El contenido usa HTML semántico y una jerarquía coherente de encabezados.
- Los enlaces y controles pueden utilizarse con teclado y presentan contraste y legibilidad adecuados.
- Las páginas informativas se renderizan en el servidor con Django; JavaScript no es necesario para leer ni navegar por el sitio.
