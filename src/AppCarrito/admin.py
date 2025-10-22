from django.contrib import admin, messages
from .models import Compra, subTotalCarrito, Carrito
from django.core.exceptions import FieldError

# Register your models here.


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('producto_id', 'cantidad', 'precio_total', 'usuario_comprador')
    list_display_links = ('producto_id','usuario_comprador')
    
    # Mejora: permite buscar por nombre de producto y de usuario
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
        
        # -----------------------------------------------------------------
        # Aquí aplicamos tu lógica, SOLO si es un objeto NUEVO (change=False)
        # -----------------------------------------------------------------
        if not change: 
            # Caso 1: "si el usuario es el mismo y el producto es el mismo"
            try:
                # Busca si ya existe una compra para ESE usuario y ESE producto
                existing_compra = Compra.objects.get(
                    usuario_comprador=obj.usuario_comprador,
                    producto_id=obj.producto_id
                )
                
                # Si existe, actualiza la cantidad de la compra existente
                existing_compra.cantidad += obj.cantidad 
                
                # Guarda la compra *existente*. Esto disparará el método .save() 
                # corregido del modelo, que recalculará el precio y el stock.
                existing_compra.save()
                
                # Muestra un mensaje de éxito/advertencia en el admin
                messages.warning(request, f"Se actualizó la cantidad del producto '{obj.producto_id.nombre}' para el usuario '{obj.usuario_comprador.username}'. No se creó una nueva entrada.")
                
                # IMPORTANTE: No llamamos a super().save_model()
                # para evitar guardar el 'obj' nuevo que se creó en el formulario.
                return 

            except Compra.DoesNotExist:
                # Caso 2 y 3: "si el usuario es el mismo y el producto es diferente"
                # O "si el usuario es diferente"
                #
                # Si no se encontró (Compra.DoesNotExist), significa que es 
                # una compra nueva y simplemente debe guardarse.
                pass 
        
        # Si 'change' es True (es una edición) O si no se encontró un duplicado,
        # simplemente ejecuta el guardado normal.
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