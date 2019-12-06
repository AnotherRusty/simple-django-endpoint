from django.urls import path
from . import views

app_name = "attendance"

urlpatterns = [
    path("", views.checkin, name="check-in"),
    path("thanks", views.thanks, name="thanks"),
]
