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
            configuration={"secret": "test"},
        )

    def test_creates_a_subscription_record(self):
        c = Client()
        response: HttpResponse = c.post(
            "/subbly/subscription-created",
            content_type="application/json",
            data=webhook_payload,
        )
        print(response)
        self.assertTrue(False)
        self.assertEqual(response.status_code, 200)

    def test_only_allows_post_request(self):
        c = Client()
        response: HttpResponse = c.get("/subbly/subscription-created")
        self.assertEqual(response.status_code, 405)
