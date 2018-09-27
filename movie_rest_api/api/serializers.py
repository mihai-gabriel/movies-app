from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Movie, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'first_name', 'last_name', 'email',)


class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = ('pk', 'title', 'user', 'user_username', 'movie', 'timestamp', 'review_text',)


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'description', 'published_date', 'author', 'reviews',)


