from django.urls import path
from apps.courses.views import *


urlpatterns = [
    path('courses/',CourseRead.as_view(), name="course-list"),
    path('curriculum/', CurriculumRead.as_view(), name="curriculum-list"),
    path('topic/', TopicRead.as_view(), name="topic-list"),
    path('lesson/', LessonRead.as_view(), name="lesson-list"),
]