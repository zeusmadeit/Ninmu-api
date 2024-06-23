from rest_framework import viewsets
from .models import Circle, CircleMember
from .serializers import CircleSerializer, CircleMemberSerializer
from rest_framework.permissions import IsAuthenticated

class CircleViewSet(viewsets.ModelViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleSerializer
    permission_classes = [IsAuthenticated]

class CircleMemberViewSet(viewsets.ModelViewSet):
    queryset = CircleMember.objects.all()
    serializer_class = CircleMemberSerializer
    permission_classes = [IsAuthenticated]
