from django.test import TestCase
from freezegun import freeze_time
from model_mommy import mommy

from .models import Produto


class TestModels(TestCase):

    def setUp(self):
        self.produto = mommy.make('Produto', id=15, nome='Super produto')

    @freeze_time('2018-01-01 08:45')
    def test_cria_produto(self):
        produto = Produto()
        produto.nome = 'Componente X'
        produto.codigo = '1RTTR34S2'
        produto.marca = 'ACME'
        produto.valor = '33.56'
        produto.quantidade_disponivel = 45
        produto.save()

        self.assertIsNotNone(produto.id)
        self.assertEqual('2018-01-01 08:45', produto.data_criado.strftime('%Y-%m-%d %H:%M'))
        self.assertEqual('2018-01-01 08:45', produto.data_alterado.strftime('%Y-%m-%d %H:%M'))
        self.assertEqual('Componente X', produto.nome)
        self.assertEqual('ACME', produto.marca)
        self.assertEqual('33.56', produto.valor)
        self.assertEqual('1RTTR34S2', produto.codigo)
        self.assertEqual(45, produto.quantidade_disponivel)

    @freeze_time('2019-05-22 22:12')
    def test_altera_produto(self):
        produto = Produto.objects.get(id=15)
        data_criado_esperado = produto.data_criado
        produto.nome = 'ABC123'
        produto.save()

        self.assertEqual('ABC123', produto.nome)
        self.assertEqual('2019-05-22 22:12', produto.data_alterado.strftime('%Y-%m-%d %H:%M'))
        self.assertEqual(data_criado_esperado, produto.data_criado)

    def test_str(self):
        produto = Produto.objects.get(id=15)
        self.assertEqual('Super produto', str(produto))
