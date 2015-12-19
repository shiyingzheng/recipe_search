# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_recipe_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='rating_num_servings',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
