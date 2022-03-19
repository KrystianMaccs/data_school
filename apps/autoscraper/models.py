from django.db import models
from apps.common.models import TimeStampedUUIDField

class Scraper(TimestampedUUIDField):
    title = models.CharField(max_length=120)
    url = models.URLField()
    keyword = models.TextField()
