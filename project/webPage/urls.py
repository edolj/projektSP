from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^index/$', views.index, name='index'),
	url(r'^index/(?P<izdelek_id>[0-9]+)/$', views.izdelek_view, name='izdelek_view'),
	url(r'^index/(?P<izdelek_id>[0-9]+)/edit/$', views.izdelek_edit, name='izdelek_edit'),
	url(r'^forum/$', views.forum, name='forum'),
	url(r'^registration/$', views.registration, name='registration'),
	url(r'^news/$', views.news, name='news'),
	url(r'^addNew/$', views.addNew, name='addNew'),
	url(r'^logout/$', views.logout_user, name='logout'),
]

