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
    player_1_verification = models.BooleanField()
    player_2_verification = models.BooleanField()
    
    def winner(self):
        if self.player1_score >= self.player2_score + 2:
            if self.player1_score >= 11:
                return self.player1
        elif self.player2_score >= self.player1_score + 2:
            if self.player2_score >= 11:
                return self.player2

    def loser(self):
        if self.player1_score >= self.player2_score + 2:
            if self.player1_score >= 11:
                return self.player2
        elif self.player2_score >= self.player1_score + 2:
            if self.player2_score >= 11:
                return self.player1
