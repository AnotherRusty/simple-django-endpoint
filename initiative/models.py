from django.db import models
from django.contrib.auth.models import User


class Initiative(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    team = models.TextField()
    team_leader = models.TextField()
    started_at = models.DateTimeField(auto_now=True)
    goal_date = models.DateField()
    timeline = models.TextField()
    retired = models.BooleanField(default=False)
