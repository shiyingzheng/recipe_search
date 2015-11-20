# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20151119_1529'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
