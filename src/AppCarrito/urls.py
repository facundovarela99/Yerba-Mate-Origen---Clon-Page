from django.urls import path
from . import views

app_name = 'AppCarrito'

urlpatterns = [
    path('carrito/', views.carrito_list, name='carrito'),
    path('finalizar-la-compra/', views.finalizarLaCompra, name='finalizarLaCompra'),
    path('agregar/<int:producto_id>', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('vaciar-carrito/', views.vaciar_carrito, name='vaciar-carrito'), #Nueva ruta para vaciar el carrito
    path('api/subtotales/', views.api_subtotales, name='api_subtotales'),
]