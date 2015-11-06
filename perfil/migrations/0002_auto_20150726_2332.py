# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen1',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagen2',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagen3',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='perfil',
            name='imagen4',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
