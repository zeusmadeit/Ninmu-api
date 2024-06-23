from rest_framework import viewsets
from .models import Habit, HabitUpdate
from .serializers import HabitSerializer, HabitUpdateSerializer
from rest_framework.permissions import IsAuthenticated

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

class HabitUpdateViewSet(viewsets.ModelViewSet):
    queryset = HabitUpdate.objects.all()
    serializer_class = HabitUpdateSerializer
    permission_classes = [IsAuthenticated]
