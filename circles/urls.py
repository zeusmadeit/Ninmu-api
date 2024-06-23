from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CircleViewSet, CircleMemberViewSet

router = DefaultRouter()
router.register(r'circles', CircleViewSet)
router.register(r'members', CircleMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
