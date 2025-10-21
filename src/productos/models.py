from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200, db_index=True, null=False)
    descripcion = models.TextField(blank=True, null=True, verbose_name='Descripcion')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to="products_images", null=True, blank=True)
    descripcion_larga = models.TextField(blank=True, null=True, verbose_name='Descripcion larga')

    def __str__(self):
        base = f'{self.nombre}'
        return base
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'