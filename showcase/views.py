from django.shortcuts import render, redirect
from .forms import SignUp

def sign_up(request):
    if request.method == "GET":
        return render(request, "create-profile.html")
    elif request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            headline = form.cleaned_data["headline"]
            profile = SignUp.objects.create(headline=headline)
            return redirect("user_profiles")

def user_profiles(request):
    profiles = SignUP.objects.all()
    return render(request, "user-profiles.html", {"profiles": profiles})



        