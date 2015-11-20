from django.forms import ModelForm, CharField
from app.models import Recipe


class AddRecipeForm(ModelForm):
    recipe_tags = CharField(required = False)

    class Meta:
        model = Recipe
        fields = ['recipe_title',
                  'recipe_text',
                  "recipe_image"]
