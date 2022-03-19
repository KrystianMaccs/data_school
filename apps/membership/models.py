from django.db import models

from apps.profiles.models import Profile
from django.utils.translation import gettext_lazy as _

class Student(Profile):
    exclude = ["is_staff"]
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        
class Teacher(Profile):
    students = models.ManyToManyField(Student)


    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"