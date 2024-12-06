from django.db import models
from usuarios.models import Usuario

# Create your models here.


class Prenda(models.Model):
    TIPO_PRENDA_CHOICES = [
        ('pantalon', 'Pantalon'),
        ('camisa', 'Camisa'),
        ('calcetines', 'Calcetines'),
        ('blusa', 'Blusa'),
        ('vestido', 'Vestido'),
        ('completada', 'Completada'),
        ('traje', 'Traje'),
        ('jeans', 'Jeans'),
        ('ropa interior', 'Ropa Interior'),
        ('ropa de baño', 'Ropa de Baño'),
        ('ropa de cama', 'Ropa de Cama'),
    ]

    tipo_prenda = models.CharField(max_length=50, choices=TIPO_PRENDA_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    def __str__(self):
        return self.tipo_prenda


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

# Creacion de modelo de Orden de servicio


class OrdenDeServicio(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('proceso', 'En Proceso'),
        ('completada', 'Completada')
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    # Se asocia mas de una prenda a la orden y la misma prenda puede estar en varias ordenes
    prendas = models.ManyToManyField(Prenda, related_name='ordenes')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # 'pendiente', va el valor no la etiqueta
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default='pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pago_realizado = models.BooleanField(default=False)
    descripcion=models.TextField()

    # Calculo del total de la orden sumando los precios de las prendas asociadas
    def calculo_total(self):
        self.total = sum(prenda.precio for prenda in self.prendas.all())
        self.save()
        return self.total

    def __str__(self):
        return f"Orden #{self.id} - {self.cliente.nombre} - {self.estado} - {self.total}"
