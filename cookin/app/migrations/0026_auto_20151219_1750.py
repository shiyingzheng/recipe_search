# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rating_rating_num_servings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient_in_recipe',
            name='unit_name',
            field=models.CharField(max_length=32, default=''),
        ),
    ]
