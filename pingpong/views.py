from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, View
from django.urls import reverse_lazy
from pingpong.models import Match
from django.contrib.auth.models import User


def compute_leaderboard(matches):
    
    leaderboard = []

    def all_players(matches):
        players = set()
        for match in matches:
            if match.winner():
                players.add(match.winner())
                players.add(match.loser())
        return players

    def total_wins(user, matches):
        wins = 0
        for match in matches:
            if user == match.winner():
                wins += 1
        return wins

    def total_losses(user, matches):
        losses = 0
        for match in matches:
            if user == match.loser():
                losses += 1
        return losses

    player_list = all_players(matches)
    player_list

    for player in player_list:
        player_stats = {
            "user": player,
            "wins": total_wins(player, matches),
            "losses": total_losses(player, matches),
        }
        leaderboard.append(player_stats)

    sorted_board = sorted(leaderboard, key=lambda i: i["wins"], reverse=True)
    return sorted_board[:5]


class Home(ListView):
    model = Match
    template_name = "pingpong/home.html"
    context_object_name = "matches"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["leaderboard"] = compute_leaderboard(Match.objects.all())
        return context


class MatchCreateView(CreateView):
    model = Match
    fields = ["player1", "player2", "player1_score", "player2_score"]
    template_name = "pingpong/create-match.html"
    success_url = reverse_lazy("pingpong:home")


class VerifyMatch(View):
    def post(self, request, id):

        match = Match.objects.get(id=id)

        if request.user == match.player1:

            match.player_1_verification = True
            match.save()

            return redirect("pingpong:home")

        elif request.user == match.player2:

            match.player_2_verification = True
            match.save()

            return redirect("pingpong:home")

