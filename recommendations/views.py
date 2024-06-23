from rest_framework import viewsets
from .models import Recommendation
from .serializers import RecommendationSerializer
from rest_framework.permissions import IsAuthenticated

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]
