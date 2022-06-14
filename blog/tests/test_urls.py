from django.test import TestCase
from django.urls import reverse, resolve
from blog import views


class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, views.PostList)

    def test_post_detail_url(self):
        url = reverse('post_detail', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.PostDetail)

    def test_create_post_url(self):
        url = reverse('create_post')
        self.assertEqual(resolve(url).func.view_class, views.PostCreate)

    def test_update_post_url(self):
        url = reverse('update_post', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.PostUpdate)

    def test_delete_post_url(self):
        url = reverse('delete_post', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.PostDelete)

    def test_post_like_url(self):
        url = reverse('post_like', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.PostLike)

    def test_delete_comment_url(self):
        url = reverse('delete_comment', args=[5])
        self.assertEqual(resolve(url).func.view_class, views.CommentDelete)

    def test_about_url(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func.view_class, views.About)
