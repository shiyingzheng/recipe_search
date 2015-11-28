from django.db import models
from django.utils import timezone
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
    recipe_title = models.CharField(max_length=200)
    recipe_text = models.TextField(default="Coming soon!")
    recipe_image = models.ImageField(upload_to=recipe_image_name,
                                     blank=True)
    publish_date = models.DateTimeField(default=timezone.now)
    recipe_ingredients = models.ManyToManyField(Ingredient,
            through='Ingredient_In_Recipe')

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

    class Meta:
        app_label = 'app'
