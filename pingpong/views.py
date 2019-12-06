from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from pingpong.models import Match


class Home(ListView):
    model = Match
    template_name = "pingpong/home.html"
    context_object_name = "matches"

class MatchCreateView(CreateView):
    model = Match
    fields = ["player1", "player2", "player1_score", "player2_score"]
    template_name = "pingpong/home.html"
    success_url = reverse_lazy('pingpong:home')
