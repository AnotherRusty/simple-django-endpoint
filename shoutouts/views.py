from django.shortcuts import render, redirect
from django.views.generic import View
from shoutouts.forms import ShoutoutForm
from shoutouts.models import Shoutout, ShoutoutLike
from django.utils import timezone

# Create your views here.


class Shoutouts(View):
    def get(self, request):
        shoutouts = Shoutout.objects.all()
        form = ShoutoutForm(request.POST)
        return render(request, "shoutouts.html", {"form": form, "shoutouts": shoutouts})

    def post(self, request):
        shoutouts = Shoutout.objects.all()
        form = ShoutoutForm(request.POST)
        if form.is_valid():
            recipient = form.cleaned_data["recipient"]
            content = form.cleaned_data["content"]
            create_new_shoutout = Shoutout.objects.create(
                recipient=recipient,
                content=content,
                datetime=timezone.now(),
                user=request.user,
                likes=0,
            )
            return redirect("home")
        elif not form.is_valid():
            return render(
                request, "shoutouts.html", {"form": form, "shoutouts": shoutouts}
            )


class ShoutoutLikes(View):
    def post(self, request, id):
        shoutout_likes = ShoutoutLike.objects.all()
        # create new row for likes, likes.count
        return redirect("home", shoutout.id)
