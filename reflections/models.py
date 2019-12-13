from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
def today_utc():
    return datetime.utcnow().date() # pragma: no cover


class Reflection(models.Model):
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Reflection {self.date}"


class Question(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.PROTECT)
    prompt = models.TextField()


class Submission(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.user.username} | Reflection {self.reflection.date}"


class QuestionSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    submission = models.ForeignKey(Submission, on_delete=models.PROTECT)
    answer = models.TextField()

    def question__prompt(self):
        return self.question.prompt
