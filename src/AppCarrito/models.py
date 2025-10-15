from django.db import models
from productos.models import Producto
from usuarios.models import User
from django.core.exceptions import ValidationError
from django.db import transaction

# Create your models here.

class Compra(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE) #models.CASCADE para que si se borra el producto, se borre del carrito tambien
    cantidad = models.PositiveIntegerField(default=1) #PositiveIntegerField para que no acepte negativos
    precio_total = models.DecimalField(max_digits=10, decimal_places=2) #DecimalField para manejar precios con decimales
    usuario_comprador = models.ForeignKey(User, on_delete=models.CASCADE) #Relacion con el usuario que agrega al carrito
    
    def clean(self):
        if self.cantidad > self.producto_id.stock:
            raise ValidationError('La cantidad no puede ser mayor al stock')
    
    def substraer_stock(self):
        self.producto_id.stock -= self.cantidad
        self.producto_id.save()

    @transaction.atomic
    def save(self, *args, **kwargs):
        subtotalcarrito = subTotalCarrito.objects.get_or_create(usuario=self.usuario_comprador)[0]
        self.clean()
        self.precio_total = self.producto_id.precio * self.cantidad
        self.full_clean()
        super().save(*args, **kwargs)
        self.substraer_stock()
        subtotalcarrito.actualizar_subtotal()

class subTotalCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cantidad_total_productos = models.PositiveIntegerField(default=0)

    def actualizar_subtotal(self):
        carrito_items = Compra.objects.filter(usuario_comprador=self.usuario) # Obtener todos los items del carrito del usuario
        self.subtotal = sum(item.precio_total for item in carrito_items) # Calcular el subtotal sumando los precios totales de cada item
        self.cantidad_total_productos = sum(item.cantidad for item in carrito_items) # Calcular la cantidad total de productos
        self.save() # Guardar los cambios en el modelo

    def __str__(self):
        return f'Subtotal del carrito: ${self.subtotal} - Cantidad total de productos: {self.cantidad_total_productos}'
    
    class Meta:
        verbose_name = 'Subtotal Carrito'
        verbose_name_plural = 'Subtotales Carrito'
 


    