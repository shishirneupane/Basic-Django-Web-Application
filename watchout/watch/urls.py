from django.urls import path
from .import views

app_name = "watch"

urlpatterns = [
    path('', views.movies_list, name="movies"),
    path('register/', views.register, name="register"),
    path('login/', views.login_page, name="login"),
    path('movies/upload/', views.upload_movies, name="upload"),
    path('movies/<int:pk>/', views.delete_movies, name="delete"),
    path('show_list/', views.show_list, name="show_list"),
    path('logout/', views.logout_page, name="logout"),
    path('update/<int:id>/', views.update_book, name="update"),
]