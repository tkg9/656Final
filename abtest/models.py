from django.db import models


class Visit(models.Model):
    VARIANTS = [("kudos", "kudos"), ("thanks", "thanks")]

    variant = models.CharField(max_length=6, choices=VARIANTS)
    impression_at = models.DateTimeField(auto_now_add=True)
    clicked_at = models.DateTimeField(null=True, blank=True)
