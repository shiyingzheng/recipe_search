from django.db import models

from .recipe_model import Recipe


class Tag(models.Model):
    tag_name = models.CharField(max_length=32)
    tag_recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return name

    class Meta:
        app_label = 'app'
