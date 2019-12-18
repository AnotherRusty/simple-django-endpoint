from django.urls import path
from . import views
from shoutouts.views import Shoutouts, ViewStudentShoutouts, LikeUpVote, PinShoutout

app_name = "shoutouts"

urlpatterns = [
    path("", Shoutouts.as_view(), name="home"),
    path(
        "<recipient_id>/shoutouts",
        ViewStudentShoutouts.as_view(),
        name="individual_shoutouts",
    ),
    path("likes/<shoutout_id>", LikeUpVote.as_view(), name="likes"),
    path("pinned/<shoutout_id>", PinShoutout.as_view(), name="pinned")
]
