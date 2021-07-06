"""
Subbly plugin

Handles incomming webhooks for subscription orders

- Store user details
- Send invite for the marketplace
"""

from saleor.plugins.base_plugin import BasePlugin


class SubblyPlugin(BasePlugin):
    PLUGIN_ID = "plugin.subbly"
    PLUGIN_NAME = "Subbly Integration"
    PLUGIN_DESCRIPTION = "Subscription box customer integration"
    DEFAULT_ACTIVE = True
