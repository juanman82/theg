# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.mx.models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0010_auto_20150812_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='a_matermo',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='a_paterno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='curp',
            field=localflavor.mx.models.MXCURPField(default=b'', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='estado',
            field=localflavor.mx.models.MXStateField(default=b'', max_length=3, null=True, choices=[('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHH', 'Chihuahua'), ('CHP', 'Chiapas'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DIF', 'Distrito Federal'), ('DUR', 'Durango'), ('GRO', 'Guerrero'), ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de M\xe9xico'), ('MIC', 'Michoac\xe1n'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo Le\xf3n'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Quer\xe9taro'), ('ROO', 'Quintana Roo'), ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potos\xed'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucat\xe1n'), ('ZAC', 'Zacatecas')]),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nacimiento',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombres',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pais',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rango_max',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rango_min',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tel',
            field=models.IntegerField(default=b'', null=True),
        ),
    ]
