from django.urls import path
from watch import views
from restapi import views

app_name = "restapi"

urlpatterns = [
    path("getallapi/", views.show_all_data, name="show_all_data"),
    path('getapi/<int:pk>/', views.get_data_json, name="get_data_json"),
    path('updateapi/<int:pk>/', views.update_data_json, name="update_data_json"),
    path('deleteapi/<int:pk>/', views.delete_data_json, name="delete_data_json"),
    path('postapi', views.post_data_json, name="post_data_json"),
    path('page/<int:PAGENO>/<int:SIZE>/', views.movie_objects_pagination, name="movie_objects_pagination")
]