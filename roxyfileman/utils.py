from django.http import HttpResponse, HttpResponseBadRequest
import json


def json_response(data, success=True):
    Response = HttpResponse if success else HttpResponseBadRequest
    return Response(json.dumps(data), content_type='application/json')
