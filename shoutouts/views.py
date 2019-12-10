from django.shortcuts import render, redirect
from django.views.generic import View
from shoutouts.forms import ShoutoutForm
from shoutouts.models import Shoutout, Like
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.


class Shoutouts(View):
    def get(self, request):
        form = ShoutoutForm(request.POST)
        shoutouts = Shoutout.objects.all()
        return render(request, "shoutouts.html", {"form": form, "shoutouts": shoutouts})

    def post(self, request):
        form = ShoutoutForm(request.POST)
        shoutouts = Shoutout.objects.all()
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
            return redirect("shoutouts:home")
        elif not form.is_valid():
            return render(
                request, "shoutouts.html", {"form": form, "shoutouts": shoutouts}
            )


class ViewStudentShoutouts(View):
    def get(self, request, recipient_id):
        recipient = User.objects.get(id=recipient_id)
        return render(
            request,
            "individual-shoutouts.html",
            {"recipient": recipient},
        )


class LikeShoutout(View):
    def post(self, request, shoutout_id):
        new_like, created = Like.objects.get_or_create(
            user=request.user, shoutout_id=shoutout_id
        )
        if not created:
            new_like += 1
            return redirect("shoutouts:home", shoutout_id)
        else:
            return redirect("shoutouts:home")

    def shoutout_detail(request, id):
        shoutout = get_object_or_404(Shoutout, pk=id)
        user_likes_this = shoutout.like_set.filter(user=request.user) and True or False
