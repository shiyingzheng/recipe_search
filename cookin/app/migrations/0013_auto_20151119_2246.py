# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20151119_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_tags',
            field=taggit.managers.TaggableManager(blank=True, to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem', verbose_name='Tags'),
        ),
    ]
