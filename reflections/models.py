from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.



class Reflection(models.Model):
    day_of_reflection = models.DateField()


class Question(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.PROTECT)
    content = models.TextField()


class Submission(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class QuestionSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    submission = models.ForeignKey(Submission, on_delete=models.PROTECT)
    answer = models.TextField()
