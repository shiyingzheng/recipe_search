from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /app/recipes/5/
    url(r'^recipes/(?P<recipe_id>[0-9]+)/?$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipes/new/?$', views.add_new_recipe, name='add_new_recipe'),
    url(r'^register/?$', views.register, name='register'),
    url(r'^login/?$', views.user_login, name='login'),
    url(r'^logout/?$', views.user_logout, name='logout'),
    url(r'^recipes/(?P<recipe_id>[0-9]+)/update/?$', views.recipe_update, name='recipe_update'),
]
