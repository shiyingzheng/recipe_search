from app.models import Rating
from django.forms import ModelForm

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating_stars', 'rating_price', 'rating_comment',
                    'rating_image']
