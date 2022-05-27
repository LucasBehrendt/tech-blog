from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """Main post model"""
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
