from django.urls import path
from apps.courses.views import CourseView, CurriculumView


urlpatterns = [
    path('api/create',CourseView.as_view()),
    path('api/create-curriculum', CurriculumView.as_view()),
]