from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializes Address for our users"""
    # user = UserProfileSerializer(required=False)

    class Meta:
        model = Post
        fields = "__all__"
        extra_kwargs = {'user_profile': {'read_only': True}}
