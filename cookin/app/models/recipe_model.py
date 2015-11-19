from django.db import models
from datetime import datetime
import uuid
import os
<<<<<<< HEAD

from .tag_model import Tag
from .ingredient_model import Ingredient
=======
from taggit.managers import TaggableManager
>>>>>>> c16bc6f72f5be8ce99bc5b250252111121c1ac54


def recipe_image_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    return "recipe_images/%s%s" % (uuid.uuid4(), extension)


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    recipe_text = models.TextField(default="Coming soon!")
    recipe_image = models.ImageField(upload_to=recipe_image_name,
                                     blank=True)
    publish_date = models.DateTimeField(default=datetime.utcnow)
    recipe_ingredients = models.ManyToManyField(Ingredient,
            through='Ingredient_In_Recipe')
    recipe_tags = TaggableManager()

    def __str__(self):
        return '%s: %s' % (self.recipe_title, self.recipe_text)

    class Meta:
        app_label = 'app'
