from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Carrito, Producto, Compra
from django.views.generic import ListView
from django.contrib import messages
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
            cantidad = int(request.POST.get('cantidad', 1))
        except (ValueError, TypeError):
            cantidad = 1
        if cantidad < 1:
            cantidad = 1

        compra = Compra(
            producto_id=producto,
            cantidad=cantidad,
            usuario_comprador=request.user
        )
        try:
            compra.save()  # Esto ejecuta toda la lógica de tu models.py
            messages.success(request, "Producto agregado al carrito.")
        except Exception as e:
            messages.error(request, f"Error: {e}")
        return redirect('productos:producto_detalle', pk=producto_id)
    return redirect('productos:producto_detalle', pk=producto_id)



