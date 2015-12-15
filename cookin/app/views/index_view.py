from django.shortcuts import render
from app.forms import SearchForm
from app.models import Recipe
from django.utils.text import slugify


def filtered_recipes(recipes, max_time, dietary_restrictions, max_cost, exclude_tools):
    if not max_time:
        max_time = float('inf')
    if not dietary_restrictions:
        dietary_restrictions = []
    if not max_cost:
        max_cost = float('inf')
    if not exclude_tools:
        exclude_tools = []

    new_recipes = []
    for recipe in recipes:
        if recipe.prep_time_minutes + recipe.cooking_time_minutes > max_time:
            continue
        fits_restrictions = True
        for restriction in dietary_restrictions:
            if slugify(restriction) not in recipe.dietary_restrictions.slugs():
                fits_restrictions = False
        if not fits_restrictions:
            continue
        if recipe.average_cost_estimate() > max_cost:
            continue
        fits_tool_restrictions = True
        for tool in exclude_tools:
            if slugify(tool) in recipe.tools.slugs():
                fits_tool_restrictions = False
        if not fits_tool_restrictions:
            continue
        new_recipes.append(recipe)
    return new_recipes


def index(request):
    form = SearchForm()
    qs = Recipe.objects.all()
    keywords = request.GET.get("keywords")
    tools = request.GET.get("tools")
    max_time = request.GET.get("max_time")
    dietary_restrictions = request.GET.get("dietary_restrictions")
    max_cost = request.GET.get("max_cost")
    exclude_tools = request.GET.get("exclude_tools")

    if tools:
        tools = tools.split(",")
    else:
        tools = []

    if exclude_tools:
        exclude_tools = exclude_tools.split(",")
    else:
        exclude_tools = []

    if dietary_restrictions:
        dietary_restrictions = dietary_restrictions.split(",")
    else:
        dietary_restrictions = []

    if keywords:
        keywords = keywords.split()
        for keyword in keywords:
            qs = qs.filter(recipe_title__icontains=keyword)

    if max_time:
        max_time = float(max_time)
    else:
        max_time = 0

    if max_cost:
        max_cost = float(max_cost)
    else:
        max_cost = 0

    unsorted_recipes = qs.all()
    unsorted_recipes = filtered_recipes(unsorted_recipes, max_time, dietary_restrictions, max_cost, exclude_tools)
    sorted_recipes = sorted(unsorted_recipes, key= lambda recipe: -recipe.relevance(my_tools=tools))

    return render(request, 'index.html', {'search_form': form, 'recipes': sorted_recipes})
