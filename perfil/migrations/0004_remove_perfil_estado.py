# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_auto_20150811_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='estado',
        ),
    ]
