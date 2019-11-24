from django.test import TestCase


class TestUserVisitsHomePage(TestCase):
    def test_successfully(self):
        response = self.client.get("/")
        self.assertContains(response, "Ascent")
