from django.test import Client, TestCase


class SubblyPluginTestCase(TestCase):
    def test_creates_a_subscription_record(self):
        pass

    def test_only_allows_post_request(self):
        c = Client()
        response = c.get("/subbly/subscription_created")
        self.assertEqual(response.status_code, 405)
