from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from . import models

# Create your tests here.
class TestStudentCreatesInitiative(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")

        self.client.force_login(user)

        self.client.post(
            reverse("initiatives:create"),
            {"title": "recycling", "description": "reduce! reuse! recycle!"},
        )

        self.assertEqual(user.initiative_set.count(), 1)

        initiative = user.initiative_set.first()

        self.assertEqual(initiative.title, "recycling")
        self.assertEqual(initiative.description, "reduce! reuse! recycle!")

    def test_with_no_data(self):
        user = User.objects.create_user("selfstartersuz")

        self.client.force_login(user)

        response = self.client.post(reverse("initiatives:create"))

        self.assertEqual(user.initiative_set.count(), 0)

        self.assertContains(response, "is required")


class TestUserSeesInitiatives(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")
        user.initiative_set.create(title="BLOAW", description="Doing big things!")

        response = self.client.get(reverse("initiatives:home"))

        self.assertContains(response, "BLOAW")


class TestUserSeesInitiative(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")
        initiative = user.initiative_set.create(
            title="BLOAW", description="Doing big things!"
        )

        response = self.client.get(reverse("initiatives:detail", args=[initiative.id]))

        self.assertContains(response, "BLOAW")

        self.assertContains(response, "Doing big things!")


class TestInitiativeLeaderMarksInitiativeAsCompleted(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")
        initiative = user.initiative_set.create(
            title="BLOAW", description="Doing big things!", completion=False
        )

        self.client.force_login(user)

        response = self.client.post(reverse("initiatives:toggle", args=[initiative.id]))

        initiative.refresh_from_db()

        self.assertTrue(initiative.completion)


class TestTeamLeaderVisitsStatusReportCreationPage(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")
        initiative = user.initiative_set.create(
            title="BLOAW", description="Doing big things!", completion=False
        )

        self.client.force_login(user)

        response = self.client.get(reverse("initiatives:status", args=[initiative.id]))

        self.assertContains(response, initiative.title)
        self.assertContains(response, "Post Status Report")


class TestTeamLeaderPostsStatusReport(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("selfstartersuz")
        initiative = user.initiative_set.create(
            title="BLOAW", description="Doing big things!", completion=False
        )

        self.client.force_login(user)

        response = self.client.post(
            reverse("initiatives:status", args=[initiative.id]),
            {"content": "All we do is win"},
        )

        self.assertEqual(initiative.statusreport_set.count(), 1)

        report = initiative.statusreport_set.first()

        self.assertEqual(report.content, "All we do is win")

    def test_without_any_content(self):
        user = User.objects.create_user("selfstartersuz")
        initiative = user.initiative_set.create(
            title="BLOAW", description="Doing big things!", completion=False, id=9001
        )

        self.client.force_login(user)

        print(initiative.id)

        response = self.client.post(reverse("initiatives:status", args=[initiative.id]))

        self.assertEqual(initiative.statusreport_set.count(), 0)


class TestTeamLeaderCreatesInitiativeTimeline(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("butterflyman")

        self.client.force_login(user)

        self.client.post(
            reverse("initiatives:create"),
            {"title": "sweeping", "description": "get rid of dust", "timeline": "12/03/2000"},
        )

        self.assertEqual(user.initiative_set.count(), 1)

        initiative = user.initiative_set.first()

        self.assertEqual(initiative.title, "sweeping")
        self.assertEqual(initiative.description, "get rid of dust")
        self.assertEqual(initiative.timeline, "12/03/2000")

    def test_with_no_data(self):
        user = User.objects.create_user("butterflyman")

        self.client.force_login(user)

        response = self.client.post(reverse("initiatives:create"))

        self.assertEqual(user.initiative_set.count(), 0)

        self.assertContains(response, "is required")
