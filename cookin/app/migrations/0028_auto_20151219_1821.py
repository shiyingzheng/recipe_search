# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20151219_1750'),
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
