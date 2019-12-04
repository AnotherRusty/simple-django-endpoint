from django.urls import path
from showcase import views

app_name = "showcase"

urlpatterns = [
    path("create-profile/", views.sign_up, name="create-profile"),
    path("user-profile", views.user_profiles, name="user-profile"),
]
