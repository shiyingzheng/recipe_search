# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_recipe_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
