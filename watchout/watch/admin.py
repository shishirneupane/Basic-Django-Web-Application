from django.contrib import admin
from .import models

admin.site.register(models.Movies)
admin.site.register(models.MovieDownloader)
admin.site.register(models.MovieUploader)
