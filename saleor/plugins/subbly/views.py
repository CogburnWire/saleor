from django.http import HttpRequest, JsonResponse

from ..models import PluginConfiguration
from .plugin import SubblyPlugin


def subscription_created(request: HttpRequest) -> JsonResponse:
    configuration = _get_config()

    print("Secret", configuration["secret"])
    print("HEADERS", request.headers)
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({"working": "yes"})

    return JsonResponse(None, status=405, safe=False)


def _get_config() -> dict:
    plugin_configuration = PluginConfiguration.objects.get(
        identifier=SubblyPlugin.PLUGIN_ID
    )

    configuration = plugin_configuration.configuration
    return {item["name"]: item["value"] for item in configuration}
