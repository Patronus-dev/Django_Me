from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactUsAdmin(admin.ModelAdmin):
    model = ContactMessage
    list_display = ('name', 'subject', 'email', 'datetime_creation', )