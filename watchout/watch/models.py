from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Movies(models.Model):  #movie model to store name of uploaded movies
	movie_title = models.CharField(max_length=100) #Movie_title represents the title of movie
	movie_description = models.TextField() #Movie_description represents the description of movie
	movie_file = models.FileField(upload_to="movies") #Movie_file represents the path of movie
	release_date = models.DateField("Release Date") #release_Date represents the date of movie released

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
	downloader = models.ManyToManyField(Movies) #Many movies can be downloaded by many users hence it has many to many relation with movies

	def __str__(self):
		return self.downloader_name

class MovieUploader(models.Model): #Movie uploader to store uploaded movies
	uploader_name = models.CharField(max_length=100)
	uploader = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True) #One to many realtion show with movies where foreign key is used movie_uploader

	def __str__(self):
		return self.uploader_name


class ReleaseDate(models.Model): #ReleaseDate model to store release date
	movie_title = models.CharField(max_length=100)
	release_date = models.OneToOneField( #One movie has only one release date hence it shows one to one realtion with movies
		Movies,
		on_delete = models.CASCADE,
        primary_key=True,
		)
	def _str_ (self):
		return self.movie_title.release_date