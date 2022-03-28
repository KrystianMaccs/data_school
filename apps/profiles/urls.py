from django.urls import path
from apps.profiles.views import ProfileSerializerView


app_name = "profiles"

urlpatterns = [
    #path("profiles", ProfileSerializerView.as_view()),
]