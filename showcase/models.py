from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    headline = models.TextField()
    bio = models.TextField()
    codepen = models.URLField()
    github_repository = models.URLField()

class StudentOfTheDay(models.Model):
    Student = models.ForeignKey(Profile, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return self.headline
