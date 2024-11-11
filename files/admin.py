from django.contrib import admin
from files.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'img', 'datetime']
