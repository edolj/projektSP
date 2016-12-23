from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Article
from .models import Naprava
from .forms import UserForm
from .forms import LoginForm
from .forms import NapravaForm

# comment
def index(request):
    context = {}

    if request.method=="POST" and 'reg' in request.POST:
        print("yes")
        form2 = UserForm(request.POST)
        if form2.is_valid():
            new_user = User.objects.create_user(username=form2.cleaned_data['username'],
                email=form2.cleaned_data['email'] ,password=form2.cleaned_data['password'])
            login(request, new_user)

    if request.method=='POST' and 'prijava' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

    if request.method=='POST' and 'addNew' in request.POST:
        whoUser = Naprava(author=request.user)
        form = NapravaForm(request.POST, request.FILES, instance=whoUser)
        if form.is_valid():
            picture = Naprava(picture = request.FILES['picture'])
            video = Naprava(video = request.FILES['video'])
            author = request.user
            form.save()
            return redirect('index')

    n = Naprava.objects.all()
    context['naprave'] = n
    context['loginForm'] = LoginForm()
    return render(request, 'webPage/index.html', context)

def forum(request):
	context = {}
	return render(request, 'webPage/forum.html', context)

def registration(request):
    context = {}
    
    if request.method=='POST' and 'prijava' in request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)

    context['form'] = UserForm()
    context['loginForm'] = LoginForm()
    return render(request, 'webPage/registration.html', context)

def news(request):
	context = {}
	a = Article.objects.all()
	
	if request.method=='POST' and 'prijava' in request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)

	context['articles'] = a
	context['loginForm'] = LoginForm()
	return render(request, 'webPage/novice.html', context)
	
def addNew(request):
	context = {}
	
	if request.method=='POST' and 'prijava' in request.POST:
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)

	context['form'] = NapravaForm()
	context['loginForm'] = LoginForm()
	return render(request, 'webPage/novaNaprava.html', context)
	
def logout_user(request):
    logout(request)
    return redirect('index')