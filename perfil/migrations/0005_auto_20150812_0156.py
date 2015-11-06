# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.mx.models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_remove_perfil_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cpostal',
            field=localflavor.mx.models.MXZipCodeField(default=b'', max_length=5),
        ),
        migrations.AddField(
            model_name='perfil',
            name='curp',
            field=localflavor.mx.models.MXCURPField(default=b'', max_length=18),
        ),
        migrations.AddField(
            model_name='perfil',
            name='estado',
            field=localflavor.mx.models.MXStateField(default=b'', max_length=3, choices=[('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHH', 'Chihuahua'), ('CHP', 'Chiapas'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DIF', 'Distrito Federal'), ('DUR', 'Durango'), ('GRO', 'Guerrero'), ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de M\xe9xico'), ('MIC', 'Michoac\xe1n'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo Le\xf3n'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Quer\xe9taro'), ('ROO', 'Quintana Roo'), ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potos\xed'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucat\xe1n'), ('ZAC', 'Zacatecas')]),
        ),
        migrations.AddField(
            model_name='perfil',
            name='rfc',
            field=localflavor.mx.models.MXRFCField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tel',
            field=models.IntegerField(default=b''),
        ),
    ]
