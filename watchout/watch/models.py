from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Movies(models.Model):
	movie_title = models.CharField(max_length=100)
	movie_description = models.TextField()

	def __str__(self):
		return (self.movie_title)

class MovieDownloader(models.Model):
	downloader_name = models.CharField(max_length=100)
	downloader = models.ManyToManyField(Movies)

	def __str__(self):
		return str(self.downloader_name)

class MovieUploader(models.Model):
	uploader_name = models.CharField(max_length=100)
	uploader = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return (self.uploader_name)
