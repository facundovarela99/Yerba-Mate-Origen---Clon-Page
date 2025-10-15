from django.contrib import admin
from .models import Carrito

# Register your models here.


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('producto_id', 'cantidad', 'precio_total', 'usuario_comprador')
    list_display_links = ('producto_id','usuario_comprador')
    search_fields = ('producto_id', 'usuario_comprador')