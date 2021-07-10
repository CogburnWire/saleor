from django.core.exceptions import ValidationError

from saleor.plugins.base_plugin import BasePlugin, ConfigurationTypeField

from ..models import PluginConfiguration


class SubblyPlugin(BasePlugin):
    PLUGIN_ID = "plugin.subbly"
    PLUGIN_NAME = "Subbly Integration"
    PLUGIN_DESCRIPTION = "Subscription box customer integration"

    CONFIG_STRUCTURE = {
        "Secret": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "Provide your subbly secret key",
            "label": "Secret",
        },
        "Test mode": {
            "type": ConfigurationTypeField.BOOLEAN,
            "help_text": "Run plugin in test mode",
            "label": "Test mode",
        },
        "Bcc Addresses": {
            "type": ConfigurationTypeField.STRING,
            "help_text": "BCC email addresses",
            "label": "Bcc Address(es)",
        },
    }

    DEFAULT_CONFIGURATION = [
        {"name": "Secret", "value": None},
        {"name": "Test mode", "value": False},
        {"name": "Bcc Addresses", "value": None},
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
