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
            field=models.CharField(db_index=True, max_length=32),
        ),
    ]
