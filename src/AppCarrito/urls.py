from django.urls import path
from . import views

app_name = 'AppCarrito'

urlpatterns = [
    path('carrito/', views.carrito_list, name='carrito'),
    path('finalizar-la-compra/', views.finalizarLaCompra, name='finalizarLaCompra'),
]