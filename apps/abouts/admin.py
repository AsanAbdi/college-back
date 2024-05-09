from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from apps.abouts.models import (
    Email_sending,
    Contact,
    Contact_information,
    FAQ,
    Sertificate,
    Sample,
    Images_for_multimedia,
    Block_of_contact,
    Lecturer,
)

@admin.register(Email_sending)
class Email_sendingAdmin(admin.ModelAdmin):
    list_display = ["id", "receiver"]

    def has_add_permission(self, request):
        count = Email_sending.objects.count()
        if count == 0:
            return True
        return False


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "answer"]


@admin.register(Contact_information)
class Contact_informationAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "text", "type"]


@admin.register(Sertificate)
class SertificateAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "image"]


@admin.register(Images_for_multimedia)
class Images_for_multimediaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "image",
        "link",
        "type"
    ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "role", "email", "contact"]

@admin.register(Block_of_contact)
class Block_of_contactAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "contact", "email"]

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "avatar", "age", "bio", "subject"]

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "file"]
