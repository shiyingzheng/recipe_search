from django.contrib.auth.models import User
from django.db import models
import uuid
import os


def user_image_name(instance, filename):
    extension = os.path.splitext(filename)[1]
    return "user_images/%s%s" % (uuid.uuid4(), extension)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='profile')

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to=user_image_name, blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username
