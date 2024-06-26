from django.db import models


class ShortURL(models.Model):
    original_url = models.URLField(
        help_text="Enter a valid URL address", verbose_name="Original URL"
    )
    short_url = models.URLField(
        max_length=100, unique=True, blank=True, verbose_name="Short URL"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Time")

    class Meta:
        verbose_name = "Short URL"
        verbose_name_plural = "Short URLs"

    def __str__(self):
        return self.short_url
