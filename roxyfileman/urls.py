from django.utils.module_loading import import_string
from django.conf import settings
from django.conf.urls import url
from roxyfileman import views

if settings.ROXY_VIEW_DECORATOR is not None:
    view_decorator = import_string(settings.ROXY_VIEW_DECORATOR)
else:
    view_decorator = lambda f: f


urlpatterns = [
    url(r'^$', view_decorator(views.index)),
    url(r'conf\.json', view_decorator(views.conf)),
    url(r'dirlist/', view_decorator(views.dirlist)),
    url(r'fileslist/', view_decorator(views.fileslist)),
    url(r'createdir/', view_decorator(views.createdir)),
    url(r'deletedir/', view_decorator(views.deletedir)),
    url(r'movedir/', view_decorator(views.movedir)),
    url(r'renamedir/', view_decorator(views.renamedir)),
    url(r'copydir/', view_decorator(views.copydir)),
    url(r'renamefile/', view_decorator(views.renamefile)),
    url(r'movefile/', view_decorator(views.movefile)),
    url(r'copyfile/', view_decorator(views.copyfile)),
    url(r'deletefile/', view_decorator(views.deletefile)),
    url(r'upload/', view_decorator(views.upload)),
    url(r'thumb/', view_decorator(views.thumb)),
    url(r'downloaddir/', view_decorator(views.downloaddir)),
    url(r'download/', view_decorator(views.download)),
]
