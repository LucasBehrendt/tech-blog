from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """Main post model"""
    title = models.CharField(max_length=150)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    excerpt = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', default='placeholder', blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True, related_name='post_like')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Main comment model"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author} wrote {self.body}'
