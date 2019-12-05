from django.urls import path
from mileage_tracker.views import set_commute

app_name = "mileage_tracker"

urlpatterns = [
    path("", set_commute, name="set_commute")
]

    