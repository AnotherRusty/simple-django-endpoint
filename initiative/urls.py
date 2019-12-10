from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from initiative.views import (
    InitiativeView,
    InitiativeCreateView,
    InitiativeStatusReportView,
    InitiativeDeleteView,
    InitiativeUpdateView,
)

app_name = "initiatives"

urlpatterns = [
    path("", InitiativeView.as_view(), name="home"),
    path("create/", InitiativeCreateView.as_view(), name="create"),
    path(
        "status/<id>", InitiativeStatusReportView.as_view(), name="status-report-create"
    ),
    path("update/<id>", InitiativeUpdateView.as_view(), name="update"),
    path("delete/<id>", InitiativeDeleteView.as_view(), name="delete"),
]
