from django.shortcuts import get_object_or_404, render

from .markdown_utils import render_markdown
from .models import AboutPage, Article


def home(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, "blog/home.html", {"articles": articles})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(
        request,
        "blog/article_detail.html",
        {"article": article, "rendered_content": render_markdown(article.content)},
    )


def about(request):
    about_page = AboutPage.objects.first()
    return render(request, "blog/about.html", {"about_page": about_page})