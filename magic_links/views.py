from django.views.generic import CreateView, View
from .models import MagicLink
from .forms import NewMagicLinkForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse


class CreateMagicLink(CreateView):
    model = MagicLink
    form_class = NewMagicLinkForm
    template_name = "magic_links/create.html"

    def form_valid(self, form):
        messages.info(
            self.request, f"Magic Link emailed to {form.cleaned_data['email']}"
        )
        for user in User.objects.filter(email=form.cleaned_data["email"]):
            link, _created = MagicLink.objects.get_or_create(user=user)
            user.email_user(
                "Ascent - Magic Link",
                self.request.build_absolute_uri(
                    reverse("magic-link:login") + "?token=" + link.token
                ),
            )
        return redirect("home")


class LoginWithMagicLink(View):
    def get(self, request):
        token = request.GET.get("token")
        try:
            link = MagicLink.objects.get(token=token)
            if link.is_valid():
                login(request, link.user)
            link.delete()
        except MagicLink.DoesNotExist:
            messages.error(request, "Failed to login via magic link")
        return redirect("home")
