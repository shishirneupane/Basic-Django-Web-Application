from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Movies(models.Model):  #movie model to store name of uploaded movies
	movie_title = models.CharField(max_length=100)
	movie_description = models.TextField()
	movie_file = models.FileField(upload_to="movies")
	release_date = models.DateField("Release Date")

	def __str__(self):
		return self.movie_title
		

	def TestTitle(self):
		return (len(self.movie_title) > 5)
	
	
	def TestMovieDescription(self):
		return (len(self.movie_description) > 10)
	
	# def TestDate(self):
	# 	return (len(self.release_date) != 0000-00-00 )
	
	


class MovieDownloader(models.Model): #Movie downloader to store downloaded movies
	downloader_name = models.CharField(max_length=100)
	downloader = models.ManyToManyField(Movies)

	def __str__(self):
		return self.downloader_name

class MovieUploader(models.Model): #Movie uploader to store uploaded movies
	uploader_name = models.CharField(max_length=100)
	uploader = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.uploader_name


class ReleaseDate(models.Model):
	movie_title = models.CharField(max_length=100)
	release_date = models.OneToOneField(
		Movies,
		on_delete = models.CASCADE,
        primary_key=True,
		)
	def _str_ (self):
		return self.movie_title.release_date