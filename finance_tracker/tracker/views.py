from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import InvestmentForm
from .models import Investment


@login_required
def home(request):
    investments = Investment.objects.all()
    return render(request, "tracker/home.html", {"investments": investments})


@login_required
def add_investment(request):
    if request.method == "POST":
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investment = form.save(commit=False)
            investment.user = request.user
            investment.save()
            return redirect("tracker:home")
    else:
        form = InvestmentForm()
    return render(request, "tracker/add_investment.html", {"form": form})
