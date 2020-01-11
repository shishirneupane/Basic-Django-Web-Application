from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)

	location = models.CharField(max_length=30)
	age = models.IntegerField()

	def __str__ (self):
		return (self.user.username)

class Movies(models.Model):
	"""docstring for Movies"""
	Movie_title = models.CharField(max_length=100)
	Movie_description = models.TextField()

	def __str__(self):
		return (self.Movie_title)

class Movie_downloader(models.Model):
	Downloader_name = models.CharField(max_length=100)
	Downloader = models.ManyToManyField(Movies)

	def __str__(self):
		return str(self.Downloader)

class Movie_uploader(models.Model):
	Uploader_name = models.CharField(max_length=100)
	Uploader = models.ManyToManyField(Movies)

	def __str__(self):
		return (self.Uploader)

class Moviedirector(models.Model):
	movie = models.OneToOneField(Movies, on_delete= models.CASCADE)
	director_name = models.CharField(max_length=50)

	def __str__(self):
		return (self.director_name)

from django.db import models

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

		


		
		

