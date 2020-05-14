from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics, mixins


# Import things
from .serializers import UserProfileSerializer, AddressSerializer
from .models import UserProfile, Address


class UserProfilesView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class AddressListGeneric(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressRetrieveUpdateGeneric(generics.RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

# class AddressListView(APIView):
#     def get(self, request):
#         address = Address.objects.all()
#         data = AddressSerializer(address, many=True).data
#         return Response(data)
