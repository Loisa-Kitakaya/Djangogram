from django.urls import path, include
from . import views

# URLconf

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("dashboard", views.dashboard),
    path("logout", views.logout),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls")),
]
