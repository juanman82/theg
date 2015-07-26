# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User




class Perfil(models.Model):
    user = models.OneToOneField(User, null=True)
    nombres = models.CharField(max_length=30, null=False)
    a_paterno = models.CharField(max_length=30, null=False)
    a_matermo = models.CharField(max_length=30, null=False)
    genero = models.CharField(max_length=30, null=True)
    nacimiento = models.DateField(auto_now_add=True, null=False)
    rango_min = models.IntegerField(null=False)
    rango_max = models.IntegerField(null=False)
    pais = models.CharField(max_length=30, null=False)
    estado = models.CharField(max_length=30, null=True)
    tel = models.IntegerField(null=False)
    agencia = models.CharField(max_length=30, null=True)
    tel_agencia = models.CharField(max_length=15, null=True)
    activo = models.BooleanField(default=True)
    imagen1 = models.ImageField(null=True)
    imagen2 = models.ImageField(null=True)
    imagen3 = models.ImageField(null=True)
    imagen4 = models.ImageField(null=True)

    def __str__(self):
        return self.nombres

    class Meta:
            verbose_name_plural = "Vista de Perfiles"
# class PropertyImage(models.Model):
#     property = Property.objects.get(pk=1)
# image_list = property.images.all()