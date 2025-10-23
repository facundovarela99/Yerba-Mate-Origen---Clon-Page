from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Carrito, Producto, Compra
from django.views.generic import ListView
from django.contrib import messages
from django.core.exceptions import ValidationError
# Create your views here.

def finalizarLaCompra(request):
    return render(request, 'AppCarrito/finalizarLaCompra.html')
    
def carrito_list(request):
    mis_carritos = Carrito.objects.filter(usuario=request.user)
    return render(request, "AppCarrito/carrito.html", {"object_list": mis_carritos})

def agregar_al_carrito(request, producto_id):
    if request.method == "POST":
        producto = get_object_or_404(Producto, pk=producto_id)
        try:
            cantidad_a_agregar = int(request.POST.get('cantidad', 1))
        except (ValueError, TypeError):
            cantidad_a_agregar = 1
        if cantidad_a_agregar < 1:
            cantidad_a_agregar = 1

        compra, created = Compra.objects.get_or_create(
            producto_id=producto,
            usuario_comprador=request.user,
            defaults={'cantidad':0, 'precio_total':0}
        )
        compra.cantidad += cantidad_a_agregar
        try:
            compra.save()  # Esto ejecuta toda la lógica de tu models.py
            if created:
                messages.success(request, f"Producto {producto.nombre} agregado al carrito.")
            else:
                messages.success(request, f'Se actualizó la cantidad de {producto.nombre}')
        except Exception as e:
                    # Captura cualquier otro error
                    messages.error(request, f"Error inesperado al guardar: {e}")
                    
        return redirect('productos:producto_detalle', pk=producto_id)
                
    return redirect('productos:producto_detalle', pk=producto_id)


def vaciar_carrito(request: HttpRequest) -> HttpResponse: #Vista para vaciar el carrito de un usuario al hacer click en el botón "Vaciar carrito"
    query = Carrito.objects.filter(usuario=request.user).first()
    query.compras.all().delete()
    if query:
        query.delete()
    return redirect('AppCarrito:carrito')
