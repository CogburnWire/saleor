from django.http import HttpRequest, JsonResponse

from ..models import PluginConfiguration
from .plugin import SubblyPlugin


def subscription_created(request: HttpRequest) -> JsonResponse:
    configuration = _get_config()

    print("Secret", configuration["secret"])
    if request.method == "POST":
        print(request.POST)
        return JsonResponse({"working": "yes"})

    return JsonResponse(None, status=405, safe=False)


def _get_config() -> dict:
    plugin_configuration = PluginConfiguration.objects.get(
        identifier=SubblyPlugin.PLUGIN_ID
    )

    return plugin_configuration.configuration
