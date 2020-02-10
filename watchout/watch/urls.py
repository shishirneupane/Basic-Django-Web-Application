from django.urls import path
from .import views

app_name = "watch"

urlpatterns = [
    path('', views.movies_list, name="movies"), #directs to movies
    path('register/', views.register, name="register"), #it directs to register function in views
    path('login/', views.login_page, name="login"),  #it directs to login function
    path('movies/upload/', views.upload_movies, name="upload"), #it directs to upload function
    path('movies/<int:pk>/', views.delete_movies, name="delete"), #it directs to delete function
    path('show_list/', views.show_list, name="show_list"), #it directs to showlist function
    path('logout/', views.logout_page, name="logout"), #it directs to logout function
    path('update/<int:id>/', views.update_book, name="update"), #it directs to update function
]