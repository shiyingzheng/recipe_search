# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietaryRestriction',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('restr_name', models.CharField(max_length=200)),
                ('restr_description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='dietary_restr',
            field=models.ManyToManyField(to='app.DietaryRestriction'),
        ),
    ]
