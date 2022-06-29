from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Inquiry(models.Model):
    """Main model for each inquiry submitted by users"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, null=False)
    inquiry = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
