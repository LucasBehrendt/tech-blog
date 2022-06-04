from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Registration form with additional email field for register page"""
    email = forms.EmailField()

    class Meta:
        """Definition of fields used in form"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
