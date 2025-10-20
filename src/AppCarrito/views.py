from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Carrito
from django.views.generic import ListView
# Create your views here.

def finalizarLaCompra(request):
    return render(request, 'AppCarrito/finalizarLaCompra.html')
    
def carrito_list(request):
    mis_carritos = Carrito.objects.filter(usuario=request.user)
    return render(request, "AppCarrito/carrito.html", {"object_list": mis_carritos})
