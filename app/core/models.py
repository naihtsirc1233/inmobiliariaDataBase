from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Persons(models.Model):
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    name = models.CharField(max_length=250, default="", editable=True, verbose_name='Nombres')
    direccion = models.TextField(null=True, verbose_name='Dirección')
    telefono1 = models.CharField(max_length=12, verbose_name='telefono', default="", editable=True)
    telefono2 = models.CharField(max_length=12, verbose_name='telefono 2', default="", editable=True)
    date_joined = models.DateTimeField(default=datetime.now, verbose_name='Fecha de Registro')
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state_existente = models.BooleanField(default=True)
    def __str__(self):
        return 'Telefono: {}     /    Nombre:  {}'.format(self.telefono1, self.name)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['id']


class Inmueble(models.Model):
    propietario = models.ForeignKey(Persons, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=150, verbose_name='Dirección Inmueble')
    TipoInmueble = models.CharField(max_length=150, verbose_name='Tipo de inmueble')
    Estado = models.CharField(max_length=150, verbose_name='Vendido o no')
    Pisos = models.PositiveIntegerField(default=0, verbose_name='Cantidad de pisos')
    PrecioTotalBase = models.DecimalField(default=0, max_digits=9, decimal_places=2,
                                          verbose_name='Precio base del inmueble')
    PrecioTotal = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Precio Total')
    cantidadMetrado = models.DecimalField(default=0.00, max_digits=9, decimal_places=2,
                                          verbose_name='Cantidad de metrado')
    PrecioMetro = models.DecimalField(default=0, max_digits=9, decimal_places=2,
                                      verbose_name='Precio por metro cuadrado')
    PrecioVenta = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Precio de Venta')
    tamañoBase = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Tamaño de Base')
    tamañoAlto = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Tamaño de alto')
    observacion = models.CharField(max_length=1200, verbose_name='Observaciones')
    Referencias = models.CharField(max_length=1200, verbose_name='Referencias')

    def __str__(self):
        return 'Tipo Inmueble:         {}       /       Propietario:          {} '.format(self.TipoInmueble,self.propietario)

    class Meta:
        verbose_name = 'Inmueble'
        verbose_name_plural = 'inmueble'
        ordering = ['id']
