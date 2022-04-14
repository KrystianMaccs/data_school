from django.urls import path
from apps.courses.views import *


urlpatterns = [
    path('courses/',CourseRead.as_view(), name="course-list"),
    path('curriculum/', CurriculumRead.as_view(), name="curriculum-list"),
]