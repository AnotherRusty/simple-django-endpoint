from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from initiative.views import (
    InitiativeView,
    InitiativeCreateView,
    InitiativeDetailView,
    InitiativeDeleteView,
    InitiativeEditView,
    InitiativeToggleView,
    InitiativeStatusReportView,
)

app_name = "initiatives"

urlpatterns = [
    path("", InitiativeView.as_view(), name="home"),
    path("create/", InitiativeCreateView.as_view(), name="create"),
    path("detail/<id>", InitiativeDetailView.as_view(), name="detail"),
    path("edit/<id>", InitiativeEditView.as_view(), name="edit"),
    path("delete/<id>", InitiativeDeleteView.as_view(), name="delete"),
    path("toggle/<id>", InitiativeToggleView.as_view(), name="toggle"),
    path("status/<id>", InitiativeStatusReportView.as_view(), name="status"),
]
