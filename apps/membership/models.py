from django.db import models
from apps.user.models import User
from apps.common.models import TimeStampedUUIDModel
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _


class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")
class Student(TimeStampedUUIDModel):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=False, editable=True)
    last_name = models.CharField(max_length=30, blank=False, null=False, editable=True)
    username = models.CharField(max_length=30, blank=False, null=False, editable=False, unique=True)
    gender = models.CharField(max_length=30, blank=False, null=False, choices=Gender.choices, default=Gender.OTHER)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+23424204242")
    email_address = models.EmailField(max_length=120, unique=True, blank=False, null=False)
    country = CountryField(verbose_name=_("Country"), default="NG", blank=False, null=False)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        
class Teacher(TimeStampedUUIDModel):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=False, editable=True)
    last_name = models.CharField(max_length=30, blank=False, null=False, editable=True)
    username = models.CharField(max_length=30, blank=False, null=False, editable=False, unique=True)
    gender = models.CharField(max_length=30, blank=False, null=False, choices=Gender.choices, default=Gender.OTHER)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+23424204242")
    email_address = models.EmailField(max_length=120, unique=True, blank=False, null=False)
    country = CountryField(verbose_name=_("Country"), default="NG", blank=False, null=False)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"