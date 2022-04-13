from django.shortcuts import render
from apps.profiles.serializers import ProfileSerializer
from rest_framework import generics
from apps.profiles.models import Profile
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import get_user_model
from apps.users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]


class ProfileEditView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
