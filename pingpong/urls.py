from django.urls import path
from . import views

app_name = "pingpong"

urlpatterns = [
    path("", views.home, name="home"),
    path("create/", views.create_match, name="create-match")
]

