from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("add-investment/", views.add_investment, name="add_investment"),
    path(
        "investment/<int:investment_id>", views.view_investment, name="view_investment"
    ),
    path(
        "investment/<int:investment_id>/edit",
        views.edit_investment,
        name="edit_investment",
    ),
]
