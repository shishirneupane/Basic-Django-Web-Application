from django.urls import path
from .import views

app_name = "watch"

urlpatterns = [
    path('', views.movies_list, name="movies"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('movies/upload/', views.upload_movies, name="upload"),
    path('movies/<int:pk>/', views.delete_movies, name="delete")
]