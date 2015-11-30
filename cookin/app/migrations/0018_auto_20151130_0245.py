# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_recipe_num_servings'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time_minutes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time_minutes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
