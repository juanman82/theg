# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
import django_filters
from django_countries.fields import CountryField
from django.template import defaultfilters




from localflavor.mx.models import (MXStateField, MXRFCField, MXCURPField,
                                   MXZipCodeField,)










class Perfil_Hombre(models.Model):
    # MASCULINO = 'M'
    # FEMENINO = 'F'
    # GENERO = (
    #     (MASCULINO,'Masculino'),
    #     (FEMENINO, 'Femenino')
    # )
    usuario = models.ForeignKey(User, null=True, blank=True)
    nombre_completo = models.CharField(max_length=100, null=True, blank=True)


    nacimiento = models.DateField(auto_now_add=True, null=True, )
    rango_min = models.IntegerField(null=True, blank=True,)
    rango_max = models.IntegerField(null=True, blank=True)
    pais = CountryField(max_length=30, null=True, blank=True)
    estado = MXStateField(null=True, default='')
    rfc = MXRFCField(null=True, blank=True)
    curp = MXCURPField(null=True, default='', blank=True)
    cpostal = MXZipCodeField(null=True)
    tel = models.IntegerField(null=True, default='', blank=True)

    tel_agencia = models.CharField(max_length=15, null=True, blank=True)
    activo = models.BooleanField(default=True, blank=True)

    imagen1 = models.ImageField(null=True, blank=True)
    imagen2 = models.ImageField(null=True, blank=True)
    imagen3 = models.ImageField(null=True, blank=True)
    imagen4 = models.ImageField(null=True, blank=True)
    imagen5 = models.ImageField(null=True, blank=True)

    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name="Dirección URL")

    estatura = models.IntegerField( null=True, blank=True)
    peso = models.CommaSeparatedIntegerField(max_length=3,null=True, blank=True)
    cintura = models.CommaSeparatedIntegerField(max_length=3,null=True, blank=True)
    cadera = models.CommaSeparatedIntegerField(max_length=3,null=True, blank=True)
    cuello = models.CommaSeparatedIntegerField(max_length=3,null=True, blank=True)
    saco = models.CommaSeparatedIntegerField(max_length=3,null=True, blank=True)
    color_de_ojos = models.CharField(max_length=3, null=True, blank=True)
    medida_de_zapato = models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)


    def image_thumb(self):
        if self.imagen1 == '':

            return 'No hay imagen'
        else:
            return '<img src="/media/%s"  height="100" />' % (self.imagen1)

    image_thumb.allow_tags = True

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre_completo)
        super(Perfil_Hombre, self).save(*args, **kwargs)

    def __unicode__ (self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = "Talentos Hombres"


class Perfil_Mujer(models.Model):
    # MASCULINO = 'M'
    # FEMENINO = 'F'
    # GENERO = (
    #     (MASCULINO,'Masculino'),
    #     (FEMENINO, 'Femenino')
    # )
    usuario = models.ForeignKey(User, null=True, blank=True)
    nombre_completo = models.CharField(max_length=100, null=True, blank=True)


    nacimiento = models.DateField(auto_now_add=True, null=True, )
    rango_min = models.IntegerField(null=True, blank=True,)
    rango_max = models.IntegerField(null=True, blank=True)
    pais = CountryField(max_length=30, null=True, blank=True)
    estado = MXStateField(null=True, default='')
    rfc = MXRFCField(null=True, blank=True)
    curp = MXCURPField(null=True, default='', blank=True)
    cpostal = MXZipCodeField(null=True)
    tel = models.IntegerField(null=True, default='', blank=True)

    tel_agencia = models.CharField(max_length=15, null=True, blank=True)
    activo = models.BooleanField(default=True, blank=True)

    imagen1 = models.ImageField(null=True, blank=True)
    imagen2 = models.ImageField(null=True, blank=True)
    imagen3 = models.ImageField(null=True, blank=True)
    imagen4 = models.ImageField(null=True, blank=True)
    imagen5 = models.ImageField(null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name="Dirección URL")
    estatura = models.IntegerField( null=True, blank=True)
    peso = models.CommaSeparatedIntegerField( max_length=3, null=True, blank=True)
    busto = models.IntegerField( null=True, blank=True)
    cintura = models.IntegerField( null=True, blank=True)
    cadera = models.IntegerField( null=True, blank=True)
    color_de_ojos  = models.CharField(max_length=3, null=True, blank=True)
    color_de_cabello = models.CharField(max_length=3, null=True, blank=True)
    medida_de_zapato = models.IntegerField( null=True, blank=True)




    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre_completo)
        super(Perfil_Mujer, self).save(*args, **kwargs)

    def __unicode__ (self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = "Talentos Mujeres"


class Perfil_Nino(models.Model):
    # MASCULINO = 'M'
    # FEMENINO = 'F'
    # GENERO = (
    #     (MASCULINO,'Masculino'),
    #     (FEMENINO, 'Femenino')
    # )
    usuario = models.ForeignKey(User, null=True, blank=True)
    nombre_completo = models.CharField(max_length=100, null=True, blank=True)


    nacimiento = models.DateField(auto_now_add=True, null=True, )
    rango_min = models.IntegerField(null=True, blank=True,)
    rango_max = models.IntegerField(null=True, blank=True)
    pais = CountryField(max_length=30, null=True, blank=True)
    estado = MXStateField(null=True, default='')
    rfc = MXRFCField(null=True, blank=True)
    curp = MXCURPField(null=True, default='', blank=True)
    cpostal = MXZipCodeField(null=True)
    tel = models.IntegerField(null=True, default='', blank=True)

    tel_agencia = models.CharField(max_length=15, null=True, blank=True)
    activo = models.BooleanField(default=True, blank=True)

    imagen1 = models.ImageField(null=True, blank=True)
    imagen2 = models.ImageField(null=True, blank=True)
    imagen3 = models.ImageField(null=True, blank=True)
    imagen4 = models.ImageField(null=True, blank=True)
    imagen5 = models.ImageField(null=True, blank=True)

    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name="Dirección URL")

    talla = models.IntegerField( null=True, blank=True)
    color_de_ojos  = models.CharField(max_length=3, null=True, blank=True)
    color_de_cabello = models.CharField(max_length=3, null=True, blank=True)
    medida_de_zapato = models.IntegerField( null=True, blank=True)






    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre_completo)
        super(Perfil_Nino, self).save(*args, **kwargs)

    def __unicode__ (self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = "Talentos Niños"

class Perfil_Nina(models.Model):
    # MASCULINO = 'M'
    # FEMENINO = 'F'
    # GENERO = (
    #     (MASCULINO,'Masculino'),
    #     (FEMENINO, 'Femenino')
    # )
    usuario = models.ForeignKey(User, null=True, blank=True)
    nombre_completo = models.CharField(max_length=100, null=True, blank=True)


    nacimiento = models.DateField(auto_now_add=True, null=True, )
    rango_min = models.IntegerField(null=True, blank=True,)
    rango_max = models.IntegerField(null=True, blank=True)
    pais = CountryField(max_length=30, null=True, blank=True)
    estado = MXStateField(null=True, default='')
    rfc = MXRFCField(null=True, blank=True)
    curp = MXCURPField(null=True, default='', blank=True)
    cpostal = MXZipCodeField(null=True)
    tel = models.IntegerField(null=True, default='', blank=True)

    tel_agencia = models.CharField(max_length=15, null=True, blank=True)
    activo = models.BooleanField(default=True, blank=True)

    imagen1 = models.ImageField(null=True, blank=True)
    imagen2 = models.ImageField(null=True, blank=True)
    imagen3 = models.ImageField(null=True, blank=True)
    imagen4 = models.ImageField(null=True, blank=True)
    imagen5 = models.ImageField(null=True, blank=True)

    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name="Dirección URL")

    talla = models.IntegerField( null=True, blank=True)
    color_de_ojos  = models.CharField(max_length=3, null=True, blank=True)
    color_de_cabello = models.CharField(max_length=3, null=True, blank=True)
    medida_de_zapato = models.IntegerField( null=True, blank=True)






    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.nombre_completo)
        super(Perfil_Nina, self).save(*args, **kwargs)

    def __unicode__ (self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = "Talentos Niñas"