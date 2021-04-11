from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.test import TestCase
from model_mommy import mommy

from .forms import CadastroForm, UserForm


class TestLogoutView(TestCase):
    def setUp(self):
        self.user = mommy.make(User, username='Usuario1')

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/login.html')
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)


class TestLoginView(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Usuario1', password='123abc')

    def test_login__success(self):
        response = self.client.post('/login.html', {"usuario": "Usuario1", "senha": "123abc"})

        self.assertRedirects(response, '/', status_code=302)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)


class TestForms(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='Usuario1', password='123abc', email='aaa@123.com')

    def test_user_form__success(self):
        form = UserForm(data={'usuario': 'Usuario1', 'senha': '123abc'})

        self.assertTrue(form.is_valid())

    def test_user_form__user_not_found(self):
        form = UserForm(data={'usuario': 'usuario', 'senha': 'senha'})

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, "user_not_found"))

    def test_cadastro_form__success(self):
        form = CadastroForm(
            data={
                'nome': 'John',
                'sobrenome': 'Lennon',
                'email': 'john@lennon.com',
                'usuario': 'j.lennon',
                'senha': '123abc',
                'senha2': '123abc',
            }
        )

        self.assertTrue(form.is_valid())

    def test_cadastro_form__email_already_exists(self):
        form = CadastroForm(
            data={'nome': 'AAA', 'email': 'aaa@123.com', 'usuario': '123abc', 'senha': '123abc', 'senha2': '123abc'}
        )

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, "email_already_exists"))
