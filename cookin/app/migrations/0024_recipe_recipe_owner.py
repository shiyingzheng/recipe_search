# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20151216_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_owner',
            field=models.ForeignKey(to='app.UserProfile', related_name='owner_recipe', blank=True, null=True),
        ),
    ]
