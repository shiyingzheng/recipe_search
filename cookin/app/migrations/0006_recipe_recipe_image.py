# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models.recipe_model


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_recipe_recipe_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image',
            field=models.ImageField(blank=True, upload_to=app.models.recipe_model.recipe_image_name),
        ),
    ]
