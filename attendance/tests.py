from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Checkin


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


class TestDailyCheckinRepot(TestCase):
    def test_one_present_one_absent_one_tardy(self):
        abe = User.objects.create_user("abe")
        betty = User.objects.create_user("betty")
        clara = User.objects.create_user("clara")

        seven_fortyfive = timezone.now().replace(hour=7, minute=45)
        nine_fifteen = timezone.now().replace(hour=9, minute=15)

        abe.checkin_set.create(datetime=seven_fortyfive)
        betty.checkin_set.create(datetime=nine_fifteen)

        report = Checkin.daily_report()

        self.assertDictEqual(report, {abe: "Present", betty: "Tardy", clara: "Absent"})

