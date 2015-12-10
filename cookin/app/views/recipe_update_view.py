from django.views.generic.edit import UpdateView
from app.models import Recipe

class RecipeUpdate(UpdateView):
    model = Recipe
    fields = ['recipe_title',
              'recipe_text',
              'recipe_image',
              'num_servings',
              'prep_time_minutes',
              'cooking_time_minutes']
              
    template_name_suffix = '_update_form'
