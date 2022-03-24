from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework import generics
from .models import Profile

class ProfileSerializerView(ProfileSerializer):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
