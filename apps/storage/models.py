from django.db import models

# Create your models here.

class empleado(models.Model):
    pk_empleado = models.AutoField(primary_key=True, null=False, blank=False)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    apellido = models.CharField(max_length=20, null=False, blank=False)
    dpi = models.CharField(max_length=12, null=False, blank=False)
    telefono = models.CharField(max_length=8, null=False, blank=False)

    class Meta:
        verbose_name='empleado'
        verbose_name_plural='empleados'
        ordering=['nombre']

    def __str__(self):
        return "{0}".format(self.nombre)


class Equipo(models.Model):
    pk_equipo = models.AutoField(primary_key=True, null=False, blank=False)
    codigo_equipo = models.CharField(max_length=9, null=False, blank=False)
    nombre_equipo = models.CharField(max_length=40, null=False, blank=False)
    descripcion_equipo = models.TextField(null=False, blank=False)
    imagen1 = models.URLField(max_length=800, default='https://i.postimg.cc/Y0gkNhTM/3aabe0e9a520b9ad90407a82f85adb42.jpg', null=False, blank=False)
    precio_equipo = models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)

    class Meta:
        verbose_name='Equipo'
        verbose_name_plural='Equipos'
        ordering=['nombre_equipo']

    def __str__(self):
        return "{0}".format(self.nombre_equipo)