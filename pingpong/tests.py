from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from .models import Match
from .views import compute_leaderboard
from django.urls import reverse


class TestComputeLeaderboard(TestCase):
    def test_no_matches(self):
        leaderboard = compute_leaderboard([])

        self.assertListEqual(leaderboard, [])

    def test_one_match(self):
        winner = User(username="winnie", id=1)
        loser = User(username="lucy", id=3)

        leaderboard = compute_leaderboard(
            [Match(player1=winner, player2=loser, player2_score=7, player1_score=11)]
        )

        self.assertListEqual(
            leaderboard, [{"user": winner, "wins": 1}, {"user": loser, "wins": 0}]
        )


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
                "player2_score": 11,
            },
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
