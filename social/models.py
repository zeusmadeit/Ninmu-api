from django.db import models
from users.models import User
from habits.models import HabitUpdate

class Comment(models.Model):
    habit_update = models.ForeignKey(HabitUpdate, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Like(models.Model):
    habit_update = models.ForeignKey(HabitUpdate, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

