from django.shortcuts import render
from rest_framework import generics
from apps.courses.models import Course, Curriculum, Lesson, Topic
from .serializers import CourseSerializer, CurriculumSerializer, TopicSerializer, LessonSerializer


class CourseView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CurriculumView(generics.CreateAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer


