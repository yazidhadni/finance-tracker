from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path(
        "",
        LoginView.as_view(
            template_name="authentication/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", views.logout_user, name="logout"),
    path("home/", views.home, name="home"),
    path("sign-up/", views.register, name="register"),
]
