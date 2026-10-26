from django.contrib import admin

from .models import AboutPage, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at", "is_published")
    list_filter = ("is_published", "published_at")
    list_editable = ("is_published",)
    search_fields = ("title", "content", "author")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    ordering = ("-published_at",)
    fieldsets = (
        (None, {"fields": ("title", "slug", "author", "content")}),
        ("Publicación", {"fields": ("published_at", "is_published")}),
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    fields = ("title", "content")

    def has_add_permission(self, request):
        return not AboutPage.objects.exists()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.pk = 1
        super().save_model(request, obj, form, change)