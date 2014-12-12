from django.conf.urls import url, patterns
from roxyfileman import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'conf\.json', views.conf),
    url(r'dirlist/', views.dirlist),
    url(r'fileslist/', views.fileslist),
)
