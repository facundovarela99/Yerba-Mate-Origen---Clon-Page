from django.db import models
from productos.models import Producto
from usuarios.models import User

# Create your models here.

class Carrito(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE) #models.CASCADE para que si se borra el producto, se borre del carrito tambien
    cantidad = models.PositiveIntegerField(default=1) #PositiveIntegerField para que no acepte negativos
    precio_total = models.DecimalField(max_digits=10, decimal_places=2) #DecimalField para manejar precios con decimales
    usuario_comprador = models.ForeignKey(User, on_delete=models.CASCADE) #Relacion con el usuario que agrega al carrito
    