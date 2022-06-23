from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from users import views


class TestUrls(TestCase):
    """Tests for all users app urls"""

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class, views.Register)

    def test_signin_url(self):
        url = reverse('signin')
        self.assertEqual(resolve(url).func.view_class, auth_views.LoginView)

    def test_signout_url(self):
        url = reverse('signout')
        self.assertEqual(resolve(url).func.view_class, auth_views.LogoutView)

    def test_profile_url(self):
        url = reverse('profile', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.Profile)

    def test_delete_user_url(self):
        url = reverse('delete_user', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.DeleteUser)

    def test_inquiry_url(self):
        url = reverse('inquiry')
        self.assertEqual(resolve(url).func.view_class, views.SendInquiry)
