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
        return render(request, "attendance.html")
    elif request.method == "POST":
        student = request.user
        checkin = Checkin.objects.create(student=student, datetime=timezone.now())
        checkin.save()
        return redirect("attendance:thanks")
    else:
        return render(request, "attendance.html", {"form": form})
    return redirect("attendance.html")


@login_required
def thanks(request):
    if request.method == "GET":
        return render(request, "thanks.html")
