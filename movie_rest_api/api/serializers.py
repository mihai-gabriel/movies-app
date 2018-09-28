from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Movie, Review


class UserSerializer(serializers.ModelSerializer):
    get_absolute_url = serializers.SerializerMethodField(method_name='custom_absolute_url')

    def custom_absolute_url(self, obj):
        return '/user/{id}/'.format(id=obj.pk)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'get_absolute_url',
        )
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }


class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Review
        fields = (
            'pk',
            'title',
            'user',
            'user_username',
            'movie',
            'timestamp',
            'review_text',
        )


class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('pk', 'title', 'description', 'published_date', 'author', 'reviews',)


