from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from attendance.models import Checkin
from django.contrib.auth.models import User
from django.utils import timezone


@login_required
def checkin(request):
    if request.method == "GET":
        users = User.objects.all()
        daily_report = Checkin.daily_report()
        user_is_checked_in = Checkin.is_user_checked_in(request.user)
        return render(
            request,
            "attendance.html",
            {"user_is_checked_in": user_is_checked_in, "daily_report": daily_report,},
        )
    elif request.method == "POST":
        Checkin.checkin_user(request.user)
        return redirect("attendance:check-in")

