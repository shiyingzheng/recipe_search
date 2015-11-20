# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0013_auto_20151120_0500'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedDietaryRestriction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedRecipe',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedTool',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_tags',
            field=taggit.managers.TaggableManager(through='app.TaggedRecipe', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.'),
        ),
        migrations.AddField(
            model_name='taggedtool',
            name='content_object',
            field=models.ForeignKey(to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='taggedtool',
            name='tag',
            field=models.ForeignKey(to='taggit.Tag', related_name='app_taggedtool_items'),
        ),
        migrations.AddField(
            model_name='taggedrecipe',
            name='content_object',
            field=models.ForeignKey(to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='taggedrecipe',
            name='tag',
            field=models.ForeignKey(to='taggit.Tag', related_name='app_taggedrecipe_items'),
        ),
        migrations.AddField(
            model_name='taggeddietaryrestriction',
            name='content_object',
            field=models.ForeignKey(to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='taggeddietaryrestriction',
            name='tag',
            field=models.ForeignKey(to='taggit.Tag', related_name='app_taggeddietaryrestriction_items'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dietary_restrictions',
            field=taggit.managers.TaggableManager(through='app.TaggedDietaryRestriction', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tools',
            field=taggit.managers.TaggableManager(through='app.TaggedTool', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.'),
        ),
    ]
