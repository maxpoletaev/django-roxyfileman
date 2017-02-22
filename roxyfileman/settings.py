from django.conf import settings

default_settings = {
    'FILES_ROOT': '',
    'RETURN_URL_PREFIX': '/media',
    'SESSION_PATH_KEY': '',
    'THUMBS_VIEW_WIDTH': '140',
    'THUMBS_VIEW_HEIGHT': '120',
    'PREVIEW_THUMB_WIDTH': '100',
    'PREVIEW_THUMB_HEIGHT': '100',
    'MAX_IMAGE_WIDTH': '1000',
    'MAX_IMAGE_HEIGHT': '1000',
    'INTEGRATION': 'custom',
    'DIRLIST': 'dirlist/',
    'CREATEDIR': 'createdir/',
    'DELETEDIR': 'deletedir/',
    'MOVEDIR': 'movedir/',
    'COPYDIR': 'copydir/',
    'RENAMEDIR': 'renamedir/',
    'FILESLIST': 'fileslist/',
    'UPLOAD': 'upload/',
    'DOWNLOAD': 'download/',
    'DOWNLOADDIR': 'downloaddir/',
    'DELETEFILE': 'deletefile/',
    'MOVEFILE': 'movefile/',
    'COPYFILE': 'copyfile/',
    'RENAMEFILE': 'renamefile/',
    'GENERATETHUMB': 'thumb/',
    'DEFAULTVIEW': 'list',
    'FORBIDDEN_UPLOADS': 'zip js jsp jsb mhtml mht xhtml xht php phtml php3 php4 php5 phps shtml jhtml pl sh py cgi exe application gadget hta cpl msc jar vb jse ws wsf wsc wsh ps1 ps2 psc1 psc2 msh msh1 msh2 inf reg scf msp scr dll msi vbs bat com pif cmd vxd cpl htpasswd htaccess',
    'ALLOWED_UPLOADS': '',
    'FILEPERMISSIONS': '0644',
    'DIRPERMISSIONS': '0755',
    'LANG': 'auto',
    'DATEFORMAT': 'dd/MM/yyyy HH:mm',
    'OPEN_LAST_DIR': 'yes',

    'VIEW_DECORATOR': 'django.contrib.admin.views.decorators.staff_member_required',
    'ROOT': settings.MEDIA_ROOT,
}

for key, value in default_settings.items():
    rkey = 'ROXY_' + key
    if not hasattr(settings, rkey):
        setattr(settings, rkey, value)
