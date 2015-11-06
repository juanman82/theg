# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0008_auto_20150812_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='imagen5',
            field=models.ImageField(null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='genero',
            field=models.CharField(default=b'', max_length=2, null=True, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')]),
        ),
    ]
