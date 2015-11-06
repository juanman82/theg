# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
from django.conf import settings
import localflavor.mx.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0018_auto_20150825_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil_Mujer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_completo', models.CharField(max_length=100, null=True, blank=True)),
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
                ('slug', models.SlugField(max_length=100, null=True, verbose_name=b'Direcci\xc3\xb3n URL', blank=True)),
                ('estatura', models.IntegerField(null=True, blank=True)),
                ('peso', models.CommaSeparatedIntegerField(max_length=3, null=True, blank=True)),
                ('busto', models.IntegerField(null=True, blank=True)),
                ('cintura', models.IntegerField(null=True, blank=True)),
                ('cadera', models.IntegerField(null=True, blank=True)),
                ('color_de_ojos', models.CharField(max_length=3, null=True, blank=True)),
                ('color_de_cabello', models.CharField(max_length=3, null=True, blank=True)),
                ('medida_de_zapato', models.IntegerField(null=True, blank=True)),
                ('agencia', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Talentos Mujeres',
            },
        ),
        migrations.CreateModel(
            name='Perfil_Nina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_completo', models.CharField(max_length=100, null=True, blank=True)),
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
                ('slug', models.SlugField(max_length=100, null=True, verbose_name=b'Direcci\xc3\xb3n URL', blank=True)),
                ('talla', models.IntegerField(null=True, blank=True)),
                ('color_de_ojos', models.CharField(max_length=3, null=True, blank=True)),
                ('color_de_cabello', models.CharField(max_length=3, null=True, blank=True)),
                ('medida_de_zapato', models.IntegerField(null=True, blank=True)),
                ('agencia', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Talentos Ni\xf1as',
            },
        ),
        migrations.CreateModel(
            name='Perfil_Nino',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_completo', models.CharField(max_length=100, null=True, blank=True)),
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
                ('slug', models.SlugField(max_length=100, null=True, verbose_name=b'Direcci\xc3\xb3n URL', blank=True)),
                ('talla', models.IntegerField(null=True, blank=True)),
                ('color_de_ojos', models.CharField(max_length=3, null=True, blank=True)),
                ('color_de_cabello', models.CharField(max_length=3, null=True, blank=True)),
                ('medida_de_zapato', models.IntegerField(null=True, blank=True)),
                ('agencia', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Talentos Ni\xf1os',
            },
        ),
        migrations.DeleteModel(
            name='Mujerdetalle',
        ),
    ]
