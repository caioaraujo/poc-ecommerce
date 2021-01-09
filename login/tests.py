from django.contrib import auth
from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy


class TestLogout(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='Usuario1')

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
