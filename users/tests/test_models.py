from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Inquiry


class TestModels(TestCase):
    """Tests for users app model"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testUser',
            password='testpassword',
            email='test@test.com'
        )

        self.inquiry = Inquiry.objects.create(
            user=self.user,
            email='test@test.com',
            inquiry='testInquiry',
        )

    def test_inquiry_model_created_successfully(self):
        inquiry = self.inquiry

        self.assertEqual(inquiry.user, self.user)
        self.assertEqual(inquiry.email, 'test@test.com')
        self.assertEqual(inquiry.inquiry, 'testInquiry')

    def test_inquiry_model_str_return(self):
        inquiry = self.inquiry

        self.assertEqual(inquiry.__str__(), inquiry.email)
