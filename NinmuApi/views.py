# views.py
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

@api_view(['GET'])
def send_test_data(request):
    return Response({
        "data": "Hello from django backend"
    })
