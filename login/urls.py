from django.urls import path

from . import views

app_name = "login"
urlpatterns = [
    path("login.html", views.Login.as_view(), name="login_view"),
    path("logout", views.Logout.as_view(), name="logout"),
    path("cadastro.html", views.Cadastro.as_view(), name="cadastro"),
    path("endereco.html", views.CadastroEndereco.as_view(), name="endereco"),
]
