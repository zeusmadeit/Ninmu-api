from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


app_name = "users"

urlpatterns = [
    path("register/", views.UserRegisterationAPIView.as_view(), name="create-user"),
    path("login/", views.UserLoginAPIView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("logout/", views.UserLogoutAPIView.as_view(), name="logout"),
    path("user", views.UserAPIView.as_view(), name="user-info"),
]

