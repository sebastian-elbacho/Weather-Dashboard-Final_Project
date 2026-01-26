from django.db import models
from django.conf import settings


# Create your models here.


class SearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="weather_searches")
    query = models.CharField(max_length=120)  # np. "Dublin, Leinster, Ireland"
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} - {self.query} ({self.created_at:%Y-%m-%d %H:%M})"

