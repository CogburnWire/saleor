from django.core.exceptions import ValidationError

from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField

from ..models import PluginConfiguration


class SubblyPlugin(BasePlugin):
    PLUGIN_ID = "plugin.subbly"
    PLUGIN_NAME = "Subbly Integration"
    PLUGIN_DESCRIPTION = "Subscription box customer integration"

    CONFIG_STRUCTURE = {
        "secret": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Provide your subbly secret key",
        },
    }

    DEFAULT_CONFIGURATION = [
        {"name": "secret", "value": None},
    ]

    DEFAULT_ACTIVE = False

    @classmethod
    def validate_plugin_configuration(cls, plugin_configuration: "PluginConfiguration"):
        """Validate if secret is provided."""
        configuration = plugin_configuration.configuration
        configuration = {item["name"]: item["value"] for item in configuration}
        if not configuration["secret"]:
            raise ValidationError(
                "To enable this plugin, you need to provide a secret key"
            )
