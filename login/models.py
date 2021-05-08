from django.conf import settings
from django.db import models


class Endereco(models.Model):
    class UF(models.TextChoices):
        ACRE = 'AC'
        ALAGOAS = 'AL'
        AMAPA = 'AP'
        AMAZONAS = 'AM'
        BAHIA = 'BA'
        CEARA = 'CE'
        DISTRITO_FEDERAL = 'DF'
        ESPIRITO_SANTO = 'ES'
        GOIAS = 'GO'
        MARANHAO = 'MA'
        MATO_GROSSO = 'MT'
        MATO_GROSSO_DO_SUL = 'MS'
        MINAS_GERAIS = 'MG'
        PARA = 'PA'
        PARAIBA = 'PB'
        PARANA = 'PR'
        PERNAMBUCO = 'PE'
        PIAUI = 'PI'
        RIO_DE_JANEIRO = 'RJ'
        RIO_GRANDE_DO_NORTE = 'RN'
        RIO_GRANDE_DO_SUL = 'RS'
        RONDONIA = 'RO'
        RORAIMA = 'RR'
        SANTA_CATARINA = 'SC'
        SAO_PAULO = 'SP'
        SERGIPE = 'SE'
        TOCANTINS = 'TO'

    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logradouro = models.CharField(max_length=120)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=120)
    cidade = models.CharField(max_length=120)
    uf = models.CharField(max_length=2, choices=UF.choices)
    cep = models.CharField(max_length=8)
    complemento = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'endereco'
        ordering = ['-id']
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return self.usuario.username
