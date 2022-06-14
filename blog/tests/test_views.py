from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment


class TestViews(TestCase):
    """Tests for all blog app views"""

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testUser', password='testpassword', email='test@test.com'
        )

        self.post = Post.objects.create(
            title='test1',
            author=self.user,
            excerpt='testExcerpt',
            content='testContent',
        )

        self.comment = Comment.objects.create(
            author=self.user,
            body='testComment',
            post=self.post,
        )

    def test_about_page_GET(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/about.html')

    def test_post_list_GET(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_post_detail_GET(self):
        url = reverse('post_detail', args=[1])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_post_detail_POST_adds_comment(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('post_detail', args=[1])
        response = self.client.post(url, {
            'author': self.user,
            'body': 'testComment2',
            'post': self.post,
        })

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.comment_set.last().body, 'testComment2')
        self.assertEqual(self.post.comment_set.count(), 2)

    def test_post_detail_POST_no_data(self):
        url = reverse('post_detail', args=[1])
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.post.comment_set.count(), 1)

    def test_post_create_GET(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('create_post')
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)

    def test_post_create_POST(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('create_post')
        response = self.client.post(url, {
            'title': 'test2',
            'author': self.user,
            'excerpt': 'testExcerpt2',
            'content': 'testContent2',
        })

        post2 = Post.objects.filter(title='test2')

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(post2.first().excerpt, 'testExcerpt2')

    def test_post_update_GET(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('update_post', args=[1])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)

    def test_post_update_POST(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('update_post', args=[1])
        response = self.client.post(url, {
            'title': 'test1 updated',
            'author': self.user,
            'excerpt': 'testExcerpt updated',
            'content': 'testContent updated',
        })

        post_updated = Post.objects.get(id=1)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(post_updated.title, 'test1 updated')
        self.assertEqual(post_updated.content, 'testContent updated')

    def test_post_delete_GET(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('delete_post', args=[1])
        response = self.client.get(url)

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 200)

    def test_post_delete_POST(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )
        url = reverse('delete_post', args=[1])
        response = self.client.post(url)

        post_deleted = Post.objects.all()

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(post_deleted.first())
        self.assertQuerysetEqual(post_deleted, [])

    def test_comment_delete_POST(self):
        logged_in = self.client.login(
            username='testuser', password='testpassword'
        )

        url = reverse('delete_comment', args=[1])
        response = self.client.post(url)

        comment_deleted = Comment.objects.all()

        self.assertTrue(logged_in)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(comment_deleted.first())
        self.assertQuerysetEqual(comment_deleted, [])
