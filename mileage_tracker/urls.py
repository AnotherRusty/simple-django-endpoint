from django.urls import path
from . import views

app_name = "mileage_tracker"

urlpatterns = [
    path("", views.DistanceToWorkCreateView.as_view(), name="home"),
    path("user_commute/", views.DriveToWorkView.as_view(), name="user_commute"),
    path("admin/", views.ShowUserList.as_view(), name="admin"),
    path("<profile_id>/gas_detail/", views.UserGasDetail.as_view(), name="gas_detail"),
]

