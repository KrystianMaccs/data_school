from django.urls import path
from apps.profiles.views import (
    ProfileCreateView, 
    ProfileListView,
    ProfileEditView,
    ProfileDeleteView
)



app_name = "profiles"

urlpatterns = [
    path("profiles", ProfileCreateView.as_view()),
    path("profiles-list", ProfileListView.as_view()),
    path("<int:pk>", ProfileEditView.as_view()),
    path("<int:pk>/delete", ProfileDeleteView.as_view())
]