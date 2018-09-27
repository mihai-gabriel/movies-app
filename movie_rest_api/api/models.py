from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    review_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{movie} review by {user}'.format(user=self.user, movie=self.movie)