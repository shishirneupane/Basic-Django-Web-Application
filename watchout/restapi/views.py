from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt

from watch.forms import UploadForm
from watch.models import Movies

# restapi get all model data
def show_all_data(request):
	movie = Movies.objects.all()
	print(type(movie))
	dict_type = {"Movies": list(movie.values("movie_title", "movie_description", "release_date"))}
	return JsonResponse(dict_type)

# restapi get specific model data by id
def get_data_json(request, pk):
    movie = Movies.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Movie Title": movie.movie_title, "Movie Description": movie.movie_description, "Release Date": movie.release_date})

# restapi update specific model data by id
@csrf_exempt
def update_data_json(request, pk):
    movie = Movies.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Movie Title": movie.movie_title, "Movie Description": movie.movie_description, "Release Date": movie.release_date})
    else:
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        movie.movie_title = json_data['movie_title']
        movie.movie_description = json_data['movie_description']
        movie.release_date = json_data['release_date']
        movie.save()
        return JsonResponse("Updated !", safe=False)

# restapi delete specific model data by id
@csrf_exempt
def delete_data_json(request, pk):
    movie = Movies.objects.get(pk=pk)
    if request.method == "GET":
        return JsonResponse({"Movie Title": movie.movie_title, "Movie Description": movie.movie_description, "Release Date": movie.release_date})
    else:
        movie.delete()
        return JsonResponse("Deleted !", safe=False)

# restapi post model data
@csrf_exempt
def post_data_json(request):
    if request.method == "POST":
        movie = Movies()
        json_body = request.body.decode('utf-8')
        json_data = json.loads(json_body)
        movie.movie_title = json_data['movie_title']
        movie.movie_description = json_data['movie_description']
        movie.movie_file = json_data['movie_file']
        movie.release_date = json_data['release_date']
        movie.save()
        return JsonResponse("Uploaded !", safe=False)

# restapi pagination with size and pageno params
def movie_objects_pagination(request,PAGENO,SIZE):
    skip = SIZE * (PAGENO -1)
    movies = Movies.objects.all() [skip:(PAGENO * SIZE)]
    dict = {
        "movies": list(movies.values("movie_title","movie_description","movie_file","release_date"))
    }
    return JsonResponse(dict)
