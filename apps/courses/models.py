from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Choices(models.IntegerChoices):
    OPTION_1 = 1, _("Django Web Framework")
    OPTION_2 = 2, _("Data Analysis")
    OPTION_3 = 3, _("Data Science")
class Course(TimeStampedUUIDModel):
    name = models.CharField(max_length=120, editable=True)
    title = models.IntegerField(choices=Choices.choices)
    overview = models.TextField()
    image = models.ImageField(upload_to=None)
    tutor = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Curriculum(TimeStampedUUIDModel):
    name = models.CharField(max_length=120, editable=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    sub_topic = models.CharField(max_length=150)

    def __str__(self):
        return self.name



class Topic(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50, null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
    objective = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.topic


class Lesson(TimeStampedUUIDModel):
    name = models.CharField(max_length=120, editable=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    objective = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name



