from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


class UserForm(forms.Form):

    usuario = forms.CharField(label='Usuário', max_length=100)
    senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(username=cleaned_data['usuario'], password=cleaned_data['senha'])
        if user is None:
            raise ValidationError('Usuário e/ou senha inválidos', code='user_not_found')

        self.user = user
