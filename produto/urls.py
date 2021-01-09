from django.urls import path

from . import views

app_name = 'produto'
urlpatterns = [
    path('', views.Produtos.as_view(), name='produtos'),
]
