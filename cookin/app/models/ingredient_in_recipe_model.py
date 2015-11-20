from django.db import models

from .recipe_model import Recipe
from .ingredient_model import Ingredient


class Ingredient_In_Recipe(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    num_units = models.IntegerField()

    def __str__(self):
        return '%s: %d %s' % (self.recipe.title, self.num_units,
                self.ingredient.name)

    class Meta:
        app_label = 'app'

