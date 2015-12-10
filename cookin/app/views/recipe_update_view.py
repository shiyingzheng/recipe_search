from django.shortcuts import get_object_or_404, render
from django.views.generic import UpdateView
from app.models import Recipe
from app.forms import AddRecipeForm

class RecipeUpdateView(UpdateView):
    model = Recipe
    template_name = 'recipes/recipe_update.html'
    form_class = AddRecipeForm
    success_url = 'app/recipes'
