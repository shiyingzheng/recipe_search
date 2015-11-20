# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('app', '0012_auto_20151120_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedTool',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content_object', models.ForeignKey(to='app.Recipe')),
                ('tag', models.ForeignKey(to='taggit.Tag', related_name='app_taggedtool_items')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='tools',
            field=taggit.managers.TaggableManager(to='taggit.Tag', help_text='A comma-separated list of tags.', verbose_name='Tags', through='app.TaggedTool'),
        ),
    ]
