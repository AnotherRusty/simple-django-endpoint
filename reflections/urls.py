from django.urls import path
from . import views

app_name = "reflections"

urlpatterns = [
    path("", views.home, name="home"),
    path("submit_reflection/<id>", views.submit_reflection, name="submit_reflection"),
    path("admin_view", views.admin_view, name="admin_view"),
    path("submission_detail", views.submission_detail, name="submission_detail"),
]

