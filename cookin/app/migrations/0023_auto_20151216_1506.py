# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20151212_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient_in_recipe',
            name='num_units',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
