from django.db import models
from datetime import datetime
import uuid
import os
from taggit.managers import TaggableManager


def recipe_image_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    return "recipe_images/%s%s" % (uuid.uuid4(), extension)


class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    recipe_text = models.TextField(default="Coming soon!")
    recipe_image = models.ImageField(upload_to=recipe_image_name,
                                     blank=True)
    publish_date = models.DateTimeField(default=datetime.utcnow)

    recipe_tags = TaggableManager()
    #recipe_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return '%s: %s' % (self.recipe_title, self.recipe_text)

    class Meta:
        app_label = 'app'
