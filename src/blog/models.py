import re

from django.db import models
from django.utils.text import Truncator


class Article(models.Model):
    title = models.CharField("título", max_length=200)
    slug = models.SlugField("identificador URL", max_length=220, unique=True)
    content = models.TextField("contenido en Markdown")
    author = models.CharField("autoría", max_length=120)
    published_at = models.DateTimeField("fecha de publicación")
    is_published = models.BooleanField("publicado", default=False)

    class Meta:
        ordering = ["-published_at", "-pk"]
        verbose_name = "artículo"
        verbose_name_plural = "artículos"

    def __str__(self):
        return self.title

    @property
    def excerpt(self):
        plain_text = re.sub(r"[#*_`>\[\]()]", "", self.content)
        return Truncator(" ".join(plain_text.split())).chars(190)


class AboutPage(models.Model):
    title = models.CharField("título", max_length=120, default="Sobre mí")
    content = models.TextField("presentación")

    class Meta:
        verbose_name = "presentación del autor"
        verbose_name_plural = "presentación del autor"

    def __str__(self):
        return self.title