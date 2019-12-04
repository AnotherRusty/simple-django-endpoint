from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class TestStudentChecksIn(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("daffy")

        self.client.force_login(user)

        self.client.post(
            reverse("attendance:check-in")
        )

        self.assertEqual(
            user.checkin_set.count(), 1
        )

        checkin = user.checkin_set.first()

        self.assertAlmostEqual(check.datetime.timestamp(), timezone.now().timestamp())
