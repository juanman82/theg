from django.contrib import admin

# Register your models here.
from perfil.models import Perfil


class PerfilAdmin(admin.ModelAdmin):
    fields = ['user','nombres', 'a_paterno', 'a_materno', 'genero', 'nacimiento', 'rango_min', 'rango_max',
              'pais', 'estado', 'email', 'tel', 'agencia', 'tel_agencia', 'activo']
    admin.site.register(Perfil)
