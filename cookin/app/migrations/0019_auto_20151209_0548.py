# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20151130_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(max_length=32, db_index=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_title',
            field=models.CharField(max_length=200, db_index=True),
        ),
    ]
