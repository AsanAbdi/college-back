from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.events.models import (
    Event
)

@admin.register(Event)
class EvemtAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "background", "duration", "description", "location", "type"]