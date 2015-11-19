from django.forms import ModelForm
from app.models import Recipe
from taggit.forms import *


class AddRecipeForm(ModelForm):
    recipe_tags = TagField()

    class Meta:
        model = Recipe
        fields = ['recipe_title',
                  'recipe_text',
                  "recipe_image",
                  "dietary_restr"]
