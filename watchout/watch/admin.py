from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.Movies)
admin.site.register(models.Movie_downloader)
admin.site.register(models.Movie_uploader)
admin.site.register(models.Moviedirector)