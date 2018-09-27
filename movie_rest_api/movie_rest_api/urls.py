"""movie_rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)
from api import views

router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet, 'movies')
router.register(r'reviews', views.ReviewsViewSet, 'reviews')
router.register(r'users', views.UsersViewSet, 'users')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeAPIView.as_view()),
    
    # auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/api-token-auth/', obtain_jwt_token),
    path('api/api-token-verify/', verify_jwt_token),
    path('api/api-token-refresh/', refresh_jwt_token),

    # movies
    path('api/', include(router.urls)),
    # path('api/movies/', views.MoviesListAPIView.as_view()),
]
