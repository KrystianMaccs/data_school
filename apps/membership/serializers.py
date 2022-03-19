from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializers):
    rater = serializers.SerializerMethodField(read_only=True)
    agent = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Rating
        exclude = ["updated_at", "pkid"]
