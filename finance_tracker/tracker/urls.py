from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path("add-investment/", views.add_investment, name="add_investment"),
    path("home/", views.home, name="home"),
]
