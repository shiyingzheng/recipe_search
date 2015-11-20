# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20151120_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_price_per_unit',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_unit',
            field=models.CharField(null=True, max_length=32),
        ),
    ]
