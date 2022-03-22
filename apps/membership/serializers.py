from .models import Student
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializers):

    class Meta:
        model = Student
        exclude = ["updated_at", "pkid"]
