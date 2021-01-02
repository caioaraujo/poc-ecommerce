from django.contrib import admin

from .models import Produto


class ProdutoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Produto, ProdutoAdmin)
