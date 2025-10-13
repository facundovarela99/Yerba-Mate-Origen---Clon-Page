from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

# Create your views here.

def shop(request):
    return render (request, 'productos/shop.html', { 'active_page': 'shop' })

def api_productos(request):
    productos = Producto.objects.all()
    data = [
        {
            "id":p.id,
            "nombre": p.nombre,
            "descripcion": p.descripcion,
            "precio": p.precio,
            "stock": p.stock,
            "imagen_url": p.imagen.url if p.imagen else ""
        }
        for p in productos
    ]
    return JsonResponse(data, safe=False)
