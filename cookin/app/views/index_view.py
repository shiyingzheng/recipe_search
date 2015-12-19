from django.shortcuts import render
from app.forms import SearchForm
from app.models import Recipe
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
        if recipe.average_cost_estimate_per_serving() > max_cost:
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
    qs = Recipe.objects.all()
    keywords = request.GET.get("keywords")
    tools = request.GET.get("tools")
    max_time = request.GET.get("max_time")
    dietary_restrictions = request.GET.get("dietary_restrictions")
    max_cost_per_serving = request.GET.get("max_cost_per_serving")
    exclude_tools = request.GET.get("exclude_tools")
    sort_by = request.GET.get("sort_by")

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
            qs = qs.filter(recipe_title__icontains=keyword).distinct() | qs.filter(recipe_tags__name__in=keywords).distinct() | qs.filter(recipe_ingredients__ingredient_name__icontains=keyword).distinct()
    else:
        keywords = []

    if max_time:
        max_time = float(max_time)
    else:
        max_time = 0

    if max_cost_per_serving:
        max_cost_per_serving = float(max_cost_per_serving)
    else:
        max_cost_per_serving = 0

    if not sort_by:
        sort_by = 'rating'

    form = SearchForm({'keywords': " ".join(keywords), 'tools':','.join(tools), 'max_time':max_time or '', 'dietary_restrictions': ",".join(dietary_restrictions), 'max_cost_per_serving': max_cost_per_serving or '', 'sort_by':sort_by})

    unsorted_recipes = qs.all()
    unsorted_recipes = filtered_recipes(unsorted_recipes, max_time, dietary_restrictions, max_cost_per_serving, exclude_tools)
    sorted_recipes = sorted(unsorted_recipes, key= lambda recipe: -recipe.relevance(my_tools=tools, sort_by=sort_by))
    paginator = Paginator(sorted_recipes, 10) # Show 10 recipes per page

    # pagination works by issuing a SELECT query with a LIMIT for number of
    # items each page, and an OFFSET to the row at the start of the page
    page = request.GET.get('page')
    try:
        sorted_recipes_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        sorted_recipes_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        sorted_recipes_page = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'search_form': form, 'recipes': sorted_recipes_page})
