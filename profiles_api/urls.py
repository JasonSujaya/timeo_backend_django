from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfilesView, AddressListGeneric, AddressRetrieveUpdateGeneric

router = DefaultRouter()
router.register('userprofile', UserProfilesView,
                base_name='userprofile')

urlpatterns = [
    path('', include(router.urls)),
    path('address/', AddressListGeneric.as_view(), name="addresslist"),
    path('address/<pk>/',
         AddressRetrieveUpdateGeneric.as_view(), name="addresspatch"),
]
