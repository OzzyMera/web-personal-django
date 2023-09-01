from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()
    opciones = models.CharField(max_length=10, choices=[('Compra', 'Compra'), ('Vende', 'Vende')])
    propiedad = models.CharField(max_length=100)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    contacto_preferido = models.CharField(max_length=10, choices=[('telefono', 'Teléfono'), ('email', 'E-mail')])
    fecha_contacto = models.DateField(null=True, blank=True)
    hora_contacto = models.TimeField(null=True, blank=True)
