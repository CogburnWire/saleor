import json

from django.http import HttpRequest, JsonResponse

from ..models import PluginConfiguration
from .models import SubblySubscription
from .plugin import SubblyPlugin
from .tasks import send_customer_invitation_email


def subscription_created(request: HttpRequest) -> JsonResponse:
    configuration = _get_config()

    if request.method == "POST":
        payload = json.loads(request.body.decode("utf-8"))
        customer = payload.get("customer").get("user", {})

        # Create subscription object
        SubblySubscription.objects.create(
            subscription_id=payload.get("id"),
            first_name=customer.get("first_name"),
            last_name=customer.get("last_name"),
            email=customer.get("email"),
        )

        onboarding_url = configuration["Onboarding url"]
        send_customer_invitation_email.delay(
            onboarding_url, customer.get("email"), customer.get("first_name")
        )

        return JsonResponse({"working": "yes"})

    return JsonResponse(None, status=405, safe=False)


def _get_config() -> dict:
    plugin_configuration = PluginConfiguration.objects.get(
        identifier=SubblyPlugin.PLUGIN_ID
    )

    configuration = plugin_configuration.configuration

    return {item["name"]: item["value"] for item in configuration}
