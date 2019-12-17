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

        self.client.post(reverse("mileage_tracker:user_commute"))

        self.assertEqual(user.drivetowork_set.count(), 1)

        drive = user.drivetowork_set.first()

        self.assertEqual(drive.distance, 300)


class TestDriveToWork(TestCase):
    def test_str(self):
        now = timezone.now()
        drive = models.DriveToWork(date=now, distance=42)
        self.assertEqual(str(drive), f"{now} | 42")


class TestStudentNeedsAGasCard(TestCase):
    "A User needs a gas card every 250 miles"

    def setUp(self):
        self.fifteen_miles_user = User.objects.create_user("nate")
        models.DistanceToWork.objects.create(user=self.fifteen_miles_user, miles=15)

        self.ten_miles_user = User.objects.create_user("evilnate")
        models.DistanceToWork.objects.create(user=self.ten_miles_user, miles=10)

    def test_not_yet(self):
        self.fifteen_miles_user.drivetowork_set.create()

        self.assertFalse(
            models.needs_a_gas_card(self.fifteen_miles_user),
            msg="1 15 mile trip is not enough for a gas card",
        )

        self.ten_miles_user.drivetowork_set.create()
        self.ten_miles_user.drivetowork_set.create()

        self.assertFalse(
            models.needs_a_gas_card(self.ten_miles_user),
            msg="2 10 mile trips is not enough for a gas card",
        )

    def test_yes(self):
        for _ in range(17):
            self.fifteen_miles_user.drivetowork_set.create()

        self.assertTrue(
            models.needs_a_gas_card(self.fifteen_miles_user),
            msg="17 15 mile trips (255 miles) is enough for a gas card",
        )

        for _ in range(25):
            self.ten_miles_user.drivetowork_set.create()

        self.assertTrue(
            models.needs_a_gas_card(self.ten_miles_user),
            msg="25 10 mile trips (250 miles) is enough for a gas card",
        )

    def test_no_after_receiving_a_card(self):
        for _ in range(17):
            self.fifteen_miles_user.drivetowork_set.create()

        models.GasCardGiven.objects.create(user=self.fifteen_miles_user)

        self.assertFalse(
            models.needs_a_gas_card(self.fifteen_miles_user),
            msg="17 15 mile trips (255 miles) is not enough if I gave you gas card",
        )

        for _ in range(25):
            self.ten_miles_user.drivetowork_set.create()
        models.GasCardGiven.objects.create(user=self.ten_miles_user)
        # self.ten_miles_user.gascard_set.create()

        self.assertFalse(
            models.needs_a_gas_card(self.ten_miles_user),
            msg="25 10 mile trips (250 miles) is not enough if I gave you gas card",
        )

    def test_yes_after_receiving_a_card(self):
        for _ in range(41):
            self.fifteen_miles_user.drivetowork_set.create()

        models.GasCardGiven.objects.create(user=self.fifteen_miles_user)
        # self.fifteen_miles_user.gascard_set.create()

        self.assertTrue(
            models.needs_a_gas_card(self.fifteen_miles_user),
            msg="41 15 mile trips (615 miles) is enough even after recieving a gas card",
        )

        for _ in range(50):
            self.ten_miles_user.drivetowork_set.create()

        models.GasCardGiven.objects.create(user=self.fifteen_miles_user)
        # self.ten_miles_user.gascard_set.create()

        self.assertTrue(
            models.needs_a_gas_card(self.ten_miles_user),
            msg="50 10 mile trips (500 miles) is enough even after recieving a card",
        )

    def test_yes_after_receiving_many_cards(self):
        for _ in range(100):
            self.fifteen_miles_user.drivetowork_set.create()

        for _ in range(3):
            models.GasCardGiven.objects.create(user=self.fifteen_miles_user)
        # self.fifteen_miles_user.gascard_set.create()

        self.assertTrue(
            models.needs_a_gas_card(self.fifteen_miles_user),
            msg="100 15 mile trips (1500 miles) is enough even after recieving 3 gas cards (750 miles)",
        )

        for _ in range(100):
            self.ten_miles_user.drivetowork_set.create()

        for _ in range(2):
            models.GasCardGiven.objects.create(user=self.fifteen_miles_user)
        # self.ten_miles_user.gascard_set.create()

        self.assertTrue(
            models.needs_a_gas_card(self.ten_miles_user),
            msg="100 10 mile trips (1000 miles) is enough even after recieving 2 gas cards (500 miles)",
        )

    def test_no_after_receiving_many_cards(self):
        for _ in range(100):
            self.fifteen_miles_user.drivetowork_set.create()

        for _ in range(6):
            models.GasCardGiven.objects.create(user=self.fifteen_miles_user)
        # self.fifteen_miles_user.gascard_set.create()

        self.assertFalse(
            models.needs_a_gas_card(self.fifteen_miles_user),
            msg="100 15 mile trips (1500 miles) is not enough even after recieving 6 gas cards (1500 miles)",
        )

        for _ in range(100):
            self.ten_miles_user.drivetowork_set.create()

        for _ in range(4):
            models.GasCardGiven.objects.create(user=self.ten_miles_user)
        # self.ten_miles_user.gascard_set.create()

        self.assertFalse(
            models.needs_a_gas_card(self.ten_miles_user),
            msg="100 10 mile trips (1000 miles) is not enough even after recieving 4 gas cards (1000 miles)",
        )
