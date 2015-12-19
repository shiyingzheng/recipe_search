# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rating_rating_num_servings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_text',
            field=models.TextField(default='Share your recipe instructions here!'),
        ),
    ]
