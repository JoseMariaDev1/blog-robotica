from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import AboutPage, Article


class PublicPagesTests(TestCase):
    def setUp(self):
        now = timezone.now()
        self.older_article = Article.objects.create(
            title="Sensores de distancia",
            slug="sensores-distancia-test",
            content="## Medir\n\nUn sensor aporta una medida.",
            author="Autora de prueba",
            published_at=now - timedelta(days=2),
            is_published=True,
        )
        self.newer_article = Article.objects.create(
            title="Control de motores",
            slug="control-motores-test",
            content="Un controlador ajusta la velocidad.",
            author="Autor de prueba",
            published_at=now - timedelta(days=1),
            is_published=True,
        )
        self.draft = Article.objects.create(
            title="Borrador privado",
            slug="borrador-privado-test",
            content="Este contenido no debe ser público.",
            author="Autor de prueba",
            published_at=now,
            is_published=False,
        )

    def test_home_lists_published_articles_newest_first(self):
        response = self.client.get(reverse("blog:home"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.newer_article.title)
        self.assertContains(response, self.older_article.title)
        self.assertNotContains(response, self.draft.title)
        self.assertLess(
            response.content.index(self.newer_article.title.encode()),
            response.content.index(self.older_article.title.encode()),
        )

    def test_article_renders_markdown_and_sanitizes_html(self):
        self.older_article.content = "## Medición\n\nDato útil.\n\n<script>alert(1)</script>"
        self.older_article.save()

        response = self.client.get(
            reverse("blog:article_detail", args=[self.older_article.slug])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h2>Medición</h2>", html=True)
        self.assertNotContains(response, "<script>")

    def test_draft_and_unknown_article_return_404(self):
        draft_response = self.client.get(
            reverse("blog:article_detail", args=[self.draft.slug])
        )
        missing_response = self.client.get(
            reverse("blog:article_detail", args=["no-existe"])
        )

        self.assertEqual(draft_response.status_code, 404)
        self.assertEqual(missing_response.status_code, 404)

    def test_about_page_is_available_and_editable_in_admin(self):
        AboutPage.objects.update_or_create(
            pk=1,
            defaults={"title": "Sobre mí", "content": "Presentación de prueba."},
        )

        response = self.client.get(reverse("blog:about"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Presentación de prueba.")
        self.assertContains(response, reverse("blog:home"))


class AdminAccessTests(TestCase):
    def test_anonymous_visitors_cannot_manage_articles(self):
        response = self.client.get(reverse("admin:blog_article_changelist"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("admin:login"), response.url)

    def test_staff_editor_can_manage_articles_and_about_page(self):
        editor = get_user_model().objects.create_user(
            username="editor", password="safe-test-password", is_staff=True
        )
        content_types = ContentType.objects.get_for_models(Article, AboutPage).values()
        permissions = Permission.objects.filter(
            content_type__in=content_types,
            codename__in=("view_article", "view_aboutpage"),
        )
        editor.user_permissions.add(*permissions)
        self.client.force_login(editor)

        article_response = self.client.get(reverse("admin:blog_article_changelist"))
        about_response = self.client.get(reverse("admin:blog_aboutpage_changelist"))

        self.assertEqual(article_response.status_code, 200)
        self.assertEqual(about_response.status_code, 200)