# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0011_auto_20150812_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='rango_min',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
