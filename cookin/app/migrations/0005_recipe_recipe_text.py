# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20151115_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_text',
            field=models.TextField(default='Coming soon!'),
        ),
    ]
