from rest_framework import viewsets
from .models import Goals
from .serializers import GoalSerializer
from rest_framework.permissions import IsAuthenticated

class GoalViewSet(viewsets.ModelViewSet):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
