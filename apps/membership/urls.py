from django.urls import path
from apps.membership.views import (
    StudentCreateView,
    StudentListView,
    StudentEditView,
    StudentDeleteView
)


urlpatterns = [
    path("student", StudentCreateView.as_view()),
    path("student-list", StudentListView.as_view()),
    path("<int:pk>", StudentEditView.as_view()),
    path("<int:pk>/delete", StudentDeleteView.as_view()),
]