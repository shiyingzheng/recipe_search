from django.shortcuts import get_object_or_404, render
from app.models import Recipe, Rating, UserProfile
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def my_recipes(request):
    profile = request.user.profile
    recipes = profile.owner_recipe.all()

    paginator = Paginator(recipes, 10) # Show 10 recipes per page

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

    return render(request, 'users/my-recipes.html',
            {'recipes': sorted_recipes_page, 'user':request.user })
