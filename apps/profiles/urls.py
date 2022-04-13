from django.urls import path
from .views import *



app_name = "profiles"

urlpatterns = [
    path("me/", ProfileListView.as_view(), name="get-profile"),
    path("update/<str:username>/", ProfileEditView.as_view(), name="update-profile"),
]