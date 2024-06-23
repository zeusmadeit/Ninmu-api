from rest_framework import serializers
from .models import Habit, HabitUpdate

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ['id', 'user', 'title', 'description', 'frequency', 'created_at', 'updated_at']

class HabitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitUpdate
        fields = ['id', 'habit', 'user', 'content', 'image', 'video', 'created_at', 'updated_at']

