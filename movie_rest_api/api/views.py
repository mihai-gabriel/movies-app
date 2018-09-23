from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets

from .serializers import UserSerializer, MovieSerializer
from .permissions import OnlyStaffCanPost
from .models import Movie

# Create your views here.
class HomeAPIView(APIView):
    permission_classes = ()
    def get(self, request, format=None):
        return Response({ 'success': 'API intialized' }) # quick check if server is set-up


class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = (OnlyStaffCanPost,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoviesListAPIView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'pk'