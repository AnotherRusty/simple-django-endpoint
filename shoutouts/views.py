from django.shortcuts import render, redirect
from django.views.generic import View
from shoutouts.forms import ShoutoutForm
# Create your views here.


class Shoutouts(View):
    def get(self, request):
        return render(request, "shoutouts.html")
    # def post(self, request):
    #     shoutout = ShoutoutForm.objects.all()
    #     pass