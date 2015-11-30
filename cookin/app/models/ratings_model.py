from django.db import models
from app.models import UserProfile, Recipe
from django.utils import timezone
import uuid
import os

def rating_image_name(instance, filename):
	extension = os.path.splitext(filename)[1]
	return "rating_images/%s%s" % (uuid.uuid4(), extension)

class Rating(models.Model):
	rating_recipe = models.ForeignKey(Recipe, related_name='ratings')
	rating_user = models.ForeignKey(UserProfile)

	# Number of Stars choices
	Stars_Choices = (
		(1, 1),
		(2, 2),
		(3, 3),
		(4, 4),
		(5, 5),
	)

	rating_stars = models.IntegerField(choices=Stars_Choices)
	rating_date = models.DateTimeField(default=timezone.now)
	rating_price = models.IntegerField()
	rating_comment = models.TextField(default="Add a comment!", blank=True)
	rating_image = models.ImageField(upload_to=rating_image_name,
									blank=True)

	def __str__(self):
		return '%s: %d %s' % (self.rating_recipe.recipe_title, 
								self.rating_stars, self.rating_comment)

	class Meta:
		app_label = 'app'




