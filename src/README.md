# Bitácora Robótica

Blog en español construido con Django. Los artículos y la presentación del autor se gestionan desde Django Admin; el contenido de los artículos admite Markdown y se sanitiza antes de mostrarse.

## Desarrollo local (Windows / PowerShell)

Desde esta carpeta (`src`), crea y activa un entorno virtual, instala las dependencias y prepara la base de datos:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
```

Si ya existe `.venv`, no es necesario volver a crear el entorno. En macOS o Linux, activa el entorno con `source .venv/bin/activate`.

### Crear el administrador y asignarle una clave

La primera vez, crea una cuenta con permisos de administrador:

```powershell
python manage.py createsuperuser
```

Sigue las indicaciones para escribir el nombre de usuario, el correo (opcional) y la contraseña. La contraseña no se muestra mientras se escribe. Si la cuenta ya existe y quieres cambiar su clave, ejecuta `python manage.py changepassword nombre_de_usuario`.

### Iniciar el servidor

Con el entorno virtual activo, ejecuta:

```powershell
python manage.py runserver
```

El sitio estará disponible en `http://127.0.0.1:8000/` y el panel editorial en `http://127.0.0.1:8000/admin/`. No existe registro público; los artículos se gestionan desde el panel.

## Configuración

En desarrollo se usa SQLite y `DEBUG` está activado de forma predeterminada. Para producción, configura `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false` y `DJANGO_ALLOWED_HOSTS` en el entorno. `SITE_NAME` cambia el nombre mostrado en la navegación. Revisa los requisitos de HTTPS y la base de datos según el proveedor de despliegue.

## Comprobaciones

```powershell
python manage.py check
python manage.py test blog
```