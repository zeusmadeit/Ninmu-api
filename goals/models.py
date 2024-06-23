from django.db import models
from users.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, related_name='goals', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
