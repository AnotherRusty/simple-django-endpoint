from django.urls import path
from . import views

app_name = "reflections"

urlpatterns = [
    path("", views.home, name="home"),
    path("submit_reflection/<id>", views.submit_reflection, name="submit_reflection"),
]

