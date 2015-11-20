from django.db import models


class DietaryRestriction(models.Model):
    restr_name = models.CharField(max_length=200)
    restr_description = models.CharField(max_length=1000)

    def __str__(self):
        return '%s' % self.restr_name

    class Meta:
        app_label = 'app'
