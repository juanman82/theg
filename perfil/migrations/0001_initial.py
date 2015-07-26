# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=30)),
                ('a_paterno', models.CharField(max_length=30)),
                ('a_matermo', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30, null=True)),
                ('nacimiento', models.DateField(auto_now_add=True)),
                ('rango_min', models.IntegerField()),
                ('rango_max', models.IntegerField()),
                ('pais', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=30, null=True)),
                ('tel', models.IntegerField()),
                ('agencia', models.CharField(max_length=30, null=True)),
                ('tel_agencia', models.CharField(max_length=15, null=True)),
                ('activo', models.BooleanField(default=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Vista de Perfiles',
            },
        ),
    ]
