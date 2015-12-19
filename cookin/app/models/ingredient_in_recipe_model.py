from django.db import models

from .recipe_model import Recipe
from .ingredient_model import Ingredient
from django.core.validators import MinValueValidator


class Ingredient_In_Recipe(models.Model):
    recipe = models.ForeignKey(Recipe)
    ingredient = models.ForeignKey(Ingredient)
    num_units = models.FloatField(validators=[MinValueValidator(0)])
    unit_name = models.CharField(max_length=32, default="units")

    def __str__(self):
        return '%s: %d %s' % (self.recipe.recipe_title, self.num_units,
                self.ingredient.ingredient_name)

    class Meta:
        app_label = 'app'

