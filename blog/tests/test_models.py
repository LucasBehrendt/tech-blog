from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment


class TestModels(TestCase):
    """Tests for all blog app models"""

    def setUp(self):
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

    def test_post_model_created_successfully(self):
        post = self.post

        self.assertEqual(post.title, 'test1')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.excerpt, 'testExcerpt')
        self.assertEqual(post.content, 'testContent')

    def test_post_model_str_return(self):
        post = self.post

        self.assertEqual(post.__str__(), post.title)

    def test_post_likes_count(self):
        post = self.post
        user = self.user
        post.likes.add(user)

        self.assertEqual(post.number_of_likes(), 1)

    def test_comment_model_created_successfully(self):
        comment = self.comment

        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post)

    def test_comment_model_str_return(self):
        comment = self.comment

        self.assertEqual(comment.__str__(),
                         f'{comment.author} wrote {comment.body}')
