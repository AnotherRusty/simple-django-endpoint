from django.urls import path
from . import views
from shoutouts.views import Shoutouts, ViewStudentShoutouts

app_name = "shoutouts"

urlpatterns = [
    path("", Shoutouts.as_view(), name="home"),
    path(
        "<shoutout_id>/shoutouts",
        ViewStudentShoutouts.as_view(),
        name="individual_shoutouts",
    ),
]
