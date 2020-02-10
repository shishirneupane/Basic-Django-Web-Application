from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
import json 
from django.contrib.auth.decorators import login_required #Decorator
from django.views.decorators.csrf import csrf_exempt

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



def login_page(request):  #Login function that carries out login task
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
		
			auth.login(request, user)
			print('login')
			return redirect('watch:upload')
		else:
			print('logout')
			messages.info(request, 'Username or password is invalid')
			return render(request,'watch/login.html')
	else:
		print('get request')
		return render(request,'watch/login.html')

def logout_page(request):
	auth.logout(request)
	return redirect('watch:login')
	


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

def get_data_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		movies = Movies.objects.filter(
            Q(movie_title__icontains = q) |
			Q(movie_description__icontains = q)
            ).distinct()

		for movie in movies:
		    queryset.append(movie)
		return list(set(queryset))

def show_list(request):
	show = ''
	if request.GET:
		query = request.GET['q']
		show = get_data_queryset(str(query))
	return render(request, "watch/movies_list.html", {"movies": show})

@login_required
def update_book(request,id):
	movie = Movies.objects.get(pk=id)
	print(movie)
	if request.method == "POST":
		title = request.POST['title']
		desc = request.POST['description']
		releasedate = request.POST['releasedate']
		movie.movie_title = title
		movie.movie_description = desc
		movie.release_date = releasedate
		movie.save()
		return redirect('watch:movies')

	return render(request,"watch/update.html",{"m":movie})
