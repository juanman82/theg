# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0019_auto_20150825_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil_hombre',
            old_name='agencia',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='perfil_mujer',
            old_name='agencia',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='perfil_nina',
            old_name='agencia',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='perfil_nino',
            old_name='agencia',
            new_name='usuario',
        ),
    ]
