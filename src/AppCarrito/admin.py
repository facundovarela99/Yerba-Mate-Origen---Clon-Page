from django.contrib import admin
from .models import Compra, subTotalCarrito, usuarios_x_compras, Carrito
from django.core.exceptions import FieldError

# Register your models here.


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('producto_id', 'cantidad', 'precio_total', 'usuario_comprador')
    list_display_links = ('producto_id','usuario_comprador')
    search_fields = ('producto_id', 'usuario_comprador')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_comprador=request.user)

@admin.register(subTotalCarrito)
class SubTotalCarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'subtotal', 'cantidad_total_productos')
    list_display_links = ('usuario',)
    search_fields = ['usuario']

@admin.register(usuarios_x_compras)
class vista_usuarios_x_compras_admin(admin.ModelAdmin):
    list_display = ('usuario_id', 'compra_id')
    list_display_links = ('usuario_id', 'compra_id')
    search_fields = ('usuario_id', 'compra_id') 

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario',)
    search_fields = ('usuario__username',)
    # filter_horizontal = ('compras',)

    def get_form(self, request, obj=None, **kwargs): #Lógica para mostrar los productos del carrito discriminando por carrito de usuario
        # Obtenemos el formulario por defecto
        form = super().get_form(request, obj, **kwargs)

        if obj:

            try:
                form.base_fields['compras'].queryset = Compra.objects.filter(usuario_comprador=obj.usuario)
            except FieldError:

                pass
        else:

            form.base_fields['compras'].queryset = Compra.objects.none()

        return form

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)