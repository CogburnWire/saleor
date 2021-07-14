from unittest.mock import patch

from django.http import HttpResponse
from django.test import Client, TestCase

from ..models import PluginConfiguration
from .models import SubblySubscription

webhook_payload: dict = {
    "id": 437704,
    "active": 1,
    "past_due": "0",
    "created_on": "2021-07-09 14:40:42",
    "cancelled_on": "",
    "gift": 0,
    "gift_message": None,
    "status": "active",
    "next_payment_date": "2021-08-09 14:40:42",
    "skipping_until": "",
    "waiting_until": "",
    "cancel_at_end_of_commitment": 0,
    "previous_subscription_id": None,
    "cancellation_extra_feedback": None,
    "cancellation_reason_submitted_on": "",
    "customer": {
        "id": 493975,
        "notes": None,
        "created_on": "2021-07-09 14:13:25",
        "marketing_consent": 0,
        "user": {
            "id": 526831,
            "email": "jason+test-2021-07-09-a@govfriend.com",
            "created_on": "2021-07-09 14:13:24",
            "first_name": "Jason",
            "last_name": "Buchanan",
        },
        "tags": [],
    },
    "product": {
        "id": 97875,
        "parent_id": 97874,
        "type": "subscription",
        "price": "1.00",
        "setup_fee": "0.00",
        "shipping_fee": "0.00",
        "shipping_fee_intl": "0.00",
        "created_on": "2021-07-09 14:23:23",
        "name": "Quality Assurance Product",
        "delivery_info": None,
        "slug": "quality-assurance-product",
        "active": 1,
        "last_updated": "2021-07-09 14:25:51",
        "archived": 0,
    },
    "cancellation_reason": None,
}


class SubblyPluginTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.plugin = PluginConfiguration.objects.create(
            identifier="plugin.subbly",
            name="Subbly integration",
            configuration=[
                {"name": "Secret", "value": "testsecret"},
                {"name": "Test mode", "value": False},
                {"name": "Bcc Addresses", "value": None},
                {"name": "Onboarding url", "value": "https://test.com"},
            ],
        )

    @patch("saleor.plugins.subbly.tasks.send_customer_invitation_email.delay")
    def test_creates_a_subscription_record(self, mock_send_email):
        c = Client()
        response: HttpResponse = c.post(
            "/subbly/subscription-created",
            content_type="application/json",
            data=webhook_payload,
        )
        self.assertEqual(response.status_code, 200)

        subscription_exists = SubblySubscription.objects.filter(
            subscription_id=webhook_payload["id"]
        ).exists()

        self.assertTrue(subscription_exists)

        mock_send_email.assert_called()

    def test_only_allows_post_request(self):
        c = Client()
        response: HttpResponse = c.get("/subbly/subscription-created")
        self.assertEqual(response.status_code, 405)
