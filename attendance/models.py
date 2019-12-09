from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Checkin(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=timezone.now)
