from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from .models import Article, Naprava, Comment
from .forms import UserForm, LoginForm, NapravaForm, CommentForm

# comment
app_name = 'webPage'
"""
landing page
"""
def index(request):
    context = {}

    if request.method=="POST" and 'reg' in request.POST:
        print(request.POST)
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

def izdelek_view(request, izdelek_id):
    n = Naprava.objects.get(pk=izdelek_id)
    if request.method=='POST':
        idNaprava = Comment(naprava=n)
        form = CommentForm(request.POST, instance=idNaprava)
        if form.is_valid():
            comment = Comment(comment=form.cleaned_data['comment'])
            author = Comment(author=request.user)
            naprava = idNaprava
            print(naprava.naprava.id)
            form.save()

    c = Comment.objects.filter(naprava = izdelek_id)
    return render(request, 'webPage/izdelek.html', {'naprava':n, 'kom':c,
                           'loginForm': LoginForm(), 'komentar': CommentForm()})

@permission_required('webPage.edit_naprava')
def izdelek_edit(request, izdelek_id):
	n = Naprava.objects.get(pk=izdelek_id)
	fillForm = NapravaForm(instance = n)
	
	if request.method=='POST' and 'edit' in request.POST:
		form = NapravaForm(request.POST, request.FILES, instance=n)
		#print(form)
		if form.is_valid():
			print(form)
			form.save()
			return HttpResponseRedirect(reverse('index'))
	
	return render(request, 'webPage/izdelek_edit.html', {'naprava':n, 'fillForm':fillForm})

def forum(request):
	context = {}
	return render(request, 'webPage/forum.html', context)

def registration(request):
    context = {}
    context['form'] = UserForm()
    return render(request, 'webPage/registration.html', context)

def news(request):
	context = {}
	a = Article.objects.all()
	context['articles'] = a
	return render(request, 'webPage/novice.html', context)
	
def addNew(request):
	context = {}
	context['form'] = NapravaForm()
	return render(request, 'webPage/novaNaprava.html', context)
	
def logout_user(request):
    logout(request)
    return redirect('index')