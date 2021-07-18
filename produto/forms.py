from django import forms


class CompraForm(forms.Form):

    quantidade = forms.IntegerField(label="Qtde.", min_value=1)
