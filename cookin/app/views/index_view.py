from django.shortcuts import render
from app.forms import SearchForm
from app.models import Recipe
from app.models import Rating
from django.utils.text import slugify

def average_cost(recipe):
    qs = Rating.objects.filter(rating_recipe__exact=recipe.id)
    recipe_ratings = qs.all()
    if len(recipe_ratings) == 0:
        return 0

    cost_sum = 0
    for rating in recipe_ratings:
        cost_sum += rating.rating_price * 1.0
    return cost_sum / len(recipe_ratings)


def filter_recipes(recipes, max_time, dietary_restrictions, max_cost, exclude_tools):
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
        if average_cost(recipe) > max_cost:
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
    time = request.GET.get("time")
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

    if time:
        time = float(time)
    else:
        time = 0

    if max_cost:
        max_cost = float(max_cost)
    else:
        max_cost = 0

    unsorted_recipes = qs.all()
    unsorted_recipes = filter_recipes(unsorted_recipes, time, dietary_restrictions, max_cost, exclude_tools)
    sorted_recipes = sorted(unsorted_recipes, key= lambda recipe: -recipe.relevance(my_tools=tools))

    relevances = []
    for recipe in sorted_recipes:
        relevances.append(recipe.relevance(my_tools=tools))

    return render(request, 'index.html', {'search_form': form, 'recipes': sorted_recipes, 'rel':relevances})
