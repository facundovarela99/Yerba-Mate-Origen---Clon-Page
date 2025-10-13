from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('api/productos/', views.api_productos, name='api_productos'),
]