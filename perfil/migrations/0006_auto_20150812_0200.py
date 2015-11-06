# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import localflavor.mx.models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0005_auto_20150812_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cpostal',
            field=localflavor.mx.models.MXZipCodeField(max_length=5, null=True),
        ),
    ]
