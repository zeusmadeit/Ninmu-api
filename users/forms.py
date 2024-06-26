from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ( "avatar", "username", "email", "bio", "first_name", "last_name", "phone_number")


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ( "avatar", "username", "email", "bio", "first_name", "last_name", "phone_number", "address",)
