# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0017_auto_20150825_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='perfil_hombre',
            options={'verbose_name_plural': 'Talentos Hombres'},
        ),
        migrations.RemoveField(
            model_name='perfil_hombre',
            name='a_matermo',
        ),
        migrations.RemoveField(
            model_name='perfil_hombre',
            name='a_paterno',
        ),
        migrations.RemoveField(
            model_name='perfil_hombre',
            name='nombres',
        ),
        migrations.AddField(
            model_name='perfil_hombre',
            name='nombre_completo',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil_hombre',
            name='slug',
            field=models.SlugField(max_length=100, null=True, verbose_name=b'Direcci\xc3\xb3n URL', blank=True),
        ),
    ]
