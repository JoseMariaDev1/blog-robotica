from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def add_sample_content(apps, schema_editor):
    Article = apps.get_model("blog", "Article")
    AboutPage = apps.get_model("blog", "AboutPage")
    Article.objects.get_or_create(
        slug="como-percibe-su-entorno-un-robot-movil",
        defaults={
            "title": "Cómo percibe su entorno un robot móvil",
            "content": (
                "Un robot móvil combina sensores y algoritmos para orientarse. "
                "La percepción transforma las señales del entorno en información "
                "que el sistema puede utilizar para decidir su siguiente movimiento.\n\n"
                "## Sensores y contexto\n\n"
                "Las cámaras, los sensores de distancia y los encoders aportan "
                "mediciones distintas. Ninguno ofrece por sí solo una imagen "
                "completa: el software debe interpretar sus límites y combinar "
                "los datos con cuidado.\n\n"
                "## Del dato a la acción\n\n"
                "Un mapa sencillo permite planificar una ruta y corregirla cuando "
                "aparece un obstáculo. En la práctica, medir, estimar y volver a "
                "medir forman un ciclo continuo."
            ),
            "author": "Equipo de Bitácora Robótica",
            "published_at": timezone.now() - timedelta(days=1),
            "is_published": True,
        },
    )
    AboutPage.objects.get_or_create(
        pk=1,
        defaults={
            "title": "Sobre mí",
            "content": (
                "Este espacio reúne ideas, pruebas y aprendizajes sobre robótica, "
                "desde los sensores hasta los sistemas autónomos."
            ),
        },
    )


def remove_sample_content(apps, schema_editor):
    Article = apps.get_model("blog", "Article")
    AboutPage = apps.get_model("blog", "AboutPage")
    Article.objects.filter(slug="como-percibe-su-entorno-un-robot-movil").delete()
    AboutPage.objects.filter(pk=1).delete()


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial")]

    operations = [migrations.RunPython(add_sample_content, remove_sample_content)]