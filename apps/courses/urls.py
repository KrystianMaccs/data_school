from django.urls import path
from apps.courses.views import CourseView


urlpatterns = [
    path('api/create',CourseView.as_view()),
]