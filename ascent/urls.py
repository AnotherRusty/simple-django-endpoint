from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path(
        "login/", RedirectView.as_view(pattern_name="magic-link:create"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("magic-link/", include("magic_links.urls"), name="magic-link"),
    path("showcase/", include("showcase.urls"), name="showcase"),
    path("initiatives/", include("initiative.urls"), name="initiatives"),
    path("mileage_tracker/", include("mileage_tracker.urls"), name="mileage_tracker"),
    path("pingpong/", include("pingpong.urls"), name="pingpong"),
    path("reflections/", include("reflections.urls"), name="reflections"),
    path("attendance/", include("attendance.urls"), name="attendance"),
    path("shoutouts/", include("shoutouts.urls"), name="shoutouts"),
]

if settings.DEBUG:
    import debug_toolbar  # pragma: no cover
    urlpatterns.append(
        path("__debug__/", include(debug_toolbar.urls))
    )  # pragma: no cover

