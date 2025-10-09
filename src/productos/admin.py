from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Producto)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock')
    list_display_links = ('nombre',)
    search_fields = ('nombre')