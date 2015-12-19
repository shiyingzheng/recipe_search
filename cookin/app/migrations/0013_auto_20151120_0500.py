# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models.ingredient_model


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=32)),
                ('ingredient_description', models.TextField(default='Coming soon!')),
                ('ingredient_image', models.ImageField(blank=True)),
                ('ingredient_price_per_unit', models.IntegerField(null=True)),
                ('ingredient_unit', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_In_Recipe',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('num_units', models.IntegerField()),
                ('ingredient', models.ForeignKey(to='app.Ingredient')),
                ('recipe', models.ForeignKey(to='app.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.ManyToManyField(to='app.Ingredient', through='app.Ingredient_In_Recipe'),
        ),
    ]
