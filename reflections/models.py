from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.



class Reflection(models.Model):
    date = models.DateField()


class Question(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.PROTECT)
    prompt = models.TextField()
    
    def __str__(self):
        return self.prompt
    


class Submission(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


class QuestionSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    submission = models.ForeignKey(Submission, on_delete=models.PROTECT)
    answer = models.TextField()
