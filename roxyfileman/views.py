from django.views.decorators.csrf import csrf_exempt
from roxyfileman.settings import default_settings
from roxyfileman.utils import json_response
from django.shortcuts import render
from django.conf import settings
import os


def index(request):
    return render(request, 'roxyfileman/index.html')


def conf(request):
    config = {}
    for key, value in default_settings.items():
        config[key] = getattr(settings, 'ROXY_' + key, value)

    return json_response(config)


@csrf_exempt
def dirlist(request):
    result = []
    for root, dirs, files in os.walk(settings.MEDIA_ROOT):
        result.append({'p': os.path.relpath(root, settings.MEDIA_ROOT), 'f': len(files), 'd': len(dirs)})

    return json_response(result[1:])


def createdir(request):
    pass


def deletedir(request):
    pass


def movedir(request):
    pass


def copydir(request):
    pass


def renamedir(request):
    pass


@csrf_exempt
def fileslist(request):
    rel_path = request.GET.get('d', '.')
    full_path = os.path.join(settings.MEDIA_ROOT, rel_path)

    files = []
    for fname in next(os.walk(full_path))[2]:
        files.append({'p': os.path.join(settings.MEDIA_URL, rel_path, fname), 'w': 0, 'h': 0, 's': 0})

    return json_response(files)


def upload(request):
    pass


def download(request):
    pass


def deletefile(request):
    pass


def uploaddir(request):
    pass


def movefile(request):
    pass


def copyfile(request):
    pass


def renamefile(request):
    pass


def generatethumb(request):
    pass
