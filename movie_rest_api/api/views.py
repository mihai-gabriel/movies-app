from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserSerializer

# Create your views here.
class HomeAPIView(APIView):
    def get(self, request, format=None):
        return Response({ 'success': 'API intialized' })


class UpdateUserAPIView(APIView):
    def get(self, request, format=None):
        user = UserSerializer(request.user)
        return Response(user.data)


class CurrentUserAPIView(APIView):
    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            user = UserSerializer(user)
            return Response({'success': 'Logged in', 'user': user.data})
        return Response({'wrong': 'username or password not correct, try again'}, status=status.HTTP_401_UNAUTHORIZED)
