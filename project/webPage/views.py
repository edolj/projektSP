from django.shortcuts import render
from django.http import HttpResponse

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
	return render(request, 'webPage/novice.html', context)
	
def addNew(request):
	context = {}
	return render(request, 'webPage/novaNaprava.html', context)