from rest_framework import viewsets
from .models import Comment, Like
from .serializers import CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticated

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
