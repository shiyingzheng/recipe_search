from django.shortcuts import redirect, render
from app.models import Recipe
from app.forms import AddRecipeForm
from app.views import recipe_detail


def add_new_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(recipe_detail, recipe_id=post.pk)
    else:
        form = AddRecipeForm()

    return render(request,
                  'recipes/add_new_recipe_form.html',
                  {'form': form})
