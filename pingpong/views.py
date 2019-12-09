from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from pingpong.models import Match
from django.contrib.auth.models import User


class Home(ListView):
    model = Match
    template_name = "pingpong/home.html"
    context_object_name = "matches"


class MatchCreateView(CreateView):
    model = Match
    fields = ["player1", "player2", "player1_score", "player2_score"]
    template_name = "pingpong/create-match.html"
    success_url = reverse_lazy("pingpong:home")

    # def post(self, request):
    #     if model["player1_score"] - 1 != model["player2_score"]:
    #         if model["player1_score"] >= 11:
    #             winner = model["player1"]
    #     elif model["player2_score"] - 1 != model["player1_score"]:
    #         if model["player2_score"] >= 11:
    #             winner = model["player1"]


class LeaderBoard(ListView):
    model = User
    matches = Match
    template_name = "pingpong/leaderboard.html"
    context_object_name = "users"
