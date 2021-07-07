from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse


def subscription_created(request: WSGIRequest) -> JsonResponse:
    if request.method == "POST":
        return JsonResponse({"working": "yes"})

    return JsonResponse(status=405, data={})
