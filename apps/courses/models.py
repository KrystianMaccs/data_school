from django.db import models
from apps.common.models import TimeStampedUUIDModel
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Course(TimeStampedUUIDModel):
    CATEGORY_CHOICES = (
        ('DS', 'Data Science'),
        ('DA', 'Data Analysis'),
        ('DJ', 'Django Web Framework'),
        ('DR', 'Django REST Framework'),
    )
    title = models.CharField(choices=CATEGORY_CHOICES, max_length=50, default="Data Science")
    overview = models.TextField()
    image = models.ImageField(upload_to="mediafiles/", default="image.jpg")
    tutor = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Curriculum(TimeStampedUUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    pdf = models.FileField(upload_to="mediafiles/", default="curriculum.pdf")



