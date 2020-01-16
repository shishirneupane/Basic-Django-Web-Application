from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth

# Create your views here.

from .forms import UploadForm
from .models import Movies

def homepage(request):
	return render(request, "base.html", context={})

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
			return redirect('watch:upload')
	return render(request, 'watch/upload.html', context={"forms":form})


def movies_list(request):
	movie = Movies.objects.all()
	return render(request, 'watch/movies_list.html', context={"movies":movie})