from django.db import models
from django.utils import timezone
from datetime import timedelta

class Pedido(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(default='example@example.com')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    tipo_producto = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.IntegerField(default=1, null=True)
    peso = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    medida_ancho = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    medida_largo = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    medida_alto = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    direccion_recogida = models.CharField(max_length=100, null=True)
    fecha_recogida = models.DateField(default=timezone.now() + timedelta(days=1))
    direccion_envio = models.TextField(max_length=100, null=True)
    fecha_entrega = models.DateField(default=timezone.now() + timedelta(days=7))

    def __str__(self):
        return self.nombre