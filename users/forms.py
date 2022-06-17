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

    def clean(self):
        cleaned_data = super(UserRegisterForm, self).clean()
        username = cleaned_data.get('username')
        if username and User.objects.filter(
                username__iexact=username).exists():
            self.add_error('username',
                           'A user with that username already exists.')
        return cleaned_data
