from django.core.exceptions import ValidationError

from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField

from ..models import PluginConfiguration


class ShipStationPlugin(BasePlugin):
    PLUGIN_ID = "plugin.shipstation"
    PLUGIN_NAME = "Ship station"
    PLUGIN_DESCRIPTION = "Ship station order forwarding plugin"

    CONFIG_STRUCTURE = {
        "api_key": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Provide your ship station API key",
            "label": "API key",
        },
        "api_secret": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Provide your ship station API secret key",
            "label": "API secret",
        },
        "shipstation_endpoint": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Ship station endpoint",
            "label": "Ship station endpoint",
        },
    }

    DEFAULT_CONFIGURATION = [
        {"name": "api_key", "value": None},
        {"name": "api_secret", "value": None},
        {"name": "shipstation_endpoint", "value": None},
    ]

    @classmethod
    def validate_plugin_configuration(cls, plugin_configuration: "PluginConfiguration"):
        """Validate if provided configuration is correct."""
        missing_fields = []
        configuration = plugin_configuration.configuration
        configuration = {item["name"]: item["value"] for item in configuration}
        if not configuration["api_key"]:
            missing_fields.append("username or account")
        if not configuration["api_secret"]:
            missing_fields.append("password or API token")
        if not configuration["shipstation_endpoint"]:
            missing_fields.append("password or API token")

        if plugin_configuration.active and missing_fields:
            error_msg = (
                "To enable a plugin, you need to provide values for the "
                "following fields: "
            )
            raise ValidationError(error_msg + ", ".join(missing_fields))
