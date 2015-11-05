from django.conf.urls import patterns, url

from board import views

urlpatterns = patterns('', 
	url(r'^lists/$',views.lists,name='lists'),
	url(r'^write/$',views.write,name='write'),
	url(r'^view/(?P<board_id>\d+)/$',views.view,name='view'),
	url(r'^update/(?P<board_id>\d+)/$',views.update,name='update'),
	url(r'^delete/(?P<board_id>\d+)/$',views.delete,name='delete'),
	url(r'^delComment/(?P<board_id>\d+)/$',views.delComment,name='delComment'),
)
