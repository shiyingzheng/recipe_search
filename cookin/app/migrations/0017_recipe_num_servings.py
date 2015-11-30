# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20151130_0022'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='num_servings',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], default=1),
        ),
    ]
