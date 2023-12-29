from django.conf import settings
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm


def home(request):
    return render(request, "authentication/home.html")


def register(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "authentication/register.html", {"form": form})
