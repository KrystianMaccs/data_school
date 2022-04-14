from apps.courses.models import Course, Curriculum
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["pkid", "title", "overview", "image", "tutor"]

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ["pkid", "name", "topic", "sub_topic", "course"]