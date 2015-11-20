# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import app.models.ingredient_model


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=32)),
                ('ingredient_description', models.TextField(default='Coming soon!')),
                ('ingredient_image', models.ImageField(blank=True, upload_to=app.models.ingredient_model.ingredient_image_name)),
                ('ingredient_price_per_unit', models.IntegerField()),
                ('ingredient_unit', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_In_Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('num_units', models.IntegerField()),
                ('ingredient', models.ForeignKey(to='app.Ingredient')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient_in_recipe',
            name='recipe',
            field=models.ForeignKey(to='app.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_ingredients',
            field=models.ManyToManyField(to='app.Ingredient', through='app.Ingredient_In_Recipe'),
        ),
    ]
