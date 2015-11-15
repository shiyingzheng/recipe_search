from django.db import models
from datetime import datetime

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.recipe_title

    class Meta:
        app_label = 'app'
