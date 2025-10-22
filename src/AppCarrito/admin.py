from django.contrib import admin, messages
from .models import Compra, subTotalCarrito, Carrito
from django.core.exceptions import FieldError

# Register your models here.


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('producto_id', 'cantidad', 'precio_total', 'usuario_comprador')
    list_display_links = ('producto_id','usuario_comprador')
    
    search_fields = ('producto_id__nombre', 'usuario_comprador__username')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario_comprador=request.user)

    def save_model(self, request, obj, form, change):
        """
        Sobrescribe el método de guardado del admin.
        'obj' es la instancia de Compra creada en el formulario del admin.
        'change' es False si es un "Añadir" nuevo, True si es una "Edición".
        """
        
        if not change: 
            try:
                existing_compra = Compra.objects.get(
                    usuario_comprador=obj.usuario_comprador,
                    producto_id=obj.producto_id
                )
                
                existing_compra.cantidad += obj.cantidad 
                
                existing_compra.save()
                
                messages.warning(request, f"Se actualizó la cantidad del producto '{obj.producto_id.nombre}' para el usuario '{obj.usuario_comprador.username}'. No se creó una nueva entrada.")
                
                return 

            except Compra.DoesNotExist:
                pass 
        
        super().save_model(request, obj, form, change)

@admin.register(subTotalCarrito)
class SubTotalCarritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'subtotal', 'cantidad_total_productos')
    list_display_links = ('usuario',)
    search_fields = ['usuario']


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario',)
    search_fields = ('usuario__username',)

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