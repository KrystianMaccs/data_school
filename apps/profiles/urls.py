from django.urls import path
from apps.profiles.views import ProfileSerializerView

urlpatterns = [
    path("", ProfileSerializerView.as_view(), name="profile"),
]