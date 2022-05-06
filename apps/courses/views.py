from django.shortcuts import render
from rest_framework import generics, permissions

from apps.courses.models import Course, Curriculum

from .serializers import CourseSerializer, CurriculumSerializer


class CourseRead(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = []


class CurriculumRead(generics.ListAPIView):
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = []
