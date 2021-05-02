from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError


class UserForm(forms.Form):

    usuario = forms.CharField(label='Usuário', max_length=150)
    senha = forms.CharField(label='Senha', max_length=128, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(username=cleaned_data['usuario'], password=cleaned_data['senha'])
        if user is None:
            raise ValidationError('Usuário e/ou senha inválidos', code='user_not_found')

        self.user = user


class CadastroForm(forms.Form):

    nome = forms.CharField(label='Nome', max_length=150)
    sobrenome = forms.CharField(label='Sobrenome', max_length=150, required=False)
    email = forms.EmailField(label='Email')
    usuario = forms.CharField(label='Nome de usuário', max_length=150,
                              help_text='Este nome será utilizado para entrar no site')
    senha = forms.CharField(label='Senha', max_length=128, widget=forms.PasswordInput(), min_length=6,
                            help_text='Escolha uma senha forte, com no mínimo 6 caracteres')
    senha2 = forms.CharField(label='Confirme a senha', max_length=128, widget=forms.PasswordInput())

    def clean_email(self):
        cleaned_data = super().clean()
        UserModel = get_user_model()
        email = cleaned_data['email']
        email_count = UserModel.objects.filter(email=email).count()
        if email_count:
            raise ValidationError('Email já cadastrado', code='email_already_exists')

        return email

    def clean_usuario(self):
        cleaned_data = super().clean()
        UserModel = get_user_model()
        usuario = cleaned_data['usuario']
        usuario_count = UserModel.objects.filter(username=usuario).count()
        if usuario_count:
            raise ValidationError('Usuário já cadastrado', code='username_already_exists')

        return usuario

    def clean(self):
        cleaned_data = super().clean()
        senha1 = cleaned_data['senha']
        senha2 = cleaned_data['senha2']

        if senha1 != senha2:
            raise ValidationError('As senhas digitadas não coincidem', code='passwords_not_match')

    def save_user(self):
        data = self.cleaned_data
        UserModel = get_user_model()

        new_user = UserModel(
            first_name=data['nome'],
            last_name=data.get('sobrenome'),
            email=data['email'],
            username=data['usuario'],
        )
        new_user.set_password(data['senha'])
        new_user.save()

        return new_user
