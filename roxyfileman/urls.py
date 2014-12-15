from django.conf.urls import url, patterns
from roxyfileman import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'conf\.json', views.conf),
    url(r'dirlist/', views.dirlist),
    url(r'fileslist/', views.fileslist),
    url(r'createdir/', views.createdir),
    url(r'deletedir/', views.deletedir),
    url(r'movedir/', views.movedir),
    url(r'renamedir/', views.renamedir),
    url(r'copydir/', views.copydir),
    url(r'renamefile/', views.renamefile),
    url(r'movefile/', views.movefile),
    url(r'copyfile/', views.copyfile),
    url(r'deletefile/', views.deletefile),
    url(r'upload/', views.upload),
    url(r'thumb/', views.thumb),
)
