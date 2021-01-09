from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Produto


class Produtos(LoginRequiredMixin, TemplateView):
    login_url = 'login:login_view'
    template_name = 'produto/produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_produtos'] = Produto.objects.all()[:5]
        return context
