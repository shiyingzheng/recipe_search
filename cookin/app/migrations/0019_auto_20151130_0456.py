# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import app.models.ratings_model


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20151130_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rating_stars', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('rating_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rating_price', models.IntegerField()),
                ('rating_comment', models.TextField(blank=True, default='Add a comment!')),
                ('rating_image', models.ImageField(blank=True, upload_to=app.models.ratings_model.rating_image_name)),
                ('rating_recipe', models.ForeignKey(related_name='ratings', to='app.Recipe')),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='rating_user',
            field=models.ForeignKey(to='app.UserProfile'),
        ),
    ]
