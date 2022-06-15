from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):
    """Tests for all users app views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testUser', password='testpassword', email='test@test.com'
        )

    def test_register_page_GET(self):
        url = reverse('register')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_page_POST(self):
        url = reverse('register')
        response = self.client.post(url, {
            'username': 'testUser2',
            'password1': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@email.com',
        })

        user = User.objects.all()

        self.assertEqual(len(user), 2)
        self.assertEqual(user.last().username, 'testUser2')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_profile_page_GET(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('profile', args=[1])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')

    def test_profile_page_POST(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('profile', args=[1])
        response = self.client.post(url, {
            'username': 'testuser_updated',
            'email': 'test@email.com',
        })

        user = User.objects.all()

        self.assertTrue(logged_in)
        self.assertEqual(len(user), 1)
        self.assertEqual(user.first().username, 'testuser_updated')
        self.assertEqual(response.status_code, 302)

    def test_delete_user_page_GET(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('delete_user', args=[1])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/delete_user.html')

    def test_delete_user_page_POST(self):
        self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('delete_user', args=[1])
        response = self.client.post(url)

        user = User.objects.all()

        self.assertEqual(len(user), 0)
        self.assertEqual(user.first(), None)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')
