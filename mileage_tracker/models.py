from django.db import models
from django.contrib.auth.models import User

class DistanceToWork(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    miles = models.FloatField()

class Commute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commute = models.TextField()
