from django.test import TestCase
from reflections import models
from datetime import datetime
from django.contrib import admin
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

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


class TestStudentSubmitsReflection(TestCase):
    def test_successfully(self):
        user = User.objects.create_user("janet")
        reflection = models.Reflection.objects.create(date=timezone.now())
        question1 = reflection.question_set.create(
            prompt="What is the meaning of Python?"
        )
        question2 = reflection.question_set.create(prompt="How was lunch?")
        question3 = reflection.question_set.create(prompt="Do you even lift, bro?")

        self.client.force_login(user)

        self.client.post(
            reverse("reflections:submit_reflection", args=[reflection.id]),
            {
                f"question-{question1.id}": "Simple is better than complex",
                f"question-{question2.id}": "Terrific",
                f"question-{question3.id}": "Come at me, bro!",
            },
        )

        self.assertEqual(user.submission_set.count(), 1)

        submission = user.submission_set.first()

        self.assertEqual(submission.reflection, reflection)
        self.assertEqual(submission.questionsubmission_set.count(), 3)

        self.assertQuerysetEqual(
            submission.questionsubmission_set.all(),
            [question1, question2, question3],
            ordered=False,
            transform=lambda sub: sub.question,
            msg="The submission should have a QuestionSubmission for each Question in the Reflection",
        )

        answer1 = submission.questionsubmission_set.get(question=question1)
        answer2 = submission.questionsubmission_set.get(question=question2)
        answer3 = submission.questionsubmission_set.get(question=question3)

        self.assertEqual(answer1.answer, "Simple is better than complex")
        self.assertEqual(answer2.answer, "Terrific")
        self.assertEqual(answer3.answer, "Come at me, bro!")

