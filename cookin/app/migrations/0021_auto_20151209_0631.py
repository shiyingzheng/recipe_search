# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20151209_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating_price',
            field=models.PositiveIntegerField(),
        ),
    ]
