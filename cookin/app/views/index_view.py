from django.shortcuts import render
from app.forms import SearchForm
from app.models import Recipe


def index(request):
    form = SearchForm()
    qs = Recipe.objects.all()
    keywords = request.GET.get("keywords")
    if keywords:
        keywords = keywords.split()
        for keyword in keywords:
            qs = qs.filter(recipe_title__icontains=keyword)

    return render(request, 'index.html', {'search_form': form, 'qs': qs})
