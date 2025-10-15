from django.contrib import admin
from .models import Producto
# Register your models here.


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'stock')
    list_display_links = ('nombre',)
    search_fields = ['nombre']