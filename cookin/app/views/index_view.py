from django.shortcuts import render
from app.forms import SearchForm


def index(request):
    form = SearchForm()
    return render(request, 'index.html', {'search_form': form})
