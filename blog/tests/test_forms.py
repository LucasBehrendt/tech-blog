from django.test import TestCase
from blog.forms import CommentForm


class TestForm(TestCase):
    """Tests for blog app form"""

    def test_comment_form(self):
        form = CommentForm(data={'body': 'testComment'})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.data['body'], 'testComment')

    def test_comment_form_invalid_data(self):
        form = CommentForm(data={'body': ''})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
