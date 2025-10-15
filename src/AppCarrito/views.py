from django.shortcuts import render

# Create your views here.

def carrito(request):
    return render(request, 'AppCarrito/carrito.html')

def finalizarLaCompra(request):
    return render(request, 'AppCarrito/finalizarLaCompra.html')