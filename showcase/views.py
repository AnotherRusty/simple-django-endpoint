from django.shortcuts import render, redirect
from showcase.forms import SignUp
from showcase.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def sign_up(request):
    if request.method == "GET":
        return render(request, "create-profile.html", {"form": SignUp()})
    elif request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            user = request.user
            headline = form.cleaned_data["headline"]
            bio = form.cleaned_data["bio"]
            profile = Profile.objects.create(user=user, headline=headline, bio=bio)
            return redirect("showcase:profile-list")
        else:
            return render(request, "create-profile.html", {"form": form})


def user_profiles(request):
    profiles = Profile.objects.all()
    return render(request, "user-profiles.html", {"profiles": profiles})
