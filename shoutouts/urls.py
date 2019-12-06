from django.urls import path
from . import views
from shoutouts.views import Shoutouts, ShoutoutLikes

app_name = "shoutouts"

urlpatterns = [
    path("", Shoutouts.as_view(), name="home"),
    path("likes/<id>", ShoutoutLikes.as_view(), name="likes"),
]
