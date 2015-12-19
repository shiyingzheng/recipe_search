from django.contrib import admin

# Register your models here.

from .models import Recipe, UserProfile, Rating, Ingredient

admin.site.register(Recipe)
admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Ingredient)
