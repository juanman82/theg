# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import localflavor.mx.models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0013_auto_20150812_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hombresdetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estatura', models.IntegerField(max_length=3, null=True, blank=True)),
                ('peso', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('cintura', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('cadera', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('cuello', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('saco', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('color_de_ojos', models.CharField(max_length=3, null=True, blank=True)),
                ('medida_de_zapato', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mujerdetalle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estatura', models.IntegerField(max_length=3, null=True, blank=True)),
                ('peso', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('busto', models.IntegerField(max_length=3, null=True, blank=True)),
                ('cintura', models.IntegerField(max_length=3, null=True, blank=True)),
                ('cadera', models.IntegerField(max_length=3, null=True, blank=True)),
                ('color_de_ojos', models.CharField(max_length=3, null=True, blank=True)),
                ('color_de_cabello', models.CharField(max_length=3, null=True, blank=True)),
                ('medida_de_zapato', models.IntegerField(max_length=3, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil_Hombre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=30, null=True, blank=True)),
                ('a_paterno', models.CharField(max_length=30, null=True, blank=True)),
                ('a_matermo', models.CharField(max_length=30, null=True, blank=True)),
                ('nacimiento', models.DateField(auto_now_add=True, null=True)),
                ('rango_min', models.IntegerField(null=True, blank=True)),
                ('rango_max', models.IntegerField(null=True, blank=True)),
                ('pais', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('estado', localflavor.mx.models.MXStateField(default=b'', max_length=3, null=True, choices=[('AGU', 'Aguascalientes'), ('BCN', 'Baja California'), ('BCS', 'Baja California Sur'), ('CAM', 'Campeche'), ('CHH', 'Chihuahua'), ('CHP', 'Chiapas'), ('COA', 'Coahuila'), ('COL', 'Colima'), ('DIF', 'Distrito Federal'), ('DUR', 'Durango'), ('GRO', 'Guerrero'), ('GUA', 'Guanajuato'), ('HID', 'Hidalgo'), ('JAL', 'Jalisco'), ('MEX', 'Estado de M\xe9xico'), ('MIC', 'Michoac\xe1n'), ('MOR', 'Morelos'), ('NAY', 'Nayarit'), ('NLE', 'Nuevo Le\xf3n'), ('OAX', 'Oaxaca'), ('PUE', 'Puebla'), ('QUE', 'Quer\xe9taro'), ('ROO', 'Quintana Roo'), ('SIN', 'Sinaloa'), ('SLP', 'San Luis Potos\xed'), ('SON', 'Sonora'), ('TAB', 'Tabasco'), ('TAM', 'Tamaulipas'), ('TLA', 'Tlaxcala'), ('VER', 'Veracruz'), ('YUC', 'Yucat\xe1n'), ('ZAC', 'Zacatecas')])),
                ('rfc', localflavor.mx.models.MXRFCField(max_length=13, null=True, blank=True)),
                ('curp', localflavor.mx.models.MXCURPField(default=b'', max_length=18, null=True, blank=True)),
                ('cpostal', localflavor.mx.models.MXZipCodeField(max_length=5, null=True)),
                ('tel', models.IntegerField(default=b'', null=True, blank=True)),
                ('tel_agencia', models.CharField(max_length=15, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen1', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('imagen2', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('imagen3', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('imagen4', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('imagen5', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('slug', models.SlugField(max_length=100, null=True, blank=True)),
                ('agencia', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('detalle', models.ManyToManyField(to='perfil.Mujerdetalle')),
                ('perfil_detallado', models.OneToOneField(null=True, blank=True, to='perfil.Hombresdetalle')),
            ],
            options={
                'verbose_name_plural': 'Vista de Perfiles',
            },
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='user',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
