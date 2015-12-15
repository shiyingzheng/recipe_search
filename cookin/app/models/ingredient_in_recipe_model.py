from django.db import models

from .recipe_model import Recipe
from .ingredient_model import Ingredient


class Ingredient_In_Recipe(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    num_units = models.IntegerField()
    unit_name = models.CharField(max_length=32, default="units")

    def __str__(self):
        return '%s: %d %s' % (self.recipe.title, self.num_units,
                self.ingredient.name)

    class Meta:
        app_label = 'app'

