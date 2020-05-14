from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes UserProfile for our API"""
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name",
                  "gender", "date_of_birth", "phone", "email")


class HelloSerializer(serializers.Serializer):
    """Serializes a name file for testing our api"""
    name = serializers.CharField(max_length=10)
