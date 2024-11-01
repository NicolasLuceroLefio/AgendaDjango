from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Telefono(models.Model):
    TIPO_TELEFONO = [
        ('Particular', 'Particular'),
        ('Privado', 'Privado'),
        ('Trabajo', 'Trabajo'),
    ]

    contacto = models.ForeignKey(Contacto, on_delete=models.CASCADE, related_name='telefonos')
    tipo_telefono = models.CharField(max_length=20, choices=TIPO_TELEFONO)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.tipo_telefono} - {self.telefono}"
