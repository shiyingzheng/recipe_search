from django.shortcuts import render
from app.forms import SearchForm
from app.models import Recipe


def index(request):
    form = SearchForm()
    qs = Recipe.objects.all()
    keywords = request.GET.get("keywords")
    tools = request.GET.get("tools")
    if tools:
        tools = tools.split(",")
    else:
        tools = []

    if keywords:
        keywords = keywords.split()
        for keyword in keywords:
            qs = qs.filter(recipe_title__icontains=keyword)

    unsorted_recipes = qs.all()
    sorted_recipes = sorted(unsorted_recipes, key= lambda recipe: -recipe.relevance(my_tools=tools))

    relevances = []
    for recipe in sorted_recipes:
        relevances.append(recipe.relevance(my_tools=tools))

    return render(request, 'index.html', {'search_form': form, 'recipes': sorted_recipes, 'rel':relevances})
