from django.shortcuts import render
from .forms import SignUp

def sign_up(request):
    if request.method == "GET":
        return render(request, "profile.html")
    elif request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            headline = form.cleaned_data["headline"]
            profile = SignUp.objects.create(headline=headline)





        