from django.shortcuts import get_object_or_404, render
from app.models import Recipe


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
