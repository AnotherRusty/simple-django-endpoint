from django.urls import path
from . import views

app_name = "pingpong"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.MatchCreateView.as_view(), name="create-match"),
]

