from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestStudentCreatesProfile(TestCase):
    def test_successfully(self):
        user = User.objects.create_user('jimbob')

        self.client.post(
            reverse("showcase:create-profile"),
            {"headline": "I like code and such you know"}
        )

        self.assertEqual(user.profile.headline, "I like code and such you know")