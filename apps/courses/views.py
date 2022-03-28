from django.shortcuts import render
from rest_framework import generics
from .models import Course, Curriculum, Lesson, Topic
from .serializers import CourseSerializer, CurriculumSerializer, TopicSerializer, LessonSerializer


class CourseView(generics.CreatePIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


