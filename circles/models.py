from django.db import models
from users.models import User

class Circle(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CircleMember(models.Model):
    circle = models.ForeignKey(Circle, related_name='members', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='circles', on_delete=models.CASCADE)
    role = models.CharField(max_length=50, default='member')
    created_at = models.DateTimeField(auto_now_add=True)
