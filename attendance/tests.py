from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class TestStudentChecksIn(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("daffy")

        self.client.force_login(user)

        self.client.post(reverse("attendance:check-in"))

        self.assertEqual(user.checkin_set.count(), 1)

        checkin = user.checkin_set.first()

        self.assertLessEqual(
            abs(timezone.now().timestamp() - checkin.datetime.timestamp()), 2
        )

        self.assertFalse(checkin.verified)

    def test_user_doesnt_see_button_if_checked_in(self):
        user = User.objects.create_user("daffy")
        user.checkin_set.create(datetime=timezone.now())

        self.client.force_login(user)

        response = self.client.get(reverse("attendance:check-in"))

        self.assertNotContains(
            response, "<button class='btn btn-primary'>Check In</button>", html=True
        )

    def test_user_sees_button_if_not_checked_in(self):
        user = User.objects.create_user("daffy")

        self.client.force_login(user)

        response = self.client.get(reverse("attendance:check-in"))

        self.assertContains(
            response, "<button class='btn btn-primary'>Check In</button>", html=True
        )

