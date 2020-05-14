from rest_framework import serializers
from .models import UserProfile, Address


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes UserProfile for our API"""
    class Meta:
        model = UserProfile
        fields = ("first_name", "last_name",
                  "gender", "date_of_birth", "phone", "email")


class AddressSerializer(serializers.ModelSerializer):
    """Serializes Address for our users"""
    # user = UserProfileSerializer(required=False)

    class Meta:
        model = Address
        fields = "__all__"
