from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, FormView

from .forms import CompraForm
from .models import Produto


class Produtos(TemplateView):
    template_name = "produto/produtos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lista_produtos"] = Produto.objects.all()[:5]
        return context


class ProdutoId(FormView, TemplateView):
    form_class = CompraForm
    template_name = "produto/produto.html"
    success_url = "/finalizar"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produto"] = Produto.objects.get(id=kwargs["produto_id"])
        return context

    def form_valid(self, form):
        compra = form.cleaned_data
        self.request.session["quantidade"] = compra["quantidade"]
        self.request.session["marca"] = compra["marca"]
        self.request.session["codigo"] = compra["codigo"]
        self.request.session["nome"] = compra["nome"]
        self.request.session["total"] = self.calcula_total(compra)
        return super().form_valid(form)

    def calcula_total(self, compra):
        quantidade = compra["quantidade"]
        valor = compra["valor"].replace(",", ".")
        return str(quantidade * Decimal(valor))


class Compra(LoginRequiredMixin, TemplateView):
    login_url = "login:login_view"
    template_name = "produto/finalizar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quantidade"] = self.request.session["quantidade"]
        context["marca"] = self.request.session["marca"]
        context["codigo"] = self.request.session["codigo"]
        context["nome"] = self.request.session["nome"]
        context["total"] = self.request.session["total"]
        return context
