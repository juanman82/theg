# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0009_auto_20150812_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='state',
            new_name='estado',
        ),
    ]
