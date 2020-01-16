from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Movies(models.Model):
	"""docstring for Movies"""
	movie_title = models.CharField(max_length=100)
	movie_description = models.TextField()

	def __str__(self):
		return (self.movie_title)

class MovieDownloader(models.Model):
	downloader_name = models.CharField(max_length=100)
	downloader = models.ManyToManyField(Movies)

	def __str__(self):
		return str(self.downloader)

class MovieUploader(models.Model):
	uploader_name = models.CharField(max_length=100)
	uploader = models.ManyToManyField(Movies)

	def __str__(self):
		return (self.uploader)

class MovieDirector(models.Model):
	movie = models.OneToOneField(Movies, on_delete= models.CASCADE)
	director_name = models.CharField(max_length=50)

	def __str__(self):
		return (self.director_name)

class Video(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)

		


		
		

