from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Article


@admin.register(Article)
class ArticleAdmin(TranslationAdmin):
    fieldsets = [
        (
            "Общее",
            {
                "fields": ['name', 'short_description', 'slug']
            }
        ),

        (
            "Описание",
            {
                "fields": ['description']
            }
        )
    ]
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')
    prepopulated_fields = {"slug": ("name",)}
