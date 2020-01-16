from django.urls import path
from .import views

app_name = "watch"

urlpatterns = [
    path('', views.homepage, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('upload/', views.upload, name="upload")
]