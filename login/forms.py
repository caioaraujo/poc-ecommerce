from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError

from .models import Endereco


class UserForm(forms.Form):

    usuario = forms.CharField(label="Usuário", max_length=150)
    senha = forms.CharField(label="Senha", max_length=128, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        user = authenticate(
            username=cleaned_data["usuario"], password=cleaned_data["senha"]
        )
        if user is None:
            raise ValidationError("Usuário e/ou senha inválidos", code="user_not_found")

        self.user = user


class CadastroForm(forms.Form):

    nome = forms.CharField(label="Nome", max_length=150)
    sobrenome = forms.CharField(label="Sobrenome", max_length=150, required=False)
    email = forms.EmailField(label="Email")
    usuario = forms.CharField(
        label="Nome de usuário",
        max_length=150,
        help_text="Este nome será utilizado para entrar no site",
    )
    senha = forms.CharField(
        label="Senha",
        max_length=128,
        widget=forms.PasswordInput(),
        min_length=6,
        help_text="Escolha uma senha forte, com no mínimo 6 caracteres",
    )
    senha2 = forms.CharField(
        label="Confirme a senha", max_length=128, widget=forms.PasswordInput()
    )

    def clean_email(self):
        cleaned_data = super().clean()
        UserModel = get_user_model()
        email = cleaned_data["email"]
        email_count = UserModel.objects.filter(email=email).count()
        if email_count:
            raise ValidationError("Email já cadastrado", code="email_already_exists")

        return email

    def clean_usuario(self):
        cleaned_data = super().clean()
        UserModel = get_user_model()
        usuario = cleaned_data["usuario"]
        usuario_count = UserModel.objects.filter(username=usuario).count()
        if usuario_count:
            raise ValidationError(
                "Usuário já cadastrado", code="username_already_exists"
            )

        return usuario

    def clean(self):
        cleaned_data = super().clean()
        senha1 = cleaned_data["senha"]
        senha2 = cleaned_data["senha2"]

        if senha1 != senha2:
            raise ValidationError(
                "As senhas digitadas não coincidem", code="passwords_not_match"
            )

    def save_user(self):
        data = self.cleaned_data
        UserModel = get_user_model()

        new_user = UserModel(
            first_name=data["nome"],
            last_name=data.get("sobrenome"),
            email=data["email"],
            username=data["usuario"],
        )
        new_user.set_password(data["senha"])
        new_user.save()

        return new_user


class EnderecoForm(forms.Form):
    uf_list = (
        ("AC", "AC"),
        ("AL", "AL"),
        ("AP", "AP"),
        ("AM", "AM"),
        ("BA", "BA"),
        ("CE", "CE"),
        ("DF", "DF"),
        ("ES", "ES"),
        ("GO", "GO"),
        ("MA", "MA"),
        ("MT", "MT"),
        ("MS", "MS"),
        ("MG", "MG"),
        ("PA", "PA"),
        ("PB", "PB"),
        ("PR", "PR"),
        ("PE", "PE"),
        ("PI", "PI"),
        ("RJ", "RJ"),
        ("RN", "RN"),
        ("RS", "RS"),
        ("RO", "RO"),
        ("RR", "RR"),
        ("SC", "SC"),
        ("SP", "SP"),
        ("SE", "SE"),
        ("TO", "TO"),
    )

    logradouro = forms.CharField(label="Logradouro", max_length=120)
    numero = forms.IntegerField(label="Número")
    bairro = forms.CharField(label="Bairro", max_length=120)
    cidade = forms.CharField(label="Cidade", max_length=120)
    uf = forms.ChoiceField(label="UF", choices=uf_list)
    cep = forms.CharField(
        label="CEP", max_length=8, min_length=8, help_text="Somente números"
    )
    complemento = forms.CharField(label="Complemento", required=False)

    def clean_cep(self):
        cleaned_data = super().clean()
        cep = cleaned_data["cep"]
        if not cep.isnumeric():
            raise ValidationError(
                "CEP inválido. Informe somente números", code="invalid_cep"
            )

        return cep

    def save_endereco(self, user):
        data = self.cleaned_data
        endereco = Endereco()
        endereco.usuario = user
        endereco.logradouro = data["logradouro"]
        endereco.cep = data["cep"]
        endereco.numero = data["numero"]
        endereco.bairro = data["bairro"]
        endereco.cidade = data["cidade"]
        endereco.uf = data["uf"]
        endereco.complemento = data.get("complemento")
        endereco.save()
