# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0015_auto_20150825_0527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil_hombre',
            name='detalle',
        ),
    ]
