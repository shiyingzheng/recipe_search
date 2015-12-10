from django.shortcuts import get_object_or_404, render
from app.models import Recipe, Rating, UserProfile
from app.forms import RatingForm, AddRecipeForm
from django.shortcuts import redirect


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    rating_form = RatingForm(request.POST or None)
    if rating_form.is_valid():
        rating = rating_form.save(commit=False)
        rating.rating_recipe = recipe
        rating.rating_user = request.user.profile
        rating.save()
        return redirect(request.path)
    return render(request, 'recipes/recipe_detail.html',
                  {'recipe': recipe, 'form': rating_form})
