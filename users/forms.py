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
        # check if case insensitive username exists
        # source: https://simpleisbetterthancomplex.com/tutorial/
        # 2017/02/06/how-to-implement-case-insensitive-username.html
        cleaned_data = super(UserRegisterForm, self).clean()
        username = cleaned_data.get('username')
        if username and User.objects.filter(
                username__iexact=username).exists():
            self.add_error('username',
                           'A user with that username already exists.')
        return cleaned_data


class UserUpdateForm(forms.ModelForm):
    """Update form with additional email field for profile page"""
    email = forms.EmailField()

    class Meta:
        """Definition of fields used in form"""
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        # get request.user in form to check for unchanged username
        # source: https://stackoverflow.com/questions/1202839/
        self.user = kwargs.pop('user', None)
        super(UserUpdateForm, self).__init__(*args, **kwargs)

    def clean(self):
        # check if case insensitive username exists
        # source: https://simpleisbetterthancomplex.com/tutorial/
        # 2017/02/06/how-to-implement-case-insensitive-username.html
        cleaned_data = super(UserUpdateForm, self).clean()
        username = cleaned_data.get('username')
        if self.user.username == username:
            return cleaned_data
        elif username and User.objects.filter(
                username__iexact=username).exists():
            self.add_error('username',
                           'A user with that username already exists.')
        return cleaned_data
