from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Initiative(models.Model):
    title = models.TextField()
    description = models.TextField()
    team_leader = models.ForeignKey(User, on_delete=models.PROTECT)
    # visual = models.URLField((""), max_length=200)
    date = models.DateField(default=timezone.now)
