from django.contrib import admin
from .models import Gestor_Banco, Pedido_Materiais

# Register your models here.
class Gestor_BancoAdmin(admin.ModelAdmin):
    list_display = ("GESTOR_BANCO","Descricao",'Codigo_Banco')
    ordering = ['Codigo_Banco']
    search_fields = ['Codigo_Banco']
    list_filter = ("Descricao",)

admin.site.register(Gestor_Banco, Gestor_BancoAdmin)

class Pedido_MateriaisAdmin(admin.ModelAdmin):
    list_display = ("PEDIDO","EMPRESA",'COTACAO')
    ordering = ['PEDIDO']
    search_fields = ['PEDIDO']
    list_filter = ("PEDIDO",)

admin.site.register(Pedido_Materiais, Pedido_MateriaisAdmin)
