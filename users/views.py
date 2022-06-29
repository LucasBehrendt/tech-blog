from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from .models import Inquiry
from .forms import UserRegisterForm, UserUpdateForm


class Register(CreateView):
    """
    View for registering new users, renders and handles the form.
    Signs the user in and redirects to home page.
    """
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        username = form.cleaned_data.get('username')
        login(self.request, user)
        messages.success(self.request, f'Account created, \
            you are now signed in as {username}!')
        return HttpResponseRedirect(self.success_url)


class Profile(LoginRequiredMixin,
              UserPassesTestMixin,
              UpdateView):
    """
    View for updating user information, renders and handles the form.
    Validates that the signed in user equals the request.user.
    """
    model = User
    form_class = UserUpdateForm
    template_name = 'users/profile.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request,
                         'Your profile was updated successfully!')
        return redirect('profile', pk=user.id)

    def test_func(self):
        user = self.get_object()
        return self.request.user == user


class DeleteUser(LoginRequiredMixin,
                 UserPassesTestMixin,
                 DeleteView):
    """
    View for deleting signed in users account.
    Validates that the signed in user equals the request.user.
    """
    model = User
    template_name = 'users/delete_user.html'
    success_message = 'Your profile has been deleted!'
    success_url = '/'

    # Source: https://stackoverflow.com/questions/24822509/
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteUser, self).delete(request, *args, **kwargs)

    def test_func(self):
        user = self.get_object()
        return self.request.user == user


class SendInquiry(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    View for sending inquiries, renders the form and defines
    the fields. Sends an email with the inquiry to the site admin
    and a copy to the registered email of the signed in user.
    """
    model = Inquiry
    fields = ['inquiry', ]
    success_message = 'Your inquiry has been sent and a \
                       copy was sent to you. Thank you!'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.email = self.request.user.email
        email_username = self.request.user.username
        email_subject = 'New inquiry from: ' + form.instance.email
        email_inquiry = form.cleaned_data.get('inquiry')
        email_message = f'{email_username} wrote:\n"{email_inquiry}"'
        send_mail(
            email_subject, email_message,
            settings.EMAIL_HOST_USER,
            [settings.DEFAULT_FROM_EMAIL, form.instance.email]
        )
        return super().form_valid(form)
