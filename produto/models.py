from django.db import models


class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, help_text="Nome do produto")
    codigo = models.CharField(max_length=250, help_text="Código do produto")
    marca = models.CharField(max_length=250, help_text="Nome da fabricante")
    quantidade_disponivel = models.IntegerField(help_text="Quantidade em estoque")
    valor = models.DecimalField(max_digits=20, decimal_places=2, help_text="Valor em BRL")
    data_criado = models.DateTimeField(auto_now_add=True)
    data_alterado = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'produto'
        ordering = ['-id']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
