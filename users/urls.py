from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('signin/', auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='users/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(
        template_name='users/signout.html'), name='signout'),
    path('profile/<int:pk>', views.Profile.as_view(), name='profile'),
    path('profile/delete/<int:pk>', views.DeleteUser.as_view(
        ), name='delete_user'),
]
