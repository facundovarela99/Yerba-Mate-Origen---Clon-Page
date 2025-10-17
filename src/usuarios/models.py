from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto
from AppCarrito.models import Compra
# Create your models here.

class User(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    contrasenia = models.CharField(max_length=30)
    email = models.CharField(max_length=100, unique=True)
    compras = models.ManyToManyField('AppCarrito.Compra', blank=True)

    def __str__(self):
        return f'{self.username}'