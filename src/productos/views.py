from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto
from django.http import HttpRequest, HttpResponse

# Create your views here.

#Vista basada en función que devuelve un JsonResponse con todos los productos en formato JSON
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

#Vista basada en función que renderiza el template shop.html con todos los productos o los productos filtrados por búsqueda para así poder acceder al producto_detalle según el producto seleccionado
def productos_list(request: HttpRequest) -> HttpResponse:
    search = request.GET.get('query')
    if search:
        queryset = Producto.objects.filter(name__icontains=request.GET.get('query'))
    else:
        queryset = Producto.objects.all()
    context = {'active_page': 'shop'}
    context2 = context.copy()
    context2.update({'object_list':queryset})
    return render(request, 'productos/shop.html', context2)

# Vista basada en función para acceder a un solo template con la información del producto seleccionado por id
def producto_detalle(request: HttpRequest, pk: id) -> HttpResponse:
    query = Producto.objects.get(id=pk)
    return render(request, 'productos/producto_detalle.html', {'object': query})
