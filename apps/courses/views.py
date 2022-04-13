from django.shortcuts import render
from rest_framework import generics, permissions
from apps.courses.models import Course, Curriculum, Lesson, Topic
from .serializers import CourseSerializer, CurriculumSerializer, TopicSerializer, LessonSerializer



class CourseRead(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []
class CurriculumRead(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = []

class TopicRead(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = []

class LessonRead(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = []
