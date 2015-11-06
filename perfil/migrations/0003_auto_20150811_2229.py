# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20150726_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='pais',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
