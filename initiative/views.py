from django.shortcuts import render, redirect
from django import views
from initiative.models import Initiative
from initiative.forms import InitiativeForm
from datetime import timezone


class InitiativeView(views.View):
    def get(self, request):
        initiatives = Initiative.objects.all()
        return render(request, "initiative.html", {"initiatives": initiatives})

    def post(self, request):
        form = InitiativeForm(request.POST)
        initiatives = Initiative.objects.all()
        if form.is_valid():
            Initiative.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                team_leader=form.cleaned_data["team_leader"],
                date=timezone.now(),
            )
            form.save()
            return redirect("initiatives")
        else:
            return render(
                request, "initiative.html", {"initiatives": initiatives, "form": form}
            )

