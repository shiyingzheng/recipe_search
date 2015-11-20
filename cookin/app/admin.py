from django.contrib import admin

# Register your models here.

from .models import Recipe, UserProfile

admin.site.register(Recipe)
admin.site.register(UserProfile)

