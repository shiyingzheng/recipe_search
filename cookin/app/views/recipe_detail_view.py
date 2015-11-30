from django.shortcuts import get_object_or_404, render
from app.models import Recipe, Rating
from app.forms import RatingForm


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ratings_form = RatingForm(request.POST or None)
    if ratings_form.is_valid():
    	rating = ratings_form.save(commit=False)
    	rating.rating_recipe = recipe.recipe_id
    	rating.save()
    	return redirect(request.path)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})
