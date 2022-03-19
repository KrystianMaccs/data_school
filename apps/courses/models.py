"""from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Course(TimeStampedUUIDModel):
    class Choices(models.Choices):
        Django = "Django Web Framework"
        Data_analysis = "Data Analysis"
        Data_science = "Data Science"

    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_membership = models.ManyToManyField(Membership)

    def __str__(self):
        return f"{self.title.title()}"

class Lesson(TimeStampedUUIDModel):
    title = models.CharField(max-length=120)
    course = models.ForeignKey(Course, on_delete=model.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.URLField()
    thumbnail = models.ImageField()

    def __str__(self):
        return f"{self.title.title()}"
"""