from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django import views
from django.views.generic import DeleteView, UpdateView, CreateView
from initiative.models import Initiative, StatusReport
from initiative.forms import InitiativeForm, InitiativeEditForm, StatusReportForm
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


class InitiativeDetailView(LoginRequiredMixin, views.View):
    def get(self, request, id):
        initiative = Initiative.objects.get(id=id)
        return render(
            request,
            "detail.html",
            {"initiative": initiative, "form": InitiativeForm()},
        )


class InitiativeEditView(LoginRequiredMixin, UpdateView):
    model = Initiative
    form_class = InitiativeEditForm
    pk_url_kwarg = "id"
    template_name = "edit.html"
    success_url = reverse_lazy("initiatives:home")


class InitiativeDeleteView(LoginRequiredMixin, DeleteView):
    model = Initiative
    pk_url_kwarg = "id"
    success_url = reverse_lazy("initiatives:home")


class InitiativeToggleView(LoginRequiredMixin, views.View):
    def get(self, request, id):
        initiative = Initiative.objects.get(id=id)
        initiative.completion = not initiative.completion
        initiative.save()
        return redirect("home")


class InitiativeStatusReportView(LoginRequiredMixin, CreateView):
    def get(self, request, id):
        initiative = Initiative.objects.get(id=id)
        form = StatusReportForm()
        return render(request, "status.html", {"initiative": initiative, "form": form})

    def post(self, request, id):
        form = StatusReportForm(request.POST)
        if form.is_valid():
            StatusReport.objects.create(
                content=form.cleaned_data["content"],
                initiative_id=id,
                author=request.user,
                date=timezone.now(),
            )
            return redirect("initiatives:home")
        else:
            return render(request, "status.html", {"form": form})

