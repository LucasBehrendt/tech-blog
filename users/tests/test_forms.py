from django.test import TestCase, Client
from django.contrib.auth.models import User
from users.forms import UserRegisterForm, UserUpdateForm


class TestForm(TestCase):
    """Tests for users app forms"""

    def test_user_register_form(self):
        form = UserRegisterForm(
            data={
                'username': 'testUser',
                'email': 'test@email.com',
                'password1': 'testpassword',
                'password2': 'testpassword',
            }
        )

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data['username'], 'testUser')
        self.assertEqual(form.data['email'], 'test@email.com')
        self.assertEqual(form.data['password1'], 'testpassword')
        self.assertEqual(form.data['password2'], 'testpassword')

    def test_user_register_form_invalid_data(self):
        form = UserRegisterForm(
            data={
                'username': 'testUser',
                'email': 'test@email.com',
                'password1': 'testpass',
                'password2': 'testpassword',
            }
        )

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'][0],
                         'The two password fields didn’t match.')

    def test_user_update_form(self):
        user = User.objects.create_user(
            username='testUser', password='testpassword', email='test@test.com'
        )
        logged_in = Client().login(
            username='testuser', password='testpassword'
        )

        form = UserUpdateForm(
            data={
                'username': 'testUser_updated',
                'email': 'test_updated@email.com',
            }, user=user
        )

        self.assertTrue(logged_in)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.data['username'], 'testUser_updated')
        self.assertEqual(form.data['email'], 'test_updated@email.com')
