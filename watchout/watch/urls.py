from django.urls import path
from .import views

app_name = "watch"

urlpatterns = [
    path('', views.watchhmo, name="watchhmo"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('upload/', views.upload, name="upload")
]