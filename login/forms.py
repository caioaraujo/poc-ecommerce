from django import forms


class UserForm(forms.Form):
    usuario = forms.CharField(label='Usuário', max_length=100)
    senha = forms.CharField(label='Senha', max_length=100, widget=forms.PasswordInput())
