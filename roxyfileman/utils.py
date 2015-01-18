from django.http import HttpResponse, HttpResponseBadRequest
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.conf import settings
import os, time, uuid, json, re


def json_response(data, success=True):
    Response = HttpResponse if success else HttpResponseBadRequest
    return Response(json.dumps(data), content_type='application/json')


def ok(msg=''):
    return json_response({'res': 'ok', 'msg': msg})


def err(msg=''):
    return json_response({'res': 'err', 'msg': msg})


def safepath(path, *paths):
    safe = re.compile(r'^\.\.|^\/')
    safe_paths = []

    for p in paths:
        safe_paths.append(safe.sub('', p))

    return os.path.join(path, *safe_paths)


class Upload:
    def __init__(self, uploaded_file):
        self.raw_name, self.ext = os.path.splitext(uploaded_file.name)
        self.storage = FileSystemStorage(location=settings.MEDIA_ROOT)
        self.name = self.build_name(self.raw_name)
        self.file = uploaded_file

    def save(self, dir):
        self.create_dir(os.path.join(settings.MEDIA_ROOT, dir))

        path = os.path.join(dir, self.name + self.ext)
        self.storage.save(path, ContentFile(self.file.read()))
        return os.path.join(os.path.dirname(settings.MEDIA_ROOT), path)

    @staticmethod
    def build_name(name):
        string_encode = ('%s&%s' % (name, time.time()))
        return uuid.uuid5(uuid.NAMESPACE_DNS, string_encode).hex

    @staticmethod
    def create_dir(path):
        if not (os.path.exists(path) and os.path.isdir(path)):
            os.makedirs(path)
