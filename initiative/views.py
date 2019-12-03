from django.shortcuts import render, redirect
from django import views
from initiative.models import Initiative
from initiative.forms import InitiativeForm

class InitiativeView(views.View):
    def get(self, request):
        initiatives = Initiative.objects.all()
        return render(request, "initiative.html", {"initiatives": initiatives})

    def post(self, request):
        form = InitiativeForm(request.POST)
        initiatives = Initiative.objects.all()
        if form.is_valid():
            Initiative.objects.create(
                name = form.cleaned_data["name"],
                team_leader = form.cleaned_data["team_leader"],
                goal_date = form.cleaned_data["goal_date"],
                team = form.cleaned_data["team"],
                timeline = form.cleaned_data["timeline"]
            )
            return redirect("initiatives")
        else:
            return render(request, "initiative.html", {"initiatives": initiatives, "form": form})