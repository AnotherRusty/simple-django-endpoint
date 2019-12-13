from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from pingpong.models import Match
from django.contrib.auth.models import User


def compute_leaderboard(matches):
    wins = {}
    for match in matches:
        if match.winner():
            wins[match.winner()] = wins.get(match.winner(), 0) + 1
            wins[match.loser()] = wins.get(match.loser(), 0)

    leaderboard = []

    for key, value in wins.items():
        thewinner = {"user": key, "wins": value}
        leaderboard.append(thewinner)

    sorted_board = sorted(leaderboard, key=lambda i: i["wins"], reverse=True)
    return sorted_board


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
