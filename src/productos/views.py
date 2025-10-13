from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto

# Create your views here.

def shop(request):
    return render (request, 'productos/shop.html', { 'active_page': 'shop' })

def api_productos(request):
    productos_qs = Producto.objects.all()
    productos = []
    for p in productos_qs:
        productos.append({
            'id': p.id,
            'nombre': getattr(p, 'nombre', ''),
            'descripcion': getattr(p, 'descripcion', ''),
            'precio': str(getattr(p, 'precio', '')),
            'stock': getattr(p, 'stock', 0),
            # include the public URL for the image when available
            'imagen': p.imagen.url if getattr(p, 'imagen') and getattr(p, 'imagen').name else '',
        })
    return JsonResponse(productos, safe=False)
