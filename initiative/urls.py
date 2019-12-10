from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from initiative.views import (
    InitiativeView,
    InitiativeCreateView,
    InitiativeDeleteView,
    InitiativeUpdateView,
)

app_name = "initiatives"

urlpatterns = [
    path("", InitiativeView.as_view(), name="home"),
    path("create/", InitiativeCreateView.as_view(), name="create"),
    path("update/<id>", InitiativeUpdateView.as_view(), name="update"),
    path("delete/<id>", InitiativeDeleteView.as_view(), name="delete"),
]
