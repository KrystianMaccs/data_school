from .models import Student
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializers):
    first_name = models.CharField(max_length=30, blank=False, null=False, editable=True)
    last_name = models.CharField(max_length=30, blank=False, null=False, editable=True)
    username = models.CharField(max_length=30, blank=False, null=False, editable=False, unique=True)
    gender = models.CharField(max_length=30, blank=False, null=False, choices=Gender.choices, default=Gender.OTHER)
    phone_number = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, default="+23424204242")
    email_address = models.EmailField(max_length=120, unique=True, blank=False, null=False)
    country = CountryField(verbose_name=_("Country"), default="NG", blank=False, null=False)


    class Meta:
        model = Student
        exclude = ["updated_at", "pkid"]
