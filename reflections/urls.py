from django.urls import path
from . import views

app_name = "reflections"

urlpatterns = [path("", views.home, name="home")]

