from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth


class TestUserVisitsHomePage(TestCase):
    def test_successfully(self):
        response = self.client.get("/")
        self.assertContains(response, "Ascent")
        self.assertContains(response, "<title>Ascent</title>", html=True)


class TestUserLogsIn(TestCase):
    def test_successfully(self):
        user = User.objects.create_user(
            "student", "student@basecampcodingacademy.org", "studentpassword"
        )

        self.client.get("/login/")

        response = self.client.post(
            "/login/", {"username": "student", "password": "studentpassword"}
        )

        self.assertEqual(user, auth.get_user(self.client))
