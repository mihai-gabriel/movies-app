from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer

# Create your views here.
class HomeAPIView(APIView):
    permission_classes = ()
    def get(self, request, format=None):
        return Response({ 'success': 'API intialized' }) # quick check if server is set-up