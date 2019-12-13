from django.urls import path
from showcase import views

app_name = "showcase"

urlpatterns = [
    path("", views.user_profiles, name="profile-list"),
    path("create-profile/", views.sign_up, name="create-profile"),
    path("profile-page/<id>", views.profile_page, name="profile-page")
]
