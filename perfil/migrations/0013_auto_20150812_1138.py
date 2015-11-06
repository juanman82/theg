# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import localflavor.mx.models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0012_auto_20150812_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='a_matermo',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='a_paterno',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='agencia',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='curp',
            field=localflavor.mx.models.MXCURPField(default=b'', max_length=18, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen1',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen2',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen3',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen4',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen5',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombres',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pais',
            field=django_countries.fields.CountryField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rango_max',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='rfc',
            field=localflavor.mx.models.MXRFCField(max_length=13, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tel',
            field=models.IntegerField(default=b'', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
