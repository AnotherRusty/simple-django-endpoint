from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from . import models

# Create your tests here.
class TestStudentSpecifiesCommuteDistance(TestCase):
    def test_successfully(self):
        examples = [
            {"username": "joe", "miles": 42},
            {"username": "betty", "miles": 456789},
        ]

        for example in examples:
            user = User.objects.create_user(example["username"])

            self.client.force_login(user)

            self.client.post(
                reverse("mileage_tracker:home"), {"miles": example["miles"]}
            )

            self.assertEqual(user.distancetowork.miles, example["miles"])

    def test_updating_their_existing_distance(self):
        user = User.objects.create_user("charlie")
        models.DistanceToWork.objects.create(user=user, miles=500)

        self.client.force_login(user)

        self.client.post(reverse("mileage_tracker:home"), {"miles": 42})

        user.distancetowork.refresh_from_db()

        self.assertEqual(user.distancetowork.miles, 42)


class TestStudentSeesTheirCommuteDistance(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("charlie")
        models.DistanceToWork.objects.create(user=user, miles=500)

        self.client.force_login(user)

        response = self.client.get(reverse("mileage_tracker:home"))

        self.assertContains(response, "500 miles")


class TestStudentSubmitsCommuteForTheDay(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("Santa")
        models.DistanceToWork.objects.create(user=user, miles=300)

        self.client.force_login(user)

        self.client.post(reverse("mileage_tracker:did_commute"))

        self.assertEqual(user.drivetowork_set.count(), 1)

        drive = user.drivetowork_set.first()

        self.assertEqual(drive.distance, 300)


class TestDriveToWork(TestCase):
    def test_str(self):
        now = timezone.now()
        drive = models.DriveToWork(date=now, distance=42)
        self.assertEqual(str(drive), f"{now} | 42")
