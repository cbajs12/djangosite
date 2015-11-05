from django.conf.urls import patterns, include, url
from django.contrib import admin
from djangosite import view
#from users.views import LoginView

urlpatterns = patterns('',
    url(r'^main/', view.index, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls', namespace="users")),
    url(r'^board/', include('board.urls', namespace="board")),
    #url(r'^login/',LoginView.as_view(),name='login'),
)
