from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.education.models import (
    Admission_date,
    Specialtie,
    Scholorship_grant,
    Schedule,
    Courses_programms
)

@admin.register(Admission_date)
class Admission_dateAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "event_date", "description"]


@admin.register(Specialtie)
class SpecialtieAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "study_time", "type", "budget", ]

@admin.register(Scholorship_grant)
class Scholorship_grantAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "type"]


@admin.register(Courses_programms)
class Courses_programmsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "duration", "mini_description", "price", "type"]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "file",
    ]
