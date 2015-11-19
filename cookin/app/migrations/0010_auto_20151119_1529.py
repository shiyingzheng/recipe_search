# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0009_auto_20151119_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_tags',
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags', through='taggit.TaggedItem'),
        ),
    ]
