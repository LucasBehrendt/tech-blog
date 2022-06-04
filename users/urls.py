from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('signin/', auth_views.LoginView.as_view(
        template_name='users/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(
        template_name='users/signout.html'), name='signout'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
]
