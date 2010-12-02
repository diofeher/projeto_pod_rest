from django.contrib import admin
from server.models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Produto, ProdutoAdmin)
