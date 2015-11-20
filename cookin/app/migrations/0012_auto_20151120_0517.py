# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0011_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedDietaryRestriction',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TaggedRecipe',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='app.TaggedRecipe', verbose_name='Tags', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='taggedrecipe',
            name='content_object',
            field=models.ForeignKey(to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='taggedrecipe',
            name='tag',
            field=models.ForeignKey(related_name='app_taggedrecipe_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='taggeddietaryrestriction',
            name='content_object',
            field=models.ForeignKey(to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='taggeddietaryrestriction',
            name='tag',
            field=models.ForeignKey(related_name='app_taggeddietaryrestriction_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dietary_restrictions',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='app.TaggedDietaryRestriction', verbose_name='Tags', to='taggit.Tag'),
        ),
    ]
