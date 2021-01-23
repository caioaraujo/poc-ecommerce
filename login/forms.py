from django import forms
from django.contrib.auth import authenticate


class UserForm(forms.Form):

    usuario = forms.CharField(label='Usuário', max_length=100)
    senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())

    def is_valid(self):
        user = authenticate(username=self.data['usuario'], password=self.data['senha'])
        if user is None:
            return False

        if user.is_active is False:
            return False

        self.user = user
        return super(UserForm, self).is_valid()
