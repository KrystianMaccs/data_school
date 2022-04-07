from .models import Student
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["student", "is_learned", "is_familiar"]
