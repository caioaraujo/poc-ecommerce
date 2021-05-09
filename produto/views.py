from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from .forms import CompraForm
from .models import Produto


class Produtos(TemplateView):
    template_name = 'produto/produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_produtos'] = Produto.objects.all()[:5]
        return context


class ProdutoId(FormView, TemplateView):
    form_class = CompraForm
    template_name = 'produto/produto.html'
    success_url = '/finalizar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produto'] = Produto.objects.get(id=kwargs['produto_id'])
        return context

    def form_valid(self, form):
        # TODO - Salvar compra
        return super().form_valid(form)


class Compra(LoginRequiredMixin, TemplateView):
    login_url = 'login:login_view'
    template_name = 'produto/finalizar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # FIXME
        context['quantidade'] = 7
        context['total'] = 56.7
        return context
