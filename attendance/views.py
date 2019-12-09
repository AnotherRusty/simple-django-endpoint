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
        # is_checked_in = request.user.     //This line needs to change.// 
        return render(request, "attendance.html")
    elif request.method == "POST":
        student = request.user
        checkin = Checkin.objects.create(student=student, datetime=timezone.now())
        messages.success(messages, "You have checked in!")
        return redirect("attendance:check-in")

@login_required
def thanks(request):
    if request.method == "GET":
        return render(request, "thanks.html")


"""

When a user checks in then they are added to the checked in students group and an admin can keep them there or delete them if they aren't (verification)

To do this:

    above the post (button cick) in the views have the group binded to a variable and .get that group name. 
    After a check in is created then you .add that user to the group. 



"""