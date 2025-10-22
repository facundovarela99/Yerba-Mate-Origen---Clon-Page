from django.db import models
from productos.models import Producto
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import F

# Create your models here.

class Compra(models.Model):
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE) 
    cantidad = models.PositiveIntegerField(default=1) 
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    usuario_comprador = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    def clean(self):
        old_cantidad = 0
        if self.pk: 
            try:
                
                old_cantidad = Compra.objects.get(pk=self.pk).cantidad
            except Compra.DoesNotExist:
                pass 
        
        cantidad_a_validar = self.cantidad - old_cantidad

        
        if cantidad_a_validar > 0: 
            self.producto_id.refresh_from_db() # Asegurarse de tener el stock actualizado
            if cantidad_a_validar > self.producto_id.stock:
                raise ValidationError(f'No hay suficiente stock. Solo puedes agregar {self.producto_id.stock} unidades más.')
    
    def substraer_stock(self, cantidad_a_substraer):
        
        self.producto_id.stock = F('stock') - cantidad_a_substraer
        self.producto_id.save(update_fields=['stock'])
        self.producto_id.refresh_from_db() 
    @transaction.atomic
    def save(self, *args, **kwargs):
        old_cantidad = 0
        if self.pk:
            try:
                old_compra = Compra.objects.get(pk=self.pk)
                old_cantidad = old_compra.cantidad
            except Compra.DoesNotExist:
                pass
        cantidad_a_substraer = self.cantidad - old_cantidad
        self.clean()
        self.precio_total = self.producto_id.precio * self.cantidad
        self.full_clean()
        super().save(*args, **kwargs)

        if cantidad_a_substraer != 0:
            self.substraer_stock(cantidad_a_substraer)

        subtotalcarrito, _ = subTotalCarrito.objects.get_or_create(usuario=self.usuario_comprador)
        subtotalcarrito.actualizar_subtotal()
        
        
        if old_cantidad == 0 and self.cantidad > 0:
            carrito, _ = Carrito.objects.get_or_create(usuario=self.usuario_comprador)
            
            carrito.compras.add(self)


    def __str__(self):
        return f'{self.producto_id.nombre} × {self.cantidad} - ${self.precio_total}'
    
    
class subTotalCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    cantidad_total_productos = models.PositiveIntegerField(default=0)
    compras = models.ManyToManyField(Compra, blank=True)

    def actualizar_subtotal(self):
        carrito_items = Compra.objects.filter(usuario_comprador=self.usuario) # Obtener todos los items del carrito del usuario
        self.subtotal = sum(item.precio_total for item in carrito_items) # Calcular el subtotal sumando los precios totales de cada item
        self.cantidad_total_productos = sum(item.cantidad for item in carrito_items) # Calcular la cantidad total de productos
        self.save() # Guardar los cambios en el modelo

    def __str__(self):
        return f'Subtotal del carrito: ${self.subtotal} de {self.usuario.username} - Cantidad total de productos: {self.cantidad_total_productos}'
    
    class Meta:
        verbose_name = 'Subtotal Carrito'
        verbose_name_plural = 'Subtotales Carrito'

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    compras = models.ManyToManyField(Compra, blank=True, related_name='carritos')

    def __str__(self):
        return f'Carrito de {self.usuario.username}'

