from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    headline = models.TextField()
    bio = models.TextField()

    def __str__(self):
        return self.headline
