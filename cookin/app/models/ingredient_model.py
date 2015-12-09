from django.db import models
from datetime import datetime
import uuid
import os


def ingredient_image_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    return "ingredient_images/%s%s" % (uuid.uuid4(), extension)


class Ingredient(models.Model):
    ingredient_name = models.CharField(db_index=True, max_length=32)
    ingredient_description = models.TextField(default="Coming soon!")
    ingredient_image = models.ImageField(upload_to=ingredient_image_name,
                                     blank=True)
    ingredient_price_per_unit = models.IntegerField(null=True)
    ingredient_unit = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        app_label = 'app'
