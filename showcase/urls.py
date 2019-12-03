from django.urls import path
from showcase import views

app_name = "showcase"

urlpatterns = [
    path("sign-up/" views.sign_up, name="sign-up")
]
