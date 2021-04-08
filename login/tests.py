from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.test import TestCase
from model_mommy import mommy

from .forms import UserForm


class TestLogoutView(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='Usuario1')

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)


class TestLoginView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Usuario1', password='123abc')

    def test_login__success(self):
        response = self.client.post('/', {"usuario": "Usuario1", "senha": "123abc"})

        self.assertRedirects(response, '/produtos/', status_code=302)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)


class TestForms(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='Usuario1', password='123abc')
        get_user_model().objects.create_user(username='Usuario2', password='AAA123', is_active=False)

    def test_user_form__success(self):
        form = UserForm(data={'usuario': 'Usuario1', 'senha': '123abc'})

        self.assertTrue(form.is_valid())

    def test_user_form__user_not_found(self):
        form = UserForm(data={'usuario': 'usuario', 'senha': 'senha'})

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, "user_not_found"))
