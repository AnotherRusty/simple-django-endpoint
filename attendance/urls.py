from django.urls import path
from . import views

app_name = "attendance"

urlpatterns = [
    path("checkin", views.checkin, name="check-in"),
]
