from django.conf.urls import url, include
from . import views

app_name = 'register'
urlpatterns = [

	url(r'^$', views.home, name='home'),
	url(r'^register/$', views.register, name='register'),
    	url(r'^login_user/$', views.login_user, name='login_user'),
    	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	
	url(r'^myaccount/$', views.myaccount, name='myaccount'),


]

