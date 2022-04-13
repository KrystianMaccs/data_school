from django.shortcuts import render
from rest_framework import generics
from apps.courses.models import Course, Curriculum, Lesson, Topic
from .serializers import CourseSerializer, CurriculumSerializer, TopicSerializer, LessonSerializer



class CourseRead(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = []
class CurriculumRead(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = []


