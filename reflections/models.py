from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Question(models.Model):
    content = models.TextField()
    answer = models.TextField()


class Reflection(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    day_of_reflection = models.DateField()


class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.TextField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class QuestionSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    answer = models.ForeignKey(Submission, on_delete=models.PROTECT)
