import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutPage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(default="Sobre mí", max_length=120, verbose_name="título")),
                ("content", models.TextField(verbose_name="presentación")),
            ],
            options={
                "verbose_name": "presentación del autor",
                "verbose_name_plural": "presentación del autor",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="título")),
                ("slug", models.SlugField(max_length=220, unique=True, verbose_name="identificador URL")),
                ("content", models.TextField(verbose_name="contenido en Markdown")),
                ("author", models.CharField(max_length=120, verbose_name="autoría")),
                ("published_at", models.DateTimeField(verbose_name="fecha de publicación")),
                ("is_published", models.BooleanField(default=False, verbose_name="publicado")),
            ],
            options={
                "verbose_name": "artículo",
                "verbose_name_plural": "artículos",
                "ordering": ["-published_at", "-pk"],
            },
        ),
    ]