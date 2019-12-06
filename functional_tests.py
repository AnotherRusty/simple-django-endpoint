from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth
from django.core import mail
from django.utils import timezone
from datetime import timedelta
from magic_links.models import MagicLink


class TestUserVisitsHomePage(TestCase):
    def test_successfully(self):
        response = self.client.get("/")
        self.assertContains(response, "Ascent")
        self.assertContains(response, "<title>Ascent</title>", html=True)


class TestUserLogsOut(TestCase):
    def test_successfully(self):
        user = User.objects.create_user(
            "student", "student@basecampcodingacademy.org", "studentpassword"
        )

        self.client.force_login(user)

        self.client.get("/logout/")

        self.assertFalse(auth.get_user(self.client).is_authenticated)


class TestUserLogsInViaMagicLink(TestCase):
    def test_successfully(self):
        self.user = User.objects.create_user("nate", "natec425@gmail.com")

        with self.subTest("user can request a magic link via email"):
            response = self.client.post(
                "/magic-link/create/", {"email": self.user.email}
            )

            emails = [(m.to, m.subject) for m in mail.outbox]

            self.assertIn(([self.user.email], "Ascent - Magic Link"), emails)

            email = next(m for m in mail.outbox if self.user.email in m.to)

        with self.subTest("user can login via the link provided in the email"):
            self.client.get(email.body)

            self.assertEqual(self.user, auth.get_user(self.client))

    def test_cannot_login_with_nonexistent_token(self):
        self.client.get("/magic-link/login/?token=blahblahblah")

        self.assertFalse(auth.get_user(self.client).is_authenticated)
