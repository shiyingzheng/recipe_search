# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20151209_0631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredient_price_per_unit',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredient_unit',
        ),
        migrations.AddField(
            model_name='ingredient_in_recipe',
            name='unit_name',
            field=models.CharField(default='units', max_length=32),
        ),
        migrations.AddField(
            model_name='recipe',
            name='estimated_cost',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
