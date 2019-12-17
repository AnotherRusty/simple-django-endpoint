from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Initiative(models.Model):
    title = models.TextField()
    description = models.TextField()
    team_leader = models.ForeignKey(User, on_delete=models.PROTECT)
    completion = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    timeline = models.TextField(blank=True)


class StatusReport(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    initiative = models.ForeignKey(Initiative, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
