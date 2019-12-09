from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class DistanceToWork(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    miles = models.FloatField()


class DriveToWork(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
