from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.utils.text import slugify
from django.db.models import Avg
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
    recipe_owner = models.ForeignKey('UserProfile', blank=True, null=True,
                                        related_name='owner_recipe')

    def __str__(self):
        return '%s: %s' % (self.recipe_title, self.recipe_text)

    def total_time(self):
        return self.prep_time_minutes + self.cooking_time_minutes

    def average_cost_estimate_per_serving(self):
        cost = self.estimated_cost
        recipe_ratings = self.ratings.all()
        cost_sum = 0
        num_estimates = 0
        if cost:
            cost_sum += (cost / self.num_servings)
            num_estimates += 1
        for rating in recipe_ratings:
            if rating.rating_price:
                cost_sum += rating.rating_price / rating.rating_num_servings
                num_estimates += 1
        if not num_estimates:
            return 0
        return cost_sum / num_estimates

    def average_cost_estimate(self):
        def truncate_2_places(x):
            return int(x * 100)/100

        return truncate_2_places(self.average_cost_estimate_per_serving()) * self.num_servings

    def relevance(self, my_tools=[], sort_by = ""):
        def sort_relevance(sort_param):
            fields = {
                "time":-self.total_time(),
                "cost":-self.average_cost_estimate()/self.num_servings,
                "rating":self.average_rating()
            }
            if sort_param in fields:
                return fields[sort_param]
            return 0

        score = 0
        if my_tools:
            my_tools = map(slugify, my_tools)
            recipe_tools = self.tools.slugs()
            for tool in recipe_tools:
                if tool in my_tools:
                    score += 1
                else:
                    score -= 1

        score += sort_relevance(sort_by) * .01
        return score



    def average_rating(self):
        qs = self.ratings.all()
        if len(qs) > 0:
            return qs.aggregate(Avg('rating_stars'))['rating_stars__avg']
        return 0

    class Meta:
        app_label = 'app'
