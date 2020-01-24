from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from django.db.models import Q
import json 

# Create your views here.

from .forms import UploadForm
from .models import Movies

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name'] #first_name is same as the name of field in html file
		last_name = request.POST['last_name']
		username = request.POST['username']
		password1 = request.POST['password1']
		password2 = request.POST['password2']
		email = request.POST['email']

		if password1==password2:
			if User.objects.filter(username=username).exists():
				print("username taken")
			elif User.objects.filter(email=email).exists():
				print("email taken")
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save()
				print('user created')
				return redirect('watch:login')
	else:
		return render(request, "watch/register.html", context={})

def registerform(request):
	pass
	

def login(request):
	return render(request, "watch/login.html", context={})


def upload_movies(request):
	form = UploadForm()
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('watch:movies')
	return render(request, 'watch/upload.html', context={"forms":form})


def movies_list(request):
	movie = Movies.objects.all()
	return render(request, 'watch/movies_list.html', context={"movies":movie})


def delete_movies(request, pk):
	movie = Movies.objects.get(pk=pk)
	movie.delete()
	return redirect('watch:movies')

def get_data_querys(query=None):
	queryset = []

	queries = query.split(" ")
	for q in queries:
		Movies = movie.objects.filter(
            Q(movie_title__icontains = q)
            ).distinct()

		for movie in movies:
		    queryset.append(movie)
		return list(set(queryset))

def show_all_data(request):
	movie = movies.objects.all()
	print(type(movie))
	dic_type = {"movies": list(movie.values("movie_title"))}

	return JsonResponse(dic_type)




