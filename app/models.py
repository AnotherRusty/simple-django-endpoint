from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    headline = models.TextField()
    resume = models.FileField()
    biography = models.TextField()
    profile_picture = models.ImageField()

