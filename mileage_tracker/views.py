from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, View, DetailView
from django.contrib.auth.models import User
from mileage_tracker.models import (
    DistanceToWork,
    DriveToWork,
    GasCardGiven,
    calculate_user_mileage_data,
)
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

    def get(self, request):
        return render(request, "mileage_tracker/submit_commute.html")


class ShowUserList(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request):
        profiles = User.objects.all()
        drives = DriveToWork.objects.all()
        gas_cards = GasCardGiven.objects.all()
        return render(
            request,
            "mileage_tracker/user_list.html",
            {"profiles": profiles, "drives": drives, "gas_cards": gas_cards},
        )


class UserGasDetail(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_staff

    def get(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        data = calculate_user_mileage_data(user)
        return render(
            request,
            "mileage_tracker/gas_detail_page.html",
            {
                "user": user,
                "days_driven": data.get("days_driven"),
                "distance": data.get("distance"),
                "compensated_miles": data.get("compensated_miles"),
                "total_mileage": data.get("total_mileage"),
                "gas_cards_given": data.get("gas_cards_given"),
            },
        )

    def post(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        GasCardGiven.objects.create(user=user, date_given=timezone.now())
        return redirect("mileage_tracker:admin")

