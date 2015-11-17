from django.db import models
from datetime import datetime

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=200)
    recipe_text = models.TextField(default="Coming soon!")
    publish_date = models.DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return '%s %s' % (self.recipe_title, self.recipe_text)

    class Meta:
        app_label = 'app'

