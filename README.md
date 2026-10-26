# Blog de robótica

Blog en español desarrollado con Django. El proyecto Django está en [`src/`](src/), y los documentos de producto están en la raíz y en [`spec/`](spec/).

## Ejecutar en Windows

Abre PowerShell en la carpeta `src` y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Si ya creaste el administrador, puedes omitir `createsuperuser`. Abre el blog en <http://127.0.0.1:8000/> y el panel para gestionar artículos en <http://127.0.0.1:8000/admin/>.

Consulta [`src/README.md`](src/README.md) para más detalles, incluyendo cómo cambiar la contraseña del administrador y la configuración de producción.
