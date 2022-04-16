from django import forms

FORMA_PAGAMENTO_CHOICES = (
    ("1", "Boleto"),
    ("2", "Débito"),
    ("3", "Crédito"),
    ("4", "Pix")
)


class CompraForm(forms.Form):

    quantidade = forms.IntegerField(label="Qtde.", min_value=1)
    marca = forms.CharField(widget=forms.HiddenInput(), required=False)
    codigo = forms.CharField(widget=forms.HiddenInput(), required=False)
    nome = forms.CharField(widget=forms.HiddenInput(), required=False)
    valor = forms.CharField(widget=forms.HiddenInput(), required=False)


class FormaPagamentoForm(forms.Form):

    forma_pagamento = forms.ChoiceField(choices=FORMA_PAGAMENTO_CHOICES)
