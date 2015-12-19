from django.shortcuts import get_object_or_404, render
from app.models import Recipe, Rating, UserProfile
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def my_recipes(request):
    profile = request.user.profile
    return render(request, 'users/my-recipes.html',
                  {'profile': profile })
