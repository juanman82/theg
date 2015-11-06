# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0007_perfil_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='estado',
            new_name='state',
        ),
    ]
