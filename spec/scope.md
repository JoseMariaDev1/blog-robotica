# Alcance: Blog de robótica

## Incluido

- Portada en `/` con el nombre del blog y los artículos publicados más recientes, ordenados del más nuevo al más antiguo. Cada artículo muestra título, fecha y extracto, y enlaza a su página. Si no hay artículos publicados, se muestra un mensaje informativo.
- Página individual en `/articulos/<slug>/` con título, fecha, autoría y contenido estructurado en párrafos y subtítulos. Una ruta inexistente responde con HTTP 404.
- Página «Sobre mí» en `/sobre-mi/`, con una presentación breve del autor que se pueda actualizar sin modificar plantillas.
- Navegación principal entre la portada y «Sobre mí», y un enlace desde cada artículo para volver a la portada.
- Diseño adaptable, accesible y centrado en la lectura, con HTML semántico y navegación básica funcional sin JavaScript.
- Contenido inicial de ejemplo relacionado con robótica, sustituible o eliminable desde la gestión editorial.
- Gestión de artículos y de la presentación del autor mediante el panel administrativo estándar de Django, disponible solo para editores autorizados. Los borradores no se muestran en las páginas públicas.
- Renderizado del lado del servidor con Django y persistencia mediante modelos y migraciones. SQLite se contempla para desarrollo inicial.

## Excluido

- Registro, cuentas o perfiles públicos para lectores.
- Comentarios, funciones sociales, suscripciones o boletines.
- Búsqueda de artículos.
- Flujos editoriales avanzados, como revisión, programación de publicaciones o múltiples roles.
- Interacción que requiera JavaScript para la navegación básica.
- Decisiones de despliegue y base de datos de producción, que se definirán según el entorno de publicación.

## Límites y supuestos

- El idioma inicial es el español y el tema del contenido es la robótica.
- La primera versión contempla un editor y una presentación principal del autor.
- El panel administrativo de Django es la única interfaz de gestión de contenido; no se incluye un CMS público o personalizado.
- El dominio, la identidad visual, el contenido definitivo y el entorno de despliegue quedan pendientes.
