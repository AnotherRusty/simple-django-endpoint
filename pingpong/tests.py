from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class TestUserUploadsMatchScore(TestCase):
    def test_successfully(self):
        player1 = User.objects.create_user("forehand franklin")
        player2 = User.objects.create_user("topspin trish")

        self.client.post(
            reverse("pingpong:create-match"),
            {
                "player1": player1.id,
                "player2": player2.id,
                "player1_score": 8,
                "player2_score": 11
            }
        )

        self.assertEqual(player1.matches_as_player1.count(), 1)
        self.assertEqual(player2.matches_as_player2.count(), 1)
        self.assertEqual(player1.matches_as_player2.count(), 0)
        self.assertEqual(player2.matches_as_player1.count(), 0)

        match = player1.matches_as_player1.first()

        self.assertEqual(match.player1, player1)
        self.assertEqual(match.player2, player2)
        self.assertEqual(match.player1_score, 8)
        self.assertEqual(match.player2_score, 11)
