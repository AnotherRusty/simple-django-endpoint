from django.urls import path
from . import views

app_name = "attendance"

urlpatterns = [
    path("/attendance", views.Attendance.as_view(), name="attendance"),
]
