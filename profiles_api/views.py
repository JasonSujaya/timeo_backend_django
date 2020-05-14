from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins


# Import things
from .serializers import UserProfileSerializer, AddressSerializer
from .models import UserProfile, Address


class UserProfilesView(viewsets.ModelViewSet):
    """Handle creating and fetching profile"""
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
