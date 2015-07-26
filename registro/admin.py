from django.contrib import admin

# Register your models here.
from perfil.models import Registro

class RegistroAdmin(admin.ModelAdmin):
    fields = ['email', 'nombre_usuario']
    admin.site.register(Registro)