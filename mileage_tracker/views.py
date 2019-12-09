from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from mileage_tracker.models import DistanceToWork

class DistanceToWorkCreateView(LoginRequiredMixin, CreateView):
    model = DistanceToWork
    fields = ["miles"]
    template_name = "mileage_tracker/mileage-form.html"

    def form_valid(self, form):
        try:
            self.request.user.distancetowork.miles = form.cleaned_data["miles"]
            self.request.user.distancetowork.save()
        except DistanceToWork.DoesNotExist:
            DistanceToWork.objects.create(
                user=self.request.user,
                miles=form.cleaned_data["miles"]
            )
        return redirect("mileage_tracker:set_commute")
