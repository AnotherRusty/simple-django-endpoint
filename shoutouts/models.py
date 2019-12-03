from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Shoutout(models.Model):
    recipient = models.ForeignKey(
        User, related_name="shoutouts_received", on_delete=models.PROTECT
    )
    content = models.TextField()
    user = models.ForeignKey(
        User, related_name="shoutouts_given", on_delete=models.PROTECT
    )
    datetime = models.DateTimeField()
    likes = models.IntegerField()
