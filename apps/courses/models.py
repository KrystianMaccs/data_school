from django.db import models
from apps.common.models import TimeStampedUUIDModel
from apps.membership.models import Student
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Course(TimeStampedUUIDModel):
    class Choices(models.IntegerChoices):
        OPTION_1 = 1, "Django Web Framework"
        OPTION_2 = 2, "Data Analysis"
        OPTION_3 = 3, "Data Science"

    title = models.CharField(max_length=120)
    description = models.TextField()
    allowed_membership = models.ManyToManyField(Student)
    course = models.IntegerField(choices=Choices.choices)

    def __str__(self):
        return f"{self.title.title()}"

class Lesson(TimeStampedUUIDModel):
    title = models.CharField(max_length=120)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField()
    video_url = models.URLField()
    thumbnail = models.ImageField()

    def __str__(self):
        return f"{self.title.title()}"

class Curriculum(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    sub_topic = models.CharField(max_length=150)

class Course(TimeStampedUUIDModel):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    image = models.ImageField(upload_to=None)
    url = models.URLField()
    tutor = models.CharField(max_length=50)

class Topic(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50)
    summary = models.TextField()
    objective = models.TextField()

class Lesson(TimeStampedUUIDModel):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    objective = models.TextField()

