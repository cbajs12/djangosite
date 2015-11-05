from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('', 
	url(r'^join/$',views.join,name='join'),
	url(r'^login/$',views.login,name='login'),
	url(r'^logout/$',views.logout,name='logout'),
	url(r'^edit/$',views.edit,name='edit'),
	url(r'^delete/$',views.delete,name='delete'),
	url(r'^show/$',views.show,name='show'),
	url(r'^check/$',views.check,name='check'),
)
