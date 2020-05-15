from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins

# Auth Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Authentication
from rest_framework.authentication import TokenAuthentication
from post_api import permissions

# Import Apps & Serializers
from .serializers import PostSerializer
from .models import Post


class PostViewset(viewsets.ModelViewSet):
    """Handles Authentication"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.InteractOwnPost,)

    """Handles creating and fetching profile"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
