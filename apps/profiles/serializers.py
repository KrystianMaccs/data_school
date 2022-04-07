from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ["user", "phone_number", "about_me", "profile_photo", "gender", "country", "city"]
