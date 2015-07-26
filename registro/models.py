from django.db import models

# Create your models here.
class Registro(models.Model):
    email = models.EmailField(max_length=30)
    nombre_usuario = models.CharField(max_length=20)

    def __str__(self):
        return  self.nombre_usuario
    class Meta:
            verbose_name_plural = "registros"