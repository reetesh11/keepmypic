from django.contrib import admin
from .models import Photos

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]

    class Meta:
        model = Photos

admin.site.register(Photos, PhotoAdmin)

