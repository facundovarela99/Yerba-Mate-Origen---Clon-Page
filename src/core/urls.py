from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('home/', views.index, name='index'), #posteriormente debe pasar a ser 'home/'
    path('donde-comprar/', views.dondeComprar, name='dondeComprar'),
]