from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Main view when registering new users"""
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)
