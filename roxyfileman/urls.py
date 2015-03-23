from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls import url, patterns
from roxyfileman import views


urlpatterns = patterns('',
    url(r'^$', staff_member_required(views.index)),
    url(r'conf\.json', staff_member_required(views.conf)),
    url(r'dirlist/', staff_member_required(views.dirlist)),
    url(r'fileslist/', staff_member_required(views.fileslist)),
    url(r'createdir/', staff_member_required(views.createdir)),
    url(r'deletedir/', staff_member_required(views.deletedir)),
    url(r'movedir/', staff_member_required(views.movedir)),
    url(r'renamedir/', staff_member_required(views.renamedir)),
    url(r'copydir/', staff_member_required(views.copydir)),
    url(r'renamefile/', staff_member_required(views.renamefile)),
    url(r'movefile/', staff_member_required(views.movefile)),
    url(r'copyfile/', staff_member_required(views.copyfile)),
    url(r'deletefile/', staff_member_required(views.deletefile)),
    url(r'upload/', staff_member_required(views.upload)),
    url(r'thumb/', staff_member_required(views.thumb)),
    url(r'downloaddir/', staff_member_required(views.downloaddir)),
    url(r'download/', staff_member_required(views.download)),
)
