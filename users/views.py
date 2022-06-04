from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.views.generic import UpdateView
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


def register(request):
    """Main view when registering new users"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, \
                you are now logged in as {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
