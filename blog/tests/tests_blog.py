from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog

class BlogTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        Blog.objects.create(title='Test Blog', subtitle='Subtitle', body='Body', author=self.user)

    def test_blog_creation(self):
        blog = Blog.objects.get(title='Test Blog')
        self.assertEqual(blog.subtitle, 'Subtitle')