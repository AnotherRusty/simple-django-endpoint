from django.urls import path
from . import views
from shoutouts.views import Shoutouts

app_name = "shoutouts"

urlpatterns = [
    path("", Shoutouts.as_view(), name="home"),
    # path("create/", CreateShoutout.as_view(), name="create"),
]

