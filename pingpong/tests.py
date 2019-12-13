from django.test import TestCase, SimpleTestCase
from django.contrib.auth.models import User
from .models import Match
from .views import compute_leaderboard
from django.urls import reverse


class TestMatchWinnerLoser(TestCase):
    def test_player1_wins(self):
        winner = User(username="winnie", id=1)
        loser = User(username="lucy", id=3)
        match = Match(player1=winner, player2=loser, player2_score=7, player1_score=11)

        self.assertEqual(match.winner(), winner)
        self.assertEqual(match.loser(), loser)

    def test_player2_wins(self):
        winner = User(username="winnie", id=1)
        loser = User(username="lucy", id=3)
        match = Match(player1=loser, player2=winner, player2_score=11, player1_score=7)

        self.assertEqual(match.winner(), winner)
        self.assertEqual(match.loser(), loser)

    def test_no_player_wins(self):
        user1 = User(username="brady", id=8)
        user2 = User(username="dilly", id=2)
        match = Match(player1=user1, player2=user2, player2_score=7, player1_score=7)

        self.assertIsNone(match.winner())
        self.assertIsNone(match.loser())



class TestComputeLeaderboard(TestCase):
    def test_no_matches(self):
        leaderboard = compute_leaderboard([])

        self.assertListEqual(leaderboard, [])

    def test_one_match(self):
        winner = User(username="winnie", id=1)
        loser = User(username="lucy", id=3)
        matches = [
            Match(player1=winner, player2=loser, player2_score=7, player1_score=11)
        ]

        leaderboard = compute_leaderboard(matches)

        self.assertListEqual(
            leaderboard, [{"user": winner, "wins": 1}, {"user": loser, "wins": 0}]
        )

    def test_two_match(self):
        two_wins = User(username="winnie", id=1)
        one_win = User(username="lucy", id=3)
        no_wins = User(username="person3", id=5)

        matches = [
            Match(player1=one_win, player2=no_wins, player1_score=11, player2_score=7),
            Match(player1=two_wins, player2=one_win, player1_score=11, player2_score=7),
            Match(player1=two_wins, player2=no_wins, player1_score=11, player2_score=7),
        ]

        leaderboard = compute_leaderboard(matches)

        self.assertListEqual(
            leaderboard,
            [
                {"user": two_wins, "wins": 2},
                {"user": one_win, "wins": 1},
                {"user": no_wins, "wins": 0},
            ],
        )

    def test_no_winner_matches_dont_show_up(self):
        not_winner = User(username="winnie", id=1)
        not_loser = User(username="lucy", id=3)
        matches = [
            Match(
                player1=not_winner, player2=not_loser, player2_score=3, player1_score=3
            )
        ]

        leaderboard = compute_leaderboard(matches)

        self.assertListEqual(leaderboard, [])


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
