from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^forum/', views.forum, name='forum'),
	url(r'^registration/', views.registration, name='registration'),
	url(r'^news/', views.news, name='news'),
	url(r'^addNew/', views.addNew, name='addNew'),
	url(r'^logout/', views.logout_user, name='logout'),
]