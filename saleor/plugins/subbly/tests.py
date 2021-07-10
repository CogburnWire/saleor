from django.http import HttpResponse
from django.test import Client, TestCase

from ..models import PluginConfiguration

webhook_payload: dict = {"subscription_id": "test"}


class SubblyPluginTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        PluginConfiguration.objects.create(
            identifier="plugin.subbly",
            name="Subbly integration",
            configuration=[
                {"name": "Secret", "value": "testsecret"},
                {"name": "Test mode", "value": False},
                {"name": "Bcc Addresses", "value": None},
            ],
        )

        # {"Secret": "test", "Bcc Addresses": None, "Test mode": False},

    def test_creates_a_subscription_record(self):
        c = Client()
        response: HttpResponse = c.post(
            "/subbly/subscription-created",
            content_type="application/json",
            data=webhook_payload,
        )
        self.assertEqual(response.status_code, 200)

    def test_only_allows_post_request(self):
        c = Client()
        response: HttpResponse = c.get("/subbly/subscription-created")
        self.assertEqual(response.status_code, 405)
