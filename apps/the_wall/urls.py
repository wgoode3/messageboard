from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logoff$', views.logoff),
	url(r'^wall$', views.wall),
	url(r'^post$', views.post),
	url(r'^comment/(?P<post_id>\d+)$', views.comment),
	url(r'^update$', views.update),
]