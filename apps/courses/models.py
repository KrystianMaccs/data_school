from django.db import models
from apps.common.models import TimeStampedUUIDModel
from apps.membership.models import Student, Teacher
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Choices(models.IntegerChoices):
    OPTION_1 = 1, _("Django Web Framework")
    OPTION_2 = 2, _("Data Analysis")
    OPTION_3 = 3, _("Data Science")
class Course(TimeStampedUUIDModel):
    title = models.IntegerField(choices=Choices.choices)
    overview = models.TextField()
    image = models.ImageField(upload_to=None)
    tutor = models.CharField(max_length=50)



class Curriculum(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    sub_topic = models.CharField(max_length=150)



class Topic(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50, null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
    objective = models.TextField(null=False, blank=False)


class Lesson(TimeStampedUUIDModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    objective = models.TextField(null=False, blank=False)



