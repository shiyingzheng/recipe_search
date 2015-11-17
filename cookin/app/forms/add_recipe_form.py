from django.forms import ModelForm
from app.models import Recipe


class AddRecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_title',
                  'recipe_text',
                  "recipe_image"]
