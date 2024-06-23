from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ( "username", "email", "first_name", "last_name", "is_premium", "is_staff", "is_active", "date_joined",)
    list_filter = ("is_staff", "is_active", "is_premium", "date_joined",)
    fieldsets = (
        (None, {'fields': ('avatar', 'username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'address', 'phone_number',)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("username",)
    ordering = ("username", "date_joined",)


admin.site.register(CustomUser, CustomUserAdmin)
