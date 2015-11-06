# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0014_auto_20150825_0522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hombresdetalle',
            name='estatura',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mujerdetalle',
            name='busto',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mujerdetalle',
            name='cadera',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mujerdetalle',
            name='cintura',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mujerdetalle',
            name='estatura',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mujerdetalle',
            name='medida_de_zapato',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
