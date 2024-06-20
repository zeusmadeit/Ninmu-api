from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name', 'phone_number']
    
    name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of CustomUser."""
        return reverse('account-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
