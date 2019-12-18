from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from . import models

# Create your tests here.


class TestStudentCreatesShoutout(TestCase):
    def test_successfully(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        self.client.force_login(shouter)

        self.client.post(
            reverse("shoutouts:home"),
            {"recipient": shoutee.id, "content": "jane is soooo dutiful"},
        )

        self.assertEqual(shoutee.shoutouts_received.count(), 1)
        self.assertEqual(shouter.shoutouts_given.count(), 1)

        shoutout = shoutee.shoutouts_received.first()

        self.assertEqual(shoutout.content, "jane is soooo dutiful")

    def test_with_no_data(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        self.client.force_login(shouter)

        response = self.client.post(reverse("shoutouts:home"),)

        self.assertEqual(shoutee.shoutouts_received.count(), 0)
        self.assertEqual(shouter.shoutouts_given.count(), 0)

        self.assertContains(response, "is required")


class TestStudentsCanSeeShoutouts(TestCase):
    def test_successfully(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        shouter.shoutouts_given.create(
            recipient=shoutee,
            content="jane is totes the dutifulest",
            datetime=timezone.now(),
        )

        self.client.force_login(shouter)

        response = self.client.get(reverse("shoutouts:home"))

        self.assertContains(response, "jane is totes the dutifulest")


class TestStudentLikesAShoutout(TestCase):
    def test_successfully(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")
        liker = User.objects.create_user("lucy")

        shoutout = shouter.shoutouts_given.create(
            recipient=shoutee,
            content="jane is totes the dutifulest",
            datetime=timezone.now(),
        )

        self.client.force_login(liker)

        self.client.post(reverse("shoutouts:likes", args=[shoutout.id]))

        self.assertEqual(shoutout.like_set.count(), 1)

        like = shoutout.like_set.first()

        self.assertEqual(like.user, liker)


class TestUserSeesAStudentsShoutouts(TestCase):
    def test_successfully(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        shoutout = shouter.shoutouts_given.create(
            recipient=shoutee,
            content="jane is totes the dutifulest",
            datetime=timezone.now(),
        )

        response = self.client.get(
            reverse("shoutouts:individual_shoutouts", args=[shoutee.id]))

        self.assertContains(response, "dutiful jane")
        self.assertContains(response, "happy joe")
        self.assertContains(response, "jane is totes the dutifulest")


class TestUserPinsShoutout(TestCase):
    def test_successfully(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        shoutout = shouter.shoutouts_given.create(
            recipient=shoutee,
            content="jane is totes the dutifulest",
            datetime=timezone.now(),
        )

        self.client.force_login(shoutee)

        self.client.post(reverse("shoutouts:pin", args=[shoutout.id]))

        shoutee.refresh_from_db()

        self.assertEqual(shoutee.pinnedshoutout.shoutout, shoutout)

    def test_replaces_pin(self):
        shouter = User.objects.create_user("happy joe")
        shoutee = User.objects.create_user("dutiful jane")

        pinned = shouter.shoutouts_given.create(
            recipient=shoutee,
            content="jane is totes the dutifulest",
            datetime=timezone.now(),
        )

        models.PinnedShoutout.objects.create(
            user=shoutee, shoutout=pinned
        )

        to_pin = shouter.shoutouts_given.create(
            recipient=shoutee,
            content="jane is totes the dutifulest, again!",
            datetime=timezone.now(),
        )

        self.client.force_login(shoutee)

        self.client.post(reverse("shoutouts:pinned", args=[to_pin.id]))

        shoutee.refresh_from_db()

        self.assertEqual(shoutee.pinnedshoutout.shoutout, to_pin)
