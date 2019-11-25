from django.urls import path
from . import views

app_name = "magic-link"

urlpatterns = [
    path("create/", views.CreateMagicLink.as_view(), name="create"),
    path("login/", views.LoginWithMagicLink.as_view(), name="login"),
]

