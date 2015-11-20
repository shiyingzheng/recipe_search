# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151119_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_price_per_unit',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_unit',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
