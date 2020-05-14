from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins


# Import things
from .serializers import UserProfileSerializer, AddressSerializer
from .models import UserProfile, Address


from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserProfilesView(viewsets.ModelViewSet):
    """Handles creating and fetching profile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # """Handles Authentication"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
