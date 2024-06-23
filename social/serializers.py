from rest_framework import serializers
from .models import Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'habit_update', 'user', 'content', 'created_at', 'updated_at']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'habit_update', 'user', 'created_at']
