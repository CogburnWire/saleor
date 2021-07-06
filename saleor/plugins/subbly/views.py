from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


def subscription_created(request: WSGIRequest) -> JsonResponse:
    return JsonResponse({"working": "yes"})
