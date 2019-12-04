from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestStudentCreatesShoutout(TestCase):
    def test_successfully(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        self.client.force_login(shouter)

        self.client.post(
            reverse("shoutouts:create"),
            {"recipient": shoutee.id, "content": "jane is soooo dutiful"},
        )

        self.assertEqual(shoutee.shoutouts_received.count(), 1)
        self.assertEqual(shouter.shoutouts_given.count(), 1)

        shoutout = shoutee.shoutouts_received.first()

        self.assertEqual(shoutout.content, "jane is soooo dutiful")
