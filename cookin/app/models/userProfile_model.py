from django.contrib.auth.models import User
from django.db import models

def user_image_name(instance, filename):
	return "user_images/%d/%s" % (instance.pk, filename)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=user_image_name, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
