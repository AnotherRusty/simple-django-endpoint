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

    def winner(self):
        if self.player1_score - 1 != self.player2_score:
            if self.player1_score >= 11:
                winner = self.player1
        elif self.player2_score - 1 != self.player1_score:
            if self.player2_score >= 11:
                winner = self.player2
        return winner
