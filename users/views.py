from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm


class Profile(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Profile page view"""
    model = User
    fields = ['username', 'email']
    template_name = 'users/profile.html'
    success_message = 'You profile was updated successfully!'
    success_url = '/profile/{id}'


class Register(SuccessMessageMixin, CreateView):
    """Main view when registering new users"""
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, \
                you are now logged in as {username}!')
            return redirect('home')
