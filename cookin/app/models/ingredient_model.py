from django.db import models
from datetime import datetime
import uuid
import os


class Ingredient(models.Model):
    ingredient_name = models.CharField(db_index=True, max_length=32)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        app_label = 'app'
