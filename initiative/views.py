from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.views.generic import DeleteView, UpdateView
from initiative.models import Initiative
from initiative.forms import InitiativeForm, InitiativeUpdateForm
from django.utils import timezone


class InitiativeView(views.View):
    def get(self, request):
        initiatives = Initiative.objects.all()
        return render(
            request,
            "initiative.html",
            {"initiatives": initiatives, "form": InitiativeForm()},
        )


class InitiativeCreateView(LoginRequiredMixin, views.View):
    def post(self, request):
        form = InitiativeForm(request.POST)
        initiatives = Initiative.objects.all()
        if form.is_valid():
            Initiative.objects.create(
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                team_leader=request.user,
                date=timezone.now(),
            )
            return redirect("initiatives:home")
        else:
            return render(
                request, "initiative.html", {"initiatives": initiatives, "form": form}
            )


class InitiativeUpdateView(LoginRequiredMixin, UpdateView):
    model = Initiative
    form_class = InitiativeUpdateForm
    pk_url_kwarg = "id"
    template_name = "edit.html"
    success_url = reverse_lazy("initiatives:home")


class InitiativeDeleteView(LoginRequiredMixin, DeleteView):
    model = Initiative
    pk_url_kwarg = "id"
    success_url = reverse_lazy("initiatives:home")
