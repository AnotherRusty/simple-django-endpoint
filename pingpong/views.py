from django.shortcuts import render, redirect
from pingpong.models import Match
from pingpong.forms import MatchForm


def home(request):
    matches = Match.objects.all()
    return render(request, "pingpong/home.html", {"matches": matches})


def create_match(request):
    if request.method == "GET":
        return render(request, "pingpong/home.html")
    elif request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            player1 = form.cleaned_data["player1"]
            player2 = form.cleaned_data["player2"]
            player1_score = form.cleaned_data["player1_score"]
            player2_score = form.cleaned_data["player2_score"]
            match = Match.objects.create(
                player1_id=player1,
                player2_id=player2,
                player1_score=player1_score,
                player2_score=player2_score,
            )
            return redirect("pingpong:home")
        else:
            return render(request, "pingpong/home.html", {"form": form})
