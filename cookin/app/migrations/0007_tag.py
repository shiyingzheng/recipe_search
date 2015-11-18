# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_recipe_recipe_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('tag_name', models.CharField(max_length=32)),
                ('tag_recipes', models.ManyToManyField(to='app.Recipe')),
            ],
        ),
    ]
