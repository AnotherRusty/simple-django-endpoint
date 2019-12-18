from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
def today_utc():
    return datetime.utcnow().date()  # pragma: no cover


class Reflection(models.Model):
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Reflection {self.date}"

class Feedback(models.Model):
    reflection = models.ForeignKey(Reflection,on_delete=models.CASCADE)
    feedback_txt = models.TextField()
    
class Question(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE)
    prompt = models.TextField()

    def __str__(self):
        ids = list(self.reflection.question_set.all().values("id"))
        index = ids.index({ "id": self.id})
        return f"Question {index + 1}"


class Submission(models.Model):
    reflection = models.ForeignKey(Reflection, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True,null=True,default="Blank")

    def __str__(self):
        return f"{self.user.username} | Reflection {self.reflection.date}"


class QuestionSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    answer = models.TextField()

    def question__prompt(self):
        return self.question.prompt

    def __str__(self):
        return self.answer
    
