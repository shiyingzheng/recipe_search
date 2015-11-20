from django.shortcuts import redirect, render
from app.models import Recipe
from app.forms import AddRecipeForm
from app.views import recipe_detail


def add_new_recipe(request):
    valid = True

    if request.method == "POST":
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            tags = form.cleaned_data.get('recipe_tags').split()
            for tag in tags:
                post.recipe_tags.add(tag)
            post = form.save()
            return redirect(recipe_detail, recipe_id=post.pk)
        else:
            valid = False
    else:
        form = AddRecipeForm()

    return render(request,
                  'recipes/add_new_recipe_form.html',
                  {'form': form, 'valid': valid})
