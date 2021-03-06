from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfilesView, AddressViewSet, UserLoginApiView, AddressRetrieveUpdate, AddressCreate

router = DefaultRouter()
router.register('userprofile', UserProfilesView,
                base_name='userprofile')
router.register('address', AddressViewSet,
                base_name='address')


urlpatterns = [
    path('', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),
    path('userprofile/<int:pk>/address-create/', AddressCreate.as_view()),
    path('userprofile/<int:pk>/address/', AddressRetrieveUpdate.as_view()),
]
