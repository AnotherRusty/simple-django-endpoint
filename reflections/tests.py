from django.test import TestCase
from reflections import models
from datetime import datetime
from django.contrib import admin


# Create your tests here.
class TestAdminCreatesReflection(TestCase):
    def test_basic_models_exist(self):
        reflection = models.Reflection.objects.create(date=datetime.now().date())

        reflection.question_set.create(prompt="What is the meaning of Python?")
        reflection.question_set.create(prompt="How was lunch?")
        reflection.question_set.create(prompt="Do you even lift, bro?")

    def test_models_are_registered_with_admin_site(self):
        self.assertIn(models.Reflection, admin.site._registry)
        self.assertIn(models.Question, admin.site._registry)
