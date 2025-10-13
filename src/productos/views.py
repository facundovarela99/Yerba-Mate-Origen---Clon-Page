from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

# Create your views here.

def shop(request):
    return render (request, 'productos/shop.html', { 'active_page': 'shop' })

def api_productos(request):
    productos = list(Producto.objects.values())
    return JsonResponse(productos, safe=False)
