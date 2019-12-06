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
        # messages.success(request, "you have checked in successfully!")
        return render(request, "attendance.html")
    elif request.method == "POST":
            student = request.user
            messages.success(request, "You are checked in.")
            checkin = Checkin.objects.create(
                    student=student, datetime=timezone.now()
                )
            checkin.save()
            return redirect("attendance:check-in")
    else:
        return render(request, "attendance.html" , {"form":form})
    return redirect("attendance.html")
