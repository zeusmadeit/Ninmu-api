from rest_framework import serializers
from .models import Circle, CircleMember

class CircleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circle
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class CircleMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = CircleMember
        fields = ['id', 'circle', 'user', 'role', 'created_at']
