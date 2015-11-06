# -*- encoding: utf-8 -*-
from django.contrib import admin
from haystack.admin import SearchModelAdmin
# Register your models here.
from perfil.models import Perfil_Hombre
from perfil.models import Perfil_Mujer
from perfil.models import Perfil_Nina
from perfil.models import Perfil_Nino



class PerfilHombreAdmin(SearchModelAdmin):

    search_fields = ['nombre_completo', 'pais', 'nacimiento', 'rango_min', 'rango_max', 'pais', 'estado', 'rfc', 'curp',
                     'cpostal', 'tel',]
    list_display = ['nombre_completo','pais','image_thumb',]



    readonly_fields = ['image_thumb']













admin.site.register(Perfil_Hombre,PerfilHombreAdmin)

class PerfilMujerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Perfil_Mujer)

class PerfilNinoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Perfil_Nino)

class PerfilNinaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Perfil_Nina)




