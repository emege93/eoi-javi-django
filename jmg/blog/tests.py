from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', password='admin')

    def test_is_published_return_false(self):
        post = Post.objects.create(author=user, title='mi titulo')

        is_published = post.is_published()

        self.assertFalse(is_published)
