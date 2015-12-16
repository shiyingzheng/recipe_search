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

            tags = form.cleaned_data.get('recipe_tags').lower().split(',')
            for tag in tags:
                post.recipe_tags.add(tag.strip())

            tools = form.cleaned_data.get('tools').lower().split(',')
            for tool in tools:
                post.tools.add(tool.strip())

            restrs = form.cleaned_data.get('dietary_restrictions').lower().split(',')
            for restr in restrs:
                post.dietary_restrictions.add(restr.strip())

            ings = form.cleaned_data.get('recipe_ingredients').split("|")
            for ing in ings:
                data = ing.split(":")
                ingredient, created = Ingredient.objects.get_or_create(ingredient_name=data[0].lower())
                num = data[1].strip()
                unit = data[2].strip()
                relation = Ingredient_In_Recipe(recipe=post,
                                                ingredient=ingredient,
                                                num_units=num)
                if len(unit) > 1:
                    relation.unit_name = unit
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
