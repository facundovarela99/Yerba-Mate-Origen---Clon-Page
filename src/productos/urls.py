from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'productos'

urlpatterns = [
    # path('shop/', views.shop, name='shop'),
    path('shop/', views.productos_list, name='shop'),
    path('api/productos/', views.api_productos, name='api_productos'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle')
]

if settings.DEBUG: #Etapa de desarrollo
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)