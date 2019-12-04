from django.test import TestCase
from reflections import models
from django.utils import timezone
from django.contrib import admin


# Create your tests here.
class TestAdminCreatesReflection(TestCase):
    def test_basic_models_exist(self):
        reflection = models.Reflection.objects.create(date=timezone.now().date)

        reflection.question_set.create(prompt="What is the meaning of Python?")
        reflection.question_set.create(prompt="How was lunch?")
        reflection.question_set.create(prompt="Do you even lift, bro?")

    def test_models_are_registered_with_admin_site(self):
        self.assertIn(admin.site._registry, models.Reflection)
        self.assertIn(admin.site._registry, models.Question)
