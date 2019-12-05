from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from . import models

# Create your tests here.
class TestStudentCreatesInitiative(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")

        self.client.post(
            reverse("initiatives:create"),
            {
                "title": "recycling",
                "description": "reduce! reuse! recycle!",
                # "team_leader": "Des Mal",
            },
        )

        self.assertEqual(user.initiative_set.count(), 1)

        initiative = user.initiative_set.first()

        self.assertEqual(initiative.title, "recycling")
        self.assertEqual(initiative.description, "reduce! reuse! recycle!")
        # self.assertEqual(initiative.team_leader, "user@basecampcodingacademy.org")

