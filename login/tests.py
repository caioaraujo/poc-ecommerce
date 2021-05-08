from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.exceptions import NON_FIELD_ERRORS
from django.test import TestCase

from .forms import CadastroForm, UserForm
from .models import Endereco


class TestViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='Usuario1', password='123abc')

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get('/logout', follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/')
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_login__success(self):
        response = self.client.post('/login.html', {"usuario": "Usuario1", "senha": "123abc"})

        self.assertRedirects(response, '/', status_code=302)
        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def test_cadastro__success(self):
        data = {
            'nome': 'Test123',
            'sobrenome': 'Silva',
            'email': 'teste@123.com',
            'usuario': 'Usuario2',
            'senha': '123abc',
            'senha2': '123abc',
        }
        response = self.client.post('/cadastro.html', data)

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

    def test_cadastro_form__clean_data_success(self):
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
        self.assertTrue(form.has_error(field='email', code='email_already_exists'))

    def test_cadastro_form__username_already_exists(self):
        form = CadastroForm(
            data={'nome': 'AAA', 'email': 'usuer@123.com', 'usuario': 'Usuario1', 'senha': '123abc', 'senha2': '123abc'}
        )

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(field='usuario', code='username_already_exists'))

    def test_cadastro_form__passwords_not_match(self):
        form = CadastroForm(
            data={'nome': 'AAA', 'email': 'usuer@123.com', 'usuario': 'Usuario2', 'senha': '123abc', 'senha2': 'abc123'}
        )

        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error(NON_FIELD_ERRORS, code='passwords_not_match'))

    def test_cadastro_form__save_user_success(self):
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
        new_user = form.save_user()
        self.assertEqual('John', new_user.first_name)
        self.assertEqual('Lennon', new_user.last_name)
        self.assertEqual('john@lennon.com', new_user.email)
        # Assert password was saved encrypted
        self.assertTrue(new_user.password)
        self.assertNotEqual('123abc', new_user.password)


class TestModels(TestCase):

    def setUp(self):
        get_user_model().objects.create_user(id=1, username='Usuario1')

    def test_cria_endereco(self):
        endereco = Endereco()
        endereco.usuario_id = 1
        endereco.cep = '88123321'
        endereco.logradouro = 'Penny Lane'
        endereco.bairro = 'Strawberry fields'
        endereco.numero = 92
        endereco.cidade = 'Florianópolis'
        endereco.uf = 'SC'
        endereco.complemento = 'Próximo a Abbey Road'
        endereco.save()

        self.assertIsNotNone(endereco.id)
        self.assertEqual('88123321', endereco.cep)
        self.assertEqual('Penny Lane', endereco.logradouro)
        self.assertEqual('Strawberry fields', endereco.bairro)
        self.assertEqual(92, endereco.numero)
        self.assertEqual('Florianópolis', endereco.cidade)
        self.assertEqual('SC', endereco.uf)
        self.assertEqual('Próximo a Abbey Road', endereco.complemento)
