from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import UpdateView
from app.views import recipe_detail
from app.models import Recipe, Ingredient, Ingredient_In_Recipe
from app.forms import AddRecipeForm
from django.template import RequestContext

def recipe_update(request, recipe_id):
    valid = True
    if request.POST:
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            form = AddRecipeForm(request.POST, instance = recipe)
            post = form.save()

            post.recipe_tags.clear()
            tags = form.cleaned_data.get('recipe_tags').lower().split(',')
            for tag in tags:
                post.recipe_tags.add(tag.strip())

            post.tools.clear()
            tools = form.cleaned_data.get('tools').lower().split(',')
            for tool in tools:
                post.tools.add(tool.strip())

            post.dietary_restrictions.clear()
            restrs = form.cleaned_data.get('dietary_restrictions').lower().split(',')
            for restr in restrs:
                post.dietary_restrictions.add(restr.strip())

            post.recipe_ingredients.clear()
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

            return redirect(recipe_detail, recipe_id=recipe_id)
        else:
            valid = False

    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients_list = recipe.ingredient_in_recipe_set.all()
    ingredients = '|'.join([x.ingredient.ingredient_name + ":" + str(x.num_units) + ":" + x.unit_name for x in ingredients_list])
    form = AddRecipeForm(instance = recipe)

    return render(request, 'recipes/recipe_update.html',
        {'recipe': recipe, 'form': form, 'ingredients': ingredients, 'valid': valid},
        context_instance=RequestContext(request))
