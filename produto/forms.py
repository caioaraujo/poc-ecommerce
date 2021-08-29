from django import forms


class CompraForm(forms.Form):

    quantidade = forms.IntegerField(label="Qtde.", min_value=1)
    marca = forms.CharField(widget=forms.HiddenInput(), required=False)
    codigo = forms.CharField(widget=forms.HiddenInput(), required=False)
    nome = forms.CharField(widget=forms.HiddenInput(), required=False)
