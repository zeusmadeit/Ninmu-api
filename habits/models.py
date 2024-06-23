from django.db import models
from users.models import User

class Habit(models.Model):
    user = models.ForeignKey(User, related_name='habits', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    frequency = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class HabitUpdate(models.Model):
    habit = models.ForeignKey(Habit, related_name='updates', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='habit_updates', on_delete=models.CASCADE)
    content = models.TextField(null=False)
    image = models.ImageField(upload_to='habit_updates/', null=True, blank=True)
    video = models.FileField(upload_to='habit_updates/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

