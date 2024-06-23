from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ['id', 'user', 'title', 'description', 'deadline', 'created_at', 'updated_at']
