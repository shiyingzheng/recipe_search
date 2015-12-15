from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
import uuid
import os

from .ingredient_model import Ingredient
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


class TaggedDietaryRestriction(TaggedItemBase):
    content_object = models.ForeignKey('Recipe')


class TaggedRecipe(TaggedItemBase):
    content_object = models.ForeignKey('Recipe')


class TaggedTool(TaggedItemBase):
    content_object = models.ForeignKey('Recipe')


def recipe_image_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    return "recipe_images/%s%s" % (uuid.uuid4(), extension)


class Recipe(models.Model):
    recipe_title = models.CharField(db_index=True, max_length=200)
    recipe_text = models.TextField(default="Coming soon!")
    recipe_image = models.ImageField(upload_to=recipe_image_name,
                                     blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    recipe_ingredients = models.ManyToManyField(Ingredient,
            through='Ingredient_In_Recipe')
    num_servings = models.IntegerField(default=1,
                                       validators=[MinValueValidator(1)])

    # total time will be a sum of the following two fields
    prep_time_minutes = models.PositiveIntegerField(default=0)
    cooking_time_minutes = models.PositiveIntegerField(default=0)

    estimated_cost = models.PositiveIntegerField(default=0)

    recipe_tags = TaggableManager(through=TaggedRecipe,
                                  related_name="recipe_tags",
                                  blank=True)
    dietary_restrictions = TaggableManager(through=TaggedDietaryRestriction,
                                           related_name="dietary_restrictions",
                                           blank=True)
    tools = TaggableManager(through=TaggedTool,
                            related_name="tools",
                            blank=True)

    def __str__(self):
        return '%s: %s' % (self.recipe_title, self.recipe_text)

    def total_time(self):
        return self.prep_time_minutes + self.cooking_time_minutes

    def relevance(self, my_tools=[]):
        score = 0
        recipe_tools = self.tools.names()
        for tool in recipe_tools:
            if tool in my_tools:
                score += 1
            else:
                score -= 1
        return score

    class Meta:
        app_label = 'app'
