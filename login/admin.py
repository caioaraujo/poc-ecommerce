from django.contrib import admin

from .models import Endereco


class EnderecoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Endereco, EnderecoAdmin)
