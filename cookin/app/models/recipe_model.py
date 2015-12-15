from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.text import slugify
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

    def average_cost_estimate(self):
        cost = self.estimated_cost
        recipe_ratings = self.ratings.all()
        if len(recipe_ratings) == 0:
            return cost
    
        cost_sum = 0
        num_estimates = 0
        if cost:
            cost_sum += cost / self.num_servings
            num_estimates += 1
        for rating in recipe_ratings:
            if rating.rating_price:
                cost_sum += rating.rating_price  * 1.0
                num_estimates += 1
        return cost_sum / num_estimates
            
    def relevance(self, my_tools=[]):
        my_tools = map(slugify, my_tools)
        score = 0
        recipe_tools = self.tools.slugs()
        for tool in recipe_tools:
            if tool in my_tools:
                score += 1
            else:
                score -= 1
        return score

    class Meta:
        app_label = 'app'
