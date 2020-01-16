from django import forms
from .models import Movies

class UploadForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ('movie_title', 'movie_description', 'movie_file', 'release_date')
