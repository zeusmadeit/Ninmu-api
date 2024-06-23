from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.mail import send_mail


from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = models.CharField(_("username"), max_length=150, unique=True, null=False, blank=False)
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    picture = models.ImageField()
    first_name = models.CharField(_("first name"), max_length=250)
    last_name = models.CharField(_("last name"), max_length=250)
    phone_number = models.CharField(_("phone number"), max_length=15, unique=True)
    address = models.TextField(_("address"),)
    is_online = models.BooleanField(_("online"), default=False)
    date_joined = models.DateTimeField(_("date joined"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("updated at"), auto_now_add=True)

    # EMAIL_FIELD = "email"
    # USERNAME_FIELD = "username"
    objects = CustomUserManager()

    REQUIRED_FIELDS = ['email', 'first_name', 'phone_number']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of CustomUser."""
        return reverse('account-detail-view', args=[str(self.id)])
    
    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    
    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
