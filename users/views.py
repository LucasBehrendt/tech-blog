from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .forms import UserRegisterForm


class Register(CreateView):
    """Main view when registering new users"""
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        login(self.request, user)
        messages.success(self.request, f'Account created, \
            you are now logged in as {username}!')
        return HttpResponseRedirect(self.success_url)


class Profile(LoginRequiredMixin,
              UserPassesTestMixin,
              SuccessMessageMixin,
              UpdateView):
    """Profile page view"""
    model = User
    fields = ['username', 'email']
    template_name = 'users/profile.html'
    success_message = 'Your profile was updated successfully!'
    success_url = '/profile/{id}'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user


class DeleteUser(LoginRequiredMixin,
                 UserPassesTestMixin,
                 SuccessMessageMixin,
                 DeleteView):
    """User delete view"""
    model = User
    template_name = 'users/delete_user.html'
    success_message = 'Your profile has been deleted!'
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        return self.request.user == user
