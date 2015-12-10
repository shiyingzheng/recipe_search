from django.shortcuts import redirect, render
from app.models import Recipe, Ingredient, Ingredient_In_Recipe
from app.forms import AddRecipeForm
from app.views import recipe_detail
from django.contrib.auth.decorators import login_required

@login_required
def add_new_recipe(request):
    valid = True

    if request.method == "POST":
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()

            post.recipe_owner = request.user.profile

            tags = form.cleaned_data.get('recipe_tags').split(',')
            for tag in tags:
                post.recipe_tags.add(tag)

            tools = form.cleaned_data.get('tools').split(',')
            for tool in tools:
                post.tools.add(tool)

            restrs = form.cleaned_data.get('dietary_restrictions').split(',')
            for restr in restrs:
                post.dietary_restrictions.add(restr)

            ings = form.cleaned_data.get('recipe_ingredients').split("|")
            for ing in ings:
                data=ing.split(":")
                ingredient,created = Ingredient.objects.get_or_create(ingredient_name=data[0].lower())
                relation = Ingredient_In_Recipe(recipe=post, ingredient = ingredient, num_units = data[1])
                relation.save()

            post = form.save()
            return redirect(recipe_detail, recipe_id=post.pk)
        else:
            valid = False
    else:
        form = AddRecipeForm()

    return render(request,
                  'recipes/add_new_recipe_form.html',
                  {'form': form, 'valid': valid})
