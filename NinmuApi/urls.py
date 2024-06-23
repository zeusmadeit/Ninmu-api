"""NinmuApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from NinmuApi import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Ninmu API",
        default_version='v1',
        description="API documentation for Ninmu project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path('', views.send_test_data, name='home'), # Link the view to a URL
    path('api/v1/', include('users.urls', namespace="users")),
    path('api/v1/goals/', include('goals.urls')),
    path('api/v1/social/', include('social.urls')),
    path('api/v1/challenges/', include('challenges.urls')),
    path('api/v1/notifications/', include('notifications.urls')),
    path('api/v1/circles/', include('circles.urls')),
    # path('api/v1/recommendations/', include('recommendations.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += i18n_patterns(path("admin/", admin.site.urls))