from django.db import models
from django.contrib.auth.models import User

# Don't forget to migrate when you return
class Match(models.Model):
    player1 = models.ForeignKey(
        User, related_name="matches_as_player1", on_delete=models.PROTECT
    )
    player2 = models.ForeignKey(
        User, related_name="matches_as_player2", on_delete=models.PROTECT
    )
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()

