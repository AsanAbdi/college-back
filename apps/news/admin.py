from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.news.models import (
    News,
    Main_page_news
)

@admin.register(Main_page_news)
class Main_page_newsAdmin(admin.ModelAdmin):
    list_display = ["id", "news_1", "news_2", "news_3", "news_4"]

    def has_add_permission(self, request):
        count = Main_page_news.objects.count()
        if count == 0:
            return True
        return False


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image", "date"]

