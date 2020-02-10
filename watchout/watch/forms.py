from django import forms
from .models import Movies

class UploadForm(forms.ModelForm): #This upload form is based off the database we created i.e movies 
    class Meta:
        model = Movies
        fields = ('movie_title', 'movie_description', 'movie_file', 'release_date')
