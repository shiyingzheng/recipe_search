# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_rating_rating_num_servings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredient_description',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='ingredient_image',
        ),
    ]
