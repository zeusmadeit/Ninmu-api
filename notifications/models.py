from django.db import models
from users.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    content = models.TextField(null=False)
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
