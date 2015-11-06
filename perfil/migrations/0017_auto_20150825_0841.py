# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0016_remove_perfil_hombre_detalle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_hombre',
            name='perfil_detallado',
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='cadera',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='cintura',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='color_de_ojos',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='cuello',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='estatura',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='medida_de_zapato',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='peso',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='saco',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Hombresdetalle',
        ),
    ]
