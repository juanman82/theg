# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0006_auto_20150812_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='slug',
            field=models.SlugField(max_length=100, null=True, blank=True),
        ),
    ]
