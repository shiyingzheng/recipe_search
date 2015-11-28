from django.shortcuts import render
from app.forms import SearchForm
from app.models import Recipe


def index(request):
    form = SearchForm()
    qs = Recipe.objects.all()
    # keywords = request.GET.get("keywords")
    return render(request, 'index.html', {'search_form': form, 'qs': qs})
