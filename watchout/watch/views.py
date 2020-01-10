from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def watchhmo(request):
	return render(request, "watch/home.html", {'name': 'Ashish Giri'})

def register(request):
	return render(request, "watch/register.html", context={})

def login(request):
	return render(request, "watch/login.html", context={})