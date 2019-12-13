from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
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
        return redirect("mileage_tracker:home")


class DriveToWorkView(LoginRequiredMixin, View):
    def post(self, request):
        distance = request.user.distancetowork.miles
        DriveToWork.objects.create(
            user=request.user, date=timezone.now(), distance=distance
        )
        messages.success(request, f"Welcome to Base Camp, {request.user}")
        return redirect("home")


class CheckIfAdmin(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        if self.test_func():
            profiles = User.objects.all()
            drives = DriveToWork.objects.all()
            return render(
                request,
                "mileage_tracker/user_list.html",
                {"profiles": profiles, "drives": drives},
            )
        else:
            return redirect("home")
