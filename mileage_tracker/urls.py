from django.urls import path
from . import views

app_name = "mileage_tracker"

urlpatterns = [path("", views.DistanceToWorkCreateView.as_view(), name="set_commute")]

