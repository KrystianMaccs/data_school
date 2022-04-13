from apps.courses.models import Course, Curriculum, Topic, Lesson
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["pkid", "name", "title", "overview", "image", "tutor"]

class CurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculum
        fields = ["pkid", "name", "topic", "sub_topic", "course"]

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ["pkid", "course", "topic", "summary", "objective"]

class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ["pkid", "name", "topic", "description", "objective"]