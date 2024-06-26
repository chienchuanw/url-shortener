from django.contrib import admin
from .models import ShortURL


class ShortURLAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at",)
    list_display = (
        "original_url",
        "short_url",
        "created_at",
    )
    search_fields = (
        "original_url",
        "short_url",
    )


admin.site.register(ShortURL, ShortURLAdmin)
