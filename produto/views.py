from django.views.generic import TemplateView

from .models import Produto


class Produtos(TemplateView):

    template_name = 'produto/produtos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lista_produtos'] = Produto.objects.all()[:5]
        return context
