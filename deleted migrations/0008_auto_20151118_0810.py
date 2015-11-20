# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tag_recipes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_tags',
            field=models.ManyToManyField(related_name='tag_recipes', to='app.Tag'),
        ),
    ]
