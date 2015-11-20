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

            tags = form.cleaned_data.get('recipe_tags')
            for tag in tags:
                post.recipe_tags.add(tag)

            dietary_restriction = form.cleaned_data.get('dietary_restr')
            for restr in dietary_restriction:
                post.dietary_restr.add(restr)

            post = form.save()
            return redirect(recipe_detail, recipe_id=post.pk)
    else:
        form = AddRecipeForm()
        valid = False

    return render(request,
                  'recipes/add_new_recipe_form.html',
                  {'form': form, 'valid': valid}))
