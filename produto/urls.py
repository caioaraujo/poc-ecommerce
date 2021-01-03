from django.urls import path

from . import views

urlpatterns = [
    path('', views.Produtos.as_view(), name='produtos'),
]
