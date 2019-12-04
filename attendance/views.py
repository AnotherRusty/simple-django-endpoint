"""

Create the view that uses a form and our check-in button to sign in the user. 


"""

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from attendance.models import Checkin
from django.contrib.auth.models import User
from attendance.forms import Checkinform

@login_required
def checkin(request):
    if not user.checked_in:
        user.checked_in = True
        user.save()
        form = Checkinform(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "you have checked in successfully!")
            return redirect("attendance.html")
        else:
            messages.warning(request, "You are already checked.")
    return render(request, "attendance.html", {"form": form})


class Attendance(View):
    def get(self, request):
        return render(request, "attendance.html")
