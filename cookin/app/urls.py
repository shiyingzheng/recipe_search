from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /app/recipes/5/
    url(r'^recipes/(?P<recipe_id>[0-9]+)/$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipes/new/$', views.add_new_recipe, name='add_new_recipe'),
]
