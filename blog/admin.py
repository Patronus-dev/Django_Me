from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime_created', 'status', 'id', )
    ordering = ('datetime_created', )
