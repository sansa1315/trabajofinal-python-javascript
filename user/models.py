from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    CATEGORIA = (
        ('Electrodomesticos' , 'Electrodomesticos'),
        ('Electrónica', 'Electrónica'),
        ('Deportes', 'Deportes'),
        ('Bebés', 'Bebés'),
        ('Hogar', 'Hogar')
    )

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    categoria = models.CharField(max_length=50, choices=CATEGORIA)
    date_created = models.DateTimeField(auto_now_add=True)
    # imagen = models.CharField(max_length=100, null=True)
    imagen = models.ImageField(upload_to="productos", blank=True, null=True)

class Order(models.Model):
    usuario = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Producto, null=True, on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

class Categorias(models.Model):
    descripcion = models.CharField(max_length=50)