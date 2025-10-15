from django.contrib import admin
from .models import Compra, subTotalCarrito

# Register your models here.


@admin.register(Compra)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('producto_id', 'cantidad', 'precio_total', 'usuario_comprador')
    list_display_links = ('producto_id','usuario_comprador')
    search_fields = ('producto_id', 'usuario_comprador')

@admin.register(subTotalCarrito)
class SubTotalCarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'subtotal', 'cantidad_total_productos')
    list_display_links = ('usuario',)
    search_fields = ['usuario']