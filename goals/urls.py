from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import GoalViewSet

router = SimpleRouter()
router.register(r'goals', GoalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
