from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfilesView

router = DefaultRouter()
router.register('userprofiles', UserProfilesView,
                base_name='userprofiles')

urlpatterns = [
    path('', include(router.urls)),
]
