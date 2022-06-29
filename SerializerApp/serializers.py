from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    roll = serializers.IntegerField()
    email = serializers.EmailField()
    city = serializers.CharField()