from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View
from mileage_tracker.models import DistanceToWork, DriveToWork
from mileage_tracker.forms import DriveToWorkForm


class DistanceToWorkCreateView(LoginRequiredMixin, CreateView):
    model = DistanceToWork
    fields = ["miles"]
    template_name = "mileage_tracker/specify_distance.html"

    def form_valid(self, form):
        try:
            self.request.user.distancetowork.miles = form.cleaned_data["miles"]
            self.request.user.distancetowork.save()
        except DistanceToWork.DoesNotExist:
            DistanceToWork.objects.create(
                user=self.request.user, miles=form.cleaned_data["miles"]
            )
        return redirect("mileage_tracker:set_distance")


class DriveToWorkView(LoginRequiredMixin, View):
    def post(self, request):
        form = DriveToWorkForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data["date"]
            DriveToWork.objects.create(user=request.user, date=date)
            messages.success(request, f"Welcome to Base Camp, {request.user}")
            return redirect("home")
        else:
            messages.error(request, "Failure to verify your commute")
            return redirect("home")

    def get(self, request):
        return render(request, "mileage_tracker/submit_commute.html")

