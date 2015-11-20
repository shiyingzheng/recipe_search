# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20151120_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='dietary_restrictions',
            field=taggit.managers.TaggableManager(to='taggit.Tag', blank=True, through='app.TaggedDietaryRestriction', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', blank=True, through='app.TaggedRecipe', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tools',
            field=taggit.managers.TaggableManager(to='taggit.Tag', blank=True, through='app.TaggedTool', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
