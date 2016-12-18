from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import authenticate
from .models import Article
# comment
def index(request):
	context = {}
	return render(request, 'webPage/index.html', context)
	
def forum(request):
	context = {}
	return render(request, 'webPage/forum.html', context)

def registration(request):
	context = {}
	return render(request, 'webPage/registration.html', context)

def news(request):
	context = {}
	a = Article.objects.all()
	
	context['articles'] = a
	return render(request, 'webPage/novice.html', context)
	
def addNew(request):
	context = {}
	return render(request, 'webPage/novaNaprava.html', context)