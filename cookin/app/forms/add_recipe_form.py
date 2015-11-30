from django.forms import ModelForm, CharField
from app.models import Recipe


class AddRecipeForm(ModelForm):
    recipe_tags = CharField(required=False)
    dietary_restrictions = CharField(required=False)
    tools = CharField(required=False)
    recipe_ingredients = CharField()

    class Meta:
        model = Recipe
        fields = ['recipe_title',
                  'recipe_text',
                  'recipe_image',
                  'num_servings']
