from django.urls import path
from .views import *



app_name = "profiles"

urlpatterns = [
    path("profiles", ProfileCreateView.as_view()),
    path("profiles-list", ProfileListView.as_view()),
    path("<int:pk>", ProfileEditView.as_view()),
    path("<int:pk>/delete", ProfileDeleteView.as_view())
]