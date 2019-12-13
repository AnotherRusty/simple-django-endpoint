from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Shoutout(models.Model):
    recipient = models.ForeignKey(
        User, related_name="shoutouts_received", on_delete=models.PROTECT
    )
    content = models.TextField()
    datetime = models.DateTimeField()
    anonymous = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, related_name="shoutouts_given", on_delete=models.PROTECT
    )

    class Meta:
        ordering = ['-datetime', ]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    shoutout = models.ForeignKey(Shoutout, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'shoutout',)